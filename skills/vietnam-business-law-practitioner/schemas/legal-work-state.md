# Legal Work State — Semantic Contract v0.2

This is a semantic contract, not a requirement to emit JSON or persist every field for every request.

Use only the depth needed for the decision, but every **material** state object must have stable identity and ownership.

## State revision

Maintain a monotonically increasing `state_revision`.

Tracks and specialists emit owner-scoped deltas against a known revision. They do not replace the whole Legal Work State. A stale write based on an older revision must be rejected or reconciled before it can overwrite newer owner state.

## Objective

What business outcome is the user trying to achieve?

Examples: proceed, sign, structure, hire, terminate, collect, defend, launch, invest, import, exit.

## Actors

For each material actor preserve:

- `actor_id`;
- identity;
- person/entity;
- asserted role;
- verified legal/business role;
- jurisdiction;
- relationship to other actors.

## Facts and evidence are separate dimensions

Do not use `USER_ASSERTED`, `DOCUMENTED`, or `EXTERNALLY_VERIFIED` as mutually exclusive truth states.

### Fact proposition

Each material factual proposition should have:

- `fact_id`;
- proposition;
- epistemic status;
- owner/custodian when relevant;
- temporal scope;
- linked evidence IDs.

Suggested epistemic status:

- `ASSERTED`
- `SUPPORTED`
- `CORROBORATED`
- `DISPUTED`
- `UNKNOWN`
- `RESOLVED`
- `STALE`

### Evidence

Evidence describes provenance, not truth.

Each material evidence item should have:

- `evidence_id`;
- linked `fact_id` or proposition ID;
- source type;
- source reference;
- date/time where material;
- reliability/context notes.

Source type may include:

- `USER`
- `DOCUMENT`
- `REGISTRY`
- `COUNTERPARTY`
- `THIRD_PARTY`
- `SYSTEM`
- `EXTERNAL_SOURCE`

A proposition may simultaneously be user-asserted, documented, and disputed. A document saying X is evidence that the document says X; it is not automatically proof that X is legally or factually true.

## Timeline and temporal anchors

There is no single universal relevant date.

Record only dates capable of changing the legal result, such as:

- formation;
- transaction/closing;
- performance;
- breach/event;
- notice;
- tax/regulatory event;
- customs entry;
- proposed future action;
- authority verification time.

Material authority-backed propositions should identify their own temporal anchor(s).

## Issues and route hypotheses

Each material issue has:

- `issue_id`;
- description;
- candidate/confirmed owning BL track;
- route status;
- open/resolved status;
- linked proposition IDs.

Route status:

- `ROUTE_CONFIRMED`
- `ROUTE_PLAUSIBLE`
- `ROUTE_UNRESOLVED`
- `ROUTE_REJECTED`

BL1 proposes initial routing. Any downstream owner may emit a `LATE_ROUTE_SIGNAL` when new evidence makes another track materially relevant.

## Classifications

A legal classification is separate from user labels.

Each material classification should have:

- `classification_id`;
- proposition/category;
- accountable owner;
- status;
- supporting/contradicting evidence IDs;
- temporal scope;
- dependency IDs where material.

Suggested status:

- `CANDIDATE`
- `UNDER_REVIEW`
- `LIKELY`
- `RESOLVED`
- `DISPUTED`
- `UNRESOLVED`
- `SUPERSEDED`

Only the accountable owner may commit a material reclassification.

## Proposition ownership

The main accountability unit is a material legal proposition.

Each proposition should identify:

- `proposition_id`;
- statement/question;
- accountable BL owner;
- status;
- temporal scope;
- dependencies;
- evidence/authority support;
- conditions.

Useful status:

- `SUPPORTED`
- `SUPPORTED_WITH_CONDITIONS`
- `AMBIGUOUS`
- `INSUFFICIENT_FACTS`
- `AUTHORITY_UNCERTAIN`
- `CONFLICTING_AUTHORITY`
- `SPECIALIST_REVIEW_REQUIRED`
- `STALE`
- `INVALIDATED`

Do not use false-precision probability/confidence percentages.

## Typed dependencies

Track-level routing is not an executable invalidation graph.

Material proposition dependencies use typed edges:

- `DEPENDS_ON`
- `CONSTRAINS`
- `SIGNALS`
- `FEEDBACK`

Only `DEPENDS_ON` automatically propagates `STALE` / `INVALIDATED` when the upstream proposition materially changes.

`SIGNALS` and `FEEDBACK` create review triggers only.

## Authorities

Each material authority result should have stable identity:

- `authority_id`;
- proposition it supports;
- source provenance;
- authority/legal-force type;
- lifecycle status;
- temporal anchor(s);
- effective period;
- `verified_at`;
- source version/amendment/replacement context;
- relevant passage/provenance;
- freshness requirement where material;
- case-applicability status assigned by the accountable proposition owner.

Lifecycle status may include:

- `CURRENT_BINDING`
- `FUTURE_EFFECTIVE`
- `HISTORICAL`
- `AMENDED`
- `SUPERSEDED`
- `SUSPENDED`
- `UNCERTAIN`

Authority/legal-force type may include:

- statute/regulation;
- treaty;
- authoritative judicial instrument/precedent where applicable;
- official guidance;
- practice material;
- academic/secondary material;
- research-only lead.

**Lifecycle is not applicability.** `CURRENT_BINDING` does not automatically mean the authority governs this transaction or proposition.

## Conditions

Each material unresolved condition should have:

- `condition_id`;
- description;
- why it matters;
- affected proposition/action IDs;
- status;
- whether blocking or conditionally manageable.

## Actions

Action readiness is per action, not global to the matter.

Each material action has:

- `action_id`;
- description;
- actor;
- material proposition dependencies;
- conditions;
- deadline/date where material;
- readiness state;
- readiness basis;
- `as_of` state revision/date.

Readiness states:

- `READY`
- `READY_WITH_CONDITIONS`
- `VERIFY_BEFORE_ACTION`
- `LEGAL_REVIEW_REQUIRED`
- `DO_NOT_PROCEED`

`READY` means all material prerequisites have been positively resolved, no unresolved material condition remains, no blocking proposition exists, and required authority freshness is satisfied. Absence of a known blocker is not enough.

## Risks

Separate, where useful:

- substantive legal risk;
- tax/financial legal risk;
- regulatory risk;
- procedural/deadline risk;
- evidentiary risk;
- enforcement risk.

Risk severity is distinct from per-action readiness.

## Reclassification state machine

Never silently replace a material classification.

Use:

```text
CLASSIFICATION_SIGNAL
→ RECLASSIFICATION_REVIEW
→ RECLASSIFICATION_COMMITTED
```

During review:

- the previous committed classification remains current;
- the competing candidate is explicit;
- materially dependent actions may move to `VERIFY_BEFORE_ACTION`;
- exact dependent propositions are identified.

When committed:

1. previous classification → `SUPERSEDED`;
2. new classification → `RESOLVED`;
3. only `DEPENDS_ON` dependents become `STALE` / `INVALIDATED`;
4. recompute only affected propositions/actions.

## Contradictory downstream evidence

A downstream track or specialist may not reconstruct upstream-owned state.

If contradictory evidence appears:

1. emit `CONTRADICTION_SIGNAL`;
2. identify affected upstream object/owner;
3. attach evidence;
4. mark dependent reasoning conditional or paused where material;
5. return to the accountable owner;
6. resume only from the updated shared state.

## Composition conflict

If current owned propositions conflict materially, create a `COMPOSITION_CONFLICT` with stable ID, involved propositions/owners, reason, and affected actions.

The synthesizer may not choose the preferred specialist conclusion.