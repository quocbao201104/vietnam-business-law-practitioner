# BL3 — Formation / Transaction State

## Owns

Determining whether a contract/transaction was formed, what transaction state exists, and whether contract-law formation/effectiveness questions are resolved or remain conditional on upstream propositions.

This unit owns **agreement/transaction existence and formation state**. It does not own corporate authority, regulatory permission, or cross-border governing-law/treaty applicability.

## Does not own

- entity/signatory authority or internal corporate approval — BL2;
- breach, excuse, remedies, damages, or dispute procedure — BL4;
- statutory tax consequences — BL5;
- public-law permission/compliance — BL7;
- governing law, treaty/CISG, or other cross-border applicability propositions — BL8.

## Activate when

Use when the decision depends on:

- whether parties actually reached agreement;
- whether a draft/offer/order/acceptance/exchange formed a transaction;
- whether acceptance was qualified, conditional, late, revoked, or superseded;
- whether required contract-law form/effectiveness conditions are material;
- whether several steps/documents together created the transaction;
- whether a transaction is proposed, negotiated, formed, condition-pending, effective, performed, terminated, or otherwise in a distinct state.

Skip or compress when formation is undisputed and cannot change the requested action.

## Required state

Where material, capture:

- parties/actors as resolved or conditioned by BL2;
- business transaction/object;
- offer/proposal/order/request;
- acceptance/confirmation/conduct relied upon as assent;
- chronology and communication channel;
- material conditions to formation/effectiveness;
- required form/signature/electronic evidence issues;
- governing-regime proposition from BL8 or another owner where material;
- regulatory/mandatory-law condition from BL7 where material;
- documents/evidence and disputed facts;
- relevant temporal anchors.

## Core distinctions

### Negotiation ≠ agreement

Commercial discussion, draft exchange, quotation, proposal, term sheet, purchase request, or unsigned document does not automatically establish a concluded transaction.

Ask what event/evidence is relied upon as assent.

### Signed document ≠ only path to formation

A signed PDF may be strong evidence, but formation may depend on the applicable regime, electronic communications, conduct, performance, incorporated terms, or other legally recognized assent mechanisms.

Do not use `no wet signature` as a universal no-contract rule.

### Formation ≠ authority

BL3 can identify apparent assent by an actor but cannot decide that actor had authority to bind the entity.

If authority is material and unresolved:

```text
formation question
→ consume BL2 authority proposition
→ keep BL3 formation conclusion conditional until resolved
```

Do not reconstruct authority inside BL3.

### Formation ≠ regulatory permission

Parties may form an agreement concerning conduct that still requires a license, approval, registration, or other public-law condition.

BL7 owns permission/compliance. Do not turn regulatory permission into a hidden element of every BL3 formation proposition unless the applicable contract-law regime makes it a specific formation/effectiveness dependency.

### Formation ≠ effectiveness ≠ performance

Keep separate propositions where material:

- agreement formed;
- contract/transaction became legally effective;
- a condition precedent was satisfied;
- performance became due;
- performance occurred.

Do not collapse them into one status called `valid contract`.

### Contract-law validity/effectiveness ≠ whole-case legality

BL3 may resolve contract-law formation/validity/effectiveness questions only within its ownership and only after consuming material upstream propositions.

Do not infer:

```text
BL2 approval defect
→ contract invalid
```

or:

```text
BL7 regulatory issue
→ no contract exists
```

without a BL3-owned transaction-effect proposition under the applicable regime.

## Decision procedure

1. **State the exact formation proposition.** Example: `Did parties A and B form transaction T by date D?`
2. **Identify candidate assent events.** Offer/order/proposal, acceptance/confirmation, signature, click/electronic action, conduct, delivery, payment, or other relied-upon event.
3. **Build the chronology.** Distinguish draft, negotiation, offer, counter-offer/qualified response, acceptance, later confirmation, and performance.
4. **Consume upstream state.** Use BL2 authority/approval propositions, BL7 mandatory/public-law propositions, and BL8 governing-regime/treaty propositions where material. Do not recreate them.
5. **Identify contract-law requirements.** Resolve current/historical authority only for the specific formation/effectiveness proposition and temporal anchor.
6. **Separate formation from effectiveness/conditions.** Record unresolved condition-precedent or form issues explicitly rather than merging them into assent.
7. **Commit transaction state.** Examples: proposed, negotiating, formed, formed-but-condition-pending, effective, disputed, unresolved, superseded.
8. **Hand terms/documents onward.** Once formation/state is sufficiently established, use `document-stack-terms.md` to resolve what the transaction contains.

## Transaction-state pattern

Use only states needed for the decision, for example:

```text
PROPOSED
NEGOTIATING
FORMED
FORMED_CONDITION_PENDING
EFFECTIVE
PERFORMANCE_DUE
PERFORMED
CHANGED
TERMINATED_OR_SETTLED
DISPUTED
UNRESOLVED
```

These are reasoning states, not statutory labels. Do not force every transaction through every state.

## Evidence requirements

Potential evidence includes:

- signed/unsigned agreements;
- quotations, purchase orders, order confirmations;
- email/chat/electronic acceptance records;
- platform/system logs;
- invoices/payment records;
- delivery/performance evidence;
- version history/drafts;
- communications showing rejection, counter-offer, condition, withdrawal, or confirmation.

Document title does not decide legal status. A file named `Contract`, `MOU`, `Quotation`, or `Draft` is evidence about the transaction, not the conclusion.

## Live authority triggers

Resolve live authority when formation/effectiveness depends on:

- current/historical form requirements;
- electronic transaction/signature rules;
- mandatory contract-law formalities;
- legally required conditions for effectiveness;
- historical law at the formation date;
- special contract regimes routed by BL1/another owner.

Do not hardcode article numbers, formalities, signature rules, or category-specific requirements as permanent knowledge.

## Cross-track handoffs

### From BL2

Consume entity, authority, and approval propositions where they are explicit dependencies. BL3 decides the transaction effect of those propositions within contract/transaction ownership.

### To BL4

Do not hand off merely because performance is imperfect. BL4 activates once BL3 has established a material obligation/performance deviation relevant to breach/remedy analysis.

### To BL7

If formation analysis exposes an activity/product/consumer/data/public-law trigger, emit a late-route signal. BL3 does not decide operating permission.

### To/from BL8

Consume governing-law/treaty/CISG propositions when material to contract formation. BL3 still owns formation/content under the resolved or explicitly conditioned regime.

## Failure modes

- signed-PDF bias;
- unsigned-document bias;
- draft title treated as dispositive;
- negotiation treated as agreement;
- performance/payment treated as automatic proof of every term;
- BL3 reconstructing signatory authority or corporate approval;
- regulatory permission collapsed into contract formation;
- `formed`, `valid`, `effective`, and `performed` collapsed into one state;
- current law used for historical formation without temporal check;
- cross-border contract analyzed before material BL8 regime propositions are resolved/conditioned.
