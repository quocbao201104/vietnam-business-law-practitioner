# BL5 — Base / Method / Rate / Timing

## Owns

Determining the tax computation and timing structure for an already characterized BL5 proposition: applicable base, method, rate/threshold rule, taxable period/event timing, and the conditions that make those values current for the relevant action.

This unit owns **tax base/method/rate/timing propositions**. It does not own the upstream business characterization, invoice/document sufficiency, incentive entitlement, or accounting recognition.

## Does not own

- transaction/employment/ownership/cross-border classification — BL2/BL3/BL6/BL8;
- tax characterization/statutory role — `characterization-events-roles.md`;
- invoice/document/evidence conditions — `documentation-invoice-evidence.md`;
- incentive/structuring/economic feedback — `incentives-structuring-economics.md`;
- bookkeeping/accounting entries.

## Activate when

Use when a committed/conditioned tax characterization exists and the answer depends on:

- taxable base or computation method;
- current rate/threshold/band;
- gross-up/withholding computation mechanics where legally material;
- event/recognition timing;
- filing/payment period or legally relevant tax date;
- historical versus current rules;
- whether a changed rate/threshold affects a planned action.

Skip when the user only needs characterization, documentary eligibility, or structural feedback.

## Required state

Where material, consume:

- committed BL5 characterization/event/role proposition;
- transaction amounts/components from BL3;
- payment/performance/transfer dates from owning tracks;
- foreign-flow/trade state from BL8 where material;
- current/historical authority for base/rate/method/timing;
- any explicit exemption/incentive proposition already committed;
- relevant currency/valuation facts where legally required;
- uncertainty in amount/date inputs.

Do not load sibling units solely to consume already committed propositions.

## Core distinctions

### Tax characterization ≠ computation rule

Knowing that a transaction falls within a tax regime does not establish:

- the base;
- the applicable method;
- the rate/band/threshold;
- timing;
- filing/payment mechanics.

Resolve each material proposition separately.

### Rate ≠ effective tax burden

A headline statutory rate does not by itself establish the economic tax burden. Base, exemptions, thresholds, credits, deductions, gross-up, withholding, timing, and transaction structure may matter.

Do not present a remembered percentage as the answer to a broader economics question.

### Amount paid ≠ taxable base

Contract price, invoice amount, gross cash paid, net receipt, accounting value, customs value, and tax base can differ.

BL5 resolves the legally relevant base under the applicable tax regime; BL8 retains customs/trade valuation ownership where that is a separate proposition.

### Current rate ≠ historical rate

Bind tax computation to the event-specific temporal anchor. A current rate/threshold may not govern a historical transaction, and a future-promulgated rule may not yet govern today's action.

### Payment date ≠ universal tax timing

Tax timing may depend on invoice/event/transfer/performance/recognition/finalization or another legal trigger depending on the proposition.

Do not create one global `TAX_DATE`.

### Tax timing ≠ accounting recognition

A tax event or filing period is a legal tax proposition. Accounting recognition/bookkeeping belongs outside BL5's legal scope unless the accounting fact is merely evidence/input to a tax rule.

### Estimated amount ≠ resolved liability

If base inputs, classification, authority, or timing remain unresolved, present a conditional range/scenario rather than false precision.

## Contribution computation and periods

Activate on committed/conditioned contribution coverage from the characterization
unit; a tax characterization is not required for this path. Identify the scheme,
contribution period and contributor roles. Consume BL6 remuneration components
and work-state dates, then verify which components enter the contribution base,
any caps/floors, employer/worker allocation, rate, commencement/suspension/end
period and payment deadline under current/historical scheme authority.

Keep contribution base and period separate from PIT taxable income and tax period.
Record scheme, coverage dependency, contribution base/rule, allocation, period,
amount or conditional range, and authority support. Do not store live percentages
or formulas as timeless knowledge. Send missing registration/payment evidence to
the documentation unit only when it changes the requested contribution position.

## Decision procedure

1. **Consume tax characterization/role.** Do not recompute the upstream BL5 characterization unless contradicted.
2. **State the computation proposition.** Example: `What base/rate applies to event E at date D?`
3. **Resolve the taxable base.** Identify included/excluded components and the legal basis.
4. **Resolve the computation method.** Gross/net/deemed/withholding/other method only as current authority supports.
5. **Resolve rate/band/threshold live.** Never rely on memory for a material current figure.
6. **Bind to the correct temporal anchor.** Distinguish event date, payment date, invoice date, filing period, transfer date, or other legally relevant clock.
7. **Check freshness before action.** If the rule can change the amount or readiness of a current/irreversible action, re-resolve stale authority.
8. **Commit computation state.** Supported amount/range, conditional, disputed, unresolved, or not applicable.
9. **Hand documentary questions to the documentation unit and structural feedback to the economics unit only if material.**

## Computation-state pattern

```text
P-BL5-COMP-01
upstream_tax_characterization: P-BL5-CHAR-...
base: <resolved / conditional>
method: <resolved / conditional>
rate_or_threshold_rule: <authority-bound reference, not memorized handbook value>
temporal_anchor: <event/date>
amount_or_range: <if safely computable>
status: SUPPORTED / CONDITIONAL / DISPUTED / UNRESOLVED / NOT_APPLICABLE
```

Do not turn the handbook into a rate table.

## Evidence requirements

Potential inputs include:

- BL3 price/payment/consideration propositions;
- transfer/ownership completion date from BL2;
- employment/pay facts after BL6 classification;
- foreign payment/trade facts from BL8;
- current authoritative tax rules;
- evidence for amounts/quantities/currency relevant to the computation;
- prior filings only as historical evidence, not proof that the same rule remains current.

## Live authority triggers

Authority resolution is normally mandatory for material questions involving:

- rates;
- thresholds/bands;
- taxable base rules;
- withholding methods;
- timing/recognition rules;
- payment/finalization periods;
- current exemptions/exclusions affecting the computation;
- historical tax rules at the event date.

Do not hardcode rates, thresholds, filing dates, payment dates, formulas, or article numbers as stable knowledge.

## Cross-track handoffs

### From BL3

Consume commercial amount/payment/allocation facts. Do not treat contract price as tax base without resolving the tax rule.

### From BL6

Consume worker classification and relevant remuneration facts. BL5 computes consequences only from committed/conditioned employment state.

### From BL8

Consume foreign payment/investment/trade classification and any BL8-owned valuation proposition where material. Do not reconstruct customs/FX/trade state.

### To documentation / incentives units

Return committed base/method/rate/timing propositions. Documentation unit decides documentary conditions; incentives/economics unit decides whether a supported tax consequence changes structure/options.

## Failure modes

- remembered rate or threshold used as current truth;
- contract/invoice amount treated as taxable base automatically;
- payment date treated as universal tax event;
- one global relevant tax date used for all propositions;
- future law applied before effective date;
- current law projected backward to historical event;
- tax timing collapsed into accounting recognition;
- exact liability stated despite unresolved base or authority;
- customs/trade valuation silently reconstructed inside BL5.

## Escalation

Increase verification for large-value transactions, historical events, rate/threshold transitions, gross-up/withholding arrangements, mixed consideration, foreign-currency or cross-border inputs, restructurings, or any planned action whose economics materially change with a different current rule.