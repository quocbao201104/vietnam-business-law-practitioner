# Decision Output — Semantic Contract v0.2

The final answer should solve the user's business decision without turning the synthesizer into a hidden ninth legal owner.

## Default structure

### Position

State the composed legal/business position supported by current owned propositions.

### Why

Give only materially relevant reasoning. Separate facts/evidence, authority, and derived owner conclusions where confusion is possible.

### Options

List only viable decision paths. Do not present an unlawful or unsupported option as equal to lawful alternatives.

### Consequences

Explain material legal, tax, regulatory, procedural, evidentiary, or operational consequences.

### Unresolved

Expose only unresolved facts, authority, classification, conflict, or condition capable of changing an affected action.

### Next action

Give concrete next steps mapped to per-action readiness.

### Sources

Provide the minimum sufficient authority set for material legal propositions when live verification is required or when the user requests sources.

## Readiness is per action

There is no single global readiness value for a multi-action matter.

Each material action receives one state:

- `READY`
- `READY_WITH_CONDITIONS`
- `VERIFY_BEFORE_ACTION`
- `LEGAL_REVIEW_REQUIRED`
- `DO_NOT_PROCEED`

Example:

```text
ACTION A — sign contract
READY

ACTION B — commence regulated service
DO_NOT_PROCEED until required approval exists
```

### READY positive-closure rule

`READY` means:

- all material prerequisite propositions are positively resolved;
- no unresolved material condition remains for that action;
- no blocking proposition exists;
- no unresolved composition conflict affects the action;
- required authority freshness is satisfied;
- action readiness is based on the current state revision.

`No known blocker` is not enough.

## Synthesizer permissions

The synthesizer may **derive** composition; it may not perform new specialist legal reasoning.

It MAY:

- project resolved propositions onto user actions;
- follow explicit dependency/constraint edges;
- apply deterministic readiness rules;
- expose blockers and conditions;
- detect unresolved dependencies;
- detect a `COMPOSITION_CONFLICT`;
- render the result in natural business-facing language.

It MAY NOT:

- promote factual propositions;
- create or change legal classifications;
- decide case applicability of authority;
- resolve a proposition owned by BL1–BL8;
- choose between conflicting specialist/owner conclusions;
- invent a permission, exception, remedy, obligation, or legal test;
- silently repair a missing route.

## Composition conflicts

When owned propositions conflict materially, create/retain a `COMPOSITION_CONFLICT` and return it to the relevant owners.

Affected actions become `VERIFY_BEFORE_ACTION` or stricter as appropriate. The synthesizer must not select the conclusion that seems more reasonable.

Example conflict record:

```text
COMPOSITION_CONFLICT
conflict_id: CC-01
proposition_a: P-BL3-04
proposition_b: P-BL7-02
owners: BL3, BL7
reason: incompatible conditions for commencing service
affected_actions: A-02
```

## Cross-track synthesis example

```text
P-BL2-01: company has authority to enter agreement — supported
P-BL3-02: agreement can be formed — supported
P-BL7-03: required operating approval is missing — supported

ACTION A: sign agreement
→ dependencies satisfied
→ READY

ACTION B: begin regulated operation
→ blocked by P-BL7-03
→ DO_NOT_PROCEED / READY_WITH_CONDITIONS depending on whether the missing approval is a current legal blocker or a resolvable precondition
```

The final prose may say:

`The company can enter the agreement, but should not begin the regulated activity until the required approval is obtained.`

This is deterministic projection of owned propositions, not a new substantive legal conclusion.

## Authority and freshness

If an action depends on volatile current law, readiness must reference authority results whose freshness requirement is satisfied at the action's `as_of` date/state revision.

A cached authority result that is stale, superseded, suspended, or affected by an authority-change signal cannot support `READY` until re-resolved.

## Proportionality

Simple questions should remain simple.

Complex or high-risk matters may expand into a fuller decision brief.

Do not force every response to contain every section if the missing section adds no value.

## Escalation

Human legal review is a decision outcome, not a generic disclaimer.

Escalate when actual facts justify it, including material irreversible employment actions, major ownership/corporate changes, substantial tax positions, regulatory blockers/enforcement, urgent deadlines, interim-relief needs, or serious dispute exposure.

Do not use escalation to avoid analysis that can safely be completed first.