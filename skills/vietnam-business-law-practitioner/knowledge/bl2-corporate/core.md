# BL2 — Entity / Authority / Ownership / Governance

BL2 resolves corporate identity, representation/authority, internal governance approval, and corporate ownership/control state.

This `core.md` is a **JIT router**, not the full BL2 handbook. Load only the capability unit needed for the material proposition.

## Owns

BL2 owns propositions about:

- legal entity and actor state;
- representation/signing/acting authority;
- internal corporate approval, reserved matters, conflicts, and related-party governance;
- corporate ownership, voting/control, and corporate-state transitions.

BL2 does **not** own the whole transaction merely because a company is involved.

## Does not own

- contract formation/content/performance — BL3;
- breach/remedies/dispute procedure — BL4;
- tax consequences — BL5;
- employment classification/pathway — BL6;
- sector/public-law permission — BL7;
- foreign-investor status, foreign-investment control tests, market access, FX, treaty/trade consequences — BL8.

## Core distinctions

- company ≠ owner ≠ manager ≠ representative;
- business/brand name ≠ legal entity;
- role/title ≠ authority;
- representation/signing authority ≠ internal corporate approval;
- conflict/related-party signal ≠ automatic invalidity;
- signed transfer/subscription ≠ completed ownership state;
- economic contribution ≠ legal ownership;
- ownership percentage ≠ complete corporate-control analysis;
- corporate control facts ≠ foreign-investment control test.

## JIT capability routing

### Entity / actor state

Load `entity-actor-state.md` when the question depends on:

- which legal entity is actually acting;
- parent/subsidiary/branch/business-unit distinctions;
- actor role/state;
- historical versus current corporate identity/role.

### Representation / authority

Load `authority-representation.md` when the question depends on:

- who may sign or bind the entity;
- source/scope/duration of delegation;
- disputed or unauthorized representation;
- ratification/acceptance/course-of-dealing effects.

### Approval / conflict / governance

Load `approval-conflict-governance.md` when the question depends on:

- board/member/shareholder/owner approval;
- reserved matters;
- conflict of interest;
- related-party governance;
- quorum/voting/disclosure/abstention or approval defects.

### Ownership / control / state change

Load `ownership-control-state-change.md` when the question depends on:

- who legally owns an interest;
- cap table/voting/control state;
- whether transfer/subscription/contribution actually changed corporate state;
- ownership/control state before or after a corporate transaction.

Do not load all four units by default.

## Typical compositions

```text
Can founder sign this agreement?
→ entity-actor-state
→ authority-representation
```

```text
CEO can sign, but is this related-party deal internally approved?
→ authority-representation
→ approval-conflict-governance
```

```text
Investor signed share purchase and paid; do they own/control the company now?
→ ownership-control-state-change
→ approval-conflict-governance only if corporate approval is material
→ BL3 for contractual closing rights/obligations
→ BL8 if foreign-investment status/market access is triggered
```

## Live authority behavior

Stable BL2 knowledge defines what must be distinguished and proved. Use Authority Resolver when current/historical law materially determines:

- corporate role/status;
- statutory representation powers;
- authorization/delegation effects;
- reserved matters or voting/approval procedure;
- related-party/conflict definitions and consequences;
- ownership creation/transfer/completion;
- corporate-state transition rules.

Do not hardcode current article numbers, thresholds, voting percentages, forms, registration procedures, or deadlines.

## Handoff rules

- BL2 → BL3: entity, authority, approval, and ownership/state propositions only; BL3 owns the transaction.
- BL2 → BL5: resolved corporate/ownership facts; BL5 owns tax consequences.
- BL2 → BL7: legal operator/ownership facts when regulation depends on them; BL7 owns permission/compliance.
- BL2 → BL8: cap table, corporate voting/control rights, state changes, and relevant dates; BL8 owns foreign-investor/control/market-access consequences.

If downstream evidence contradicts a BL2-owned proposition, the downstream owner emits `CONTRADICTION_SIGNAL`; it must not silently reconstruct BL2 state.

## Failure modes

- owner/founder treated as company;
- title treated as unlimited authority;
- signature treated as internal approval;
- missing POA treated as automatic non-binding result;
- related-party status treated as automatic invalidity;
- payment or signed transfer treated as completed ownership;
- ownership percentage used as universal control rule;
- BL2 deciding foreign-investment market-access/control propositions;
- loading all corporate knowledge for a narrow authority question.
