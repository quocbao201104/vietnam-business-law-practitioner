# BL3 — Formation / Transaction State

## Owns

Determining whether a contract/transaction was formed and whether contract-law formation/effectiveness questions are resolved or remain conditional on upstream propositions.

This unit owns **agreement/transaction existence and formation/effectiveness state**. It does not own performance state, later variation state, corporate authority, regulatory permission, or cross-border governing-law/treaty applicability.

## Does not own

- entity/signatory authority or internal corporate approval — BL2;
- performance/due state — `obligations-conditions-performance.md`;
- later variation/waiver/settlement state — `variation-waiver-settlement.md`;
- breach, excuse, remedies, damages, termination/remedy consequence, or dispute procedure — BL4;
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
- whether formation/effectiveness is proposed, negotiating, unresolved, formed, condition-pending, effective, disputed, or superseded.

Skip or compress when formation/effectiveness is undisputed and cannot change the requested action.

## Required state

Where material, capture:

- parties/actors as resolved or conditioned by BL2;
- business transaction/object;
- offer/proposal/order/request;
- acceptance/confirmation/conduct relied upon as assent;
- chronology and communication channel;
- material conditions to formation/effectiveness;
- required form/signature/electronic evidence issues;
- resolved/conditioned BL8 governing-law/treaty/CISG proposition where a cross-border overlay is material;
- regulatory/mandatory-law condition from BL7 where material;
- documents/evidence and disputed facts;
- relevant temporal anchors.

For a domestic BL3 proposition, BL3 itself resolves the applicable contract-law authority using Authority Resolver where required. BL1 may route the regime hypothesis but does not decide BL3's substantive applicability proposition.

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
- a condition to effectiveness was satisfied;
- performance became due;
- performance occurred.

This unit owns only the first three. Due/performance state belongs to `obligations-conditions-performance.md`.

Do not collapse them into one status called `valid contract`.

### Formation/effectiveness state ≠ later transaction lifecycle

Do not use this unit to own post-formation performance, later amendment/waiver, settlement changes, or remedy/termination consequences.

Use:

```text
formation/effectiveness
→ formation-transaction-state.md

performance due/performed
→ obligations-conditions-performance.md

changed/waived/settled contractual state
→ variation-waiver-settlement.md

breach/remedy/termination consequence
→ BL4 where material
```

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
3. **Build the chronology.** Distinguish draft, negotiation, offer, counter-offer/qualified response, acceptance, later confirmation, and performance evidence used only insofar as it bears on formation.
4. **Consume upstream state.** Use BL2 authority/approval propositions, BL7 mandatory/public-law propositions, and BL8 governing-law/treaty propositions where material. Do not recreate them.
5. **Resolve BL3 contract-law requirements.** For domestic BL3 propositions, call Authority Resolver directly when current/historical contract law is material. For cross-border matters, consume BL8's resolved/conditioned governing-law/treaty/CISG proposition first where required.
6. **Separate formation from effectiveness/conditions.** Record unresolved condition-to-effectiveness or form issues explicitly rather than merging them into assent.
7. **Commit formation/effectiveness state.** Use only states owned by this unit.
8. **Hand terms/documents onward only when needed.** Load `document-stack-terms.md` only if document/term ownership is unresolved, disputed, stale, contradictory, or material to reopen. Otherwise consume the committed term state from shared state.

## Formation-state pattern

Use only states needed for the decision, for example:

```text
PROPOSED
NEGOTIATING
FORMATION_UNRESOLVED
FORMED
FORMED_CONDITION_PENDING
EFFECTIVE
FORMATION_DISPUTED
SUPERSEDED
```

These are reasoning states, not statutory labels. Do not force every transaction through every state.

Do not encode these sibling-owned states here:

```text
PERFORMANCE_DUE / PERFORMED
→ obligations-conditions-performance.md

CHANGED / PARTIALLY_WAIVED / SETTLED_CHANGE
→ variation-waiver-settlement.md

termination/remedy/dispute state
→ BL4 where material
```

## Evidence requirements

Potential evidence includes:

- signed/unsigned agreements;
- quotations, purchase orders, order confirmations;
- email/chat/electronic acceptance records;
- platform/system logs;
- invoices/payment records where they bear on assent/effectiveness;
- delivery/performance evidence where it bears on assent/effectiveness;
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
- special contract regimes routed by BL1 and resolved by the accountable owner.

Do not hardcode article numbers, formalities, signature rules, or category-specific requirements as permanent knowledge.

## Cross-track handoffs

### From BL2

Consume entity, authority, and approval propositions where they are explicit dependencies. BL3 decides the transaction effect of those propositions within contract/transaction ownership.

### To sibling BL3 units

Pass committed formation/effectiveness propositions through shared state. Do **not** require sibling units to reload this knowledge unit merely because they consume those propositions.

### To BL4

Do not hand off merely because later performance is imperfect. BL4 activates once BL3's obligations/performance unit has established a material deviation relevant to breach/remedy analysis.

### To BL7

If formation analysis exposes an activity/product/consumer/data/public-law trigger, emit a late-route signal. BL3 does not decide operating permission.

### To/from BL8

Consume BL8 governing-law/treaty/CISG propositions only when a cross-border overlay is material to contract formation. BL3 still owns formation/content under the resolved or explicitly conditioned regime.

## Failure modes

- signed-PDF bias;
- unsigned-document bias;
- draft title treated as dispositive;
- negotiation treated as agreement;
- performance/payment treated as automatic proof of every term;
- formation unit owning due/performed/changed/settled/remedy lifecycle states;
- BL3 reconstructing signatory authority or corporate approval;
- regulatory permission collapsed into contract formation;
- `formed`, `valid`, `effective`, and `performed` collapsed into one state;
- BL1/another generic router treated as owner of domestic BL3 contract-law applicability;
- current law used for historical formation without temporal check;
- cross-border contract analyzed before material BL8 regime propositions are resolved/conditioned.
