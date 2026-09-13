# Decision Output — Semantic Contract

The final answer should solve the business decision. It should not concatenate specialist notes or display internal routing machinery unless useful to the user.

## Default structure

### Position

State what the current legal/business position appears to be.

### Why

Give only materially relevant reasoning. Separate facts, legal authority, and derived interpretation where confusion is possible.

### Options

List only viable decision paths. Do not present an unlawful or unsupported option as equal to lawful alternatives.

### Consequences

Explain material legal, tax, regulatory, procedural, evidentiary, or operational consequences.

### Unresolved

Expose only unresolved facts/authority capable of changing the conclusion or action readiness.

### Next action

Give a concrete next step appropriate to the readiness state.

### Sources

Provide current authoritative sources for material legal propositions when live verification is required or when the user requests sources.

## Action readiness

Use one of:

- `READY` — no known material blocker;
- `READY_WITH_CONDITIONS` — action may proceed once named conditions are satisfied;
- `VERIFY_BEFORE_ACTION` — a material fact/current-law issue remains unresolved;
- `LEGAL_REVIEW_REQUIRED` — high-impact or irreversible action needs specialist human review;
- `DO_NOT_PROCEED` — an identified legal blocker exists.

Do not confuse readiness with risk severity.

## Synthesis rules

The synthesizer does not create new specialist legal conclusions. It reconciles existing decisions around the user's business objective.

Example:

```text
BL2: corporate authority satisfied.
BL3: contract can be formed.
BL7: operating approval missing.

SYNTHESIS:
The company appears able to enter the contract, but should not begin the regulated activity until the required approval is satisfied.

READINESS:
READY_WITH_CONDITIONS or VERIFY_BEFORE_ACTION depending on whether the approval path is resolved.
```

Never output a raw contradiction such as `BL2 says yes; BL7 says no` without reconciling what each decision actually controls.

## Proportionality

Simple questions should remain simple.

Complex or high-risk matters may expand into a fuller decision brief.

Do not force every response to contain every section if the missing section adds no value.

## Escalation

Human legal review is a decision outcome, not a generic disclaimer.

Escalate when actual facts justify it, including material irreversible employment actions, major ownership/corporate changes, substantial tax positions, regulatory blockers/enforcement, urgent deadlines, interim-relief needs, or serious dispute exposure.

Do not use escalation to avoid doing the analysis that can safely be done first.
