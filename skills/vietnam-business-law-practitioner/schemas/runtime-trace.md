# Runtime Trace — Observable Event Contract v0.7

This contract exists to prove execution path independently of final prose.

A runtime trace is append-only JSONL. Each line is one event object.

## Required envelope

Every event must include:

- `run_id`
- `seq`
- `ts`
- `candidate_sha`
- `fixture_id`
- `event`

`seq` must increase monotonically within a run.

## File-access events

### `READ`

Required fields:

- `path`
- `content_sha256`
- `bytes`

Use the walker to read skill/knowledge/reference/schema files so the read path and file content hash are externally observable.

### `SKIP`

Optional explicit event for a track/path intentionally skipped when the oracle requires proving a skip.

Fields:

- `target`
- `reason`

## Routing events

- `ROUTE_HYPOTHESIS`
- `ACTIVATE`
- `ROUTE_STATUS`
- `LATE_ROUTE_SIGNAL`

Material route events should identify:

- track
- route status
- triggering fact/proposition where applicable

## Proposition/ownership events

- `PROPOSITION_OPEN`
- `PROPOSITION_STATUS`
- `OWNER_ASSIGN`
- `DEPENDENCY_ADD`

Typed dependency edges use:

- `DEPENDS_ON`
- `CONSTRAINS`
- `SIGNALS`
- `FEEDBACK`

## Authority events

- `AUTHORITY_CALL`
- `AUTHORITY_RESULT`
- `AUTHORITY_REUSE`
- `AUTHORITY_RERESOLVE`
- `AUTHORITY_CHANGE_SIGNAL`
- `AUTHORITY_APPLICABILITY_DECISION`
- `AUTHORITY_IDENTITY_LOCK`
- `AUTHORITY_SOURCE_DRIFT`
- `AUTHORITY_SOURCE_UNAVAILABLE`

### Authority call / re-resolution

Where material, `AUTHORITY_CALL` and `AUTHORITY_RERESOLVE` should identify:

- `request_id`;
- proposition ID;
- accountable owner;
- exact legal authority question;
- jurisdiction(s);
- temporal anchor(s);
- freshness requirement;
- prior authority result ID when re-resolving.

A whole-case generic authority call is invalid when materially different propositions have different owners/temporal anchors.

### Authority result

`AUTHORITY_RESULT` should identify where material:

- `request_id`;
- `authority_result_id`;
- proposition ID requested;
- owner;
- proposition-level `resolution_status`;
- authority/source IDs;
- resolved document identity;
- provision locator;
- lifecycle/temporal scope;
- `verified_at` and freshness data.

Authority source-attempt events must use `attempt_status` for attempt-local conditions such as `SOURCE_DRIFT` or `SOURCE_UNAVAILABLE`. `AUTHORITY_RESULT` must use proposition-level `resolution_status`. A failed source attempt followed by successful fallback must preserve both events rather than collapsing them.

Example:

```text
AUTHORITY_SOURCE_DRIFT source=VN-VBPL attempt_status=SOURCE_DRIFT
→ AUTHORITY_RESULT resolution_status=RESOLVED
```

### Authority reuse

Emit `AUTHORITY_REUSE` when an existing authority result is used instead of a new resolver call.

Where material include:

- `authority_result_id`;
- current proposition ID and owner;
- reuse basis showing scope/jurisdiction/temporal/freshness compatibility;
- current state revision;
- any prior proposition/request from which the result originated.

`AUTHORITY_REUSE` proves reuse of the resolver result only. It must not imply that another proposition's applicability conclusion was inherited.

### Owner applicability decision

Emit `AUTHORITY_APPLICABILITY_DECISION` after the resolver result/reuse and before an authority-backed proposition is promoted on that basis.

Required where material:

- proposition ID;
- accountable owner;
- authority result ID(s);
- applicability status:
  - `APPLICABLE_TO_CASE`
  - `NOT_APPLICABLE_TO_CASE`
  - `APPLICABILITY_CONDITIONAL`
  - `APPLICABILITY_UNRESOLVED`
- temporal anchor(s);
- current `state_revision`;
- material condition/fact IDs when the decision is conditional.

This event is owner-scoped. Resolver `RESOLVED` or lifecycle `CURRENT_BINDING` never substitutes for it.

## Specialist events

- `SPECIALIST_CALL`
- `SPECIALIST_RETURN`

Both must identify the owning BL track. A specialist without an owner is invalid.

## State-transition events

- `CONTRADICTION_SIGNAL`
- `CLASSIFICATION_SIGNAL`
- `RECLASSIFICATION_REVIEW`
- `RECLASSIFICATION_COMMITTED`
- `STATE_DELTA`
- `STALE`
- `INVALIDATE`
- `RECOMPUTE`

Invalidation events must identify the exact proposition/classification ID and dependency basis where applicable.

### `STATE_DELTA`

Use `STATE_DELTA` for every material owner-scoped shared-state mutation that is relevant to runtime proof.

Required fields:

- `owner`;
- `base_state_revision` — revision the owner reasoned from;
- `affected_object_ids` — non-empty list of stable state object IDs the delta proposes to change;
- `write_result` — one of:
  - `APPLIED`
  - `REJECTED`
  - `RECONCILED`
- `committed_state_revision` when `write_result` is `APPLIED` or `RECONCILED`.

Semantics:

```text
APPLIED
→ base_state_revision equals current committed revision
→ committed_state_revision advances monotonically

REJECTED
→ shared state is unchanged by the rejected delta
→ no committed_state_revision is created by that delta

RECONCILED
→ base_state_revision may be stale/conflicting
→ runtime explicitly reconciles against current state
→ the reconciliation result advances committed_state_revision
```

A delta based on a stale revision must never appear as `write_result=APPLIED`.

Where reclassification, contradiction repair, authority writeback, or another state transition mutates material shared state, the trace should connect that semantic transition to a revision-aware `STATE_DELTA` with the affected object IDs.

Authority freshness/change may make an exact authority-backed proposition `STALE` or review-required. Do not emit global invalidation merely because one authority result aged or changed.

If re-resolution changes the owned proposition materially, downstream `INVALIDATE` / `RECOMPUTE` must still identify exact `DEPENDS_ON` basis. If freshness is restored without changing the owned proposition, readiness may be recomputed without substantive downstream invalidation.

## Composition events

- `COMPOSITION_CONFLICT`
- `CONFLICT_RESOLVED`
- `ACTION_READINESS`
- `RUN_CONVERGED`

### Composition conflict lifecycle

`COMPOSITION_CONFLICT` must identify where material:

- `conflict_id`;
- involved proposition IDs;
- owners;
- affected action IDs;
- reason;
- `status`.

Allowed conflict status:

- `ACTIVE`
- `TERMINAL_UNRESOLVED`

Emit `COMPOSITION_CONFLICT status=ACTIVE` when the conflict is first created.

If the same conflict is later terminalized without substantive resolution, emit another `COMPOSITION_CONFLICT` event with the same `conflict_id` and:

- `status=TERMINAL_UNRESOLVED`;
- `terminal_reason`;
- remaining uncertainty IDs or a non-empty `required_external_input_or_review` description;
- affected action IDs;
- current `state_revision`.

`TERMINAL_UNRESOLVED` means no material internal resolution step remains in the current run. It must not be emitted while a material late-route, contradiction/reclassification, stale-state repair, authority re-resolution, or available specialist step could still resolve the conflict.

Emit `CONFLICT_RESOLVED` only for substantive resolution. It must identify:

- `conflict_id`;
- resolution basis;
- current `state_revision`.

`ACTION_READINESS` must include `action_id`, state, and explicit prerequisite proposition/condition IDs. When readiness is capped by a terminal unresolved conflict, it should also identify the relevant `conflict_id`.

When a new/re-resolved authority result is material to readiness, the trace should make it possible to connect:

```text
AUTHORITY_CALL / AUTHORITY_RERESOLVE
→ AUTHORITY_RESULT
→ AUTHORITY_APPLICABILITY_DECISION
→ PROPOSITION_STATUS
→ ACTION_READINESS
```

When an existing authority result is reused, the path is:

```text
AUTHORITY_REUSE
→ AUTHORITY_APPLICABILITY_DECISION
→ PROPOSITION_STATUS
→ ACTION_READINESS
```

On freshness change:

```text
AUTHORITY_CHANGE_SIGNAL / freshness failure
→ STALE exact proposition
→ AUTHORITY_RERESOLVE
→ AUTHORITY_RESULT
→ AUTHORITY_APPLICABILITY_DECISION
→ PROPOSITION_STATUS
→ ACTION_READINESS
```

## Materiality events

When activation/skip is not obvious, emit `MATERIALITY_DECISION` with:

- candidate fact/proposition/issue;
- material: true/false;
- reason category;
- affected route/classification/result/dependency/authority version/option set/readiness, if true.

Use this event when the decision whether to call/reuse/re-resolve authority is contestable.

## Convergence

`RUN_CONVERGED` may be emitted only when all requested actions satisfy the stop condition in `runtime-composition.md`, including authority-aware convergence and composition-conflict lifecycle.

No conflict may remain `ACTIVE` at convergence.

A run may converge with a `TERMINAL_UNRESOLVED` conflict only when the terminal event is explicit and each affected action is subsequently recorded as `VERIFY_BEFORE_ACTION`, `LEGAL_REVIEW_REQUIRED`, or independently supported `DO_NOT_PROCEED`.

A run may converge with an unresolved authority result only when the unresolved authority/applicability state is explicit and reflected in non-READY readiness.

## Integrity

The trace checker should reject, where the applicable oracle encodes the requirement or the invariant is generic:

- non-monotonic sequence numbers;
- candidate SHA mismatch;
- fixture mismatch;
- malformed required fields;
- `READ` events whose file hash does not match the candidate checkout;
- specialist events without an owner;
- source-attempt status used as final resolver `resolution_status` or vice versa;
- authority-backed proposition promotion that skips a required owner applicability decision;
- `AUTHORITY_REUSE` whose recorded temporal/freshness/scope basis does not satisfy the fixture;
- repeated identical authority calls with no new material input when the prior unresolved result has already been recorded;
- a `STATE_DELTA` missing revision/owner/object metadata;
- a stale `STATE_DELTA` recorded as `APPLIED`;
- non-monotonic `committed_state_revision` values;
- malformed composition-conflict lifecycle or terminalization metadata;
- `RUN_CONVERGED` while any conflict remains `ACTIVE`;
- terminal unresolved conflict followed by `READY` / `READY_WITH_CONDITIONS` for an affected action;
- readiness before unresolved required conflict/stale state/authority applicability or freshness issue is reflected in the action state.

## Evidence status

A trace proves only events that are actually observable in it. It does not prove hidden model reasoning.

Therefore the freeze gate should rely on observable path properties such as file reads, event order, owner/route transitions, resolver calls/reuse/re-resolution, owner applicability decisions, revision-aware state-delta outcomes, composition-conflict lifecycle, source-attempt/fallback events, invalidation targets, and readiness outputs rather than chain-of-thought.
