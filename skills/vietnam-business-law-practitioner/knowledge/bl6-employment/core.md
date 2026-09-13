# BL6 — Employment / People-side Business Law

BL6 resolves the legal state and employer-side pathway for business relationships with workers: relationship classification, employment terms/current state, performance/conduct management, restructuring/separation, and post-employment business protection.

This `core.md` is a **JIT router**, not the full employment handbook. Load only the capability unit needed for the material proposition.

## Owns

BL6 owns propositions about:

- employee/contractor and employment-law employer/relationship classification;
- employment-specific engagement terms and current work state;
- performance/conduct/capability issue classification and lawful employer-action pathway;
- restructuring, organizational-change and separation pathways;
- employment-state consequences of separation;
- employment-specific confidentiality and post-employment business-protection propositions.

BL6 does **not** own every consequence of an employment fact merely because the matter involves a worker.

## Does not own

- corporate entity/decision-maker authority or approval — BL2;
- ordinary commercial-contract propositions outside the employment relationship — BL3;
- dispute remedies, limitation/deadline and procedure — BL4;
- tax, withholding, BHXH and other contribution consequences — BL5;
- privacy/data/monitoring, sector regulation or other public-law compliance — BL7;
- foreign-investment/FX/trade/cross-border propositions — BL8.

## Core distinctions

- contract label ≠ employment classification;
- employee classification ≠ employer identity automatically resolved;
- employment relationship ≠ every private term valid/effective;
- performance problem ≠ misconduct;
- misconduct ≠ automatic dismissal;
- desired outcome ≠ legal ground/pathway;
- restructuring ≠ poor performance ≠ misconduct;
- management instruction ≠ unlimited unilateral-change power;
- termination ≠ all obligations end;
- confidentiality ≠ non-compete ≠ non-solicit;
- worker consent ≠ privacy/regulatory compliance;
- employment classification ≠ tax/contribution consequence;
- tax economics feedback ≠ reclassification ground.

## JIT capability routing

### Relationship / employer classification

Load `relationship-classification.md` when the question depends on:

- employee/contractor/work-relationship classification;
- who the employment-law employer is;
- whether contract labels match actual work facts;
- review of a committed classification after new non-tax evidence.

### Engagement / terms / work state

Load `engagement-terms-work-state.md` when classification is sufficiently resolved and the question depends on:

- hiring/probation/onboarding terms;
- role/remuneration/workplace/schedule/leave/current employment state;
- employment-specific term validity/effect;
- a proposed change to ongoing employment terms/state.

### Performance / conduct / employer action

Load `performance-conduct-employer-action.md` when the question depends on:

- poor/disputed performance;
- misconduct/conduct/attendance/capability;
- warnings, investigation, discipline or other ongoing employer-management action;
- selecting the lawful action pathway from committed facts rather than a desired outcome.

### Restructuring / separation / protection

Load `restructuring-separation-protection.md` when the question depends on:

- restructuring/redundancy/organizational change;
- unilateral or mutual separation;
- whether an upstream performance/conduct pathway can support final separation;
- final employment state and continuing obligations;
- confidentiality, return of property/access, non-solicit/non-compete or other post-employment protection.

Do not load all four units by default.

## Sibling JIT rule

BL6 sibling units are **not a mandatory pipeline**.

A committed BL6 proposition may be consumed directly from shared state without loading its owning sibling when it is already reliable and not material to reopen.

Load the sibling only when its proposition is unresolved, disputed, stale, contradictory, or material to the current action.

Examples:

```text
Employee relationship already committed; user asks only whether proposed pay/workplace change is lawful
→ engagement-terms-work-state
```

```text
Performance issue already committed; user asks whether final separation is supportable
→ restructuring-separation-protection
```

Do not force:

```text
classification
→ terms
→ performance/conduct
→ separation
```

for every employment question.

## Internal ownership rules

### Relationship classification precedes dependent consequences

Where employee/contractor or employer state is material and unresolved:

```text
relationship-classification
→ committed / conditioned BL6 relationship state
→ dependent BL6 / BL5 propositions
```

A downstream unit must not independently reconstruct the classification merely to continue.

### Performance/conduct classification precedes dependent separation

Where a proposed separation relies on performance or misconduct:

```text
performance-conduct-employer-action
→ committed issue/action-path proposition
→ restructuring-separation-protection
```

The separation unit must not invent a performance/misconduct ground because the employer wants to terminate.

### Tax/BHXH consequences do not flow backward into classification

BL5 consumes BL6 relationship/employer state for tax, withholding, BHXH or other contribution consequences.

```text
BL6 classification
→ BL5 consequence
```

not:

```text
BL5 cheaper tax result
→ BL6 reclassifies worker
```

Tax economics alone never justify relationship or employer reclassification.

### Privacy/monitoring is a separate public-law proposition

BL6 may decide that monitoring/system evidence is relevant to an employment proposition. BL7 decides whether collection/processing/monitoring is legally permitted and compliant where material.

Evidence usefulness does not absorb privacy legality into BL6.

## Reclassification lifecycle

A committed BL6 relationship classification must not change silently.

When new non-tax facts/evidence materially contradict the committed state:

```text
CONTRADICTION_SIGNAL / CLASSIFICATION_SIGNAL
→ RECLASSIFICATION_REVIEW
→ prior committed state remains visible during review
→ dependent actions may become VERIFY_BEFORE_ACTION
→ RECLASSIFICATION_COMMITTED only after BL6 resolves the review
```

Do not promote a competing classification merely because it creates a preferred tax, termination or business outcome.

## Upstream / cross-track dependency rules

BL6 consumes other owners' propositions rather than reconstructing them:

- BL2 owns corporate actor/authority/approval state;
- BL4 owns claim/remedy/deadline/procedure once an employment issue becomes a dispute;
- BL5 owns tax/contribution consequences;
- BL7 owns privacy/data/monitoring and other regulatory compliance;
- BL8 owns cross-border/investment/FX/trade propositions where material.

If downstream evidence contradicts an upstream proposition, emit a signal to its accountable owner instead of silently rewriting it.

## Live authority behavior

Stable BL6 knowledge defines decision structure and ownership. Use Authority Resolver whenever current/historical law materially determines:

- relationship/employer classification;
- required employment terms or worker protections;
- probation, pay, working-time, leave or change rules;
- performance-management/disciplinary process;
- restructuring/separation pathways and required process;
- post-employment confidentiality/restrictive obligations;
- historical rules at the relevant work/action/separation date.

Do not hardcode wage figures, probation limits, working-hour limits, leave entitlements, notice periods, severance/payment formulas, discipline steps, protected categories, restrictive-covenant rules, forms, or article numbers.

Before an irreversible employer action, re-resolve stale authority when a legal change could materially affect ground, process, option set or action readiness.

## Handoff rules

- BL2 → BL6: committed entity/authority/approval state where material; BL6 owns the employment proposition.
- BL6 → BL5: committed/conditioned relationship, employer, pay and separation facts; BL5 owns tax/withholding/BHXH/contribution consequences only.
- BL6 ↔ BL7: BL6 owns employment merits/pathway; BL7 owns privacy/data/monitoring/regulatory compliance.
- BL6 → BL4: committed employment merits/pathway/state when challenged; BL4 owns dispute posture/remedies/deadlines/procedure.
- BL5 → BL6: tax economics normally return as `FEEDBACK`; only new non-tax facts/evidence may justify classification review.

## Failure modes

- freelancer/consultant label treated as dispositive;
- payer/brand/corporate role treated as automatic employer;
- signed employment term treated as automatically valid against mandatory law;
- poor performance relabeled misconduct;
- misconduct treated as automatic dismissal;
- desired `remove employee` outcome used to invent a ground;
- restructuring used to disguise performance/misconduct termination;
- monitoring evidence pursued without BL7 where material;
- NDA treated as automatic non-compete;
- tax/BHXH economics used to reclassify worker/employer state;
- BL4 dispute procedure absorbed into employment merits;
- current employment rules recalled from memory;
- loading the whole employment handbook for a narrow classification, term or action question.
