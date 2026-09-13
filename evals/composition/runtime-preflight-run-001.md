# Runtime Preflight Run 001 — Architecture v0.2

**Candidate SHA:** `73831e0e30df7a0950c36cbcfbf6880abb2e8584`

**Scope:** RF-01 through RF-10 from `runtime-fixtures-v0.2.md`.

**Run type:** manual model-execution trace against the v0.2 runtime contracts and canonical route map. This run checks whether the architecture can preserve the required activation path, ownership, authority-service behavior, state transitions, invalidation semantics, specialist return path, and per-action readiness. It is **not** an instrumented cold-start harness and is not independent reviewer evidence.

## Verdict

`10/10 TRACE PASS`

No architecture blocker was observed in the ten runtime fixtures under this execution trace.

However, this run does **not** by itself make Phase 4 freeze-ready. The freeze gate still requires an instrumented or otherwise independently observable path run that can prove actual load/skip/order behavior rather than relying only on a self-reported reasoning trace.

---

## RF-01 — Late regulatory activation after contract framing

**Result:** PASS

**Observed path**

```text
BL1
→ ROUTE_CONFIRMED(BL3)
→ BL3 reads transaction/agreement facts
→ discovers consumer-payment + end-user-data facts
→ LATE_ROUTE_SIGNAL(BL7)
→ BL7 activated
→ BL3 retains contract-content propositions
→ BL7 owns consumer/data/platform-regulatory propositions
→ BL5 skipped
→ BL8 skipped
→ separate sign / operate action prerequisites preserved
```

**Why pass**

Initial routing did not become a closed world. BL3 did not attempt to resolve privacy/consumer law itself, and the newly material regulatory track was activated explicitly.

---

## RF-02 — Authority service called during owner reasoning

**Result:** PASS

**Observed path**

```text
BL6 owns employer-action proposition
→ proposition requires a current procedural rule
→ BL6 calls Authority Resolver before committing conclusion
→ resolver returns provenance / legal force / lifecycle / temporal anchor / verified_at
→ BL6 decides case applicability
→ BL6 commits or conditions proposition
```

**Why pass**

Authority resolution operated as a callable service inside owner reasoning. The resolver did not become the owner of legal applicability and was not relegated to post-hoc citation.

---

## RF-03 — Candidate reclassification without premature invalidation

**Result:** PASS

**Observed path**

```text
BL6
→ employee-like evidence detected
→ CLASSIFICATION_SIGNAL
→ RECLASSIFICATION_REVIEW
→ prior contractor classification remains committed
→ employment candidate remains explicit but unresolved
→ terminate-tomorrow action = VERIFY_BEFORE_ACTION
→ BL5 tax/BHXH proposition remains conditional on unresolved classification
→ no committed downstream invalidation yet
```

**Why pass**

The competing classification affected action readiness without silently replacing the current committed state.

---

## RF-04 — Committed reclassification invalidates exact dependents

**Result:** PASS

**Observed path**

```text
additional evidence resolves employment classification
→ BL6 RECLASSIFICATION_COMMITTED
→ old contractor classification = SUPERSEDED
→ employment classification = RESOLVED
→ exact DEPENDS_ON dependents marked STALE/INVALIDATED
→ BL5 employment tax/BHXH proposition recomputed
→ unrelated BL2 authority proposition remains current
```

**Why pass**

Invalidation followed proposition-level `DEPENDS_ON` edges rather than the track-level routing map.

---

## RF-05 — Evidence provenance separated from truth status

**Result:** PASS

**Observed state**

```text
FACT F-01
proposition: payment occurred
status: DISPUTED / UNRESOLVED

EVIDENCE
E-01 USER          supports F-01
E-02 DOCUMENT      supports F-01
E-03 COUNTERPARTY  contradicts F-01
```

**Why pass**

The PDF receipt remained evidence that supports the proposition; `DOCUMENT` provenance did not promote the proposition to established truth. Source count did not resolve the dispute.

---

## RF-06 — Transition rule separates lifecycle from applicability

**Result:** PASS

**Observed path**

```text
owner identifies proposition-specific anchors:
- formation date
- breach date

→ Authority Resolver returns current instrument + historical/transition authority set
→ current statute lifecycle = CURRENT_BINDING
→ owner separately decides applicability for formation proposition
→ owner separately decides applicability for breach proposition
→ different regimes remain possible where transition rule requires it
```

**Why pass**

No single universal `RELEVANT_DATE` was used and `CURRENT_BINDING` did not become `APPLICABLE_TO_CASE` automatically.

---

## RF-07 — Authority freshness before irreversible action

**Result:** PASS

**Observed path**

```text
launch action
→ DEPENDS_ON regulatory permission proposition
→ previous authority result verified yesterday
→ authority-change signal: implementing rule suspended
→ freshness requirement no longer satisfied
→ re-resolve authority
→ regulatory proposition becomes STALE pending BL7 applicability review
→ launch action cannot remain READY
```

**Why pass**

The stale authority result was not reused as a readiness basis, and the change was scoped to dependent propositions rather than invalidating the whole case.

---

## RF-08 — Feedback is not invalidation

**Result:** PASS

**Observed path**

```text
BL3 legal-validity proposition = current
→ BL5 resolves tax economics
→ structure is expensive but not unlawful
→ BL5 emits FEEDBACK to BL3/BL2
→ review trigger created
→ BL3 legal-validity proposition remains current
→ user may retain or restructure transaction
```

**Why pass**

Economic feedback did not silently rewrite contract terms or invalidate a legally valid transaction.

---

## RF-09 — Specialist returns to owner

**Result:** PASS

**Observed path**

```text
BL8 owns preferential-origin proposition
→ BL8 emits SPECIALIST_DEPTH_REQUIRED
→ BL8 invokes origin specialist
→ specialist returns candidate finding + authority + missing technical facts + uncertainty
→ result returns to BL8
→ BL8 accepts / conditions / rejects candidate
→ BL8 alone promotes owned proposition
→ no specialist final business answer
```

**Why pass**

The specialist remained owner-bound and could not bypass BL8 or write final action readiness.

---

## RF-10 — Composition conflict and action-specific readiness

**Result:** PASS

**Observed path**

```text
ACTION A: sign contract
→ BL2 authority prerequisite resolved
→ BL3 formation/content prerequisite resolved
→ required authority fresh
→ READY

ACTION B: commence regulated service
→ BL7 permission proposition conflicts with unresolved exception proposition
→ COMPOSITION_CONFLICT created
→ returned to accountable owner(s)
→ action cannot be READY
→ VERIFY_BEFORE_ACTION (or stricter if owner resolves a blocker)
```

**Why pass**

Readiness was action-specific and the synthesizer did not choose the business-friendly exception or create a substantive permission conclusion.

---

# Cross-fixture observations

The v0.2 repair closes the principal architecture defects identified by the two adversarial reviews:

- BL1 routing behaves as an initial hypothesis rather than a closed world;
- Authority Resolver behaves as an owner-callable service;
- ownership is proposition-level;
- provenance and epistemic status are separate;
- reclassification distinguishes signal, review, and committed change;
- invalidation is proposition-level and typed;
- `SIGNALS` / `FEEDBACK` do not silently invalidate state;
- specialist depth is owner-bound;
- authority lifecycle, freshness, temporal anchors, and case applicability remain separate;
- readiness is action-specific and requires positive prerequisite closure;
- synthesizer derives composition but does not resolve substantive conflicts.

# Remaining freeze gap

This trace is generated inside the same model session that has already inspected the architecture. It therefore cannot independently prove:

1. that a fresh runtime actually reads only the expected JIT files;
2. that intentionally skipped tracks were not available through hidden/preloaded context;
3. exact read order and late-load order;
4. that another model/runtime configuration preserves the same path;
5. that path events can be externally audited rather than self-reported.

Accordingly:

```text
ARCHITECTURE CONTRACT EXECUTABILITY: PASS
MANUAL PATH TRACE:               10/10 PASS
INSTRUMENTED PATH PROOF:          NOT YET PROVEN
PHASE 4 FREEZE:                   HOLD
```

## Next gate

Run the same frozen RF-01–RF-10 set in a fresh instrumented runtime/walker that records at minimum:

```text
activate
skip
read(path)
authority_call(proposition, anchors)
late_route
specialist_call(owner, specialist)
state_transition
invalidate(proposition_id)
feedback/signal
composition_conflict
action_readiness(action_id)
```

The expected paths in this file and `runtime-fixtures-v0.2.md` should be treated as the oracle. A correct final answer reached through a wrong or unobservable path remains a failure.
