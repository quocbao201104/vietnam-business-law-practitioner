#!/usr/bin/env python3
"""Check an observable runtime JSONL trace against a frozen RF oracle."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ATTEMPT_STATUSES = {
    "SUCCEEDED",
    "SOURCE_UNAVAILABLE",
    "SOURCE_DRIFT",
    "SOURCE_LAGGING",
}

RESOLUTION_STATUSES = {
    "RESOLVED",
    "PARTIALLY_RESOLVED",
    "CONFLICTING_AUTHORITY",
    "DOCUMENT_IDENTITY_UNRESOLVED",
    "CURRENTNESS_UNRESOLVED",
    "PROVISION_UNRESOLVED",
    "CONSOLIDATION_UNRESOLVED",
    "INSUFFICIENT_AUTHORITY",
    "TEMPORAL_SCOPE_UNRESOLVED",
}

APPLICABILITY_STATUSES = {
    "APPLICABLE_TO_CASE",
    "NOT_APPLICABLE_TO_CASE",
    "APPLICABILITY_CONDITIONAL",
    "APPLICABILITY_UNRESOLVED",
}

STATE_DELTA_RESULTS = {"APPLIED", "REJECTED", "RECONCILED"}
CONFLICT_EVENT_STATUSES = {"ACTIVE", "TERMINAL_UNRESOLVED"}
TERMINAL_CONFLICT_READINESS = {
    "VERIFY_BEFORE_ACTION",
    "LEGAL_REVIEW_REQUIRED",
    "DO_NOT_PROCEED",
}


def git_bytes(repo: Path, *args: str) -> bytes:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8", errors="replace").strip() or "git command failed")
    return proc.stdout


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{lineno}: invalid JSON: {exc}") from exc
        if not isinstance(item, dict):
            raise ValueError(f"{path}:{lineno}: event must be an object")
        events.append(item)
    return events


def matches(event: dict[str, Any], pattern: dict[str, Any]) -> bool:
    for key, expected in pattern.items():
        if key not in event:
            return False
        actual = event[key]
        if isinstance(expected, dict):
            if not isinstance(actual, dict) or not matches(actual, expected):
                return False
        elif actual != expected:
            return False
    return True


def find_in_order(events: list[dict[str, Any]], patterns: list[dict[str, Any]]) -> tuple[bool, str]:
    idx = 0
    for pattern in patterns:
        found = False
        while idx < len(events):
            if matches(events[idx], pattern):
                found = True
                idx += 1
                break
            idx += 1
        if not found:
            return False, f"missing ordered event pattern: {json.dumps(pattern, ensure_ascii=False)}"
    return True, ""


def ordered_subsequence(actual: list[str], expected: list[str]) -> bool:
    idx = 0
    for item in expected:
        while idx < len(actual) and actual[idx] != item:
            idx += 1
        if idx >= len(actual):
            return False
        idx += 1
    return True


def validate_authority_events(events: list[dict[str, Any]], errors: list[str]) -> None:
    for e in events:
        event = e.get("event")
        seq = e.get("seq")

        if event in {"AUTHORITY_SOURCE_DRIFT", "AUTHORITY_SOURCE_UNAVAILABLE"}:
            attempt_status = e.get("attempt_status")
            if attempt_status not in ATTEMPT_STATUSES:
                errors.append(
                    f"authority source-attempt event has invalid/missing attempt_status at seq {seq}: {attempt_status!r}"
                )

        if event == "AUTHORITY_RESULT":
            status = e.get("resolution_status")
            if status in ATTEMPT_STATUSES:
                errors.append(
                    f"AUTHORITY_RESULT uses attempt_status value as resolution_status at seq {seq}: {status}"
                )
            elif status is not None and status not in RESOLUTION_STATUSES:
                errors.append(f"AUTHORITY_RESULT has unknown resolution_status at seq {seq}: {status!r}")

        if event == "AUTHORITY_APPLICABILITY_DECISION":
            status = e.get("applicability_status")
            if status not in APPLICABILITY_STATUSES:
                errors.append(
                    f"AUTHORITY_APPLICABILITY_DECISION has invalid/missing applicability_status at seq {seq}: {status!r}"
                )


def validate_state_deltas(events: list[dict[str, Any]], errors: list[str]) -> None:
    """Enforce revision-safe semantics for observable owner-scoped state writes."""

    current_revision: int | None = None

    for e in events:
        if e.get("event") != "STATE_DELTA":
            continue

        seq = e.get("seq")
        owner = e.get("owner")
        base_revision = e.get("base_state_revision")
        affected = e.get("affected_object_ids")
        write_result = e.get("write_result")
        committed_revision = e.get("committed_state_revision")

        if not isinstance(owner, str) or not owner:
            errors.append(f"STATE_DELTA missing owner at seq {seq}")
        if not isinstance(base_revision, int) or base_revision < 0:
            errors.append(f"STATE_DELTA invalid base_state_revision at seq {seq}: {base_revision!r}")
            continue
        if not isinstance(affected, list) or not affected or not all(isinstance(x, str) and x for x in affected):
            errors.append(f"STATE_DELTA invalid/missing affected_object_ids at seq {seq}: {affected!r}")
        if write_result not in STATE_DELTA_RESULTS:
            errors.append(f"STATE_DELTA invalid write_result at seq {seq}: {write_result!r}")
            continue

        # The first observed material delta establishes the revision it reasoned from.
        if current_revision is None:
            current_revision = base_revision

        is_stale = base_revision < current_revision
        is_ahead = base_revision > current_revision

        if is_ahead:
            errors.append(
                f"STATE_DELTA base revision is ahead of observed committed revision at seq {seq}: "
                f"base={base_revision}, current={current_revision}"
            )

        if write_result == "APPLIED":
            if is_stale:
                errors.append(
                    f"stale STATE_DELTA incorrectly APPLIED at seq {seq}: "
                    f"base={base_revision}, current={current_revision}"
                )
            if base_revision != current_revision:
                errors.append(
                    f"APPLIED STATE_DELTA must use current revision at seq {seq}: "
                    f"base={base_revision}, current={current_revision}"
                )
            if not isinstance(committed_revision, int) or committed_revision <= current_revision:
                errors.append(
                    f"APPLIED STATE_DELTA must advance committed_state_revision at seq {seq}: "
                    f"committed={committed_revision!r}, current={current_revision}"
                )
            else:
                current_revision = committed_revision

        elif write_result == "REJECTED":
            if committed_revision is not None:
                errors.append(
                    f"REJECTED STATE_DELTA must not create committed_state_revision at seq {seq}: "
                    f"{committed_revision!r}"
                )

        elif write_result == "RECONCILED":
            if not isinstance(committed_revision, int) or committed_revision <= current_revision:
                errors.append(
                    f"RECONCILED STATE_DELTA must advance committed_state_revision at seq {seq}: "
                    f"committed={committed_revision!r}, current={current_revision}"
                )
            else:
                current_revision = committed_revision


def validate_composition_conflicts(events: list[dict[str, Any]], errors: list[str]) -> None:
    """Enforce observable composition-conflict lifecycle and convergence semantics."""

    conflict_status: dict[str, str] = {}
    terminal_actions: dict[str, tuple[int, list[str]]] = {}
    latest_readiness: dict[str, tuple[int, dict[str, Any]]] = {}

    for e in events:
        event = e.get("event")
        seq = e.get("seq")

        if event == "ACTION_READINESS":
            action_id = e.get("action_id")
            if isinstance(action_id, str) and action_id:
                latest_readiness[action_id] = (seq, e)

        elif event == "COMPOSITION_CONFLICT":
            conflict_id = e.get("conflict_id")
            status = e.get("status")
            affected_actions = e.get("affected_actions")

            if not isinstance(conflict_id, str) or not conflict_id:
                errors.append(f"COMPOSITION_CONFLICT missing conflict_id at seq {seq}")
                continue
            if status not in CONFLICT_EVENT_STATUSES:
                errors.append(f"COMPOSITION_CONFLICT invalid/missing status at seq {seq}: {status!r}")
                continue
            if not isinstance(affected_actions, list) or not affected_actions or not all(
                isinstance(x, str) and x for x in affected_actions
            ):
                errors.append(
                    f"COMPOSITION_CONFLICT invalid/missing affected_actions at seq {seq}: {affected_actions!r}"
                )
                continue

            previous = conflict_status.get(conflict_id)

            if status == "ACTIVE":
                if previous in {"TERMINAL_UNRESOLVED", "RESOLVED"}:
                    errors.append(
                        f"composition conflict {conflict_id} reactivated after terminal/resolved state at seq {seq}"
                    )
                conflict_status[conflict_id] = "ACTIVE"

            elif status == "TERMINAL_UNRESOLVED":
                if previous != "ACTIVE":
                    errors.append(
                        f"TERMINAL_UNRESOLVED conflict must transition from ACTIVE at seq {seq}: "
                        f"conflict={conflict_id}, previous={previous!r}"
                    )
                terminal_reason = e.get("terminal_reason")
                remaining_ids = e.get("remaining_uncertainty_ids")
                external_need = e.get("required_external_input_or_review")
                state_revision = e.get("state_revision")

                if not isinstance(terminal_reason, str) or not terminal_reason.strip():
                    errors.append(f"terminal conflict missing terminal_reason at seq {seq}: {conflict_id}")
                has_remaining_ids = isinstance(remaining_ids, list) and bool(remaining_ids) and all(
                    isinstance(x, str) and x for x in remaining_ids
                )
                has_external_need = isinstance(external_need, str) and bool(external_need.strip())
                if not (has_remaining_ids or has_external_need):
                    errors.append(
                        f"terminal conflict missing remaining uncertainty/external review need at seq {seq}: {conflict_id}"
                    )
                if not isinstance(state_revision, int) or state_revision < 0:
                    errors.append(
                        f"terminal conflict invalid/missing state_revision at seq {seq}: {state_revision!r}"
                    )

                conflict_status[conflict_id] = "TERMINAL_UNRESOLVED"
                terminal_actions[conflict_id] = (seq, affected_actions)

        elif event == "CONFLICT_RESOLVED":
            conflict_id = e.get("conflict_id")
            if not isinstance(conflict_id, str) or not conflict_id:
                errors.append(f"CONFLICT_RESOLVED missing conflict_id at seq {seq}")
                continue

            previous = conflict_status.get(conflict_id)
            if previous != "ACTIVE":
                errors.append(
                    f"CONFLICT_RESOLVED must transition from ACTIVE at seq {seq}: "
                    f"conflict={conflict_id}, previous={previous!r}"
                )
            resolution_basis = e.get("resolution_basis")
            state_revision = e.get("state_revision")
            if not isinstance(resolution_basis, str) or not resolution_basis.strip():
                errors.append(f"CONFLICT_RESOLVED missing resolution_basis at seq {seq}: {conflict_id}")
            if not isinstance(state_revision, int) or state_revision < 0:
                errors.append(
                    f"CONFLICT_RESOLVED invalid/missing state_revision at seq {seq}: {state_revision!r}"
                )
            conflict_status[conflict_id] = "RESOLVED"
            terminal_actions.pop(conflict_id, None)

        elif event == "RUN_CONVERGED":
            active = sorted(cid for cid, status in conflict_status.items() if status == "ACTIVE")
            if active:
                errors.append(f"RUN_CONVERGED with ACTIVE composition conflict(s) at seq {seq}: {active}")

            for conflict_id, (terminal_seq, affected_actions) in terminal_actions.items():
                if conflict_status.get(conflict_id) != "TERMINAL_UNRESOLVED":
                    continue
                for action_id in affected_actions:
                    readiness_record = latest_readiness.get(action_id)
                    if readiness_record is None:
                        errors.append(
                            f"terminal conflict {conflict_id} affected action {action_id} has no ACTION_READINESS before convergence"
                        )
                        continue
                    readiness_seq, readiness_event = readiness_record
                    readiness_state = readiness_event.get("state")
                    if readiness_seq <= terminal_seq:
                        errors.append(
                            f"terminal conflict {conflict_id} requires recomputed readiness after terminalization "
                            f"for action {action_id}"
                        )
                    if readiness_state not in TERMINAL_CONFLICT_READINESS:
                        errors.append(
                            f"terminal conflict {conflict_id} affected action {action_id} has invalid converged readiness: "
                            f"{readiness_state!r}"
                        )
                    conflict_ref = readiness_event.get("conflict_id")
                    conflict_refs = readiness_event.get("conflict_ids")
                    linked = conflict_ref == conflict_id or (
                        isinstance(conflict_refs, list) and conflict_id in conflict_refs
                    )
                    if not linked:
                        errors.append(
                            f"ACTION_READINESS for {action_id} does not identify terminal conflict {conflict_id}"
                        )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--oracle", required=True)
    ap.add_argument("--trace", required=True)
    ap.add_argument("--fixture")
    args = ap.parse_args()

    repo = Path(args.repo_root).resolve()
    oracle_doc = load_json(Path(args.oracle).resolve())
    events = load_jsonl(Path(args.trace).resolve())
    errors: list[str] = []

    if not events:
        errors.append("trace is empty")
    else:
        run_ids = {e.get("run_id") for e in events}
        fixture_ids = {e.get("fixture_id") for e in events}
        candidate_shas = {e.get("candidate_sha") for e in events}
        if len(run_ids) != 1:
            errors.append(f"multiple/missing run_id values: {run_ids}")
        if len(fixture_ids) != 1:
            errors.append(f"multiple/missing fixture_id values: {fixture_ids}")
        if len(candidate_shas) != 1:
            errors.append(f"multiple/missing candidate_sha values: {candidate_shas}")

        seqs = [e.get("seq") for e in events]
        if seqs != list(range(1, len(events) + 1)):
            errors.append(f"sequence is not contiguous 1..N: {seqs}")

    fixture = args.fixture or (events[0].get("fixture_id") if events else None)
    fixtures = oracle_doc.get("fixtures", {})
    if fixture not in fixtures:
        errors.append(f"fixture not found in oracle: {fixture}")
        rule = {}
    else:
        rule = fixtures[fixture]

    candidate_sha = oracle_doc.get("candidate_sha")
    if not candidate_sha:
        errors.append("oracle missing candidate_sha")
    elif events and any(e.get("candidate_sha") != candidate_sha for e in events):
        errors.append("trace candidate_sha does not match oracle candidate_sha")

    # Candidate must exist.
    if candidate_sha:
        proc = subprocess.run(
            ["git", "-C", str(repo), "cat-file", "-e", f"{candidate_sha}^{{commit}}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if proc.returncode != 0:
            errors.append(f"candidate commit not available locally: {candidate_sha}")

    # Integrity-check every observable READ against frozen candidate content.
    read_events = [e for e in events if e.get("event") == "READ"]
    for e in read_events:
        path = e.get("path")
        if not isinstance(path, str) or not path:
            errors.append(f"READ event missing path at seq {e.get('seq')}")
            continue
        try:
            content = git_bytes(repo, "show", f"{candidate_sha}:{path}")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"cannot resolve READ path {path!r} at candidate: {exc}")
            continue
        digest = hashlib.sha256(content).hexdigest()
        if e.get("content_sha256") != digest:
            errors.append(f"READ hash mismatch for {path}")
        if e.get("bytes") != len(content):
            errors.append(f"READ byte-count mismatch for {path}")

    actual_reads = [e["path"] for e in read_events if isinstance(e.get("path"), str)]
    required_reads = rule.get("required_reads", [])
    if required_reads and not ordered_subsequence(actual_reads, required_reads):
        errors.append(f"required READ order not preserved: expected subsequence {required_reads}, actual {actual_reads}")

    for path in rule.get("forbidden_reads", []):
        if path in actual_reads:
            errors.append(f"forbidden READ observed: {path}")

    ok, why = find_in_order(events, rule.get("event_sequence", []))
    if not ok:
        errors.append(why)

    for pattern in rule.get("required_events", []):
        if not any(matches(e, pattern) for e in events):
            errors.append(f"missing required event: {json.dumps(pattern, ensure_ascii=False)}")

    for pattern in rule.get("forbidden_events", []):
        if any(matches(e, pattern) for e in events):
            errors.append(f"forbidden event observed: {json.dumps(pattern, ensure_ascii=False)}")

    if rule.get("require_converged", True):
        if not any(e.get("event") == "RUN_CONVERGED" for e in events):
            errors.append("RUN_CONVERGED missing")

    # Basic specialist ownership invariant independent of fixture.
    for e in events:
        if e.get("event") in {"SPECIALIST_CALL", "SPECIALIST_RETURN"} and not e.get("owner"):
            errors.append(f"specialist event missing owner at seq {e.get('seq')}")

    # Generic authority vocabulary, revision-safe state-write, and conflict convergence invariants.
    validate_authority_events(events, errors)
    validate_state_deltas(events, errors)
    validate_composition_conflicts(events, errors)

    result = {
        "fixture": fixture,
        "candidate_sha": candidate_sha,
        "events": len(events),
        "reads": actual_reads,
        "verdict": "PASS" if not errors else "FAIL",
        "errors": errors,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
