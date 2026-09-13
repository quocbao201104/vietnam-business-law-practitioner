# BL3 — Contracts / Commercial Transactions

BL3 resolves what transaction/agreement exists, what contractual terms and obligations govern, what performance state exists, and whether the parties later changed that state.

This `core.md` is a **JIT router**, not the full BL3 handbook. Load only the capability unit needed for the material proposition.

## Owns

BL3 owns propositions about:

- formation and transaction state;
- governing document stack and contractual term content;
- obligations, conditions, due state, and performance state;
- variation, waiver, later agreement, settlement terms that change obligations, and course-of-dealing effects;
- existence/content of dispute-resolution clauses.

BL3 does **not** own the whole legal position merely because a contract exists.

## Does not own

- entity/signatory authority, corporate approval, ownership/control — BL2;
- breach, excuse, remedies, damages, limitation, dispute posture/procedure — BL4;
- statutory tax consequences — BL5;
- employment classification — BL6;
- public-law permission/compliance — BL7;
- governing-law/conflict/treaty/CISG, FX, trade/customs, international-enforcement overlay — BL8.

## Core distinctions

- negotiation ≠ agreement;
- signed document ≠ complete contract position;
- formation ≠ effectiveness ≠ performance;
- authority/approval ≠ formation;
- document existence ≠ incorporation;
- term ≠ obligation;
- obligation exists ≠ obligation due;
- deviation/non-performance ≠ breach;
- contractual allocation ≠ statutory liability;
- amendment ≠ waiver;
- course of dealing ≠ automatic contract rewrite;
- dispute-clause content ≠ governing-law/treaty overlay ≠ dispute procedure/enforcement.

## JIT capability routing

### Formation / transaction state

Load `formation-transaction-state.md` when the question depends on:

- whether agreement/assent occurred;
- draft/offer/order/acceptance sequence;
- formation versus effectiveness/conditions;
- contract-law form/electronic assent issues;
- current transaction state.

### Document stack / terms / interpretation

Load `document-stack-terms.md` when the question depends on:

- which document/version governs;
- incorporation/precedence;
- negotiated versus standard/external terms;
- interpretation of a material clause;
- existence/content of a dispute-resolution clause.

### Obligations / conditions / performance

Load `obligations-conditions-performance.md` when the question depends on:

- what a party had to do/pay/deliver/refrain from doing;
- due/trigger/condition state;
- performance/acceptance state;
- evidence of performance or non-performance.

### Variation / waiver / settlement

Load `variation-waiver-settlement.md` when the question depends on:

- amendment/later agreement;
- waiver/accommodation;
- course of dealing/conduct;
- settlement terms that change transaction/obligation state.

Do not load all four units by default.

## Typical compositions

```text
Did this unsigned PO + email exchange create a deal?
→ formation-transaction-state
```

```text
Which payment clause governs: MSA, order form, or later amendment?
→ document-stack-terms
→ variation-waiver-settlement only if later change is material
```

```text
Was delivery actually due and completed?
→ obligations-conditions-performance
→ BL4 only if breach/remedy becomes material
```

```text
They settled the dispute and changed payment obligations.
→ BL4 for dispute/settlement posture
→ variation-waiver-settlement for the new agreement/state
→ BL4 consumes the changed state for remaining remedy/procedure questions
```

## Upstream dependency rules

BL3 consumes upstream propositions rather than reconstructing them.

- BL2 resolves entity, authority, approval, and corporate state.
- BL8 resolves governing-law/treaty/CISG and other cross-border propositions where material.
- BL7 resolves public-law permission/compliance.

If an upstream proposition is unresolved, BL3 keeps dependent transaction propositions conditional or emits the appropriate signal. It does not silently solve the upstream issue.

## Live authority behavior

Stable BL3 knowledge defines the distinctions and proof path. Use Authority Resolver when current/historical law materially determines:

- formation/effectiveness/form requirements;
- incorporation or standard-term treatment;
- electronic transaction/signature issues;
- mandatory contract rules affecting obligations/performance;
- variation/waiver/settlement effect;
- historical contract law at the relevant event date.

Do not hardcode article numbers, category-specific formalities, statutory deadlines, or current mandatory terms.

## Handoff rules

- BL2 → BL3: committed/conditioned authority/approval/entity propositions; BL3 decides transaction effect within its ownership.
- BL3 → BL4: committed obligation/performance and dispute-clause-content propositions; BL4 owns breach/remedy/procedure.
- BL3 → BL5: commercial payment/tax/cost allocation facts only; BL5 owns statutory tax treatment.
- BL3 ↔ BL7: contract/consent/allocation does not replace regulatory permission/compliance.
- BL8 → BL3: resolved/conditioned governing-law/treaty/CISG proposition where material; BL3 applies it to contract formation/content.
- BL3 → BL8: exact governing-law/dispute/payment/trade clause content and cross-border facts; BL8 owns overlay consequences.

If downstream evidence contradicts BL3-owned transaction state, emit `CONTRADICTION_SIGNAL`; downstream owners must not reconstruct BL3 state.

## Failure modes

- signed-PDF bias;
- draft treated as concluded contract;
- main document treated as entire deal;
- every website term treated as incorporated;
- every clause treated as an obligation;
- obligation due/performance/breach collapsed;
- every email treated as amendment;
- one accommodation treated as permanent waiver;
- BL3 reconstructing BL2 authority/approval;
- BL3 deciding BL7 permission or BL8 governing-law/treaty propositions;
- commercial tax/customs allocation treated as statutory conclusion;
- dispute clause content collapsed into forum/procedure/enforcement;
- loading all contract knowledge for a narrow transaction question.
