# Composition Evaluation

## Canonical architecture oracles

Semantic/adversarial cases:

- `ct-v0.2.md` — composition adversarial suite CT-01 through CT-29;
- `runtime-fixtures-v0.2.md` — human-readable RF-01 through RF-10 scenarios.

Architecture cold-start oracle (pre-knowledge-synthesis candidate):

- `rf-oracles-v0.3.json` — machine-checkable RF path/read/event oracle bound to candidate `c4fe8200f67adf6fa44fdbb95612836d817f3574`;
- `runtime-agent-protocol-v0.3.md` — fresh-session/local execution protocol;
- `../../scripts/runtime_walker.py` — frozen candidate file reader + append-only event logger;
- `../../scripts/check_runtime_trace.py` — trace integrity/path checker.

BL1 knowledge-synthesis JIT oracle:

- `bl1-jit-fixtures-v0.1.md` — BL1-JIT-01 through BL1-JIT-04 selectivity scenarios;
- `bl1-jit-oracles-v0.1.json` — machine-checkable BL1 JIT read/event oracle bound to repaired semantic candidate `af030a3b491c078c2e278f5a1b2f0ce718090892`.

BL2 knowledge-synthesis JIT oracle:

- `bl2-jit-fixtures-v0.1.md` — BL2-JIT-01 through BL2-JIT-04, including the BL2-JIT-02 voting-state perturbation;
- `bl2-jit-oracles-v0.1.json` — machine-checkable BL2 JIT read/event oracle bound to repaired semantic candidate `6dec6a6172f99a44353f1f29561ed3015202b6fc`.

BL3 knowledge-synthesis JIT oracle:

- `bl3-jit-fixtures-v0.1.md` — BL3-JIT-01 through BL3-JIT-04, including the BL3-JIT-03 late-delivery perturbation;
- `bl3-jit-oracles-v0.1.json` — machine-checkable BL3 JIT read/event oracle bound to repaired semantic candidate `1ce89ad5f624d541b8ebeb4673b10b0ef4ae95ba`.

BL4 knowledge-synthesis JIT oracle:

- `bl4-jit-fixtures-v0.1.md` — BL4-JIT-01 through BL4-JIT-04, including the BL4-JIT-03 deadline-to-arbitration perturbation;
- `bl4-jit-oracles-v0.1.json` — machine-checkable BL4 JIT read/event oracle bound to repaired semantic candidate `bd456e45ab50c72e7a073c91d7120979312a50e5`.

BL5 knowledge-synthesis JIT oracle:

- `bl5-jit-fixtures-v0.1.md` — BL5-JIT-01 through BL5-JIT-04, including the BL5-JIT-01 foreign-payment-mode perturbation;
- `bl5-jit-oracles-v0.1.json` — machine-checkable BL5 JIT read/event oracle bound to repaired semantic candidate `108d7292df27aeec9fbc265a2a224a900cf7178c`.

BL6 knowledge-synthesis JIT oracle:

- `bl6-jit-fixtures-v0.1.md` — exactly four BL6 probes covering relationship selectivity, current terms, performance/action routing, and controlled reclassification; confidentiality and timing boundaries are embedded as perturbations inside the relevant probes;
- `bl6-jit-oracles-v0.1.json` — machine-checkable BL6 JIT read/event oracle bound to repaired semantic candidate `1c199a5771a1f22f38285bff1ebee84785c25786`.

BL7 knowledge-synthesis JIT oracle:

- `bl7-jit-fixtures-v0.1.md` — four BL7 probes covering perimeter selectivity, permission scope, market-conduct routing, and privacy/data routing, with a BL7-JIT-02 specialist-activation perturbation;
- `bl7-jit-oracles-v0.1.json` — machine-checkable BL7 JIT read/event oracle bound to repaired semantic candidate `2d07f0b6917fedc522532a07a789b2696bf9090a`.

The older RF oracle is **not evidence for BL1/BL2/BL3/BL4/BL5/BL6/BL7 internal knowledge-unit routing**. Each synthesis layer must be evaluated against its own candidate-bound JIT oracle.

`ct-v0.1.md` and `vertical-slices-v0.1.md` are retained only as superseded historical markers.

## What must be evaluated

Do not score only final prose.

Where material, the harness/reviewer must establish:

1. initial BL1 route hypothesis;
2. activated and intentionally skipped BL tracks;
3. JIT knowledge-unit reads and intentionally skipped units;
4. internal owner-to-owner/unit dependencies where one unit consumes state owned by another;
5. late-route activation;
6. accountable owner for each material proposition;
7. observable file `READ` path/order against the frozen candidate;
8. Authority Resolver calls, temporal anchors, freshness and owner applicability decision;
9. owner-bound JIT specialist invocation and return path;
10. contradiction/reclassification transitions;
11. typed `DEPENDS_ON` invalidation versus `SIGNALS` / `FEEDBACK` review triggers;
12. composition conflicts;
13. per-action readiness;
14. controlled-loop convergence.

A plausible legal answer reached through the wrong path is an architecture failure.

## Evidence levels

### Level 0 — Markdown representability

The architecture can describe the case. Not runtime evidence.

### Level 1 — self-reported/manual trace

Useful for contract debugging but not sufficient to freeze. `runtime-preflight-run-001.md` is Level 1 evidence.

### Level 2 — observable cold-start trace

Fresh runtime, candidate-bound walker-mediated file reads, append-only semantic events, and checker PASS against the applicable candidate-bound oracle.

For the pre-knowledge architecture this is `rf-oracles-v0.3.json`.

For BL1 knowledge synthesis this is `bl1-jit-oracles-v0.1.json`.

For BL2 knowledge synthesis this is `bl2-jit-oracles-v0.1.json`.

For BL3 knowledge synthesis this is `bl3-jit-oracles-v0.1.json`.

For BL4 knowledge synthesis this is `bl4-jit-oracles-v0.1.json`.

For BL5 knowledge synthesis this is `bl5-jit-oracles-v0.1.json`.

For BL6 knowledge synthesis this is `bl6-jit-oracles-v0.1.json`.

For BL7 knowledge synthesis this is `bl7-jit-oracles-v0.1.json`.

### Level 3 — held-out / perturbation + independent review

Run held-out/perturbed cases after the relevant Level 2 path tests pass, then perform independent freeze review.

## Current status

The semantic architecture has passed manual trace preflight.

BL1 knowledge synthesis v0.1 has an accepted decomposition with local repairs and a dedicated JIT selectivity oracle; runtime JIT evidence remains **NOT YET PROVEN**.

BL2 knowledge synthesis v0.1 has an accepted decomposition with local ownership-boundary repairs and a dedicated JIT/internal-dependency oracle; runtime JIT evidence remains **NOT YET PROVEN**.

BL3 knowledge synthesis v0.1 has an accepted decomposition with local formation/JIT/waiver/dispute-clause repairs and a dedicated JIT/internal-handoff oracle; runtime JIT evidence remains **NOT YET PROVEN**.

BL4 knowledge synthesis v0.1 has an accepted decomposition with local deadline/liability-remedy/evidence-preservation/procedure repairs and a dedicated JIT/internal-handoff oracle; runtime JIT evidence remains **NOT YET PROVEN**.

BL5 knowledge synthesis v0.1 has an accepted decomposition with local tax-event/exemption/anti-reclassification repairs and a dedicated JIT/upstream-handoff/feedback oracle; runtime JIT evidence remains **NOT YET PROVEN**.

BL6 knowledge synthesis v0.1 has an accepted decomposition with local reclassification-invalidation/current-vs-post-employment/deadline-ownership repairs and a dedicated JIT/reclassification oracle; runtime JIT evidence remains **NOT YET PROVEN**.

BL7 knowledge synthesis v0.1 has an accepted decomposition with local route-role/data-role, specialist-activation, and permission-maintenance-scope repairs plus a dedicated JIT/specialist-handoff oracle; runtime JIT evidence remains **NOT YET PROVEN**.

Phase 4 also remains open until the broader RF/held-out runtime evidence gate is eventually completed.
