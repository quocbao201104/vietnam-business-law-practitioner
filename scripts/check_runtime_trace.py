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
SUPPORTED_BLOCKER_STATUSES = {"SUPPORTED"}


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


def nonempty_str_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(isinstance(x, str) and x for x in value)


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


def validate_state_deltas(
    events: list[dict[str, Any]], errors: list[str]
) -> dict[int, dict[str, Any]]:
    """Enforce revision-safe semantics and return deltas keyed by observable seq."""

    current_revision: int | None = None
    delta_index: dict[int, dict[str, Any]] = {}
    proposition_owners: dict[str, str] = {}

    for e in events:
        if e.get("event") in {"OWNER_ASSIGN", "PROPOSITION_OPEN", "PROPOSITION_STATUS"}:
            proposition_id = e.get("proposition_id")
            declared_owner = e.get("owner")
            if isinstance(proposition_id, str) and proposition_id and isinstance(declared_owner, str) and declared_owner:
                previous_owner = proposition_owners.get(proposition_id)
                if previous_owner is not None and previous_owner != declared_owner:
                    errors.append(f"proposition owner changed without a new proposition at seq {e.get('seq')}: {proposition_id}")
                else:
                    proposition_owners[proposition_id] = declared_owner
        if e.get("event") != "STATE_DELTA":
            continue

        seq = e.get("seq")
        owner = e.get("owner")
        base_revision = e.get("base_state_revision")
        affected = e.get("affected_object_ids")
        write_result = e.get("write_result")
        committed_revision = e.get("committed_state_revision")

        if isinstance(seq, int):
            delta_index[seq] = e

        if not isinstance(owner, str) or not owner:
            errors.append(f"STATE_DELTA missing owner at seq {seq}")
        if not isinstance(base_revision, int) or base_revision < 0:
            errors.append(f"STATE_DELTA invalid base_state_revision at seq {seq}: {base_revision!r}")
            continue
        if not nonempty_str_list(affected):
            errors.append(f"STATE_DELTA invalid/missing affected_object_ids at seq {seq}: {affected!r}")
        if write_result not in STATE_DELTA_RESULTS:
            errors.append(f"STATE_DELTA invalid write_result at seq {seq}: {write_result!r}")
            continue

        if write_result in {"APPLIED", "RECONCILED"} and isinstance(affected, list):
            for object_id in affected:
                if not isinstance(object_id, str):
                    continue
                accountable = proposition_owners.get(object_id)
                if accountable is not None and accountable != owner:
                    errors.append(f"STATE_DELTA owner {owner!r} cannot mutate proposition {object_id} owned by {accountable} at seq {seq}")

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

    return delta_index


def validate_conflict_transition_delta(
    event: dict[str, Any],
    conflict_id: str,
    delta_index: dict[int, dict[str, Any]],
    errors: list[str],
) -> dict[str, Any] | None:
    """Bind a conflict lifecycle mutation to a prior accepted revision-safe STATE_DELTA."""

    seq = event.get("seq")
    delta_seq = event.get("state_delta_seq")
    state_revision = event.get("state_revision")

    if not isinstance(delta_seq, int):
        errors.append(f"conflict transition missing/invalid state_delta_seq at seq {seq}: {delta_seq!r}")
        return None
    if not isinstance(seq, int) or delta_seq >= seq:
        errors.append(
            f"conflict transition must reference an earlier STATE_DELTA at seq {seq}: state_delta_seq={delta_seq!r}"
        )
        return None

    delta = delta_index.get(delta_seq)
    if delta is None:
        errors.append(f"conflict transition references missing STATE_DELTA at seq {seq}: {delta_seq}")
        return None

    if delta.get("write_result") not in {"APPLIED", "RECONCILED"}:
        errors.append(
            f"conflict transition references non-committing STATE_DELTA at seq {seq}: "
            f"delta_seq={delta_seq}, write_result={delta.get('write_result')!r}"
        )

    affected = delta.get("affected_object_ids")
    if not isinstance(affected, list) or conflict_id not in affected:
        errors.append(
            f"conflict transition STATE_DELTA does not affect conflict {conflict_id} at seq {seq}: delta_seq={delta_seq}"
        )

    committed_revision = delta.get("committed_state_revision")
    if not isinstance(state_revision, int) or state_revision < 0:
        errors.append(f"conflict transition invalid/missing state_revision at seq {seq}: {state_revision!r}")
    elif state_revision != committed_revision:
        errors.append(
            f"conflict transition revision does not match linked STATE_DELTA at seq {seq}: "
            f"state_revision={state_revision!r}, committed={committed_revision!r}"
        )

    return delta


def validate_scope_change(
    conflict_id: str,
    previous_scope: set[str] | None,
    new_scope: set[str],
    event: dict[str, Any],
    delta: dict[str, Any] | None,
    errors: list[str],
) -> None:
    """Require explicit revision-safe basis whenever affected-action scope changes."""

    if previous_scope is None or previous_scope == new_scope:
        return

    seq = event.get("seq")
    basis = event.get("scope_change_basis_ids")
    if not nonempty_str_list(basis):
        errors.append(
            f"composition conflict {conflict_id} changes affected_actions without scope_change_basis_ids at seq {seq}: "
            f"previous={sorted(previous_scope)}, new={sorted(new_scope)}"
        )
        return

    if delta is None:
        errors.append(
            f"composition conflict {conflict_id} scope change lacks revision-safe STATE_DELTA linkage at seq {seq}"
        )
        return

    delta_affected = delta.get("affected_object_ids")
    if not isinstance(delta_affected, list) or not any(item in delta_affected for item in basis):
        errors.append(
            f"composition conflict {conflict_id} scope-change basis is not included in linked STATE_DELTA at seq {seq}"
        )


def blocker_ids(readiness_event: dict[str, Any]) -> list[str]:
    values: list[str] = []
    one = readiness_event.get("blocking_proposition_id")
    many = readiness_event.get("blocking_proposition_ids")
    if isinstance(one, str) and one:
        values.append(one)
    if isinstance(many, list):
        values.extend(x for x in many if isinstance(x, str) and x)
    return list(dict.fromkeys(values))


def validate_composition_conflicts(
    events: list[dict[str, Any]],
    errors: list[str],
    delta_index: dict[int, dict[str, Any]],
) -> None:
    """Enforce observable conflict lifecycle, revision safety, scope, blockers, and convergence."""

    conflict_status: dict[str, str] = {}
    conflict_scope: dict[str, set[str]] = {}
    conflict_propositions: dict[str, set[str]] = {}
    terminal_actions: dict[str, tuple[int, list[str]]] = {}
    terminal_revision: dict[str, int] = {}
    resolved_actions: dict[str, tuple[int, list[str]]] = {}
    latest_readiness: dict[str, tuple[int, dict[str, Any]]] = {}
    latest_prop_status: dict[str, str] = {}

    for e in events:
        event = e.get("event")
        seq = e.get("seq")

        if event == "PROPOSITION_STATUS":
            proposition_id = e.get("proposition_id")
            status = e.get("status")
            if isinstance(proposition_id, str) and proposition_id and isinstance(status, str):
                latest_prop_status[proposition_id] = status

        elif event in {"STALE", "INVALIDATE"}:
            proposition_id = e.get("proposition_id")
            if isinstance(proposition_id, str) and proposition_id:
                latest_prop_status[proposition_id] = "STALE" if event == "STALE" else "INVALIDATED"

        elif event == "ACTION_READINESS":
            action_id = e.get("action_id")
            if isinstance(action_id, str) and action_id and isinstance(seq, int):
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
            if not nonempty_str_list(affected_actions):
                errors.append(
                    f"COMPOSITION_CONFLICT invalid/missing affected_actions at seq {seq}: {affected_actions!r}"
                )
                continue

            previous = conflict_status.get(conflict_id)
            new_scope = set(affected_actions)
            proposition_ids = e.get("proposition_ids")
            if nonempty_str_list(proposition_ids) and conflict_id not in conflict_propositions:
                conflict_propositions[conflict_id] = set(proposition_ids)

            if status == "ACTIVE":
                if previous in {"TERMINAL_UNRESOLVED", "RESOLVED"}:
                    errors.append(
                        f"composition conflict {conflict_id} silently reactivated after terminal/resolved state at seq {seq}; "
                        "use CONFLICT_REOPENED for a terminal conflict with new material input"
                    )
                elif previous == "ACTIVE" and conflict_scope.get(conflict_id) != new_scope:
                    delta = validate_conflict_transition_delta(e, conflict_id, delta_index, errors)
                    validate_scope_change(
                        conflict_id,
                        conflict_scope.get(conflict_id),
                        new_scope,
                        e,
                        delta,
                        errors,
                    )
                conflict_status[conflict_id] = "ACTIVE"
                conflict_scope[conflict_id] = new_scope

            elif status == "TERMINAL_UNRESOLVED":
                if previous != "ACTIVE":
                    errors.append(
                        f"TERMINAL_UNRESOLVED conflict must transition from ACTIVE at seq {seq}: "
                        f"conflict={conflict_id}, previous={previous!r}"
                    )

                terminal_reason = e.get("terminal_reason")
                remaining_ids = e.get("remaining_uncertainty_ids")
                external_need = e.get("required_external_input_or_review")
                if not isinstance(terminal_reason, str) or not terminal_reason.strip():
                    errors.append(f"terminal conflict missing terminal_reason at seq {seq}: {conflict_id}")
                has_remaining_ids = nonempty_str_list(remaining_ids)
                has_external_need = isinstance(external_need, str) and bool(external_need.strip())
                if not (has_remaining_ids or has_external_need):
                    errors.append(
                        f"terminal conflict missing remaining uncertainty/external review need at seq {seq}: {conflict_id}"
                    )

                delta = validate_conflict_transition_delta(e, conflict_id, delta_index, errors)
                validate_scope_change(
                    conflict_id,
                    conflict_scope.get(conflict_id),
                    new_scope,
                    e,
                    delta,
                    errors,
                )

                state_revision = e.get("state_revision")
                if isinstance(state_revision, int):
                    terminal_revision[conflict_id] = state_revision

                conflict_status[conflict_id] = "TERMINAL_UNRESOLVED"
                conflict_scope[conflict_id] = new_scope
                if isinstance(seq, int):
                    terminal_actions[conflict_id] = (seq, list(affected_actions))
                resolved_actions.pop(conflict_id, None)

        elif event == "CONFLICT_REOPENED":
            conflict_id = e.get("conflict_id")
            affected_actions = e.get("affected_actions")
            reopen_basis = e.get("reopen_basis_ids")

            if not isinstance(conflict_id, str) or not conflict_id:
                errors.append(f"CONFLICT_REOPENED missing conflict_id at seq {seq}")
                continue
            if not nonempty_str_list(affected_actions):
                errors.append(f"CONFLICT_REOPENED invalid/missing affected_actions at seq {seq}: {affected_actions!r}")
                continue
            if not nonempty_str_list(reopen_basis):
                errors.append(f"CONFLICT_REOPENED missing reopen_basis_ids at seq {seq}: {conflict_id}")

            previous = conflict_status.get(conflict_id)
            prior_terminal_revision = terminal_revision.get(conflict_id)

            if previous != "TERMINAL_UNRESOLVED":
                previous_status = e.get("previous_status")
                prior_from_event = e.get("prior_terminal_state_revision")
                resumed_terminal = (
                    previous is None
                    and previous_status == "TERMINAL_UNRESOLVED"
                    and isinstance(prior_from_event, int)
                    and prior_from_event >= 0
                )
                if resumed_terminal:
                    prior_terminal_revision = prior_from_event
                else:
                    errors.append(
                        f"CONFLICT_REOPENED must follow TERMINAL_UNRESOLVED at seq {seq}: "
                        f"conflict={conflict_id}, previous={previous!r}"
                    )

            delta = validate_conflict_transition_delta(e, conflict_id, delta_index, errors)
            state_revision = e.get("state_revision")
            if isinstance(prior_terminal_revision, int) and isinstance(state_revision, int):
                if state_revision <= prior_terminal_revision:
                    errors.append(
                        f"CONFLICT_REOPENED must use newer state revision at seq {seq}: "
                        f"terminal={prior_terminal_revision}, reopen={state_revision}"
                    )

            new_scope = set(affected_actions)
            validate_scope_change(
                conflict_id,
                conflict_scope.get(conflict_id),
                new_scope,
                e,
                delta,
                errors,
            )

            conflict_status[conflict_id] = "ACTIVE"
            conflict_scope[conflict_id] = new_scope
            terminal_actions.pop(conflict_id, None)
            resolved_actions.pop(conflict_id, None)

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
            if not isinstance(resolution_basis, str) or not resolution_basis.strip():
                errors.append(f"CONFLICT_RESOLVED missing resolution_basis at seq {seq}: {conflict_id}")

            validate_conflict_transition_delta(e, conflict_id, delta_index, errors)

            scope = sorted(conflict_scope.get(conflict_id, set()))
            if not scope:
                errors.append(f"CONFLICT_RESOLVED has no known affected-action scope at seq {seq}: {conflict_id}")

            conflict_status[conflict_id] = "RESOLVED"
            if isinstance(seq, int):
                resolved_actions[conflict_id] = (seq, scope)
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

                    if readiness_state == "DO_NOT_PROCEED":
                        blockers = blocker_ids(readiness_event)
                        conflict_props = conflict_propositions.get(conflict_id, set())
                        independent_supported = [
                            blocker
                            for blocker in blockers
                            if blocker not in conflict_props
                            and latest_prop_status.get(blocker) in SUPPORTED_BLOCKER_STATUSES
                        ]
                        if not blockers:
                            errors.append(
                                f"terminal conflict {conflict_id} action {action_id} uses DO_NOT_PROCEED without blocking proposition ID"
                            )
                        elif not independent_supported:
                            errors.append(
                                f"terminal conflict {conflict_id} action {action_id} uses DO_NOT_PROCEED without an independent current SUPPORTED blocker"
                            )

            for conflict_id, (resolved_seq, affected_actions) in resolved_actions.items():
                if conflict_status.get(conflict_id) != "RESOLVED":
                    continue
                for action_id in affected_actions:
                    readiness_record = latest_readiness.get(action_id)
                    if readiness_record is None:
                        errors.append(
                            f"resolved conflict {conflict_id} affected action {action_id} has no ACTION_READINESS before convergence"
                        )
                        continue
                    readiness_seq, _ = readiness_record
                    if readiness_seq <= resolved_seq:
                        errors.append(
                            f"resolved conflict {conflict_id} requires recomputed readiness after resolution for action {action_id}"
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

    # Generic authority vocabulary, revision-safe state-write, and conflict lifecycle invariants.
    validate_authority_events(events, errors)
    delta_index = validate_state_deltas(events, errors)
    validate_composition_conflicts(events, errors, delta_index)

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
