#!/usr/bin/env python3
"""Check an observable runtime JSONL trace against a frozen RF oracle."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


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
