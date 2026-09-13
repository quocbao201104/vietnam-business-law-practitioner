# Composition Evaluation

## Canonical Phase 4 architecture oracles

Semantic/adversarial cases:

- `ct-v0.2.md` — composition adversarial suite CT-01 through CT-29;
- `runtime-fixtures-v0.2.md` — human-readable RF-01 through RF-10 scenarios.

Executable cold-start oracle:

- `rf-oracles-v0.3.json` — machine-checkable RF path/read/event oracle bound to frozen candidate `c4fe8200f67adf6fa44fdbb95612836d817f3574`;
- `runtime-agent-protocol-v0.3.md` — fresh-session/local execution protocol;
- `../../scripts/runtime_walker.py` — frozen candidate file reader + append-only event logger;
- `../../scripts/check_runtime_trace.py` — trace integrity/path checker.

`ct-v0.1.md` and `vertical-slices-v0.1.md` are retained only as superseded historical markers.

## What must be evaluated

Do not score only final prose.

Where material, the harness/reviewer must establish:

1. initial BL1 route hypothesis;
2. activated and intentionally skipped BL tracks;
3. late-route activation;
4. accountable owner for each material proposition;
5. observable file `READ` path/order against the frozen candidate;
6. Authority Resolver calls, temporal anchors, freshness and owner applicability decision;
7. owner-bound JIT specialist invocation and return path;
8. contradiction/reclassification transitions;
9. typed `DEPENDS_ON` invalidation versus `SIGNALS` / `FEEDBACK` review triggers;
10. composition conflicts;
11. per-action readiness;
12. controlled-loop convergence.

A plausible legal answer reached through the wrong path is an architecture failure.

## Evidence levels

### Level 0 — Markdown representability

The architecture can describe the case. Not runtime evidence.

### Level 1 — self-reported/manual trace

Useful for contract debugging but not sufficient to freeze. `runtime-preflight-run-001.md` is Level 1 evidence.

### Level 2 — observable cold-start trace

Fresh runtime, candidate-bound walker-mediated file reads, append-only semantic events, and checker PASS against `rf-oracles-v0.3.json`.

This is the minimum RF evidence required before Phase 4 can become freeze-ready.

### Level 3 — held-out / perturbation + independent review

Run CT held-out/perturbed cases after RF Level 2 passes, then perform independent freeze review.

## Current status

The semantic architecture has passed manual trace preflight, but **Phase 4 remains open until Level 2 cold-start path evidence exists for RF-01 through RF-10 and held-out perturbation does not expose a concrete composition failure**.