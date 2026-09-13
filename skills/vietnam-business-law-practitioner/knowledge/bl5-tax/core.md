# BL5 — Tax / Financial Legal Consequences

BL5 resolves statutory tax consequences of already resolved business/legal state: tax characterization and roles, base/method/rate/timing, documentary eligibility, and tax-aware incentive/structuring feedback.

This `core.md` is a **JIT router**, not a tax encyclopedia. Load only the capability unit needed for the material proposition.

## Owns

BL5 owns propositions about:

- tax characterization of resolved business events;
- taxpayer/withholder and other statutory tax roles;
- tax base/method/rate/threshold/timing under current/historical authority;
- tax-document/invoice/evidence conditions;
- tax incentive entitlement;
- tax-aware structuring/economic feedback to upstream owners.

BL5 does **not** own the underlying corporate, contract, employment, regulatory, or cross-border state merely because tax consequences depend on it.

## Does not own

- entity/ownership/governance/corporate state — BL2;
- transaction formation/content/obligation/performance — BL3;
- breach/remedy/dispute procedure — BL4;
- employment classification/action pathway — BL6;
- public-law permission/compliance — BL7;
- foreign-investment/FX/cross-border-payment/trade/customs classification — BL8;
- bookkeeping/accounting entries, financial reporting, or general financial analysis.

## Core distinctions

- business label ≠ tax characterization;
- one transaction ≠ one tax proposition;
- contractual tax allocation ≠ statutory tax liability;
- cash movement ≠ universal tax event;
- tax characterization ≠ base/rate/timing;
- invoice validity ≠ VAT credit ≠ deductibility ≠ accounting recognition;
- document defect ≠ transaction did not occur;
- tax incentive category match ≠ entitlement;
- lower nominal tax ≠ better structure;
- tax economics feedback ≠ upstream invalidation;
- tax law ≠ bookkeeping/accounting.

## JIT capability routing

### Characterization / events / roles

Load `characterization-events-roles.md` when the question depends on:

- what tax-relevant event/transaction occurred;
- taxpayer/payer/recipient/withholder or another statutory role;
- candidate tax regime(s);
- whether a payment/business label matches tax characterization;
- tax consequences that depend on upstream employment/ownership/cross-border classifications.

### Base / method / rate / timing

Load `base-method-rate-timing.md` when tax characterization is sufficiently resolved and the question depends on:

- taxable base;
- computation/withholding method;
- current rate/band/threshold;
- event/tax-period timing;
- historical/current/future-effective rule differences.

### Documentation / invoice / evidence

Load `documentation-invoice-evidence.md` when the question depends on:

- invoice/documentary requirements;
- VAT-credit/deduction/deductibility evidence conditions;
- payment/document conditions;
- whether a document defect changes a specific tax position;
- evidence needed to substantiate a tax treatment.

### Incentives / structuring / economics

Load `incentives-structuring-economics.md` when the question depends on:

- incentive/exemption/preference entitlement;
- tax consequence comparison across already lawful options;
- whether tax cost/timing/document burden materially changes an upstream option;
- returning tax-aware structuring feedback to BL2/BL3/BL6/BL8.

Do not load all four units by default.

## Sibling JIT rule

BL5 sibling units are **not a mandatory pipeline**.

A committed BL5 proposition may be consumed directly from shared state without loading its owning sibling unit when it is already reliable and not material to reopen.

Load the sibling only when the owned proposition is unresolved, disputed, stale, contradictory, or material to the current decision.

Examples:

```text
Taxpayer/withholder role already committed; user asks only current rate/base
→ base-method-rate-timing
```

```text
Tax treatment already committed; user asks whether invoice/payment evidence supports deductibility
→ documentation-invoice-evidence
```

Do not force:

```text
characterization
→ base/rate
→ documents
→ structuring
```

for every tax question.

## Upstream dependency rules

BL5 consumes upstream propositions rather than reconstructing them.

- BL2 owns entity/ownership/control/corporate state.
- BL3 owns transaction terms/payment/performance and contractual tax allocation.
- BL6 owns employee/contractor classification.
- BL8 owns foreign-payment/investment/trade/customs classification.

If upstream state is unresolved, BL5 keeps dependent tax propositions conditional or emits the appropriate contradiction/reclassification/late-route signal. It does not silently solve the upstream issue.

Examples:

```text
freelancer label + worker facts unresolved
→ BL6 owns classification
→ BL5 tax consequence remains conditional
```

```text
foreign payment mode unresolved
→ BL8 owns cross-border classification
→ BL5 does not guess one fixed foreign-contractor treatment
```

## Tax feedback semantics

Tax economics normally return to upstream owners as `FEEDBACK`, not automatic invalidation.

```text
BL3 transaction option
→ BL5 tax consequence is expensive
→ FEEDBACK to BL3
→ BL3 may reconsider/restructure
```

BL5 may invalidate only its own dependent propositions or exact downstream propositions connected by explicit `DEPENDS_ON` edges when upstream state changes.

A tax result does not make an otherwise valid transaction/corporate/employment state false merely because the economics are unattractive.

## Live authority behavior

Stable BL5 knowledge defines the decision structure and proof path. Use Authority Resolver whenever current/historical law materially determines:

- taxpayer/withholder definitions;
- taxable/non-taxable characterization;
- rates/thresholds/base/method;
- timing/recognition/payment/finalization rules;
- invoice/document conditions;
- deductions/credits/deductibility conditions;
- incentives/exemptions/preferences;
- historical tax rules at the relevant event date.

Do not hardcode rates, thresholds, filing deadlines, invoice fields, payment-condition amounts, incentive lists, forms, or article numbers.

Before a current/irreversible action, re-resolve stale authority where a changed tax rule could materially change amount, eligibility, option set, or readiness.

## Handoff rules

- BL2 → BL5: committed entity/ownership/relationship state where tax-relevant; BL5 owns tax consequence.
- BL3 → BL5: transaction/payment/performance/allocation facts; contractual allocation never substitutes for statutory tax analysis.
- BL6 → BL5: committed/conditioned employment classification; BL5 owns tax/contribution consequence only.
- BL8 → BL5: foreign-payment/investment/trade classification; BL5 owns tax consequence, not cross-border mode.
- BL5 → BL2/BL3/BL6/BL8: tax-economic consequence normally as `FEEDBACK`, with explicit uncertainty/authority freshness.

If downstream evidence contradicts an upstream classification, emit `CONTRADICTION_SIGNAL` to the accountable owner rather than rewriting it inside BL5.

## Failure modes

- rates/thresholds recalled from memory;
- payment label treated as tax characterization;
- contractual tax clause treated as statutory liability;
- invoice treated as automatic VAT credit/deductibility;
- cash movement treated as universal tax trigger;
- freelancer label used to decide employment-tax treatment without BL6;
- foreign supplier/payment mapped to one fixed tax treatment without BL8 where material;
- tax-document defect used to erase BL3 transaction state;
- lowest-tax option treated as automatically best/legal structure;
- tax feedback used to silently invalidate BL2/BL3/BL6/BL8 state;
- tax analysis presented as bookkeeping/accounting advice;
- loading the whole tax handbook for a narrow rate, invoice, or incentive question.
