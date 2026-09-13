# BL4 — Dispute Posture / Procedure / Settlement

## Owns

Determining how an existing or threatened dispute should be procedurally handled under a resolved or explicitly conditioned forum/regime, including invocation of a dispute-resolution clause, filing mechanics/sequence, urgent protection, settlement posture, and coordination of preserved claims/remedies.

This unit owns **dispute posture and procedure**, not the contractual existence/content of the dispute clause, not the deadline proposition itself, and not cross-border governing-law/treaty/international-enforcement overlay.

## Does not own

- contract formation/content/obligations/performance — BL3;
- dispute-clause existence/content and its contract-law formation/incorporation/validity/effect as a contractual term — BL3;
- breach/excuse/liability — `breach-excuse-liability.md`;
- remedy/loss/mitigation — `remedies-loss-mitigation.md`;
- notice/evidence-preservation/limitation/deadline timing state — `notice-evidence-deadlines.md`;
- foreign governing-law/treaty/international-enforcement overlay — BL8;
- regulatory enforcement/compliance — BL7.

## Activate when

Use when the user needs to decide how to act in an existing or imminent dispute, including:

- whether/how to invoke a resolved dispute-resolution clause;
- pre-action negotiation/escalation procedure;
- arbitration/court/other forum procedure under the resolved regime;
- filing mechanics and procedural sequence using an already resolved/conditioned filing window where material;
- urgent/interim protection;
- preserving options while negotiating;
- settlement posture;
- procedural consequence of a committed BL3 waiver/change/settlement term;
- coordinating claim/remedy strategy with committed deadline/evidence-preservation state.

Skip when no dispute/procedural decision is material to the requested action.

## Required state

Where material, consume:

- committed BL3 dispute-resolution clause proposition;
- BL3 contractual validity/effect proposition for the clause where material;
- BL8 governing-law/treaty/international-enforcement overlay where cross-border;
- committed/conditioned BL4 breach/liability state;
- available/conditioned remedies;
- committed notice/deadline/evidence-preservation state where material;
- parties and relevant procedural actors;
- dispute objective;
- settlement/change state from BL3 where terms were actually agreed;
- current/historical procedural authority where material.

A sibling knowledge unit need not be loaded solely because its committed proposition is consumed.

## Core distinctions

### Dispute-clause content/effect ≠ invocation/procedure

BL3 owns whether the clause exists, what it says, whether it was contractually incorporated, and its contract-law validity/effect as a term.

BL4 owns what to do procedurally with that resolved/conditioned clause:

- invocation;
- preconditions to filing;
- filing mechanics;
- procedural sequence;
- posture/remedies in the forum.

### WHEN to file ≠ HOW/WHERE to file

`notice-evidence-deadlines.md` owns the temporal/deadline proposition:

```text
trigger
→ clock
→ tolling/suspension/extension
→ expiry / filing window
→ preservation state
```

This unit consumes that committed timing state and owns the procedural action:

```text
where to file
how to invoke
what sequence to follow
what filing/defense/interim step to take
```

Example:

```text
Deadline expires on D.
→ committed deadline proposition from notice-evidence-deadlines.md

How do we commence arbitration before D?
→ dispute-posture-procedure-settlement.md
```

Do not reopen the notice/deadline unit merely because a procedural step consumes its committed proposition. Reopen only when timing itself becomes unresolved, disputed, stale, contradictory, or material to recalculate.

### Forum/procedure ≠ governing-law/treaty overlay

BL8 owns cross-border conflict/treaty/international-enforcement propositions where material. BL4 consumes them and decides dispute posture within the resolved or conditioned regime.

Do not infer:

```text
arbitration clause exists
→ arbitration definitely has jurisdiction
```

without resolving the material contractual/cross-border/procedural propositions.

### Claim strength ≠ procedural readiness

A strong merits position may still require notice, evidence preservation, deadline action, jurisdiction/forum analysis, or procedural prerequisites.

### Negotiation ≠ waiver/tolling

Settlement discussions do not automatically suspend deadlines, waive objections, or change contractual rights.

Consume committed timing state from `notice-evidence-deadlines.md` and BL3 change/waiver propositions where material.

### Settlement posture ≠ settlement transaction state

BL4 owns:

- whether to negotiate;
- claim/remedy posture;
- reservation/preservation strategy;
- procedural implications of settlement steps.

For ordinary commercial settlement terms, BL3 `variation-waiver-settlement.md` owns the new transaction state. Employment-specific ongoing terms return to BL6 engagement/terms; agreed separation/end-state returns to BL6 separation/protection. Split mixed terms into owned propositions.

Then BL4 consumes that committed state for remaining claims/remedies/procedure.

### Filing option ≠ business recommendation

A procedure may be legally available but commercially irrational. BL4 may explain procedural/legal trade-offs, but should not invent business facts or guarantee outcomes.

## Decision procedure

1. **State the dispute objective.** Preserve performance, collect, exit, defend, stop conduct, protect assets/evidence, settle, or obtain a ruling.
2. **Consume clause/forum state.** Use committed BL3 dispute-clause proposition and BL8 overlay where material. Do not reconstruct them.
3. **Consume preservation/timing state.** Use committed notice, evidence-preservation, limitation/deadline, cure, and reservation propositions. Reopen the timing unit only if that state is itself unresolved/stale/material to recalculate.
4. **Consume remedy state.** Identify what relief is actually available/conditioned rather than pleading every conceivable remedy.
5. **Resolve procedural prerequisites and mechanics.** Negotiation/escalation/mediation/arbitration/court or other steps only under current/historical authority where material.
6. **Assess urgent protection.** Identify whether immediate evidence/asset/status-quo preservation is material; do not promise availability without authority.
7. **Choose posture.** Negotiate, demand, reserve rights, file, defend, seek interim relief, pause pending verification, or other action supported by state.
8. **Protect against silent waiver/deadline loss.** Consume committed timing/preservation state; do not own/recalculate the clock unless returned to the timing owner.
9. **Handle settlement loop correctly.** Return commercial changes to BL3 and employment-specific changes to the relevant BL6 unit. Resume dependent BL4 reasoning from the substantive owner's committed or conditioned update.
10. **Commit procedural state.** Ready, conditional, verification-required, legally review-required, blocked, or unresolved as appropriate for the action.

## Dispute-state pattern

```text
P-BL4-DISP-01
objective: <collect / defend / terminate / preserve / settle / other>
clause_dependency: P-BL3-...
bl8_overlay_dependency: <if cross-border>
remedy_dependency: P-BL4-REM-...
deadline_dependency: P-BL4-DEADLINE-...
procedural_step: <negotiation / filing / interim / defense / settlement / other>
status: READY / CONDITIONAL / VERIFY / REVIEW_REQUIRED / BLOCKED / UNRESOLVED
```

Use the canonical action-readiness states at synthesis time; these labels are local working state only.

For employment claims, `clause_dependency` and the BL3 clause inputs apply only
if a material BL3-owned clause exists. Use BL6 term/merits/change IDs for
employment-specific content and resolve the procedural forum under the applicable
regime. No commercial contract or arbitration clause is required merely to
analyze a statutory employment claim.

Employment settlement path: BL4 claim posture -> BL6 terms/separation update ->
BL4 remaining claims/remedies/procedure. The commercial example below applies to
BL3-owned changes only.

## Settlement loop

Correct architecture:

```text
BL4
→ settlement posture / negotiation
→ candidate settlement terms
→ BL3 resolves whether terms formed and what obligations changed
→ BL3 commits changed transaction state
→ BL4 consumes new state
→ remaining claim/remedy/procedure analysis
```

Incorrect:

```text
BL4 negotiates settlement
→ BL4 silently rewrites contract obligations
```

## Evidence requirements

Potential evidence includes:

- committed dispute-resolution clause and source document;
- committed notices/reservations/cure and deadline propositions;
- proof of service/transmission where relevant;
- procedural correspondence;
- filing/registration records;
- evidence-preservation inventory from the timing/preservation unit;
- settlement offers/communications with appropriate confidentiality/privilege caution where applicable;
- evidence of agreed settlement terms returned to BL3;
- authority for forum/procedural requirements.

This unit may consume preserved evidence but does not become the merits owner merely because evidence is used procedurally.

Do not confuse a negotiation communication with a formed settlement agreement.

## Live authority triggers

Use Authority Resolver where the result depends on:

- procedural prerequisites;
- filing/invocation mechanics and sequence;
- interim/urgent relief availability;
- arbitration/court/forum procedure;
- settlement procedural effect;
- historical procedure at the relevant date;
- current invocation/procedural treatment under the resolved/conditioned clause/forum.

Deadline/limitation/tolling calculations remain owned by `notice-evidence-deadlines.md`. If procedure exposes a new timing question, return that proposition to the timing owner.

Do not hardcode filing deadlines, arbitration/court procedures, limitation periods, fee schedules, or forum-specific mechanics as stable knowledge.

## Cross-track handoffs

### From BL3

Consume:

- dispute-clause existence/content;
- clause contract-law validity/effect;
- settlement/change propositions.

BL4 must not reinterpret a disputed clause stack without returning the term/content question to BL3.

### From notice/evidence/deadlines

Consume committed temporal/deadline/preservation propositions. Use them to choose and sequence procedural actions.

Do not duplicate the trigger/clock/expiry/tolling proposition here.

### From BL8

Consume governing-law/treaty/international-enforcement overlay when material. BL4 does not resolve those cross-border propositions independently.

### To BL3

Return ordinary commercial settlement/amendment/waiver terms to BL3. Return employment-specific changes to BL6 terms/separation and consume its update before deciding remaining claim/procedural consequences.

### To BL7

If the dispute reveals a regulatory enforcement/reporting/public-law issue, route BL7 separately. Private dispute procedure does not absorb regulatory procedure.

## Failure modes

- arbitration/court/forum selected from clause keywords without resolving clause state;
- clause content or contractual validity/effect reconstructed inside BL4 instead of consumed from BL3;
- deadline trigger/clock/expiry duplicated inside dispute procedure;
- committed deadline proposition unnecessarily reopened when user only asks how/where to file;
- governing law, forum, procedure, and enforcement collapsed;
- claim merits treated as procedural readiness;
- negotiation assumed to toll deadlines;
- every available remedy pleaded without objective/prerequisite analysis;
- settlement discussion treated as formed settlement;
- BL4 silently rewriting BL3 obligations after settlement;
- urgent relief promised from memory;
- current procedural rules applied to historical situation without verification.

## Escalation

Increase verification for imminent filing/limitation deadlines, injunction/interim relief, asset dissipation, high-value disputes, contested arbitration/jurisdiction issues, cross-border enforcement, settlement releasing material claims, or any irreversible procedural step.
