# Specialist Handoff — Semantic Contract v0.2

A handoff transfers resolved state, unresolved state, ownership context, and a precise proposition request. It is not permission for the receiver to reinterpret upstream decisions silently.

## Required handoff elements

A useful handoff should identify:

- activating issue / `issue_id`;
- sending track;
- receiving accountable owner or owner-bound specialist;
- shared `state_revision` read by the sender;
- resolved fact/classification/proposition IDs;
- unresolved material condition IDs;
- reusable authority IDs;
- exact proposition/question requested from the receiver;
- downstream proposition/action IDs waiting on the result.

The receiver emits an owner-scoped delta. It does not replace the whole Legal Work State.

## Track-to-track example — BL2 to BL3

```text
ACTIVATING ISSUE:
Can the company enter the proposed distribution agreement?

FROM:
BL2

TO:
BL3

STATE REVISION:
r17

UPSTREAM PROPOSITIONS:
P-BL2-01 — Company A entity identity confirmed
P-BL2-02 — Director B representation confirmed
P-BL2-03 — authority scope likely within scope
P-BL2-04 — corporate approval unresolved

OPEN CONDITION:
C-04 — member/board approval may be required

PROPOSITION REQUESTED:
Determine whether an agreement is formed and what contractual obligations it creates.

DEPENDENCY:
Any binding/enforceability proposition that requires corporate approval DEPENDS_ON P-BL2-04.
```

## Return-to-owner rule

A receiving track must **never reconstruct or replace upstream-owned state**.

If contradictory evidence appears:

1. emit `CONTRADICTION_SIGNAL`;
2. identify the affected upstream fact/classification/proposition ID;
3. identify accountable owner;
4. attach the new evidence ID(s);
5. identify dependent reasoning/actions that should become conditional or paused;
6. return to owner;
7. resume only after the shared state revision contains the owner's update.

Examples:

- BL3 discovers a power of attorney → contradiction/signal to BL2;
- BL5 sees payroll-style evidence relevant to worker classification → signal BL6;
- BL7 discovers foreign-platform evidence affecting cross-border status → signal BL8;
- BL8 discovers domestic product regulation → late-route signal to BL7.

The existence of contradictory evidence never creates an exception allowing a downstream track to reclassify upstream state itself.

## Late-route activation

Any active owner may emit `LATE_ROUTE_SIGNAL` when new evidence reveals a materially relevant track that was not initially loaded.

A late-route signal should identify:

- triggering evidence/proposition;
- target BL track;
- route status (`ROUTE_PLAUSIBLE` or `ROUTE_CONFIRMED`);
- proposition requested;
- affected current propositions/actions.

The new track is activated through the canonical route map in `knowledge/INDEX.md`.

## Specialist-depth handoff

A JIT specialist is a temporary depth provider and may only be invoked **under an accountable BL owner**.

Example:

```text
OWNER:
BL8

SPECIALIST:
preferential-origin

QUESTION:
Does product X qualify for preferential origin under the relevant FTA for the planned import date?

INPUTS:
- candidate HS classification
- production/process facts
- country inputs
- shipment facts
- relevant FTA
- temporal anchor(s)

OUTPUT EXPECTED:
- candidate technical finding(s)
- authority/result provenance
- unresolved technical facts
- uncertainty/status

RETURN TO:
BL8
```

The specialist output is **candidate depth**, not an owned legal proposition until BL8 accepts/conditions/rejects it.

## Specialist prohibitions

A specialist must not:

- bypass the owning BL track;
- promote its finding directly into another owner's state;
- decide the whole business matter;
- emit final action readiness;
- resolve a composition conflict;
- overwrite shared state from an older revision.

## Owner integration

After specialist return, the accountable owner:

1. checks technical finding + authority + unresolved facts;
2. decides accept / reject / condition / request more evidence;
3. updates only owned propositions/classifications;
4. creates typed dependencies;
5. triggers downstream invalidation only for `DEPENDS_ON` edges;
6. emits feedback/signals separately from invalidation.

## BL8 dual-role note

BL8 may own cross-border propositions (governing law, treaty/CISG, foreign-investment market access, FX, trade/customs) or merely provide a cross-border overlay to another owner's substantive proposition. The handoff must state which role BL8 is performing.