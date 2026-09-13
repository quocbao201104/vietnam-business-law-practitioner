# BL2 — Representation / Authority

## Owns

Determining whether a person or other actor can bind, represent, or otherwise act for the relevant entity for the proposition at issue.

This unit owns **representation and authority scope**. It does not own the contract terms themselves or the separate question of whether an internal corporate approval was required and obtained.

## Does not own

- transaction formation/content/performance — BL3;
- internal reserved-matter/related-party approval — `approval-conflict-governance.md`;
- tax consequences — BL5;
- sector permission — BL7;
- foreign-investment approval/market-access consequences — BL8.

## Activate when

Use when the decision depends on:

- who may sign or act for the entity;
- whether a representative's authority covered the specific act;
- whether delegation or authorization is valid/current/sufficient;
- whether apparent conduct, ratification, acceptance, or course of dealing may affect binding effect after disputed authority;
- whether authority existed at the relevant transaction/action date.

## Required state

Where material, capture:

- resolved entity identity;
- actor identity and role;
- claimed source of authority;
- scope/limits of authority;
- relevant time period;
- delegation/authorization documents;
- charter/resolution/appointment evidence where relevant;
- counterparty knowledge or notice where material;
- post-act conduct: acceptance, performance, payment, confirmation, objection, ratification-like behavior;
- separate internal-approval requirements, if any.

## Core distinctions

### Role/title ≠ authority

`Founder`, `owner`, `director`, `CEO`, `manager`, `employee`, `legal representative`, `authorized representative`, or similar labels do not by themselves answer the whole authority question.

Resolve the source and scope of authority for the act in question.

### Representation ≠ internal approval

A person may be able to represent/sign for an entity while the transaction still requires an internal approval, reserved-matter decision, or conflict process.

Do not collapse:

```text
can represent/sign
=
company internally approved transaction
```

The second question belongs to `approval-conflict-governance.md`.

### Authority source ≠ unlimited scope

Authority may be limited by:

- transaction type;
- amount/value;
- duration;
- geography;
- counterparty;
- subject matter;
- condition or approval dependency;
- revocation/expiry;
- corporate document or legal rule.

Do not infer unlimited authority from the existence of some authority.

### Missing written authorization ≠ automatic non-binding result

Absence of a visible power of attorney or other written authorization is a fact requiring analysis, not an automatic conclusion that the entity is not bound.

Other legally relevant evidence may include role, prior authorization, subsequent confirmation, performance, acceptance, knowledge, payment, course of dealing, or other conduct. Whether those facts have legal effect must be verified under the applicable current/historical authority.

### Signature ≠ proof of authority

A signature proves that someone signed. It does not by itself prove the signer had authority, that authority covered this transaction, or that required internal approvals were satisfied.

### Internal limit ≠ automatically external result

A restriction internal to the company and its effect against a counterparty can be different questions. Preserve counterparty knowledge/notice and the applicable legal rule rather than assuming every internal limitation automatically controls the external transaction.

## Decision procedure

1. **Resolve the entity and actor.** Consume `entity-actor-state.md` rather than reconstructing entity identity here.
2. **State the exact act.** Authority to sign one agreement, borrow, dispose of assets, hire, litigate, or file may not be interchangeable.
3. **Identify claimed authority source.** Role, statutory/corporate position, charter, resolution, delegation, power of attorney, or another legal source.
4. **Resolve temporal validity.** Was the authority in force at the relevant action date?
5. **Resolve scope.** Did the authority cover this exact act and material conditions?
6. **Separate internal approval.** If a reserved-matter/conflict/related-party approval may be required, activate `approval-conflict-governance.md` rather than treating representation as sufficient.
7. **If authority is disputed, inspect legally relevant conduct.** Preserve evidence of knowledge, acceptance, confirmation, performance, payment, objection, or course of dealing.
8. **Call live authority where binding effect depends on current/historical law.** Do not decide ratification/apparent authority/effect from generic common-law intuition.
9. **Commit an owned proposition.** Examples: `authority supported`, `authority conditional`, `authority unresolved`, `authority exceeded`, subject to live-law verification.
10. **Hand the authority proposition to downstream owners.** BL3 uses it as a dependency where formation/binding effect depends on authority.

## Authority proposition design

Prefer proposition-level conclusions such as:

- `P-BL2-AUTH-01: Actor X held authority to perform Act Y for Entity Z at time T.`
- `P-BL2-AUTH-02: Scope of delegation included transaction category Q.`
- `P-BL2-AUTH-03: Binding effect remains conditional on unresolved post-act ratification/knowledge rule.`

Avoid global statements such as `the CEO can sign anything`.

## Evidence requirements

Potential evidence may include:

- corporate/registry status;
- charter or governance documents;
- appointment instrument;
- board/member/shareholder resolution;
- power of attorney/delegation;
- transaction-specific authorization;
- specimen/signature records where relevant;
- emails/communications about authority;
- prior similar dealings;
- invoices, delivery, payment, performance, acceptance, confirmation, or objection after the act.

Evidence is proposition-specific. Do not require every document for every authority question.

## Live authority triggers

Live verification is normally required when the answer turns on:

- legal representative powers or limits;
- statutory authority of a corporate role;
- effect of delegation/revocation/expiry;
- effect of unauthorized representation;
- ratification/acceptance/course-of-dealing consequences;
- enforceability against a counterparty despite internal limits;
- historical authority rules at the transaction date.

Do not hardcode current statutory powers, thresholds, registration effects, formalities, or article numbers.

## Cross-track handoffs

### From entity/actor state

Consume entity identity, actor identity/role, temporal anchor, and evidence. Do not reopen them unless contradictory evidence appears; then emit `CONTRADICTION_SIGNAL`.

### To approval/conflict governance

If representation is established but internal approval may still be required, hand off:

- transaction/act;
- actor and authority proposition;
- conflict/related-party signals;
- candidate reserved matter;
- unresolved internal approval question.

### To BL3

Provide only the authority proposition and conditions relevant to transaction formation/binding effect. BL3 owns agreement/terms/obligations.

### To BL4

Where a dispute turns on authority, provide the committed authority proposition. BL4 owns dispute posture/remedy/procedure, not authority classification.

## Failure modes

- founder/owner status treated as signing authority;
- title treated as unlimited power;
- signature treated as proof of authority;
- representation treated as proof of internal approval;
- missing POA treated as automatic invalidity;
- internal authority restriction automatically projected against the counterparty without checking the applicable rule;
- later company conduct ignored when authority is disputed;
- generic common-law concepts imported without verifying Vietnamese legal authority;
- BL3 or BL5 independently reconstructing authority instead of consuming BL2 state.

## Escalation

Increase verification when authority is disputed, the act is high-value/irreversible, a counterparty may have relied on the representative, the signer acted outside visible scope, corporate records conflict, or the matter is already in dispute/enforcement.