# Runtime Trace — Observable Event Contract v0.3

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
- `AUTHORITY_RERESOLVE`
- `AUTHORITY_CHANGE_SIGNAL`

Where material include proposition ID, owner, temporal anchors, resolver status, and authority IDs.

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

## Composition events

- `COMPOSITION_CONFLICT`
- `CONFLICT_RESOLVED`
- `ACTION_READINESS`
- `RUN_CONVERGED`

`ACTION_READINESS` must include `action_id`, state, and explicit prerequisite proposition/condition IDs.

## Materiality events

When activation/skip is not obvious, emit `MATERIALITY_DECISION` with:

- candidate fact/proposition/issue
- material: true/false
- reason category
- affected route/classification/result/dependency/authority version/option set/readiness, if true

## Convergence

`RUN_CONVERGED` may be emitted only when all requested actions satisfy the stop condition in `runtime-composition.md`.

## Integrity

The trace checker should reject:

- non-monotonic sequence numbers;
- candidate SHA mismatch;
- fixture mismatch;
- malformed required fields;
- `READ` events whose file hash does not match the candidate checkout;
- specialist events without an owner;
- readiness before unresolved required conflict/stale state is closed, when encoded by the oracle.

## Evidence status

A trace proves only events that are actually observable in it. It does not prove hidden model reasoning.

Therefore the freeze gate should rely on observable path properties such as file reads, event order, owner/route transitions, resolver calls, invalidation targets, and readiness outputs rather than chain-of-thought.