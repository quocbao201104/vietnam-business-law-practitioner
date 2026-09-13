# BL6 — Relationship / Employer Classification

## Owns

Determining the legal nature of a work relationship and the employment-law actor state that downstream employment decisions depend on, including employee/contractor classification and who is acting as employer within BL6 ownership.

This unit owns **employment relationship classification**. It does not infer tax treatment from the label, reconstruct corporate authority, or decide a termination/discipline pathway merely because the relationship is classified.

## Does not own

- corporate entity/signing/decision-maker authority — BL2;
- ordinary commercial transaction propositions outside the employment relationship — BL3;
- dispute remedies/procedure — BL4;
- tax, withholding, BHXH or other contribution consequences — BL5;
- privacy/data/monitoring or sector-regulatory compliance — BL7;
- cross-border/investment/FX/trade overlay — BL8.

## Activate when

Use when a material decision depends on:

- whether a person is an employee, contractor, service provider, manager, representative, or another work-related legal category;
- whether the stated contract label matches the actual work relationship;
- who the employment-law employer is where group/company/platform/intermediary facts are material;
- whether a prior committed classification should be reviewed because new non-tax facts/evidence materially contradict it;
- whether downstream hiring, management, termination, tax/contribution, or protection analysis depends on the classification.

Skip or compress when the employment relationship and employer state are already reliably committed and cannot change the requested action.

## Required state

Where material, capture or consume:

- legal actors/entities from BL2;
- written agreement and role description;
- actual work performed;
- payment/remuneration structure as a fact, not tax conclusion;
- control, direction, supervision, scheduling, integration, tools/workplace, delegation/substitution, economic arrangement, and other legally relevant work facts;
- chronology and duration;
- who directs, pays, evaluates, disciplines, and may end the relationship;
- competing evidence and source provenance;
- relevant temporal anchors;
- current/historical employment authority where classification depends on law.

Do not promote one factual signal into the classification by itself unless current authority makes that signal dispositive.

## Core distinctions

### Contract label ≠ employment classification

`freelancer`, `collaborator`, `consultant`, `service provider`, `probationer`, `manager`, or another label is evidence about the intended arrangement, not the legal conclusion.

Resolve classification from the legally relevant facts and current/historical authority.

### Payment method ≠ relationship classification

Salary-like, invoice-based, commission-based, hourly, project-based, cash, or bank-transfer payment can be relevant evidence, but no payment format should automatically decide employee/contractor status.

BL5 consumes the committed BL6 classification for tax/contribution consequences; BL5 must not reverse this direction merely because one tax result is cheaper.

### Corporate role ≠ employment relationship

Founder, shareholder, director, legal representative, officer, or manager status does not by itself establish or negate an employment relationship.

BL2 owns corporate role/authority. BL6 separately resolves the employment-law relationship where material.

### One company group ≠ one employer

Parent, subsidiary, branch, affiliate, platform, staffing intermediary, or shared-services arrangement may involve several actors.

Do not assume the entity paying money, signing one document, or owning the brand is automatically the employment-law employer.

Consume BL2 entity state and resolve the BL6 employer proposition separately.

### Work fact ≠ tax consequence

Facts such as supervision, fixed schedule, workplace integration, invoice issuance, or payroll records may support classification analysis but do not themselves decide tax/BHXH consequences.

BL5 owns those consequences after BL6 commits or conditions the relationship state.

### Classification review ≠ tax optimization

A committed relationship may be reopened only when new non-tax facts/evidence materially undermine the prior classification under the owning rules.

Do not use:

```text
employee tax/contribution cost is high
→ classify contractor
```

Tax economics may create `FEEDBACK`, not a reclassification ground.

## Decision procedure

1. **State the exact relationship proposition.** Example: `Is Worker W in an employment relationship with Entity E for the relevant period?`
2. **Resolve actor identity.** Consume BL2 entity/actor state where several entities or representatives are involved.
3. **Separate written label from actual facts.** Record both without treating either as dispositive by default.
4. **Map legally relevant work facts.** Control/supervision, work organization, payment, integration, tools/location, duration, substitution/delegation, evaluation, discipline/termination control, and other authority-supported factors.
5. **Preserve conflicts.** Do not choose user statement, contract wording, payroll record, or operational evidence by source count alone.
6. **Resolve current/historical classification authority.** Use the relevant work period/decision date; do not apply current law backward without checking.
7. **Commit relationship state.** Supported, conditional, disputed, review-pending, not established, or unresolved.
8. **Commit employer state separately where material.** Do not collapse `employee` and `employer identity` into one proposition.
9. **Hand downstream.** Engagement/management/separation units consume the committed state; BL5 consumes it for tax/contribution consequences.

## Classification pattern

```text
P-BL6-REL-01
worker: <actor>
putative_employer: <entity>
period: <temporal scope>
written_label: <if any>
material_work_facts: [...]
classification: EMPLOYEE / NON_EMPLOYEE / CONDITIONAL / DISPUTED / UNRESOLVED
employer_state: <supported / conditional / disputed / unresolved>
```

These are reasoning states, not statutory labels to be hardcoded into final advice.

## Evidence requirements

Potential evidence includes:

- employment/service/collaboration agreements;
- job descriptions and internal policies;
- schedules, attendance, work allocation, approvals, reporting lines;
- instructions/supervision/evaluation records;
- payroll/payment/invoice records;
- tool/workplace/access provisioning;
- organizational charts and entity records;
- communications about leave, performance, discipline, replacement, or termination;
- evidence of independent business activity/substitution where relevant;
- contemporaneous records for the relevant period.

Preserve evidence provenance separately from classification status.

## Live authority triggers

Use Authority Resolver where current/historical law materially determines:

- employee/contractor or employment-relationship criteria;
- employer/joint/intermediary relationship classification;
- special worker categories;
- mandatory presumptions or exclusions;
- historical classification rules for the relevant work period.

Do not hardcode universal factor weights, numerical tests, labels, or article numbers.

## Cross-track handoffs

### From BL2

Consume legal-entity/actor facts. BL6 determines employment-law relationship/employer state; it does not rewrite corporate identity or authority.

### To BL5

Provide committed/conditioned employee/contractor and employer state. BL5 owns tax, withholding, BHXH and other contribution consequences only.

If BL5 surfaces new payroll/payment evidence inconsistent with the committed relationship, it should emit `CONTRADICTION_SIGNAL`; BL6 decides whether reclassification review is warranted.

### To BL7

If classification analysis exposes monitoring, biometric, employee-data, platform, immigration/sector, or other regulatory issues, route BL7 rather than resolving public-law compliance here.

### To BL4

If classification is disputed in an active claim/dispute, BL6 owns the relationship proposition while BL4 owns dispute posture/remedies/procedure.

## Failure modes

- freelancer/consultant label treated as dispositive;
- salary/invoice format treated as dispositive;
- founder/director/shareholder status treated as automatic employee or non-employee status;
- payer/brand/company group treated as automatic employer;
- tax cost used as a reclassification reason;
- BL5 tax treatment used to back-solve BL6 classification;
- one factual signal used as a universal employee test;
- current classification law projected backward without temporal verification;
- disputed evidence silently promoted into committed relationship state.

## Escalation

Increase verification for senior managers/founders, group-company arrangements, platform/intermediary labor, long-running contractor relationships, mixed evidence, cross-border workers, classification changes affecting termination or large contribution exposure, or any case where a mistaken classification would change action readiness.