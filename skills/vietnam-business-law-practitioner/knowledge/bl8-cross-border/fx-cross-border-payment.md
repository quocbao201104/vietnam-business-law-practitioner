# BL8 — FX / Cross-border Payment / Capital-flow Classification

## Owns

Determining the legally relevant cross-border payment/capital-flow classification and FX-regulatory proposition for an already described business transaction, investment, loan, service, goods, dividend/distribution, capital contribution, or other foreign-currency/cross-border flow.

This unit owns **cross-border payment/flow classification and FX-regulatory propositions**. It does not reconstruct the underlying contract, investment, tax, customs, or accounting transaction merely because money moves across a border.

## Does not own

- contract formation/content/payment obligation — BL3;
- tax/withholding treatment — BL5;
- corporate ownership/contribution completion — BL2;
- foreign-investment market-access/control state — `foreign-investment-market-access.md`;
- trade/customs/HS/origin/tariff propositions — `trade-customs-origin-tariff.md`;
- domestic operating permission — BL7;
- bookkeeping/accounting recognition.

## Activate when

Use when a material decision depends on:

- classifying a cross-border monetary flow as service/trade payment, loan/debt, capital contribution, investment flow, dividend/distribution, reimbursement, royalty/license payment, or another legally relevant mode;
- whether an account/payment route/currency/registration/reporting/FX condition materially affects the proposed transfer;
- whether incoming/outgoing funds match the committed underlying transaction/investment state;
- whether a change in payment structure creates a different FX/capital-flow proposition;
- whether BL5 tax treatment depends on a BL8-owned foreign-payment classification.

Skip when the payment is purely domestic and no foreign-currency/cross-border/capital-flow rule can change the requested action.

## Required state

Where material, consume:

- committed BL3 transaction/payment obligation and purpose;
- committed BL2 ownership/capital state where contribution/distribution is involved;
- committed BL8 investment state where investment/capital flow is involved;
- payer/payee identity and jurisdiction/location;
- currency, amount, direction, timing, account/payment channel, intermediary and bank/payment-provider facts;
- loan/debt/equity/service/goods documentation where relevant;
- BL8 trade/customs facts where the payment depends on a goods transaction, without reconstructing customs state here;
- relevant temporal anchors;
- current/historical FX/payment authority.

Do not guess the flow type from invoice wording, currency, payment memo, or foreign party alone.

## Core distinctions

### Foreign invoice payment ≠ one fixed flow type

A foreign invoice can relate to goods, services, royalties, loan repayment, reimbursement, capital transaction, or another mode.

Use the resolved underlying transaction facts; do not shortcut:

```text
foreign invoice
→ service payment
```

### Payment label ≠ legal flow classification

`capital`, `loan`, `advance`, `reimbursement`, `fee`, `royalty`, `dividend`, or similar labels are evidence/context. BL8 resolves the legal payment/flow proposition from the underlying committed facts and current authority.

### Contract payment obligation ≠ FX permission

BL3 may establish that Party A owes Party B amount X. BL8 separately resolves whether/how the cross-border payment may be made under applicable FX/capital-flow rules.

### Investment state ≠ capital-flow mechanics automatically resolved

A permitted investment structure does not automatically resolve the payment/account/reporting path for capital contribution, acquisition payment, profit remittance, or another investment flow.

### FX classification ≠ tax treatment

BL8 owns the foreign-payment/capital-flow classification. BL5 consumes it for statutory tax/withholding consequence.

```text
BL8 flow classification
→ BL5 tax consequence
```

not:

```text
preferred tax result
→ BL8 changes flow classification
```

### Payment timing ≠ tax timing ≠ accounting timing

These are separate propositions owned by different systems/owners. A transfer date may be an input to BL5 but does not automatically determine tax event or accounting recognition.

### Currency choice ≠ governing law

Paying in a foreign currency does not determine governing law, CISG/private-law treaty applicability, or dispute forum.

### Cross-border payment ≠ import/export

A foreign payment for software, services, financing, investment, or intellectual property does not automatically activate goods-trade/customs analysis.

## Decision procedure

1. **State the payment/flow proposition.** Example: `What legal cross-border flow is Payment P, and what FX conditions govern transfer on date D?`
2. **Consume underlying owner state.** BL3 transaction/payment purpose; BL2 capital state; investment/trade state where material.
3. **Classify the economic/legal mode from facts.** Goods/service payment, loan/debt, capital contribution/acquisition, distribution/remittance, royalty/license, reimbursement, advance, or another supported mode.
4. **Preserve ambiguity.** If upstream transaction purpose or investment state is unresolved, condition the BL8 flow rather than guessing.
5. **Resolve FX/capital-flow rules live.** Account/channel/currency/registration/reporting/document conditions as material to the requested action.
6. **Separate payment legality from tax consequence.** Return committed flow classification to BL5.
7. **Separate payment flow from customs.** Late-route trade/customs only when actual goods movement/customs proposition is material.
8. **Commit payment state with explicit `bl8_role` / `substantive_owner`.** Supported, conditional, verify, blocked, disputed, or unresolved.
9. **Link action readiness.** `MAKE PAYMENT`, `RECEIVE FUNDS`, `REMIT PROFIT`, `CONTRIBUTE CAPITAL`, etc. only through explicit proposition dependencies.

## Payment-state pattern

```text
P-BL8-FX-01
bl8_role: OWNER / OVERLAY
substantive_owner: BL2 / BL3 / BL4 / BL5 / BL6 / BL7 / null
payer: <actor>
payee: <actor>
underlying_dependency: <BL3/BL2/BL6/BL8 proposition as appropriate>
flow_mode: GOODS / SERVICE / LOAN / CAPITAL / ACQUISITION / DISTRIBUTION / ROYALTY / REIMBURSEMENT / OTHER
currency: <...>
direction: INBOUND / OUTBOUND / OTHER
account_channel: <if material>
temporal_anchor: <...>
fx_conditions: [...]
status: SUPPORTED / CONDITIONAL / VERIFY / BLOCKED / DISPUTED / UNRESOLVED
```

The FX/flow proposition itself will normally use `bl8_role: OWNER` with `substantive_owner: null`. Use `OVERLAY` only where a BL8 payment result is explicitly conditioning another owner's action/proposition; the marker never transfers that proposition to BL8.

These are reasoning states, not bank-operation instructions or statutory labels.

## Evidence requirements

Potential evidence includes:

- BL3 contract/invoice/payment obligation and transaction purpose;
- loan, contribution, acquisition, distribution or service/goods documentation;
- BL2 ownership/capital records where material;
- bank/account/payment-provider instructions and transfer records;
- currency/amount/timing evidence;
- investment approvals/registrations where relevant as upstream state;
- official FX/payment rules and guidance;
- evidence of actual recipient/payer/intermediary/account route.

A payment memo or invoice title is not dispositive evidence of legal flow classification.

## Live authority triggers

Use Authority Resolver where current/historical law materially determines:

- cross-border/current/capital-flow classifications;
- foreign-currency/payment/account conditions;
- loan/investment/capital contribution/distribution payment requirements;
- registration/reporting/document requirements;
- restrictions/prohibitions/exemptions;
- historical FX rules at the payment/contribution/remittance date.

Do not hardcode account types, reporting thresholds, registration triggers, permitted currencies, forms, bank-document checklists, agency names, or article numbers.

## Cross-track handoffs

### From BL3

Consume the committed transaction/payment obligation and purpose. If payment evidence contradicts BL3 transaction state, emit `CONTRADICTION_SIGNAL` rather than redefining the contract.

### From BL2 / investment unit

Consume committed corporate capital/ownership or foreign-investment state where the flow implements contribution/acquisition/distribution. Do not treat payment alone as proof the corporate/investment state changed.

### To BL5

Provide committed/conditioned flow classification, payer/payee facts, amount/timing and relevant status. BL5 owns tax/withholding consequences.

### To trade/customs unit

If the underlying payment concerns goods movement and customs/trade treatment is material, consume or late-route the trade/customs proposition. Do not infer import/export from payment alone.

### To BL7

If payment-provider/regulated-service or domestic operating permission becomes separately material, late-route BL7; BL8 does not absorb domestic licensing.

## Failure modes

- foreign invoice automatically classified as service payment;
- payment label treated as dispositive flow status;
- cross-border payment treated as import/export by default;
- contract payment obligation treated as sufficient FX permission;
- investment permission treated as automatically resolving payment mechanics;
- tax outcome used to back-solve BL8 flow classification;
- payment date collapsed into tax/accounting timing;
- currency used to infer governing law;
- `bl8_role` / `substantive_owner` omitted where overlay status is material;
- current FX/account/registration rules recalled from memory.

## Escalation

Increase verification for capital contributions/acquisitions, shareholder/related-party loans, profit/dividend remittance, unusual payment chains, third-party/intermediary payments, netting/set-off, fintech/platform payment structures, large or irreversible transfers, or any case where a wrong flow classification could block transfer or materially change BL5 consequences.