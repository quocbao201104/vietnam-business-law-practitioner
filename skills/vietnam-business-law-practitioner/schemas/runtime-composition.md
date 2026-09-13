# Runtime Composition — Semantic Contract v0.2

This contract defines how BL1–BL8, live authority, and JIT specialists compose at runtime. It is normative for routing, ownership, invalidation, and synthesis.

## 1. Controlled reasoning loop

The runtime is not a one-way pipeline. It is a controlled loop:

```text
business problem
→ BL1 initial framing + route hypothesis
→ owning BL proposition reasoning
↔ authority resolver as needed
↔ JIT specialist under an owning BL track
↔ late-route activation
↔ contradiction / reclassification review
→ proposition composition
→ per-action readiness
→ business-facing answer
```

A newly discovered fact or authority may activate another owner or invalidate a prior dependent proposition.

## 2. Route hypothesis

BL1 owns initial framing and routing hypotheses, not every substantive legal classification.

Each material route has one of:

- `ROUTE_CONFIRMED`
- `ROUTE_PLAUSIBLE`
- `ROUTE_UNRESOLVED`
- `ROUTE_REJECTED`

Any BL owner may emit `LATE_ROUTE_SIGNAL` when its reasoning reveals a materially relevant track that BL1 did not initially activate.

Late activation must be explicit. The new track receives the shared state and may create or invalidate proposition dependencies. A missed initial route is not repaired by silently reasoning from an unloaded domain.

## 3. Proposition ownership

The accountable unit is a material legal proposition, not an entire case-level decision.

Every material proposition has:

- `proposition_id`
- statement/question
- accountable BL owner
- status
- dependencies
- evidence/authority support
- temporal scope

A proposition may depend on propositions owned by other tracks.

Example:

```text
P-BL2-01: Signatory had authority to bind Company A.       owner BL2
P-BL3-04: Agreement was formed.                            owner BL3
P-BL7-02: Regulated activity may commence.                 owner BL7

ACTION: sign agreement
→ depends on P-BL2-01 + P-BL3-04

ACTION: commence regulated service
→ also depends on P-BL7-02
```

Do not assign multiple owners to the same proposition. Do not force a whole multi-domain business decision into one BL owner.

## 4. Typed dependency edges

Track-level routing is not an executable invalidation graph.

Use proposition-level edges:

- `DEPENDS_ON` — the dependent proposition cannot remain current if the upstream proposition materially changes;
- `CONSTRAINS` — upstream result limits the downstream option space but does not automatically invalidate it;
- `SIGNALS` — information that another owner should review;
- `FEEDBACK` — business/legal consequence that may justify restructuring or re-review.

Only `DEPENDS_ON` propagates automatic `STALE` / `INVALIDATED` status.

`SIGNALS` and `FEEDBACK` create review triggers, not silent invalidation.

## 5. State updates and revisions

All material state objects have stable IDs. The shared state has a monotonically increasing `state_revision`.

Owners emit owner-scoped state deltas. They do not replace the entire shared state.

A stale write based on an older state revision must be rejected or reconciled before it can overwrite newer owner state.

## 6. Contradiction protocol

A downstream track or specialist must never reconstruct or replace upstream-owned state.

When contradictory evidence appears:

1. emit `CONTRADICTION_SIGNAL`;
2. identify the affected upstream fact/classification/proposition;
3. identify the evidence creating the contradiction;
4. return to the accountable owner;
5. mark dependent reasoning conditional or paused where material;
6. resume only after the owner commits an updated state.

## 7. Reclassification state machine

A possible new classification does not immediately rewrite legal reality.

```text
CLASSIFICATION_SIGNAL
→ RECLASSIFICATION_REVIEW
→ RECLASSIFICATION_COMMITTED
```

During `RECLASSIFICATION_REVIEW`:

- the previous classification remains the current committed classification;
- the competing candidate is explicit;
- materially dependent actions may move to `VERIFY_BEFORE_ACTION`;
- exact dependent propositions are identified.

When committed:

- previous classification → `SUPERSEDED`;
- new classification → `RESOLVED`;
- only `DEPENDS_ON` dependents are invalidated/recomputed.

## 8. Authority Resolver is a callable service

The Authority Resolver is not a fixed pipeline stage and does not own substantive applicability.

Any accountable BL owner may call it while resolving a proposition. Composition may request re-resolution when a proposition or temporal anchor changes.

Authority resolution returns source/lifecycle metadata. The accountable proposition owner decides case applicability.

A material authority result must distinguish at least:

- source provenance;
- legal force / authority type;
- lifecycle status;
- temporal anchor(s);
- verification time/freshness;
- source version or amendment context;
- case-applicability status owned by the proposition owner.

`CURRENT_BINDING` does not imply `APPLICABLE_TO_CASE`.

## 9. Temporal anchors

There is no single universal `RELEVANT_DATE`.

Each authority-backed proposition binds to the temporal anchor(s) that govern that proposition, such as:

- formation date;
- transaction/closing date;
- performance date;
- breach date;
- notice date;
- tax event;
- customs entry date;
- planned action date.

A relationship spanning multiple regimes may require several authority results.

## 10. Authority freshness

Authority records include `verified_at` and a freshness requirement appropriate to the action.

Before a material irreversible or current action, any authority whose freshness can affect readiness must be re-resolved if its freshness requirement is no longer satisfied or an authority-change signal exists.

A cached result may not keep an action `READY` merely because it was current when first retrieved.

## 11. Specialist ownership

A JIT specialist may only be invoked under an owning BL track.

The specialist returns candidate findings, technical classifications, authority, evidence needs, and uncertainty to that owner.

The owner decides whether to accept, reject, condition, or integrate the specialist result into an owned proposition.

A specialist cannot:

- bypass BL ownership;
- update another owner's proposition;
- create the final business answer;
- promote a candidate technical finding directly into shared legal state without owner review.

## 12. BL8 dual role

BL8 may act as an accountable owner for propositions such as:

- governing-law/conflict analysis;
- treaty/CISG applicability;
- foreign-investor/market-access status;
- FX/cross-border payment classification;
- trade/customs propositions.

BL8 may also operate only as a cross-border overlay when the substantive proposition remains owned elsewhere.

Examples:

- BL2 owns corporate cap table and corporate control; BL8 owns foreign-investment control tests and market-access consequences.
- BL3 owns the existence/content of a dispute-resolution clause; BL8 owns cross-border governing-law/treaty/international-enforcement overlay; BL4 owns dispute posture, invocation, deadlines, and remedies under the resolved regime/forum.

## 13. Composition conflict

The synthesizer cannot choose between conflicting specialist propositions.

If current owned propositions are materially inconsistent, create:

```text
COMPOSITION_CONFLICT
- conflict_id
- proposition_a
- proposition_b
- owners
- reason
- affected_actions
```

Return the conflict to the owners. Affected actions cannot be `READY` until the conflict is resolved or safely conditioned.

## 14. Path correctness

An eval passes only when both the output and execution path are correct.

Path evidence should prove, where material:

- initial route hypothesis;
- activated tracks;
- intentionally skipped tracks;
- late-route activation;
- accountable owner for each proposition;
- authority calls and temporal anchors;
- specialist invocation and return path;
- contradiction/reclassification transition;
- dependency invalidation;
- composition/conflict handling;
- per-action readiness.

A substantively plausible final answer produced through the wrong ownership/routing path is an architecture failure.