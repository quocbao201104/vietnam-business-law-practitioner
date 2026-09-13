# BL5 — Tax Characterization / Events / Roles

## Owns

Determining the tax-relevant characterization of an already resolved business fact pattern, including which committed business event(s) are legally relevant as tax events/triggers, taxpayer/payer/recipient/withholder roles, and candidate tax regimes that must be resolved under current authority.

This unit owns **tax characterization and statutory tax-role propositions**. It does not reconstruct whether the underlying contract, payment, employment, ownership, transfer, foreign-payment, or customs event actually occurred.

## Does not own

- entity/ownership/corporate state — BL2;
- transaction formation/content/performance or factual occurrence of payment/service/transfer events — BL3;
- breach/remedy state — BL4;
- employee/contractor or employment-law employer classification — BL6;
- public-law permission/compliance — BL7;
- FX/cross-border-payment, investment, trade/customs classification — BL8;
- preferential incentive/exemption/holiday entitlement after taxable scope is established — `incentives-structuring-economics.md`;
- bookkeeping/accounting recognition.

## Activate when

Use when the answer depends on:

- which already-resolved business event(s) are legally relevant as a tax event/trigger;
- who may be taxpayer, payer, recipient, withholding party, employer-for-tax-purposes, transferor, transferee, distributor, service recipient, or another tax-relevant statutory actor;
- whether one business transaction produces several tax positions;
- whether a payment label accurately reflects its tax characterization;
- whether an upstream classification change requires tax re-analysis;
- whether an event falls inside/outside taxable scope, including exclusions integral to defining the regime;
- which tax regime(s) must be verified before base/rate/document questions can be answered.

Skip or compress when the tax characterization/roles are already reliably committed and only a base/rate/timing or documentation question remains.

## Required state

Where material, consume from shared state:

- legal entity/actor state from BL2;
- transaction/content/payment/performance state from BL3;
- employment classification from BL6;
- foreign payment/investment/trade classification from BL8;
- relevant dates and places;
- payer/payee/beneficiary relationships;
- ownership/related-party facts where already resolved by their owner;
- committed evidence that the underlying business event occurred;
- current/historical authority where the tax characterization depends on law.

A sibling BL5 or upstream unit need not be loaded merely because its committed proposition is consumed. Reopen only when the owned proposition is unresolved, disputed, stale, contradictory, or material to reopen.

## Core distinctions

### Business event occurrence ≠ tax-event significance

Upstream owners establish whether the business event actually occurred.

BL5 asks a different question:

```text
resolved business event
→ is this event legally relevant as a tax event/trigger?
→ what tax characterization/role follows?
```

Do not infer or reconstruct the underlying service, payment, transfer, employment, ownership, or cross-border event merely to reach a tax result.

### Business label ≠ tax characterization

`service fee`, `salary`, `commission`, `loan`, `dividend`, `reimbursement`, `royalty`, `capital contribution`, `sale proceeds`, or another commercial label is evidence about the transaction, not the tax conclusion.

Consume the underlying owned facts and resolve the tax characterization under current authority.

### One transaction ≠ one tax proposition

A single transaction may create several independent tax questions.

For example, the same payment may create separate propositions about:

- taxpayer/withholder role;
- VAT or transaction-tax treatment;
- income-tax treatment;
- documentary/invoice conditions;
- deductibility/credit conditions;
- timing;
- incentive eligibility.

Do not collapse them into one status called `tax compliant`.

### Taxable-scope exclusion ≠ incentive entitlement

This unit owns exclusions/non-taxable characterization only when they are integral to determining whether the event falls within the taxable regime at all.

`incentives-structuring-economics.md` owns a claimed preferential benefit, exemption, holiday, or incentive after the relevant taxable regime/business state is otherwise established and entitlement depends on qualifying conditions.

Do not let the word `exemption` create dual ownership. Ask what proposition is being decided.

### Contractual tax allocation ≠ statutory liability

BL3 may establish that one party agreed to bear or reimburse a tax cost. That does not determine who the statute treats as taxpayer, withholding party, filer, or liable person.

Keep separate:

```text
contractual economic allocation — BL3
statutory tax role/consequence — BL5
```

### Cash movement ≠ taxable event

Payment or receipt may be relevant evidence, but the tax event/timing can depend on transaction type, recognition rule, invoice/event date, transfer/completion state, or another legal trigger.

Do not use `money moved` as a universal tax trigger.

### Upstream classification ≠ BL5-owned reconstruction

If BL6 has not resolved whether a worker is an employee/contractor or who is the employment-law employer, BL5 must not choose that classification merely to compute tax/contribution consequences.

If BL8 has not resolved whether a foreign payment is service payment, loan, capital contribution, investment flow, or another cross-border mode where that classification is material, BL5 must not silently reconstruct it.

Use a conditioned tax proposition or return a signal to the accountable owner.

### Related-party fact ≠ tax consequence

Corporate/relationship facts may activate a tax rule, but BL5 must resolve the specific tax test. Do not treat a generic `related party` label as the tax conclusion.

## Contribution coverage and statutory roles

Activate this unit for compulsory social-insurance/contribution coverage even
when no tax question is open. Consume BL6 employment/employer state and relevant
work-period, remuneration, concurrent-employment, nationality/residency or other
facts only insofar as the scheme's verified rules make them material.

Identify the scheme and temporal anchor; resolve coverage, ordinary exclusions,
participant and legally liable contributor separately under live authority.
Employee status is an input, not automatic coverage of every scheme. Record
`regime_kind: CONTRIBUTION`, scheme identity, coverage status, contributor roles,
BL6 dependency and authority/applicability links. This is not a tax conclusion.
Return covered/conditional/excluded/unresolved state to computation or evidence
only as needed. Ordinary coverage exclusions remain here; a separately claimed
preferential relief goes to incentives. Never reclassify employment to reduce cost.

## Decision procedure

1. **State the tax proposition.** Example: `Who is the statutory withholding party for payment P?` or `Does committed business event E fall within taxable scope?`
2. **Consume the business fact pattern.** Use committed BL2/BL3/BL6/BL8 propositions. Do not reconstruct whether the underlying event occurred.
3. **Map resolved events to tax significance.** Identify which committed sale/service/payment/employment/transfer/distribution/import-related or other event is legally relevant as a tax event/trigger.
4. **Identify candidate statutory roles.** Taxpayer, payer, recipient, withholder, employer-for-tax-purposes, transferor/transferee, or another role as supported by current authority. Do not use this step to decide employment-law employer status owned by BL6.
5. **Identify candidate tax regimes and taxable-scope exclusions.** Do not decide by transaction nickname alone; route preferential incentive/exemption entitlement to the incentives unit.
6. **Resolve authority live.** Use proposition-specific temporal anchors and current/historical authority.
7. **Commit characterization/role state.** Supported, conditional, disputed, unresolved, or not applicable.
8. **Hand downstream within BL5.** Base/rate/timing questions go to `base-method-rate-timing.md`; invoice/document questions go to `documentation-invoice-evidence.md`; preferential incentive/structuring questions go to `incentives-structuring-economics.md` only when material.

## Proposition pattern

```text
P-BL5-CHAR-01
business_event: <resolved upstream event>
tax_characterization: <candidate/resolved>
statutory_role: <taxpayer / withholder / other>
regime: <candidate/resolved>
temporal_anchor: <event date>
status: SUPPORTED / CONDITIONAL / DISPUTED / UNRESOLVED / NOT_APPLICABLE
```

Do not encode current rates/thresholds in this state.

## Evidence requirements

Potential evidence includes:

- committed BL3 agreement/payment/performance propositions;
- invoices/receipts/payment records as evidence of facts, not automatic tax conclusions;
- payroll/worker records consumed after BL6 classification where material;
- ownership/transfer records consumed from BL2;
- foreign-payment/trade classification consumed from BL8;
- statutory registrations/identifiers where tax role depends on them;
- authority supporting the tax characterization.

Preserve evidence provenance separately from the legal conclusion.

## Live authority triggers

Use Authority Resolver where the result depends on:

- taxpayer/withholder definitions;
- taxable/non-taxable characterization;
- exclusions integral to taxable scope;
- current treatment of a transaction type;
- related-party/special-regime definitions;
- historical tax law at the event date.

Preferential incentive/exemption/holiday entitlement belongs to `incentives-structuring-economics.md` after taxable scope is sufficiently resolved.

Do not hardcode current statutory definitions, rates, thresholds, scope exclusions, forms, or article numbers as stable knowledge.

## Cross-track handoffs

### From BL2

Consume entity/ownership/control/relationship facts only where they are already committed and tax-relevant. BL5 owns the tax consequence, not the corporate proposition.

### From BL3

Consume transaction terms, payment facts, commercial tax allocation, and performance state. BL3 owns whether those business events occurred; contractual allocation never substitutes for statutory tax-role analysis.

### From BL6

Consume committed employee/contractor and employment-law relationship/employer propositions where material. BL5 owns only tax/withholding/contribution consequences of that committed or conditioned state.

If classification is under review, keep dependent tax propositions conditional or `VERIFY_BEFORE_ACTION`; do not promote the competing employment classification yourself.

### From BL8

Consume foreign-payment/investment/trade classification when material. BL5 owns the tax consequence; BL8 owns the cross-border mode/classification.

### To sibling BL5 units

Return committed characterization/tax-event/role propositions. Siblings must not independently reconstruct them unless a contradiction requires review.

## Failure modes

- BL5 deciding whether the underlying business event occurred instead of consuming upstream state;
- transaction nickname used as tax classification;
- contractual tax clause treated as statutory liability;
- one payment mapped to one universal tax treatment;
- cash movement treated as universal tax trigger;
- taxable-scope exclusion and incentive entitlement given duplicate owners;
- BL5 reclassifying worker or employment-law employer instead of consuming BL6;
- BL5 reclassifying foreign payment instead of consuming BL8;
- related-party label treated as complete tax consequence;
- current tax rule applied to historical event without temporal verification;
- downstream rate/document analysis performed before the tax role/regime is sufficiently resolved.

## Escalation

Increase verification for cross-border payments, related-party transactions, worker-classification uncertainty, ownership transfers, restructurings, distributions, unusual mixed transactions, historical events spanning law changes, or any characterization whose error would materially change filing/payment/action readiness.