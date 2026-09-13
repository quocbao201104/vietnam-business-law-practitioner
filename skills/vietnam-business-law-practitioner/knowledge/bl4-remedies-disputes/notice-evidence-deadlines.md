# BL4 — Notice / Evidence / Deadlines

## Owns

Preserving the user's legal position through required notices, objections, reservations of rights, evidence preservation, cure/escalation steps, limitation/deadline tracking, and other time-sensitive claim-preservation actions.

This unit owns **preservation and timing state**. It does not decide the underlying BL3 obligation, breach/liability proposition, or the final remedy merely because a deadline or notice exists.

## Does not own

- contract formation/terms/obligations/performance — BL3;
- breach/excuse/liability — `breach-excuse-liability.md`;
- remedy/loss/mitigation — `remedies-loss-mitigation.md`;
- forum/procedure/dispute posture — `dispute-posture-procedure-settlement.md`;
- employment classification — BL6;
- public-law enforcement/compliance — BL7;
- governing-law/treaty/cross-border enforcement overlay — BL8.

## Activate when

Use when the user's rights/options may depend on:

- notice of breach/default/defect;
- cure demand or objection;
- reservation of rights;
- acceptance/rejection procedure;
- evidence preservation;
- claim filing or contractual time bar;
- statutory limitation/prescription/deadline;
- escalation window;
- settlement/negotiation that may affect time limits;
- urgent need to stop evidence loss or preserve a procedural option.

Skip when no material preservation/timing proposition remains unresolved.

## Required state

Where material, consume:

- exact BL3 obligation/performance/change proposition;
- exact BL4 breach/remedy proposition whose preservation is at issue;
- contract clause governing notice/cure/deadline where resolved;
- dispute-clause proposition from BL3 where timing depends on it;
- governing-law/forum overlay from BL8 where material;
- known event dates and temporal anchors;
- existing notices/communications;
- evidence inventory and source provenance;
- action objective and urgency.

Do not load sibling units solely to consume already committed propositions.

## Core distinctions

### Having a right ≠ preserving/exercising it correctly

A remedy can exist in principle while being unavailable, weakened, delayed, or disputed because required notice, timing, cure, election, or procedure was not satisfied.

### Notice sent ≠ notice legally sufficient

Resolve where material:

- sender/recipient;
- required channel/address;
- content;
- timing;
- triggering event;
- proof of transmission/receipt;
- contractual/statutory form requirements;
- whether later conduct altered or waived the notice requirement.

Do not treat an email subject line or internal memo as sufficient by default.

### Notice requirement ≠ breach proposition

A notice may preserve a right, trigger cure, start a period, or exercise an option. It does not itself prove breach/liability.

### Negotiation ≠ deadline suspension

Settlement talks, informal discussions, promises to resolve, or silence do not automatically suspend contractual/statutory deadlines.

Treat deadline suspension/tolling/extension as a separate proposition requiring support.

### Evidence exists ≠ fact resolved

Preserve provenance and conflicts. A receipt, screenshot, invoice, log, email, witness statement, or system record is evidence concerning a proposition, not automatic truth.

### Evidence preservation ≠ evidence sufficiency

Preserving material prevents loss; it does not establish admissibility, weight, authenticity, or legal sufficiency in every forum.

### One deadline ≠ all deadlines

A matter may contain different clocks for:

- contractual notice;
- cure;
- acceptance/rejection;
- claim submission;
- limitation/prescription;
- arbitration/court filing;
- appeal/review;
- interim protection;
- regulatory or administrative action.

Do not create one `DEADLINE` field for the whole dispute.

## Decision procedure

1. **Identify the right/action being preserved.** Example: termination option, damages claim, defect objection, payment demand, arbitration filing.
2. **Map triggering event(s).** Use proposition-specific temporal anchors.
3. **Identify notice/cure/election requirements.** Consume resolved contract terms and live authority where material.
4. **Map each material deadline separately.** Record source, trigger, duration/date, uncertainty, and affected action.
5. **Check prior communications.** Determine whether existing notice/objection/reservation may satisfy, alter, or complicate the requirement.
6. **Build evidence inventory.** Preserve source, date, custodian/location, authenticity concerns, and proposition supported.
7. **Identify evidence-loss risk.** Logs, CCTV, ephemeral chats, system data, physical goods, witness availability, or third-party records may require prompt preservation.
8. **Avoid silent waiver.** If negotiation/accommodation could affect rights, record reservation/waiver questions and hand contractual-change issues to BL3.
9. **Commit preservation state.** Preserved, action-needed, deadline-uncertain, disputed, expired/at-risk subject to authority, or unresolved.
10. **Hand execution/procedure onward.** If filing/forum/procedure becomes material, activate `dispute-posture-procedure-settlement.md`.

## Deadline-state pattern

```text
P-BL4-DEADLINE-01
right/action: <termination / claim / filing / objection / other>
source: <contract / statute / forum rule / other>
trigger_event: <event>
temporal_anchor: <date or unresolved>
deadline: <date/range/unresolved>
status: OPEN / ACTION_REQUIRED / DISPUTED / UNRESOLVED / EXPIRED_OR_AT_RISK
freshness_required: yes/no
```

Do not calculate a date from memory when the governing rule or trigger is unresolved.

## Notice-state pattern

```text
P-BL4-NOTICE-01
purpose: <default / cure / objection / reservation / exercise right>
required_content: <resolved/conditioned>
channel/recipient: <resolved/conditioned>
trigger/date: <...>
evidence_of_send/receipt: <...>
status: SATISFIED / CONDITIONAL / DISPUTED / ACTION_REQUIRED / UNRESOLVED
```

## Evidence ledger

For material disputes, map evidence to propositions rather than collecting files indiscriminately:

```text
EVIDENCE_ID
source/custodian
created_at
proposition_supported
supports / contradicts / context-only
authenticity/integrity issue
preservation risk
```

Do not turn evidence volume into confidence by source count.

## Live authority triggers

Use Authority Resolver where the result depends on:

- statutory limitation/prescription;
- contractual notice enforceability/effect;
- cure/election requirements;
- procedural filing periods;
- tolling/suspension/extension rules;
- historical rules at the relevant trigger date;
- evidence/form requirements whose current status affects action readiness.

Do not hardcode limitation periods, filing windows, notice forms, or procedural deadlines as permanent knowledge.

## Cross-track handoffs

### From BL3

Consume committed notice/cure/acceptance/termination clause content and changed transaction state. If a notice/negotiation arguably modified contractual rights, return that change question to BL3.

### From breach/remedy units

Receive the exact breach/remedy proposition whose preservation depends on notice/evidence/deadline. Do not broaden into a global dispute checklist.

### To dispute posture/procedure

Provide:

- preserved/unpreserved rights;
- filing/notice deadlines;
- evidence risks;
- required next procedural step;
- unresolved timing conditions.

### To BL8

Where cross-border governing law, treaty, or international-enforcement rules affect limitation/forum/procedure, consume BL8 overlay rather than deciding it here.

## Failure modes

- notice treated as paperwork after remedy analysis;
- email automatically treated as legally sufficient notice;
- settlement talks assumed to suspend deadlines;
- one deadline field used for the whole case;
- current limitation period applied to historical claim without verification;
- evidence document label treated as truth;
- evidence preservation confused with evidentiary sufficiency;
- expired/uncertain deadline hidden behind confident remedy advice;
- contractual waiver/change silently decided inside BL4 instead of returning to BL3;
- broad evidence collection unrelated to material propositions.

## Escalation

Increase verification when a deadline may expire soon, evidence is ephemeral, termination/claim rights depend on notice, large-value recovery is at risk, a counterparty disputes receipt/authenticity, negotiations are ongoing near a deadline, or procedural timing is uncertain.