# BL3 — Variation / Waiver / Settlement / Course of Dealing

## Owns

Determining whether and how the parties changed the transaction after initial formation, including amendment, waiver, later agreement, settlement terms that alter obligations, and legally relevant course of dealing/conduct.

This unit owns **changed transaction state**. It does not own breach/remedy posture merely because a change arose during a dispute.

## Does not own

- entity/signing authority or corporate approval for the change — BL2;
- breach, excuse, remedies, damages, limitation, or dispute procedure — BL4;
- statutory tax consequences of the change — BL5;
- regulatory permission/compliance — BL7;
- cross-border governing-law/treaty/international-enforcement overlay — BL8.

## Activate when

Use when the decision depends on whether:

- parties amended or replaced a term;
- a later order/SOW/side letter changed the deal;
- a party waived strict compliance or a specific right;
- repeated conduct/course of dealing changed or clarified transaction state;
- a settlement agreement changed existing obligations;
- a temporary accommodation became a permanent variation;
- an oral/electronic change is alleged;
- a no-oral-modification/entire-agreement/waiver clause interacts with later conduct.

Skip or compress when no material post-formation change is alleged.

## Required state

Where material, capture:

- prior committed transaction/document/term state;
- alleged change event/document/conduct;
- chronology;
- actor identity and BL2 authority/approval dependencies;
- acceptance/assent evidence for the alleged change;
- scope/duration/condition of alleged waiver;
- repeated conduct and objection history;
- settlement text where relevant;
- affected obligations/actions;
- applicable regime/temporal anchor where material.

## Core distinctions

### Later communication ≠ amendment

An email, message, invoice, operational instruction, courtesy accommodation, or silence does not automatically amend the contract.

Resolve whether the event legally changed transaction state under the applicable regime and facts.

### Amendment ≠ waiver

An amendment changes contractual terms/state. A waiver may concern enforcement or insistence on a right/requirement without necessarily rewriting the underlying term.

Keep separate propositions when the distinction matters.

### Waiver ≠ permanent surrender of every related right

A waiver may be limited by scope, time, condition, transaction, or conduct. Do not generalize one accommodation into a global permanent waiver.

### Course of dealing ≠ automatic contract rewrite

Repeated conduct may be relevant to interpretation, performance expectations, waiver, variation, or evidence. It does not automatically displace written terms.

### Settlement posture ≠ settlement transaction state

BL4 owns dispute/settlement posture, negotiation strategy, remedies, and preservation of rights.

If parties actually reach settlement terms that alter obligations, BL3 owns the resulting agreement/content/changed transaction state.

Use:

```text
BL4 dispute/settlement posture
→ settlement terms reached
→ BL3 resolves settlement agreement/change
→ new BL3 transaction/obligation state
→ BL4 consumes new state for any remaining dispute/remedy questions
```

### Changed term ≠ authorized change

If the actor's authority or required corporate approval for an amendment/waiver/settlement is material, consume BL2. Do not infer authority merely because the original signer or account manager communicated the change.

### Commercial accommodation ≠ statutory permission

Parties can modify commercial allocation without changing statutory tax, regulatory, customs, employment, or other public-law responsibilities.

## Decision procedure

1. **State the change proposition.** Example: `Did the parties validly extend the delivery deadline from D1 to D2?`
2. **Fix the prior state.** Consume the committed BL3 document/term/obligation state before evaluating a change.
3. **Identify the alleged change mechanism.** Formal amendment, later agreement, order/SOW, side letter, electronic/oral agreement, waiver, settlement, or course of dealing.
4. **Build chronology.** Distinguish pre-change conduct, proposed change, acceptance/objection, later performance, and subsequent communications.
5. **Consume BL2 authority/approval if material.** An amendment/settlement may require different authority/approval analysis from the original transaction.
6. **Resolve applicable change/waiver rules live where material.** Do not use generic common-law/contract folklore.
7. **Define scope/effect.** Identify exactly which term/obligation changed, for what period/transaction, and what remained unchanged.
8. **Commit changed transaction state.** Mark prior term/obligation superseded, waived-for-scope, supplemented, disputed, or unchanged as supported.
9. **Propagate exact dependencies.** Recompute only propositions/actions that depend on the changed term/state.
10. **Return to downstream owners.** BL4/BL5/BL7/BL8 consume the new transaction facts within their own ownership.

## Change-state pattern

For material changes:

```text
P-BL3-TERM-OLD
status: SUPERSEDED / PARTIALLY_WAIVED / CURRENT

P-BL3-CHANGE-01
mechanism: AMENDMENT / WAIVER / SETTLEMENT / COURSE_OF_DEALING
scope: <specific term/obligation>
start/end or transaction scope: <if material>
authority dependency: P-BL2-...
status: SUPPORTED / CONDITIONAL / DISPUTED / UNRESOLVED
```

Do not overwrite history. Preserve which version governed at each temporal anchor.

## Settlement boundary

BL3 owns settlement only to the extent settlement creates/changes contractual transaction state.

BL4 remains owner of:

- whether settlement should be pursued;
- claim/remedy posture;
- limitation/deadline/evidence preservation;
- dispute procedure;
- effect on existing claims/remedies insofar as that is a BL4 proposition under the resolved settlement terms.

BL3 should not turn settlement-document interpretation into a global dispute conclusion.

## Evidence requirements

Potential evidence includes:

- executed amendments/side letters;
- later orders/SOWs;
- emails/messages confirming change;
- version history/redlines;
- repeated invoices/delivery schedules accepted without objection;
- notices reserving rights or rejecting change;
- settlement agreements;
- payment/performance behavior consistent or inconsistent with the alleged change;
- authority/approval evidence for the actor agreeing the change.

Silence or conduct must be interpreted under the applicable regime/facts, not as a universal acceptance rule.

## Live authority triggers

Resolve live authority when outcome depends on:

- required form for amendment/waiver/settlement;
- effect of no-oral-modification or entire-agreement clauses;
- legal effect of conduct/silence/course of dealing;
- special statutory requirements for changing particular transactions;
- historical rules at the change date;
- settlement form/effect under the relevant regime.

Do not hardcode universal waiver/amendment doctrines.

## Cross-track handoffs

### From/to BL2

Consume authority/approval for the change when material. Return only transaction-state consequences; BL2 retains corporate ownership of authority/approval propositions.

### From/to BL4

BL4 may signal that settlement/negotiation produced a candidate change. BL3 resolves agreement/content/change state. BL4 then consumes the committed new state for remaining breach/remedy/procedure questions.

### To BL5

Provide changed commercial consideration/payment/cost allocation. BL5 decides statutory tax consequences.

### To BL7

If parties purport to waive/allocate mandatory compliance, route BL7. Private variation does not remove public-law duties.

### To BL8

Provide exact changed governing-law/dispute/payment/trade clause content. BL8 owns cross-border legal consequences where material.

## Failure modes

- every email treated as amendment;
- one accommodation treated as permanent waiver;
- course of dealing treated as automatic override of written terms;
- prior contract state overwritten without history;
- amendment accepted without checking actor authority/approval when material;
- settlement posture and settlement transaction state collapsed;
- BL3 resolving remedies merely because it interpreted a settlement;
- private amendment treated as changing statutory tax/regulatory responsibility;
- all downstream propositions invalidated instead of exact dependents.
