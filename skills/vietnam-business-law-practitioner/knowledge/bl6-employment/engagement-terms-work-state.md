# BL6 — Engagement / Terms / Work State

## Owns

Determining the employment-specific engagement terms and current relationship state after the relevant BL6 relationship classification is committed or sufficiently conditioned, including hiring/probation/onboarding terms, remuneration/work conditions, leave/working-state propositions, and material changes to the ongoing employment relationship.

This unit owns **employment terms and current work-state propositions during ongoing employment**. It does not decide employee/contractor classification from scratch, tax consequences, corporate decision-maker authority, disciplinary/termination consequences, or post-employment survival/effect merely because a term is confidential or protective.

## Does not own

- employee/contractor and employment-law employer classification — `relationship-classification.md`;
- post-employment survival/effect of confidentiality, restrictive obligations, return/access and other separation protection — `restructuring-separation-protection.md`;
- corporate authority/approval of the employer-side actor — BL2;
- general commercial-contract propositions outside the employment relationship — BL3;
- dispute remedies/claim-preservation timing/procedure — BL4;
- tax, withholding, BHXH and other contribution consequences — BL5;
- privacy/data/monitoring and sector-regulatory compliance — BL7;
- cross-border/investment/FX/trade overlay — BL8.

## Activate when

Use when the decision depends on:

- whether an employment engagement has started, is in probation/onboarding, active, suspended, changed, or otherwise in a material current state;
- what employment-specific terms govern role, remuneration, workplace, schedule, leave, benefits, duties, mobility, confidentiality during ongoing employment, or other current conditions;
- whether a proposed employer-side change affects current employment terms/state;
- whether a hiring/probation/onboarding step has employment-law consequences;
- whether a current term/state must be established before performance, conduct, restructuring, or separation analysis.

Skip or compress when the material employment terms/current state are already reliably committed and the question only concerns performance/conduct, separation/post-employment survival, tax, privacy, or dispute procedure.

## Required state

Where material, consume:

- committed/conditioned relationship/employer classification from `relationship-classification.md`;
- legal entity/decision-maker state from BL2 where material;
- employment agreement, offer, annex, policy, onboarding/probation documents;
- role/duties and actual working arrangement;
- remuneration/benefits facts as employment terms, not tax treatment;
- location/schedule/working-time/leave/current-status facts;
- current confidentiality/duty terms where material;
- prior changes and consent/notice records;
- current policies and evidence of communication/acceptance where material;
- relevant temporal anchors;
- current/historical employment authority.

A sibling unit need not be loaded solely because its committed proposition is consumed. Reopen only when unresolved, disputed, stale, contradictory, or material to reopen.

## Core distinctions

### Engagement document ≠ relationship classification

A signed employment/service/probation document is evidence of terms, but `relationship-classification.md` owns whether the legal relationship is employment where that remains disputed.

Do not use this unit to back-solve classification from document title alone.

### Employment relationship ≠ every term valid/effective

Once employment status is established, each material term may still require separate analysis under mandatory employment law.

Do not infer:

```text
signed by worker
→ every term enforceable
```

or:

```text
company policy says X
→ X automatically governs
```

### Written term ≠ complete current work state

Current state may depend on later changes, actual assignments, leave/suspension, policy updates, role changes, or other legally relevant events.

Preserve the distinction between:

- original term;
- later valid change;
- temporary arrangement;
- actual practice;
- disputed/unauthorized practice.

### Current confidentiality ≠ post-employment survival/effect

This unit owns whether a confidentiality/duty term exists, what it requires, and its current effect **during ongoing employment**.

If the question is whether that duty survives or changes after separation, hand the committed current-term proposition to `restructuring-separation-protection.md`.

```text
Does Employee E currently have a confidentiality duty concerning X?
→ engagement-terms-work-state

Does that duty survive after Employee E leaves?
→ restructuring-separation-protection
```

Do not give both units ownership of the same temporal proposition.

### Employment term ≠ tax consequence

Salary, allowance, bonus, benefit, reimbursement, equity-linked compensation, or other employment terms are BL6 facts/state. BL5 owns statutory tax/withholding/contribution treatment.

### Employer instruction ≠ unlimited unilateral change power

Managerial direction may exist, but a material change to role, pay, workplace, schedule, or another protected term may require a distinct legal basis/process.

Do not assume `management can instruct` means `management can rewrite every employment term`.

### Consent ≠ privacy/regulatory compliance

Worker acknowledgement/consent to monitoring, data processing, background checks, device controls, or another data practice does not by itself resolve BL7 privacy/regulatory legality.

## Decision procedure

1. **State the employment-term/state proposition.** Example: `What role/pay/workplace/current confidentiality terms govern Employee E on date D?`
2. **Consume relationship classification.** Use committed/conditioned BL6 relationship/employer state; do not reconstruct it here unless contradictory evidence requires review.
3. **Inventory material employment sources.** Agreement, annex, policy, notice, role description, later change, actual state.
4. **Bind each source to chronology.** Distinguish original, later, temporary, superseded, disputed, or current state.
5. **Resolve mandatory-law constraints live where material.** Do not assume private agreement or policy can override mandatory employment rules.
6. **Separate current term from proposed change.** Identify what is true now and what the employer wants to change.
7. **Resolve change mechanism.** Agreement, notice, managerial direction, temporary measure, statutory pathway, or another supported mechanism.
8. **Commit current work state.** Active, probation/onboarding, changed, suspended, leave-related, disputed, conditional, or unresolved as needed for the decision.
9. **Hand downstream.** Performance/conduct questions go to `performance-conduct-employer-action.md`; post-employment survival/separation/protection questions go to `restructuring-separation-protection.md`; BL5/BL7 receive only their owned consequences.

## Work-state pattern

```text
P-BL6-STATE-01
relationship_dependency: P-BL6-REL-...
material_terms: [...]
current_role: <...>
remuneration_state: <...>
workplace/schedule_state: <...>
current_confidentiality_state: <if material>
change_event: <if any>
state: CURRENT / CHANGED / CONDITIONAL / DISPUTED / UNRESOLVED
```

Use only fields material to the decision.

## Evidence requirements

Potential evidence includes:

- employment/probation/offer documents;
- annexes and change notices;
- compensation/benefit records;
- role descriptions and organizational assignments;
- attendance/schedule/leave records;
- current confidentiality/policy terms;
- policy versions and communication records;
- worker/employer acknowledgements;
- actual-work records where current state differs from paper terms;
- approval/authority evidence when a material employer-side change depends on it.

Document title or signature does not erase mandatory-law or actual-state questions.

## Live authority triggers

Use Authority Resolver where current/historical law materially determines:

- required employment terms/form;
- probation/onboarding limits or conditions;
- remuneration/working-time/leave/benefit obligations;
- unilateral-change or temporary-change powers;
- mandatory employment protections affecting a current term;
- current effect of confidentiality/duty terms during ongoing employment;
- historical rules for the relevant engagement/change date.

Do not hardcode wage figures, contribution amounts, leave days, working-hour limits, employment-action notice periods, probation durations, forms, or article numbers as stable knowledge.

## Cross-track handoffs

### From relationship classification

Consume employee/contractor and employer state. If new term/work evidence materially contradicts the committed relationship classification, emit `CONTRADICTION_SIGNAL` to `relationship-classification.md` rather than silently rewriting it.

### To separation/protection

Provide the committed current confidentiality/duty proposition when post-employment survival/effect becomes material. Do not decide the post-employment proposition here.

### To BL5

Provide remuneration/payment/benefit and committed relationship facts. BL5 owns tax/withholding/BHXH or contribution consequences.

### To BL7

Route monitoring, employee-data, biometric/device, privacy, background-check, or sector-regulatory propositions to BL7.

### To BL2

If a material employment change depends on who has corporate authority/approval to make it, consume BL2 rather than inferring authority from job title.

### To BL4

If an employment-term dispute escalates into claim/remedy/procedure, BL6 keeps employment-law term/state ownership while BL4 owns dispute posture/remedy and claim/dispute-preservation timing/procedure.

## Failure modes

- employment document title used to bypass relationship classification;
- signed term treated as automatically valid against mandatory law;
- company policy treated as automatically binding;
- actual current work state ignored after later change;
- current confidentiality and post-employment survival/effect collapsed into one proposition owner;
- management instruction treated as unlimited unilateral-change power;
- remuneration term collapsed into tax treatment;
- worker consent treated as privacy compliance;
- current rates/limits/leave/probation rules recalled from memory;
- every employment-term question loading performance/separation knowledge unnecessarily.

## Escalation

Increase verification for material pay/role/location changes, probation disputes, protected leave/state, unilateral changes, executive employment, cross-border work arrangements, current confidentiality duties whose post-employment survival may later matter, or any proposed change whose error could make a later discipline/termination pathway unsafe.
