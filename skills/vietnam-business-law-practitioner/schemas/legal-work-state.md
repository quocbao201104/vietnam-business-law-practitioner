# Legal Work State — Semantic Contract

This is a semantic contract, not a requirement to emit JSON or persist every field for every request.

Use only the depth needed for the decision.

## Objective

What business outcome is the user trying to achieve?

Examples: proceed, sign, structure, hire, terminate, collect, defend, launch, invest, import, exit.

## Actors

For each material actor, distinguish:

- identity;
- person/entity;
- asserted role;
- verified legal/business role;
- jurisdiction;
- relationship to other actors.

## Facts

Every material factual proposition should preserve its evidence status:

- `USER_ASSERTED`
- `DOCUMENTED`
- `EXTERNALLY_VERIFIED`
- `DISPUTED`
- `UNKNOWN`

A statement in a contract is `DOCUMENTED`; it is not automatically externally true.

## Timeline

Record only dates capable of changing the legal result, such as:

- formation;
- transaction/closing;
- performance;
- breach/event;
- notice;
- tax/regulatory event;
- proposed future action;
- relevant law effective date.

## Issues

Each material issue has:

- issue description;
- owning BL track;
- open/resolved status;
- dependencies.

## Classifications

A legal classification is separate from user labels.

Suggested status:

- `CANDIDATE`
- `LIKELY`
- `CONFIRMED`
- `DISPUTED`
- `UNRESOLVED`

Only the owning track may promote a material classification.

## Authorities

A material authority record should capture enough context to prevent temporal/authority drift:

- proposition supported;
- source;
- authority type;
- lifecycle status;
- effective period;
- relevant passage/provenance;
- amendment/replacement context if material.

Lifecycle status may include:

- `CURRENT_BINDING`
- `FUTURE_EFFECTIVE`
- `HISTORICAL`
- `AMENDED`
- `SUPERSEDED`
- `SUSPENDED`
- `UNCERTAIN`

Authority type may include:

- statute/regulation;
- treaty;
- authoritative judicial instrument/precedent where applicable;
- official guidance;
- practice material;
- academic/secondary material;
- research-only lead.

## Decisions

Each material decision should identify:

- decision ID/description;
- owner;
- conclusion;
- status;
- dependencies;
- explicit conditions;
- authorities/evidence relied on.

Useful status:

- `SUPPORTED`
- `SUPPORTED_WITH_CONDITIONS`
- `AMBIGUOUS`
- `INSUFFICIENT_FACTS`
- `AUTHORITY_UNCERTAIN`
- `CONFLICTING_AUTHORITY`
- `SPECIALIST_REVIEW_REQUIRED`

Do not use false-precision probability/confidence percentages.

## Open Conditions

Track unresolved matters only when they could change classification, regime, decision, or action readiness.

For each open condition record:

- what is unresolved;
- why it matters;
- what decisions depend on it;
- whether it is blocking or can be handled conditionally.

## Risks

Separate, where useful:

- substantive legal risk;
- tax/financial legal risk;
- regulatory risk;
- procedural/deadline risk;
- evidentiary risk;
- enforcement risk.

## Actions

Actions may be:

- immediate;
- conditional;
- deferred;
- specialist/human escalation.

## Readiness

Final action-readiness state:

- `READY`
- `READY_WITH_CONDITIONS`
- `VERIFY_BEFORE_ACTION`
- `LEGAL_REVIEW_REQUIRED`
- `DO_NOT_PROCEED`

Readiness is distinct from risk severity.

## Reclassification

Never silently replace a material classification.

When new evidence changes classification:

1. identify previous classification;
2. identify new candidate/classification;
3. identify owner;
4. record reason/evidence;
5. identify dependent decisions;
6. invalidate affected downstream conclusions;
7. recompute only affected decisions.
