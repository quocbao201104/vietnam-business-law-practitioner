"""Synthetic checker probes, NOT legal-runtime or cold-start evidence.

Run from any directory with Python. No oracle, runtime file, or trace is changed.
Exit 0 means the probes ran; inspect detected/rejected fields for actual results.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import runpy


REPO = Path(__file__).resolve().parents[2]
CHECKER = REPO / "scripts" / "check_runtime_trace.py"


def inspect_events(checker: dict, events: list[dict]) -> list[str]:
    events = [dict(event, seq=i) for i, event in enumerate(events, 1)]
    errors: list[str] = []
    checker["validate_authority_events"](events, errors)
    deltas = checker["validate_state_deltas"](events, errors)
    checker["validate_composition_conflicts"](events, errors, deltas)
    return errors


def terminal_blocker_events(change: str | None) -> list[dict]:
    events = [
        {"event": "PROPOSITION_STATUS", "owner": "BL7",
         "proposition_id": "P-BLOCK", "status": "SUPPORTED"},
        {"event": "COMPOSITION_CONFLICT", "conflict_id": "C-1",
         "status": "ACTIVE", "affected_actions": ["A-1"],
         "proposition_ids": ["P-X", "P-Y"], "owners": ["BL3", "BL7"],
         "reason": "Synthetic conflict unrelated to P-BLOCK"},
        {"event": "STATE_DELTA", "owner": "BL7",
         "base_state_revision": 0, "committed_state_revision": 1,
         "affected_object_ids": ["C-1"], "write_result": "APPLIED"},
        {"event": "COMPOSITION_CONFLICT", "conflict_id": "C-1",
         "status": "TERMINAL_UNRESOLVED", "affected_actions": ["A-1"],
         "state_delta_seq": 3, "state_revision": 1,
         "terminal_reason": "Synthetic exhausted internal review",
         "required_external_input_or_review": "Missing external record"},
    ]
    if change:
        events.append({
            "event": "STATE_DELTA", "owner": "BL7",
            "base_state_revision": 1, "committed_state_revision": 2,
            "affected_object_ids": ["P-BLOCK"], "write_result": "APPLIED",
        })
        if change == "PROPOSITION_STATUS_STALE":
            events.append({"event": "PROPOSITION_STATUS", "owner": "BL7",
                           "proposition_id": "P-BLOCK", "status": "STALE"})
        else:
            events.append({"event": change, "owner": "BL7",
                           "proposition_id": "P-BLOCK", "basis": "DEPENDS_ON",
                           "dependency_id": "P-UPSTREAM", "state_delta_seq": 5,
                           "state_revision": 2})
    events.extend([
        {"event": "ACTION_READINESS", "action_id": "A-1",
         "state": "DO_NOT_PROCEED", "conflict_id": "C-1",
         "blocking_proposition_ids": ["P-BLOCK"],
         "prerequisite_proposition_ids": ["P-BLOCK"],
         "state_revision": 2 if change else 1},
        {"event": "RUN_CONVERGED"},
    ])
    return events


def owner_events(delta_owner: str) -> list[dict]:
    return [
        {"event": "OWNER_ASSIGN", "owner": "BL6", "proposition_id": "P-REL"},
        {"event": "STATE_DELTA", "owner": delta_owner,
         "base_state_revision": 0, "committed_state_revision": 1,
         "affected_object_ids": ["P-REL"], "write_result": "APPLIED",
         "mutation_kind": "REPLACE_PROPOSITION",
         "changes": {"P-REL": {"statement": "Synthetic replacement conclusion"}}},
    ]


def main() -> None:
    argparse.ArgumentParser(description=__doc__).parse_args()
    checker = runpy.run_path(str(CHECKER))
    results = []
    for change in [None, "PROPOSITION_STATUS_STALE", "STALE", "INVALIDATE"]:
        errors = inspect_events(checker, terminal_blocker_events(change))
        results.append({
            "probe": "terminal_blocker_" + (change or "current_control"),
            "contract_requires_rejection": change is not None,
            "generic_validators_rejected": bool(errors),
            "errors": errors,
        })
    for owner in ["BL6", "BL5"]:
        errors = inspect_events(checker, owner_events(owner))
        results.append({
            "probe": "BL6_owned_proposition_written_by_" + owner,
            "contract_requires_rejection": owner != "BL6",
            "generic_validators_rejected": bool(errors),
            "errors": errors,
        })
    print(json.dumps({
        "evidence_type": "SYNTHETIC_GENERIC_CHECKER_PROBES_NOT_RUNTIME_PROOF",
        "checker_sha256": hashlib.sha256(CHECKER.read_bytes()).hexdigest(),
        "results": results,
    }, indent=2))


if __name__ == "__main__":
    main()
