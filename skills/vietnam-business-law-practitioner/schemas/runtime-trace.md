# Runtime Trace — Observable Event Contract v0.8

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

When a current supported proposition is used as an independent action blocker, its `PROPOSITION_STATUS` should be observable before readiness is finalized.

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

### Observable proposition ownership and stale status

Before a material proposition mutation, expose its accountable owner through
`OWNER_ASSIGN` or an owner-bearing `PROPOSITION_OPEN` / `PROPOSITION_STATUS`.
Keep that owner for the proposition ID; a different substantive proposition uses
its own ID and explicit dependencies rather than relabeling another owner's ID.
An accepted/reconciled delta may not change a proposition assigned to another
owner. Rejected proposals do not mutate state. Authority results and composition
conflicts are separate objects, not BL propositions inferred from their ID names.

`STALE` and `INVALIDATE` update the effective status of the identified proposition
just as an explicit `PROPOSITION_STATUS` does. A later `RECOMPUTE` alone does not
prove restored support: record the resulting owner status before using it as a
current supported blocker. An unrelated stale object does not change that blocker.

The checker can compare ownership only when it is observable. Missing ownership
history is an evidence gap, not proof that a write was authorized.

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

Where reclassification, contradiction repair, authority writeback, composition-conflict status/scope change, or another state transition mutates material shared state, the trace must connect that semantic transition to a revision-aware `STATE_DELTA` with the affected object IDs.

For `ACTIVE → RESOLVED`, `ACTIVE → TERMINAL_UNRESOLVED`, or explicit conflict reopen, the lifecycle event must carry `state_delta_seq` pointing to an earlier accepted/reconciled `STATE_DELTA` whose `affected_object_ids` includes the same `conflict_id`. The lifecycle event's `state_revision` must equal that delta's `committed_state_revision`.

Authority freshness/change may make an exact authority-backed proposition `STALE` or review-required. Do not emit global invalidation merely because one authority result aged or changed.

If re-resolution changes the owned proposition materially, downstream `INVALIDATE` / `RECOMPUTE` must still identify exact `DEPENDS_ON` basis. If freshness is restored without changing the owned proposition, readiness may be recomputed without substantive downstream invalidation.

## Composition events

- `COMPOSITION_CONFLICT`
- `CONFLICT_RESOLVED`
- `CONFLICT_REOPENED`
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

The initial affected-action set becomes the current conflict scope. A later lifecycle event must preserve that set unless a revision-safe state/dependency change explicitly changes scope. When scope changes, expose non-empty `scope_change_basis_ids`; the linked state delta must include the conflict and at least one cited scope/dependency object.

If the same conflict is later terminalized without substantive resolution, emit another `COMPOSITION_CONFLICT` event with the same `conflict_id` and:

- `status=TERMINAL_UNRESOLVED`;
- `terminal_reason`;
- remaining uncertainty IDs or a non-empty `required_external_input_or_review` description;
- affected action IDs;
- current committed `state_revision`;
- `state_delta_seq` for the revision-safe conflict mutation;
- `scope_change_basis_ids` if and only if the affected-action scope materially changed.

`TERMINAL_UNRESOLVED` means no material internal resolution step remains in the current run. It must not be emitted while a material late-route, contradiction/reclassification, stale-state repair, authority re-resolution, or available specialist step could still resolve the conflict.

Emit `CONFLICT_RESOLVED` only for substantive resolution. It must identify:

- `conflict_id`;
- resolution basis;
- current committed `state_revision`;
- `state_delta_seq` for the revision-safe conflict mutation.

After `CONFLICT_RESOLVED`, every action in the conflict's current affected-action scope must have a later `ACTION_READINESS` recomputation before convergence.

### Reopening terminal unresolved conflict

If new material evidence, authority, external input, or human review arrives after terminalization and can change the conflict, emit `CONFLICT_REOPENED` for the same `conflict_id` rather than silently emitting a new `ACTIVE` event.

Required fields:

- `conflict_id`;
- `reopen_basis_ids` — non-empty IDs for the new material evidence/authority/input/review;
- affected action IDs;
- current committed `state_revision`;
- `state_delta_seq` for the revision-safe reopen mutation;
- `prior_terminal_state_revision` when the terminal event belongs to a prior run/episode and is not visible in the current trace;
- `scope_change_basis_ids` when affected-action scope changes.

The reopen revision must be newer than the terminal revision. `CONFLICT_REOPENED` returns the same conflict to `ACTIVE`; prior terminal readiness is no longer current and must be recomputed after subsequent resolution/reterminalization.

A plain `COMPOSITION_CONFLICT status=ACTIVE` after terminalization is invalid. Reopening requires explicit new material basis.

### Action readiness linkage

`ACTION_READINESS` must include `action_id`, state, and explicit prerequisite proposition/condition IDs.

When readiness is capped by a terminal unresolved conflict, it must also identify the relevant `conflict_id` or `conflict_ids`.

If such readiness is `DO_NOT_PROCEED`, it must additionally identify at least one independent `blocking_proposition_id` or `blocking_proposition_ids`. The current trace must make the blocker support observable; unresolved conflict itself is not a blocker.

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

A run may converge with a `TERMINAL_UNRESOLVED` conflict only when the terminal event is explicit, revision-safe, and each affected action is subsequently recorded as `VERIFY_BEFORE_ACTION`, `LEGAL_REVIEW_REQUIRED`, or independently supported `DO_NOT_PROCEED`.

A conflict resolved in the current run may converge only after every action in its affected scope has a post-resolution `ACTION_READINESS` event.

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
- conflict terminalization/resolution/reopen not linked to an accepted revision-safe `STATE_DELTA` affecting that conflict;
- terminal/resolved/reopen event whose `state_revision` differs from the linked committed revision;
- silent affected-action-scope shrink/change without an explicit revision-safe scope/dependency basis;
- silent `TERMINAL_UNRESOLVED → ACTIVE` reactivation;
- reopen without new material basis or without a newer committed revision;
- `RUN_CONVERGED` while any conflict remains `ACTIVE`;
- terminal unresolved conflict followed by `READY` / `READY_WITH_CONDITIONS` for an affected action;
- terminal unresolved conflict followed by `DO_NOT_PROCEED` without an independent current supported blocker;
- resolved conflict with no post-resolution readiness recomputation for an affected action;
- readiness before unresolved required conflict/stale state/authority applicability or freshness issue is reflected in the action state.

## Evidence status

A trace proves only events that are actually observable in it. It does not prove hidden model reasoning.

Therefore the freeze gate should rely on observable path properties such as file reads, event order, owner/route transitions, resolver calls/reuse/re-resolution, owner applicability decisions, revision-aware state-delta outcomes, composition-conflict lifecycle/reopen/scope transitions, source-attempt/fallback events, invalidation targets, and readiness outputs rather than chain-of-thought.
