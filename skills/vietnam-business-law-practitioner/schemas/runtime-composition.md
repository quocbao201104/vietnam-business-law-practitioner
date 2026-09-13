# Runtime Composition — Semantic Contract v0.4

This contract defines how BL1–BL8, live authority, and JIT specialists compose at runtime. It is normative for routing, ownership, invalidation, convergence, and synthesis.

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
→ convergence check
→ business-facing answer
```

A newly discovered fact or authority may activate another owner or invalidate a prior dependent proposition.

## 2. Canonical materiality gate

A fact, proposition, condition, authority question, route, or specialist issue is **material** when resolving it can change at least one of:

- activated route or accountable owner;
- legal classification;
- proposition result/status;
- proposition dependency;
- authority version/lifecycle applicable to a proposition;
- available option set;
- required evidence/procedure/deadline;
- action readiness.

If none of those can change, treat the item as non-material for the current decision and do not activate extra depth merely because the topic is legally interesting.

When activation/skip is contestable, record a materiality decision in the runtime trace.

## 3. Route hypothesis lifecycle

BL1 owns initial framing and routing hypotheses, not every substantive legal classification.

Each material route has one of:

- `ROUTE_CONFIRMED`
- `ROUTE_PLAUSIBLE`
- `ROUTE_UNRESOLVED`
- `ROUTE_REJECTED`

### Who may change route status

- BL1 may create and update the initial route hypothesis from framing facts.
- An active accountable owner may emit `LATE_ROUTE_SIGNAL` when new evidence makes another track material.
- The newly activated owner may confirm or reject its own route after inspecting the relevant state.
- A previously rejected route may be reopened only by new material evidence/authority, using an explicit late-route or contradiction signal. It must not silently reappear.

Late activation must be explicit. The new track receives the shared state. A missed initial route is not repaired by silently reasoning from an unloaded domain.

## 4. Proposition ownership

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

## 5. Typed dependency edges

Track-level routing is not an executable invalidation graph.

Use proposition-level edges:

- `DEPENDS_ON` — the dependent proposition cannot remain current if the upstream proposition materially changes;
- `CONSTRAINS` — upstream result narrows the option space but does not itself change action readiness unless the constraint is explicitly linked to that action;
- `SIGNALS` — information that another owner should review;
- `FEEDBACK` — business/legal consequence that may justify restructuring or re-review.

Only `DEPENDS_ON` propagates automatic `STALE` / `INVALIDATED` status.

`SIGNALS` and `FEEDBACK` create review triggers, not silent invalidation.

A `CONSTRAINS` edge affects action readiness only through an explicit action prerequisite/condition link. The synthesizer may not infer a new blocker from a free-floating constraint.

## 6. State updates and revisions

All material state objects have stable IDs. The shared state has a monotonically increasing `state_revision`.

Owners emit owner-scoped state deltas. They do not replace the entire shared state.

A stale write based on an older state revision must be rejected or reconciled before it can overwrite newer owner state.

## 7. Contradiction protocol

A downstream track or specialist must never reconstruct or replace upstream-owned state.

When contradictory evidence appears:

1. emit `CONTRADICTION_SIGNAL`;
2. identify the affected upstream fact/classification/proposition;
3. identify the evidence creating the contradiction;
4. return to the accountable owner;
5. mark dependent reasoning conditional or paused where material;
6. resume only after the owner commits an updated state.

## 8. Reclassification state machine

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

## 9. Authority Resolver is a callable service

The Authority Resolver is not a fixed pipeline stage and does not own substantive applicability.

Use `authority-resolver.md` as the normative request/result/failure contract.

Any accountable BL owner may call it while resolving a proposition. Composition may request re-resolution when a proposition or temporal anchor changes.

Authority resolution returns provenance/legal-force/lifecycle/freshness/source-set metadata. The accountable proposition owner decides case applicability.

`CURRENT_BINDING` does not imply `APPLICABLE_TO_CASE`.

## 10. Temporal anchors

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

## 11. Authority freshness

Authority records include `verified_at` and a freshness requirement appropriate to the action.

Before a material irreversible or current action, any authority whose freshness can affect readiness must be re-resolved if its freshness requirement is no longer satisfied or an authority-change signal exists.

A cached result may not keep an action `READY` merely because it was current when first retrieved.

## 11A. Authority orchestration behavior

This section connects the frozen retrieval subsystem to proposition ownership, shared state, composition, and action readiness. It does not redesign search/retrieval.

### Owner decides whether authority work is needed

For each material owned proposition, the accountable owner decides whether it can proceed from already sufficient authority support or whether live/historical authority resolution is material.

Use the canonical materiality gate. A resolver call is justified when a current/historical authority result can change the proposition result/status, applicable version/lifecycle, option set, required procedure/evidence/deadline, dependency, or action readiness.

Do not call the resolver merely to decorate prose with citations.

When the call/no-call decision is contestable, emit `MATERIALITY_DECISION` with the affected proposition/action.

### Construct proposition-specific requests

A material authority request must identify the exact legal proposition/question, accountable owner, jurisdiction(s), proposition-specific temporal anchor(s), required authority class when known, freshness requirement, and known candidate authorities/sources when useful.

Do not send a whole case as one undifferentiated request when different propositions have different owners, temporal anchors, or authority needs.

### Reuse gate

An existing authority result may be reused instead of searched again only when all material reuse conditions remain satisfied:

- its legal question/scope is sufficient for the current proposition;
- jurisdiction and required authority class still match;
- temporal anchor(s) and effective-period/version context remain compatible;
- document identity, lifecycle and provision resolution are sufficient for the current proposition;
- its freshness requirement is still satisfied;
- no unresolved `AUTHORITY_CHANGE_SIGNAL` affects it;
- no material fact/classification change has changed what authority must be resolved.

Reuse the **authority result**, not another proposition's applicability conclusion. The current accountable owner must still decide applicability for the current proposition unless the exact same proposition, material facts, temporal anchors and owner decision remain current at the same or a later reconciled state revision.

If any material reuse condition fails, re-resolve rather than silently extending the old result.

### Resolver stop versus owner stop

The resolver stops according to `authority-resolver.md`; the owner then decides what the result permits.

- `RESOLVED` means the authority set is sufficient to proceed to owner applicability review for the requested authority question.
- `PARTIALLY_RESOLVED` may support only the resolved sub-proposition. If the unresolved part is material to the owned proposition/action, it remains unresolved for runtime purposes.
- unresolved statuses such as `CURRENTNESS_UNRESOLVED`, `PROVISION_UNRESOLVED`, `CONFLICTING_AUTHORITY`, `INSUFFICIENT_AUTHORITY`, or `TEMPORAL_SCOPE_UNRESOLVED` must be preserved rather than converted into a convenient legal conclusion.
- one failed/lagging source attempt does not prevent a usable final result when another sufficient official path yields `RESOLVED`.

Do not loop indefinitely on the same unresolved request. Re-call the resolver only when a new material source/fallback, temporal anchor, fact/classification, authority-change signal, or other material input can change the result.

### Writeback and owner applicability

Write the resolver result into shared Legal Work State before using it to promote an owned proposition.

The result remains resolver-owned evidence/authority support. The accountable BL owner then records a separate applicability decision for the proposition using one of:

- `APPLICABLE_TO_CASE`
- `NOT_APPLICABLE_TO_CASE`
- `APPLICABILITY_CONDITIONAL`
- `APPLICABILITY_UNRESOLVED`

The applicability decision must identify the proposition, accountable owner, authority result(s), relevant material facts/conditions, temporal anchor(s), and state revision.

`CURRENT_BINDING`, `RESOLVED`, or discovery of a provision never substitutes for this owner decision.

### Unresolved authority and readiness

If a material owned proposition requires authority support and the final authority/applicability state remains unresolved, the proposition must remain `AUTHORITY_UNCERTAIN`, `AMBIGUOUS`, or otherwise unresolved/conditional rather than being promoted to a supported conclusion.

For an action that depends on that proposition:

- unresolved material authority normally prevents `READY` and `READY_WITH_CONDITIONS` and yields at most `VERIFY_BEFORE_ACTION`;
- use `LEGAL_REVIEW_REQUIRED` when the runtime can state the issue/options but authoritative conflict, unresolved primary authority, or specialist legal judgment cannot be safely resolved for a high-impact/irreversible action;
- use `DO_NOT_PROCEED` only when a supported current blocking proposition exists, not merely because authority is unresolved.

An unresolved authority issue that is not material to a particular action does not cap that action's readiness.

### Freshness, change signals, and re-resolution

When a required authority result fails freshness or receives `AUTHORITY_CHANGE_SIGNAL`:

1. identify the exact authority-supported proposition(s) affected;
2. mark those proposition(s) `STALE` or review-required where the authority is material;
3. recompute readiness for actions whose dependency closure includes them;
4. emit `AUTHORITY_RERESOLVE` when re-resolution starts;
5. write back the new resolver result;
6. require owner applicability review again before restoring the proposition as current.

Do not globally invalidate unrelated propositions.

If re-resolution restores freshness and the owned proposition result/conditions do not materially change, no substantive downstream invalidation is required; recompute readiness from the refreshed current proposition. If the owned proposition materially changes, propagate `STALE` / `INVALIDATED` only through exact `DEPENDS_ON` edges and recompute affected propositions/actions.

### Authority-aware convergence

For a requested action, authority orchestration has converged only when:

- every material authority-backed prerequisite has either a sufficiently fresh usable result plus owner applicability decision, or an explicit unresolved authority/applicability state reflected in non-READY readiness;
- no pending material `AUTHORITY_RERESOLVE` or unresolved authority-change signal affects the action;
- there is no repeated identical resolver call with no new material input;
- authority result and applicability decisions are attached to the current state revision used for readiness.

A run may therefore converge with unresolved authority only when that uncertainty is explicit in proposition state and readiness.

## 12. Specialist ownership

A JIT specialist may only be invoked under an owning BL track.

The specialist returns candidate findings, technical classifications, authority, evidence needs, and uncertainty to that owner.

The owner decides whether to accept, reject, condition, or integrate the specialist result into an owned proposition.

A specialist cannot:

- bypass BL ownership;
- update another owner's proposition;
- create the final business answer;
- promote a candidate technical finding directly into shared legal state without owner review.

## 13. BL8 dual role

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

## 14. Composition conflict

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

Return the conflict to the owners. Affected actions cannot be `READY` until the conflict is resolved or safely conditioned by the accountable owner(s).

## 15. Per-action readiness semantics

Readiness is computed for each action, never globally for the whole matter.

Use:

- `READY`
- `READY_WITH_CONDITIONS`
- `VERIFY_BEFORE_ACTION`
- `LEGAL_REVIEW_REQUIRED`
- `DO_NOT_PROCEED`

### READY

Use only when all material prerequisites are positively resolved, all required authority freshness conditions are satisfied, there is no unresolved material condition/conflict/stale dependency, and no blocking proposition applies.

### READY_WITH_CONDITIONS

Use when the action may lawfully proceed after one or more explicit, objectively identifiable conditions are satisfied and the legal pathway for satisfying them is itself sufficiently resolved.

Do not use this state when the condition's legal effect or applicability is still unresolved.

### VERIFY_BEFORE_ACTION

Use when a material fact, classification, authority applicability/freshness question, route, or composition conflict remains unresolved and could change whether/how the action may proceed.

### LEGAL_REVIEW_REQUIRED

Use when the architecture can state the current position/options but the action is materially irreversible/high-impact or the unresolved issue requires specialist human judgment beyond safe runtime resolution. This is not a substitute for analysis.

### DO_NOT_PROCEED

Use when a currently supported blocking proposition prohibits the action or a required legal prerequisite is definitively absent and cannot be cured before the proposed action.

The synthesizer may derive readiness only from explicit proposition/condition links to the action. It may not invent blockers or conditions.

## 16. Convergence / stop condition

The controlled loop has converged for a requested action only when all of the following are true:

1. no pending `LATE_ROUTE_SIGNAL` affects that action;
2. no pending `CONTRADICTION_SIGNAL` or `RECLASSIFICATION_REVIEW` affects a prerequisite proposition;
3. no `STALE` / `INVALIDATED` proposition remains in that action's dependency closure;
4. no unresolved `COMPOSITION_CONFLICT` affects the action;
5. all authority results required for readiness satisfy their freshness requirement or are explicitly marked unresolved and reflected in readiness;
6. every material proposition in the action's dependency closure has an accountable owner and current status;
7. the action has an explicit readiness state derived from those prerequisites;
8. every material authority-backed prerequisite satisfies the authority-aware convergence rule in Section 11A.

A run may converge with `VERIFY_BEFORE_ACTION`, `LEGAL_REVIEW_REQUIRED`, or `DO_NOT_PROCEED`; convergence does not mean permission.

Emit `RUN_CONVERGED` only after this condition is met.

## 17. Path correctness

An eval passes only when both the output and execution path are correct.

Path evidence should prove, where material:

- initial route hypothesis;
- activated tracks;
- intentionally skipped tracks;
- late-route activation;
- accountable owner for each proposition;
- authority call/reuse/re-resolution decisions and temporal anchors;
- resolver result followed by owner applicability decision;
- specialist invocation and return path;
- contradiction/reclassification transition;
- dependency invalidation;
- composition/conflict handling;
- per-action readiness;
- convergence.

A substantively plausible final answer produced through the wrong ownership/routing/authority path is an architecture failure.

Use `runtime-trace.md` for the observable event contract.
