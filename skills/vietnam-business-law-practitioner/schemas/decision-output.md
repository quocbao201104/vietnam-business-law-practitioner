# Decision Output — Semantic Contract v0.6

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

Expose only unresolved facts, authority, classification, route, conflict, or condition capable of changing an affected action.

A `TERMINAL_UNRESOLVED` composition conflict must remain visible here with the remaining external verification/input or human-review need. Do not render it as if the owners agreed.

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

### READY

Use only when:

- all material prerequisite propositions are positively resolved;
- no unresolved material condition remains for that action;
- no blocking proposition exists;
- no `ACTIVE` or `TERMINAL_UNRESOLVED` composition conflict affects the action;
- no stale/invalidated dependency remains in the action's dependency closure;
- required authority freshness is satisfied;
- readiness is based on the current state revision.

`No known blocker` is not enough.

### READY_WITH_CONDITIONS

Use only when:

- the action is not presently blocked by an unresolved legal question;
- one or more explicit, objectively identifiable preconditions remain;
- the legal effect/pathway for satisfying those conditions is sufficiently resolved;
- no `ACTIVE` or `TERMINAL_UNRESOLVED` composition conflict affects the action;
- the action becomes READY once those named conditions are satisfied and no new material issue appears.

Do not use this state when the condition itself is legally uncertain or its applicability is unresolved; use `VERIFY_BEFORE_ACTION` instead.

### VERIFY_BEFORE_ACTION

Use when a material fact, classification, route, authority applicability/freshness question, stale dependency, or composition conflict remains unresolved and could change whether/how the action may proceed.

A `TERMINAL_UNRESOLVED` conflict may legitimately converge here when the remaining issue is explicit and requires external verification/input before acting.

### LEGAL_REVIEW_REQUIRED

Use when the runtime can state the current position/options but the action is materially high-impact/irreversible or requires specialist human judgment beyond safe runtime resolution. This is an action outcome, not a generic disclaimer and not a substitute for analysis.

A `TERMINAL_UNRESOLVED` conflict may legitimately converge here when the remaining conflict requires human legal judgment rather than another available runtime step.

### DO_NOT_PROCEED

Use when a current supported proposition prohibits the action, or a required legal prerequisite is definitively absent and cannot be cured before the proposed action.

An unresolved conflict alone does not justify this state.

When `DO_NOT_PROCEED` coexists with an `ACTIVE` or `TERMINAL_UNRESOLVED` conflict, the readiness basis must identify at least one **independent current supported blocker** (`blocking_proposition_id` or equivalent). The blocker must not merely restate the conflict or select one side of it.

## Constraints and readiness

A `CONSTRAINS` edge limits options but does not automatically change readiness.

A constraint affects readiness only when an accountable owner explicitly links the constrained proposition/condition to the action as a prerequisite or blocker.

The synthesizer may not create that link by inference merely because a constraint appears important.

## Synthesizer permissions

The synthesizer may **derive** composition; it may not perform new specialist legal reasoning.

It MAY:

- project resolved propositions onto user actions;
- follow explicit dependency/constraint-to-action links;
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
- invent a permission, exception, remedy, obligation, legal test, blocker, or action prerequisite;
- silently repair a missing route.

## Composition conflicts

When owned propositions conflict materially, create/retain a `COMPOSITION_CONFLICT` and return it to the relevant owners.

A new conflict is `ACTIVE`. While it remains `ACTIVE`, do not present the affected action as converged if another material runtime resolution step is still available.

After owner review, the conflict may become:

- `RESOLVED` — the owned proposition/condition state is coherent enough to recompute readiness normally; or
- `TERMINAL_UNRESOLVED` — no material internal resolution step remains in the current run, the remaining external fact/authority/human judgment is explicit, and affected actions have been recomputed to non-READY readiness.

For `TERMINAL_UNRESOLVED`, affected actions must be `VERIFY_BEFORE_ACTION` or `LEGAL_REVIEW_REQUIRED`, unless an independent supported blocker justifies `DO_NOT_PROCEED`. If `DO_NOT_PROCEED` is used, expose the independent blocker identity in the readiness basis; the conflict itself cannot serve as that blocker.

The synthesizer must not select the conclusion that seems more reasonable or business-friendly, and terminalization must not be used to hide an available late-route, authority, reclassification, contradiction, stale-state, or specialist step.

If a terminal conflict is explicitly reopened after new material input, prior terminal readiness is no longer current merely because it existed. Recompute affected readiness from the reopened current state.

If a conflict becomes `RESOLVED`, recompute readiness for every action in its current affected-action scope before final convergence.

## Cross-track synthesis example

```text
P-BL2-01: company has authority to enter agreement — supported
P-BL3-02: agreement can be formed — supported
P-BL7-03: operating approval required before commencement — supported

ACTION A: sign agreement
→ dependencies satisfied
→ READY

ACTION B: begin regulated operation
→ explicit prerequisite P-BL7-03 not yet satisfied
→ READY_WITH_CONDITIONS if the approval pathway/effect is fully resolved
→ VERIFY_BEFORE_ACTION if approval applicability/path remains unresolved
→ DO_NOT_PROCEED if a supported prohibition/blocker applies to the proposed commencement
```

The final prose may say:

`The company can enter the agreement, but it should not begin the regulated activity until the required approval position is resolved and, if required, the approval is obtained.`

This is deterministic projection of owned propositions, not a new substantive legal conclusion.

## Authority and freshness

If an action depends on volatile current law, readiness must reference authority results whose freshness requirement is satisfied at the action's `as_of` date/state revision.

A cached authority result that is stale, superseded, suspended, affected by an authority-change signal, or whose **final proposition-level authority support remains insufficient/unresolved** cannot support `READY` until re-resolved or explicitly reflected in non-READY readiness.

A single source/adapter attempt with `SOURCE_UNAVAILABLE`, `SOURCE_DRIFT`, or `SOURCE_LAGGING` does **not** by itself cap readiness when another sufficient official path produces a usable final authority result and the accountable owner records current applicability.

## Convergence

Do not render final readiness as if the reasoning loop has converged while a material late-route signal, contradiction/reclassification review, stale dependency, `ACTIVE` composition conflict, or required authority freshness failure still affects the action.

A `TERMINAL_UNRESOLVED` conflict may be part of a converged run only when its remaining uncertainty/review need is explicit, no further material internal resolution step remains, and every affected action is already in non-READY readiness.

A resolved conflict may be part of a converged run only after every action in its affected scope has been recomputed after the resolution transition.

A run may legitimately converge to `VERIFY_BEFORE_ACTION`, `LEGAL_REVIEW_REQUIRED`, or `DO_NOT_PROCEED`.

## Proportionality

Simple questions should remain simple.

Complex or high-risk matters may expand into a fuller decision brief.

Do not force every response to contain every section if the missing section adds no value.

## Escalation

Human legal review is a decision outcome, not a generic disclaimer.

Escalate when actual facts justify it, including material irreversible employment actions, major ownership/corporate changes, substantial tax positions, regulatory blockers/enforcement, urgent deadlines, interim-relief needs, or serious dispute exposure.

Do not use escalation to avoid analysis that can safely be completed first.
