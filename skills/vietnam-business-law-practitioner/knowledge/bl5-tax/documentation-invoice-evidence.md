# BL5 — Documentation / Invoice / Evidence Conditions

## Owns

Determining whether documentary, invoice, payment, filing-support, and evidence conditions required for a tax proposition are satisfied, unresolved, or defective.

This unit owns **tax-documentary eligibility and evidence-condition propositions**. It does not decide the underlying tax characterization, base/rate, accounting treatment, or regulatory validity of a business document outside the tax proposition.

## Does not own

- transaction/employment/ownership/cross-border classification — BL2/BL3/BL6/BL8;
- tax characterization/statutory role — `characterization-events-roles.md`;
- base/method/rate/timing — `base-method-rate-timing.md`;
- incentive/structuring consequence — `incentives-structuring-economics.md`;
- accounting recognition/bookkeeping;
- general document authenticity/dispute merits owned elsewhere.

## Activate when

Use when the result depends on:

- invoice/document requirements;
- evidence supporting VAT credit/deduction/deductibility or another tax treatment;
- payment-method/document conditions;
- whether a document defect changes a specific tax consequence;
- missing/late/inconsistent tax records;
- evidence needed to substantiate a tax position;
- whether a tax benefit/consequence is blocked by documentary conditions despite substantive characterization.

Skip when the question is purely about tax characterization/rate and documentary conditions cannot change the answer.

## Required state

Where material, consume:

- committed BL5 tax characterization/role proposition;
- committed BL5 base/timing proposition where relevant;
- underlying BL3 transaction/payment/performance state;
- document/invoice/payment records;
- document dates/versions/issuers/recipients;
- evidence provenance and inconsistencies;
- current/historical authority for the exact documentary condition;
- any upstream dispute about whether the transaction/payment actually occurred.

A document may be evidence for several propositions; do not let one document's status automatically resolve all of them.

## Core distinctions

### Invoice exists ≠ tax consequence satisfied

An invoice can exist and still fail to establish a particular VAT credit, deduction, deductibility, timing, or other tax condition.

Resolve the exact tax proposition.

### Invoice validity ≠ VAT credit ≠ deductibility ≠ accounting recognition

These are separate questions with potentially different legal/evidentiary requirements.

Do not infer:

```text
invoice formally valid
→ VAT credit allowed
→ expense deductible
→ accounting recognition correct
```

Each proposition needs its own owner and authority.

### Document defect ≠ transaction did not occur

A defective/missing tax document may affect a tax treatment without erasing the underlying BL3 transaction/performance fact.

Do not rewrite upstream transaction state to make the tax conclusion fit.

### Payment record ≠ substantive tax entitlement

Bank record, receipt, internal ledger, cash acknowledgement, payment platform record, or invoice status may establish or dispute payment facts. It does not automatically satisfy every tax-document condition.

### Documentary condition ≠ statutory tax characterization

Missing evidence may make a position unsupported or unavailable, but it does not necessarily change the underlying characterization of the event/role.

Keep separate:

```text
substantive tax position
vs
proof/documentary eligibility
```

### Tax evidence ≠ accounting evidence

A document may support a tax proposition without deciding bookkeeping/accounting recognition. BL5 should not turn tax-document analysis into an accounting opinion.

## Contribution evidence

Activate for a material compulsory-contribution evidence question after coverage
and relevant computation state are committed or conditioned. Resolve the required
scheme-specific registration, participant declaration, payroll/base records,
payment evidence and correction/reconciliation pathway against live authority.
Payroll withholding is not proof of remittance; registration is not proof of
correct coverage or contribution base. An invoice is not a universal prerequisite.

Map each record to the scheme, participant/contributor, period and proposition.
Return contradictions about employment/pay facts to BL6; keep documentary
sufficiency and the contribution consequence in BL5. Record missing evidence and
whether it is curable without inventing completion or silently erasing coverage.

## Decision procedure

1. **State the exact documentary proposition.** Example: `Are the conditions for tax treatment X sufficiently supported?`
2. **Consume substantive BL5 state.** Use committed tax characterization/role/base/timing propositions; do not reconstruct them.
3. **Identify required documentary elements.** Resolve current/historical authority for the specific tax treatment.
4. **Inventory evidence actually available.** Invoice, contract, payment proof, delivery/performance record, declaration, certificate, registration, or other relevant material.
5. **Map each item to the proposition it supports.** Do not use document volume as confidence.
6. **Identify defects/inconsistencies.** Missing fields, wrong party/date, mismatch with transaction state, unavailable source, unsupported payment method, version conflict, or other material issue.
7. **Separate curable/documentary issue from substantive failure.** Do not overstate consequence before current authority is resolved.
8. **Commit documentary state.** Satisfied, satisfied-with-conditions, defective, disputed, missing, unresolved, or not required.
9. **Return any contradiction to the upstream owner.** If records materially contradict the committed transaction/payment/classification, emit `CONTRADICTION_SIGNAL`; do not silently rewrite upstream state.

## Evidence-condition pattern

```text
P-BL5-DOC-01
upstream_tax_proposition: P-BL5-...
required_condition: <authority-bound condition>
evidence: [E-...]
defect_or_gap: <if any>
status: SATISFIED / CONDITIONAL / DEFECTIVE / DISPUTED / MISSING / UNRESOLVED / NOT_REQUIRED
```

## Evidence requirements

Potential evidence includes:

- invoice/e-invoice records;
- underlying contracts/orders/settlement/payment terms from BL3;
- delivery/performance evidence;
- bank/payment records;
- tax declarations/certificates/registrations where relevant;
- withholding/remittance evidence;
- import/trade documents consumed from BL8 where tax treatment depends on them;
- contemporaneous correction/replacement records;
- official records showing document status where legally material.

Use only evidence necessary for the proposition. Do not demand a full accounting archive for a narrow tax question.

## Live authority triggers

Use Authority Resolver when the result depends on:

- current invoice/document requirements;
- payment-method conditions;
- documentary requirements for VAT credit/deduction/deductibility;
- evidence required for a tax exemption/incentive/treatment;
- correction/replacement procedures whose legal effect is material;
- historical documentary rules at the transaction date.

Do not hardcode current invoice fields, forms, thresholds, payment-condition amounts, filing formats, or article numbers.

## Cross-track handoffs

### From BL3

Consume transaction/payment/performance facts and contract documents. A tax-document defect does not rewrite BL3 transaction state.

### From BL8

Consume committed customs/trade/payment documents or classifications only when the tax proposition depends on them. BL5 does not reconstruct HS/origin/customs state.

### To characterization/base units

If documentary evidence materially contradicts an upstream BL5 proposition, emit a contradiction signal to that owning unit. Do not directly reclassify.

### To incentives/structuring

Provide only the committed documentary eligibility/gap. The economics unit may treat a documentary burden or unavailable benefit as feedback; it must not invent entitlement.

## Failure modes

- invoice existence treated as automatic tax entitlement;
- invoice validity, VAT credit, deductibility, and accounting recognition collapsed;
- missing document treated as proof transaction never occurred;
- payment record treated as satisfying every tax condition;
- evidence volume substituted for proposition-specific sufficiency;
- BL5 document unit rewriting BL3 transaction/payment state;
- current invoice rules applied to historical records without temporal verification;
- accounting advice smuggled into a tax-document conclusion.

## Escalation

Increase verification for large deductions/credits, conflicting invoice/payment records, missing source documents, corrected/replaced invoices, historical transactions, cross-border documentation, or any position where a documentary defect could materially change tax exposure or action readiness.