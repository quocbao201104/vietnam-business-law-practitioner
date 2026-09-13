# Audit repair status — 2026-09-13

Base: `18ae61152a3250b2d0627e1848492f78b3557c54`; repairs are uncommitted.
The original audit remains historical evidence and has not been rewritten to
erase its pre-repair observations.

## Implemented

- F1: BL4 receives BL6 employment merits without an invented BL3 commercial
  prerequisite; employment settlement changes return to BL6 terms/separation.
  Commercial settlement changes remain BL3-owned; mixed settlements are split.
- F2: BL8 overlay markers can name BL6; governing-law inputs and handoffs now
  explicitly accept employment term content from BL6.
- F3: sibling reload conditions consistently concern review of the existing
  result, not merely a downstream dependency on that result.
- F4: existing BL5 units explicitly route contribution coverage/roles,
  base/rate/period, evidence and separate preferential relief/economics.
- F5: generic conflict validation consumes `STALE` and `INVALIDATE` events before
  accepting an independent supported blocker.
- F6: generic delta validation tracks observable proposition ownership, rejects
  accepted/reconciled foreign-owner writes, and rejects owner relabeling of an
  existing proposition. Rejected writes and separate authority/conflict objects
  remain supported. The checker does not infer owners from ID spelling and cannot
  certify ownership when the trace omits ownership history.

## Evidence

`python scripts/test_runtime_trace.py` ran 11 tests successfully. Before the
checker change, the initial eight-test suite failed in four assertions/subtests:
stale event, invalidation event, foreign-owner write, and owner reassignment.
Controls covered current/refreshed blockers, unrelated stale state, correct and
rejected owner writes, reconciled writes, and separate metadata objects.

The CLI test uses disposable, explicitly synthetic oracle/trace files and checks
exit status plus verdict. It does not alter frozen oracles or claim LLM execution.
`python scripts/check_runtime_trace.py --help` also succeeded.

The four scenario groups in
[`audit-repair-cases-v0.1.md`](../../evals/composition/audit-repair-cases-v0.1.md)
cover the semantic repairs and controls. Static review was performed, but their
agent behavior remains unproven: the requested baseline subagent stayed in
`pending_init` and was interrupted without returning any result. No baseline or
post-repair agent PASS is claimed.

## Still open

- Candidate-bound cold-start and held-out legal-answer evaluation of these edits.
- D1: kernel/index footprint reduction; no measured runtime improvement claimed.
- D2: retained/inconclusive classification-review completion semantics.
- D3: regulator-facing challenge/procedure coverage in BL7.

These design concerns need their own concrete behavior evidence before further
architecture changes. Historical oracle candidates and freeze status are intact.
No current law, contribution percentage, threshold, or deadline was added as a
static rule. Existing `AGENTS.md` and earlier audit artifacts were preserved.
