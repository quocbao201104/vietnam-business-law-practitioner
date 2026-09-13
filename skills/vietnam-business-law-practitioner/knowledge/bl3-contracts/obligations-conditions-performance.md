# BL3 — Obligations / Conditions / Performance State

## Owns

Reconstructing contractual obligations, conditions, due states, performance state, and the evidence path needed to determine what each party was required to do and what actually occurred.

This unit owns **obligation and performance state**. It does not decide whether a deviation is an actionable breach, whether liability is excused, or which remedy is available.

## Does not own

- entity/signing authority or corporate approval — BL2;
- breach/materiality/excuse/remedies/damages/dispute procedure — BL4;
- statutory tax consequences — BL5;
- public-law permission/compliance — BL7;
- cross-border governing-law/treaty/trade overlay — BL8.

## Activate when

Use when the decision depends on:

- what a party had to deliver/pay/do/refrain from doing;
- quality/service/acceptance standards;
- timing, location, method, milestone, or dependency;
- conditions precedent/subsequent or prerequisites to performance;
- whether performance became due;
- whether performance occurred, partially occurred, was late, defective, disputed, waived, or not yet due;
- what evidence proves or disputes performance;
- which obligation a later breach/remedy question should be based on.

Skip or compress when the obligation and performance state are undisputed and already committed.

## Required state

Where material, capture:

- committed formation/effectiveness proposition from shared state when formation matters;
- resolved governing term/document proposition from shared state;
- actors/parties;
- obligation source;
- condition/dependency structure;
- due event/date;
- required standard/quantity/quality;
- actual performance event/state;
- acceptance/rejection/inspection records;
- evidence provenance and disputes;
- relevant temporal anchors;
- upstream BL2/BL7/BL8 propositions where performance depends on them.

Do not load `formation-transaction-state.md` or `document-stack-terms.md` merely because this unit consumes their propositions. Load a sibling unit only when its owned proposition is unresolved, disputed, stale, contradictory, or material to reopen.

## Core distinctions

### Term ≠ obligation state

A clause may describe a right, condition, representation, warranty, discretion, procedure, or obligation. Do not convert every sentence into a duty.

### Obligation ≠ due obligation

A duty may exist but not yet be due because a condition, milestone, notice, approval, dependency, or other trigger remains unsatisfied.

### Due ≠ performed

A due obligation requires a separate performance proposition.

### Performance deviation ≠ breach

BL3 can establish:

- not delivered;
- delivered late;
- delivered partially;
- quality/specification disputed;
- payment not received;
- acceptance refused;
- condition unsatisfied.

BL4 determines whether that state constitutes breach/material breach, whether an excuse applies, and what remedy follows.

### Payment evidence ≠ every payment proposition resolved

Invoice, receipt, internal ledger, bank transfer, counterparty statement, and user assertion are separate evidence sources. Preserve disputes rather than promoting a document label such as `PAID` into truth.

### Acceptance ≠ regulatory approval

Contractual acceptance/inspection/approval by a buyer or customer does not prove public-law compliance or regulatory permission.

### Commercial tax allocation ≠ statutory tax obligation

BL3 may record who agreed to bear an economic tax/cost burden. BL5 owns taxpayer/withholder/deductibility/VAT/PIT/CIT or other statutory consequence.

## Obligation tuple

Represent a material obligation explicitly where useful:

```text
WHO
WHAT
STANDARD
WHEN / TRIGGER
WHERE / CHANNEL
CONDITION / DEPENDENCY
EVIDENCE OF PERFORMANCE
EVIDENCE OF ACCEPTANCE / REJECTION
CURRENT STATE
```

Do not force every trivial obligation into a full tuple. Use it for propositions that can change action readiness, breach analysis, payment, termination, or other material outcomes.

## Decision procedure

1. **State the obligation proposition.** Example: `Seller had to deliver specification S by date D after condition C.`
2. **Consume the governing term proposition from shared state.** If the governing term/document stack is already committed and not material to reopen, do not load `document-stack-terms.md`. Load it only when term source/content/incorporation/precedence is unresolved, disputed, stale, contradictory, or material to reopen.
3. **Consume formation/effectiveness state only if needed.** If formation/effectiveness is already reliably established, do not load the formation unit. Reopen it only when formation/effectiveness can materially change the obligation proposition.
4. **Map obligation tuple.** Identify actor, performance, standard, trigger/date, condition, and proof path.
5. **Resolve conditions/dependencies.** Separate existence of the obligation from whether it became due.
6. **Build performance timeline.** Record actual events and evidence against the obligation.
7. **Preserve disputed facts.** Do not choose document/user/counterparty evidence by source count alone.
8. **Commit performance state.** Examples: not-yet-due, due, performed, partially performed, late, defective/disputed, non-performed, acceptance disputed, unresolved.
9. **Late-route upstream issues.** If authority, regulatory permission, or cross-border regime becomes material, return to the accountable owner rather than resolving it in BL3.
10. **Hand deviations to BL4.** BL4 receives the committed obligation/performance proposition; it does not need to reconstruct BL3 state.

## Performance-state pattern

For a material obligation:

```text
P-BL3-OBL-01
source_term: P-BL3-TERM-04
obligor: PARTY-A
obligation: deliver X to standard S
trigger: CONDITION-C
when: DATE-D
state: PARTIALLY_PERFORMED
performance_evidence: E-12, E-13
acceptance_state: DISPUTED
```

Then BL4 may consume this state for breach/remedy analysis.

## Conditions and dependencies

Keep different concepts separate where material:

- condition to formation/effectiveness;
- condition precedent to an obligation becoming due;
- milestone/dependency in performance sequencing;
- contractual acceptance/inspection condition;
- public-law permit/approval dependency owned by BL7/BL8;
- corporate approval dependency owned by BL2.

Do not relabel every unresolved prerequisite as a condition precedent unless the contract/regime supports that characterization.

## Evidence requirements

Potential evidence includes:

- delivery/service records;
- system/application logs;
- acceptance/rejection/inspection records;
- invoices and payment records;
- bank records;
- timesheets/milestone records;
- specifications/test results;
- communications acknowledging completion or defects;
- notices invoking contractual procedures;
- third-party evidence where relevant.

Evidence sufficiency depends on the proposition. Preserve source provenance separately from truth status.

## Live authority triggers

Resolve live authority when obligation/performance state materially depends on:

- mandatory contract rules affecting due/performance/acceptance;
- special statutory performance standards;
- legally required notice/form for performance events;
- electronic records/proof rules;
- historical law at the relevant performance date.

Do not hardcode category-specific deadlines, acceptance rules, or statutory standards as stable knowledge.

## Cross-track handoffs

### To BL4

Provide:

- exact obligation proposition;
- source term/document proposition ID;
- due/condition state;
- actual performance state;
- disputed facts/evidence;
- temporal anchors.

A state such as `LATE`, `DEFECTIVE`, or `NON_PERFORMED` is still a BL3 performance proposition. When breach/remedy becomes material, emit/record the BL4 activation explicitly; BL3 must not promote the deviation into `BREACH` itself.

BL4 owns breach, attribution, excuse, liability, remedy, loss, notice, and dispute posture.

### To BL5

Provide payment/consideration/cost-allocation facts and contract terms. BL5 owns statutory tax consequences.

### To BL7

If performance requires regulated permission/compliance or exposes a consumer/data/product issue, late-route BL7. Contractual performance state does not settle public-law permission.

### To BL8

Provide performance location/payment/goods-movement facts where they create cross-border consequences. BL8 owns the cross-border proposition.

## Failure modes

- every clause converted into an obligation;
- obligation existence collapsed into due state;
- due state collapsed into performance;
- late/defective/non-performance labeled breach inside BL3;
- formation/document-stack units loaded despite reliable committed sibling propositions;
- `PAID` invoice/receipt treated as conclusive payment fact;
- contractual acceptance treated as regulatory approval;
- commercial tax allocation treated as statutory liability;
- BL4 reconstructing contract obligations independently instead of consuming BL3 state;
- current law applied to historical performance without temporal verification.
