# Specialist Handoff — Semantic Contract v0.3

A handoff transfers resolved state, unresolved state, ownership context, and a precise proposition request. It is not permission for the receiver to reinterpret upstream decisions silently.

## Deployment-topology neutrality

A `sending track`, `receiving track`, `owner`, or `owner-bound specialist` is a **semantic role**, not a requirement for a separate agent, process, model, thread, or network hop.

A single assistant/runtime may execute several BL roles sequentially against the same shared Legal Work State. In that topology, `handoff`, `return to owner`, and `activate another track` mean that semantic control for the relevant proposition moves to the role that owns the decision; they do not imply spawning another agent.

Multi-agent execution is optional. Whether execution is single-agent or multi-agent, the same invariants apply:

- every material proposition keeps one accountable owner;
- only that owner may commit or replace its owned proposition/classification;
- shared object IDs and `state_revision` remain authoritative;
- contradictory downstream evidence returns to the semantic owner rather than being rewritten locally;
- specialist findings remain candidate depth until accepted/conditioned/rejected by the owning BL role.

Do not create extra agents merely because a handoff boundary exists.

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

In a single-runtime implementation, the `sender` and `receiver` may be successive semantic roles executed by the same model instance. The handoff fields still remain meaningful because they prove which role owned each decision and which shared-state revision it used.

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

The same runtime may execute BL2 and then BL3. The example records a semantic ownership transition, not a mandatory agent-to-agent message.

## Return-to-owner rule

A receiving track must **never reconstruct or replace upstream-owned state**.

If contradictory evidence appears:

1. emit `CONTRADICTION_SIGNAL`;
2. identify the affected upstream fact/classification/proposition ID;
3. identify accountable owner;
4. attach the new evidence ID(s);
5. identify dependent reasoning/actions that should become conditional or paused;
6. return semantic control to the owner;
7. resume only after the shared state revision contains the owner's update.

`Return to owner` may be an in-process role transition inside one assistant. It does not require a distinct agent, but it still forbids the currently active non-owner role from mutating the upstream-owned proposition.

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

Activation means making that BL role and its required knowledge/runtime contracts active for the proposition. It does not inherently mean creating another agent.

## Specialist-depth handoff

A JIT specialist is a temporary depth provider and may only be invoked **under an accountable BL owner**.

A specialist may be implemented as another tool/agent/model, or as a bounded specialist role inside the same runtime. Topology does not change the ownership rule: the specialist never becomes the proposition owner merely because it produced the technical analysis.

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

This integration step is required even when the specialist and owner were executed by the same underlying assistant/model.

## BL8 dual-role note

BL8 may own cross-border propositions (governing law, treaty/CISG, foreign-investment market access, FX, trade/customs) or merely provide a cross-border overlay to another owner's substantive proposition. The handoff must state which role BL8 is performing.