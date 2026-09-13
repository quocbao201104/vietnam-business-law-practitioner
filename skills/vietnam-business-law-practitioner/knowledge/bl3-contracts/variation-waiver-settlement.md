# BL3 — Variation / Waiver / Settlement / Course of Dealing

## Owns

Determining whether and how the parties changed the contractual transaction after initial formation, including amendment, waiver of contractual terms/requirements, later agreement, settlement terms that alter obligations, and legally relevant course of dealing/conduct.

This unit owns **changed contractual transaction state**. It does not own breach/remedy/procedural consequences merely because a change or waiver arose during a dispute.

## Does not own

- entity/signing authority or corporate approval for the change — BL2;
- breach, excuse, claims, remedies, damages, limitation/deadlines, procedural rights/objections, or dispute posture — BL4;
- statutory tax consequences of the change — BL5;
- regulatory permission/compliance — BL7;
- cross-border governing-law/treaty/international-enforcement overlay — BL8.

## Activate when

Use when the decision depends on whether:

- parties amended or replaced a term;
- a later order/SOW/side letter changed the deal;
- a party waived strict contractual compliance or a specific contractual requirement;
- repeated conduct/course of dealing changed or clarified transaction state;
- a settlement agreement changed existing obligations;
- a temporary accommodation became a permanent variation;
- an oral/electronic change is alleged;
- a no-oral-modification/entire-agreement/waiver clause interacts with later conduct.

Skip or compress when no material post-formation contractual change is alleged.

## Required state

Where material, capture:

- prior committed transaction/document/term/obligation state from shared state;
- alleged change event/document/conduct;
- chronology;
- actor identity and BL2 authority/approval dependencies;
- acceptance/assent evidence for the alleged change;
- scope/duration/condition of alleged contractual waiver;
- repeated conduct and objection history;
- settlement text where relevant;
- affected obligations/actions;
- applicable regime/temporal anchor where material.

Do not load sibling BL3 units merely because their propositions are inputs. Reopen a sibling only when its owned proposition is unresolved, disputed, stale, contradictory, or material to reopen.

## Core distinctions

### Later communication ≠ amendment

An email, message, invoice, operational instruction, courtesy accommodation, or silence does not automatically amend the contract.

Resolve whether the event legally changed contractual transaction state under the applicable regime and facts.

### Amendment ≠ waiver

An amendment changes contractual terms/state. A contractual waiver may concern insistence on a term/requirement without necessarily rewriting the underlying term.

Keep separate propositions when the distinction matters.

### Contractual waiver ≠ waiver of claim/remedy/procedural right

BL3 owns whether agreement or conduct changed, waived, supplemented, or conditioned a **contractual term, obligation, or transaction state**.

BL4 owns what that committed BL3 state means for:

- breach/excuse;
- claim or remedy availability;
- damages;
- limitation/deadline;
- objection or procedural right;
- settlement/dispute posture.

Examples:

```text
Repeated acceptance of late payment
→ BL3: did strict contractual payment timing change or become waived for a defined scope?
→ BL4: what does that state mean for breach/remedy/claim posture?
```

```text
Settlement releases existing damages claim
→ BL3: what release/change term was agreed and what does the contractual text cover?
→ BL4: what is the consequence for the existing claim/remedy/dispute posture?
```

Do not let BL3 conclude `claim waived`, `damages unavailable`, `arbitration objection waived`, or similar BL4 propositions merely because it resolved the underlying contractual change.

### Waiver ≠ permanent surrender of every related contractual right

A waiver may be limited by scope, time, condition, transaction, or conduct. Do not generalize one accommodation into a global permanent contractual waiver.

### Course of dealing ≠ automatic contract rewrite

Repeated conduct may be relevant to interpretation, performance expectations, contractual waiver, variation, or evidence. It does not automatically displace written terms.

### Settlement posture ≠ settlement transaction state

BL4 owns dispute/settlement posture, negotiation strategy, remedies, deadlines, procedural rights, and preservation of claims.

If parties reach ordinary commercial settlement terms, BL3 owns the resulting agreement/content/changed contractual transaction state. Employment-specific ongoing terms and mutual separation remain with the relevant BL6 capability, including when agreed during a dispute. Split mixed settlements rather than assigning all terms to BL3.

Use:

```text
BL4 dispute/settlement posture
→ settlement terms reached
→ BL3 resolves settlement agreement/change
→ new BL3 transaction/obligation state
→ BL4 consumes new state for remaining claim/remedy/procedure questions
```

### Changed term ≠ authorized change

If the actor's authority or required corporate approval for an amendment/waiver/settlement is material, consume BL2. Do not infer authority merely because the original signer or account manager communicated the change.

### Commercial accommodation ≠ statutory permission

Parties can modify commercial allocation without changing statutory tax, regulatory, customs, employment, or other public-law responsibilities.

## Decision procedure

1. **State the contractual change proposition.** Example: `Did the parties validly extend the delivery deadline from D1 to D2?`
2. **Fix the prior state from shared state.** If the prior BL3 term/obligation state is already committed and not material to reopen, consume it without loading sibling knowledge.
3. **Identify the alleged change mechanism.** Formal amendment, later agreement, order/SOW, side letter, electronic/oral agreement, contractual waiver, settlement, or course of dealing.
4. **Build chronology.** Distinguish pre-change conduct, proposed change, acceptance/objection, later performance, and subsequent communications.
5. **Consume BL2 authority/approval if material.** An amendment/settlement may require different authority/approval analysis from the original transaction.
6. **Resolve applicable change/waiver rules live where material.** Do not use generic common-law/contract folklore.
7. **Define contractual scope/effect.** Identify exactly which term/obligation changed or was waived, for what period/transaction, and what remained unchanged.
8. **Commit changed transaction state.** Mark prior term/obligation superseded, waived-for-scope, supplemented, disputed, or unchanged as supported.
9. **Propagate exact dependencies.** Recompute only propositions/actions that depend on the changed contractual state.
10. **Return downstream consequences to their owners.** BL4/BL5/BL7/BL8 consume the new transaction facts within their own ownership.

## Change-state pattern

For material changes:

```text
P-BL3-TERM-OLD
status: SUPERSEDED / PARTIALLY_WAIVED / CURRENT

P-BL3-CHANGE-01
mechanism: AMENDMENT / CONTRACTUAL_WAIVER / SETTLEMENT / COURSE_OF_DEALING
scope: <specific contractual term/obligation>
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
- procedural objections/rights;
- dispute procedure;
- effect on existing claims/remedies under the resolved settlement terms.

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

- required form for amendment/contractual waiver/settlement;
- effect of no-oral-modification or entire-agreement clauses;
- legal effect of conduct/silence/course of dealing;
- special statutory requirements for changing particular transactions;
- historical rules at the change date;
- settlement contract form/effect under the relevant regime.

Do not hardcode universal waiver/amendment doctrines.

## Cross-track handoffs

### From/to BL2

Consume authority/approval for the change when material. Return only transaction-state consequences; BL2 retains corporate ownership of authority/approval propositions.

### From/to BL4

BL4 may signal that settlement/negotiation or dispute conduct produced a candidate contractual change. BL3 resolves agreement/content/change state. BL4 then consumes the committed new state for remaining breach/claim/remedy/deadline/procedure questions.

BL3 must not convert a contractual waiver proposition directly into a waived claim, remedy, objection, deadline, or procedural right.

### To BL5

Provide changed commercial consideration/payment/cost allocation. BL5 decides statutory tax consequences.

### To BL7

If parties purport to waive/allocate mandatory compliance, route BL7. Private variation does not remove public-law duties.

### To BL8

Provide exact changed governing-law/dispute/payment/trade clause content. BL8 owns cross-border legal consequences where material.

## Failure modes

- every email treated as amendment;
- one accommodation treated as permanent contractual waiver;
- contractual waiver promoted directly into waiver of claim/remedy/procedural right;
- course of dealing treated as automatic override of written terms;
- prior contract state overwritten without history;
- sibling units loaded despite reliable committed prior state;
- amendment accepted without checking actor authority/approval when material;
- settlement posture and settlement transaction state collapsed;
- BL3 resolving remedies merely because it interpreted a settlement;
- private amendment treated as changing statutory tax/regulatory responsibility;
- all downstream propositions invalidated instead of exact dependents.
