# BL2 — Entity / Actor State

## Owns

Establishing the legally relevant business actor before authority, approval, ownership, or transaction conclusions are made.

This unit determines **who the actor actually is and what corporate role/state is materially relevant**. It does not decide whether a transaction exists, whether conduct is regulated, or whether a foreign-investment regime applies.

## Does not own

- contract formation/content/performance — BL3;
- breach/remedy/dispute conclusions — BL4;
- tax consequences — BL5;
- employment classification — BL6;
- sector/public-law permission — BL7;
- corporate ownership/cap-table/voting/control state — `ownership-control-state-change.md`;
- foreign-investor status, market-access or foreign-investment control tests — BL8.

## Activate when

Use when the answer depends on any of the following:

- which legal entity is acting;
- whether the named business unit is actually a separate legal actor;
- whether the relevant person acts for the company, a parent, subsidiary, branch, office, owner, or another entity;
- whether corporate form/state changes the downstream proposition;
- whether current corporate records are needed before authority or ownership can be analyzed.

Skip or compress when the entity and actor identity are already reliably established and cannot change the requested action.

## Required state

Where material, capture:

- legal name and entity identity;
- asserted trading/brand name versus legal entity name;
- corporate form/status;
- parent/subsidiary/affiliate/branch/business-unit relationships;
- actor name and asserted role;
- relevant corporate records/documents;
- event date or proposed action date;
- evidence provenance and any inconsistency between documents.

## Core distinctions

### Business brand ≠ legal actor

A commercial name, product name, platform name, project name, department, or internal business unit is not automatically the legal entity that owns rights, owes obligations, employs people, holds licenses, or signs contracts.

### Company ≠ owner

An owner, member, shareholder, founder, or parent company is not automatically identical to the company itself.

Do not transfer rights, obligations, authority, assets, liabilities, or approvals between them merely because of ownership or control.

### Parent ≠ subsidiary

Economic control, branding, shared management, or group membership does not by itself collapse separate entities into one legal actor.

### Branch/business unit ≠ automatically separate entity

First establish the legal status and relationship of the operating unit before treating it as independently capable of owning rights or obligations.

### Role ≠ authority

Entity/actor identification determines who the person is and which office/role they hold. Whether that role can bind the company belongs to `authority-representation.md`.

### Entity relationship ≠ ownership/control state

This unit may establish that entities or actors are related, but it does not reconstruct cap tables, voting rights, control rights, or completed ownership state.

When those propositions are material, load `ownership-control-state-change.md` and consume its committed result.

### Current record ≠ historical state

Corporate state may change over time. A current registry extract, charter, appointment, member/shareholder record, or internal resolution may not prove the state at an earlier transaction date.

## Decision procedure

1. **Identify the business action.** Determine which entity must perform, authorize, receive, own, pay, employ, invest, or otherwise act.
2. **Separate commercial labels from legal identity.** Normalize brand names, abbreviations, group names, and internal units into candidate legal actors.
3. **Resolve the relevant entity.** Use documents/records appropriate to the proposition and date.
4. **Map actor relationships.** Distinguish owner, shareholder/member, manager, legal representative, employee, delegate, parent, subsidiary, affiliate, branch, or external agent without assuming authority or reconstructing ownership/control state.
5. **Bind state to time.** Use the entity/role state applicable to the transaction or proposed action date.
6. **Preserve uncertainty.** If records conflict or entity identity is unresolved, keep downstream propositions conditional.
7. **Hand off only resolved state.** Authority questions go to BL2 authority; ownership/control questions go to BL2 ownership; transaction questions go to BL3; foreign-investment consequences go to BL8.

## Evidence hierarchy by proposition

There is no universal corporate-document hierarchy. Ask what proposition is being proved.

Examples:

- legal entity identity may require registry/current corporate records;
- role/appointment may require appointment instruments, charter, resolutions, or official records;
- historical role may require records effective at the relevant time;
- group relationship may require corporate records showing the relationship;
- internal business-unit descriptions may be evidence of operations but not separate legal personality.

If cap-table, voting, or control evidence becomes material, route that proposition to `ownership-control-state-change.md` rather than resolving it here.

Do not treat a website, email signature, business card, invoice header, or contract recital as conclusive when authoritative corporate records are material.

## Live authority triggers

Resolve current authority when the legal status of an entity form, branch, representative office, corporate actor, registry effect, or corporate-state rule materially affects the proposition.

Do not hardcode:

- current registration procedures;
- filing forms;
- registry mechanics;
- statutory role definitions likely to depend on current legislation;
- current documentary requirements.

Stable knowledge should describe what must be established, not memorize current administrative detail.

## Cross-track handoffs

### To authority / representation

Provide:

- entity identity;
- actor identity;
- asserted and documented roles;
- temporal anchor;
- relevant charter/appointment/delegation evidence;
- unresolved identity issues.

Do not pre-decide authority.

### To ownership / control

Provide entity identity, actor/entity relationships, temporal anchor, and relevant identity records. The ownership unit resolves cap-table, voting, control, and corporate-state propositions.

### To BL3

Provide the resolved contracting/transaction actor and any identity condition that affects transaction analysis.

### To BL5

Provide entity/actor classification only where tax consequences depend on it. BL5 decides tax treatment.

### To BL7

Provide the legal operator/entity when regulatory permission depends on who conducts the activity.

### To BL8

Provide only the entity identity, actor/entity relationship, and temporal state resolved by this unit.

Ownership/control facts may be handed to BL8 **only when already resolved by `ownership-control-state-change.md`**. This unit must not reconstruct cap-table or control state merely because BL8 needs those facts.

BL8 owns foreign-investor/control tests and market-access consequences.

## Failure modes

- founder treated as company;
- group brand treated as contracting entity;
- parent and subsidiary collapsed;
- branch/business unit assumed to be independently liable without resolving status;
- title or job description promoted directly into signing authority;
- entity unit reconstructing cap table/voting/control state instead of activating ownership unit;
- current corporate records used to prove historical state without checking timing;
- company website treated as authoritative corporate-state evidence;
- foreign investor/control conclusion made inside BL2 from corporate identity alone.

## Escalation

Increase verification when entity identity is disputed, records conflict, the transaction is material/irreversible, ownership is changing, authority depends on historical state, or an enforcement/dispute issue turns on which entity actually acted.