# Changelog

All notable project changes are documented here.

## [0.2.0] — 2026-09-13

### Added

- Claude Code and Codex plugin packaging backed by the same runtime skill source.
- Just-in-time runtime contract loading so simple matters avoid blanket schema/reference preloading while governed behavior still loads its coupled contracts before execution.
- Explicit composition-conflict lifecycle with `ACTIVE`, `RESOLVED`, and `TERMINAL_UNRESOLVED` outcomes.
- Revision-safe conflict terminalization/resolution, explicit conflict reopening after new material input, stable affected-action scope, and post-transition readiness recomputation.
- Single-runtime semantic ownership: BL owners are decision boundaries, not a requirement for one agent/process per BL track.
- Stronger runtime-trace validation for ownership, conflict state, blocker evidence, state revisions, and affected-action linkage.
- Repository contributor/agent instructions and targeted audit-repair evaluation scenarios.
- Public capability roadmap covering practitioner capabilities, work episodes, specialist candidates, legal operations, and architecture research questions.

### Changed

- Authority and specialist paths now load shared Legal Work State when revision-sensitive integration becomes material.
- Contract-loading triggers were narrowed so ordinary multi-step reasoning alone does not force heavy state-contract loading.
- Composition convergence now permits explicit non-READY terminal outcomes without pretending unresolved owner conflict was substantively resolved.
- `DO_NOT_PROCEED` under terminal conflict requires an independently supported blocker rather than uncertainty alone.
- Routing and trace ownership validation were tightened following adversarial review.
- Public documentation was aligned with proposition ownership, BL8 owner/overlay semantics, live-law verification, and runtime limitations.

### Notes

This is a **minor release**, not a patch release. The BL1–BL8 legal reasoning kernel remains intact, but runtime contract loading, conflict/convergence semantics, ownership execution semantics, packaging, and validation behavior changed materially from v0.1.0.

The project remains suitable for early dogfooding and real-world evaluation. This release does not claim exhaustive Vietnamese-law coverage or final runtime proof.

## [0.1.0] — 2026-09-13

Initial public release of the Vietnam Business Law Practitioner research-first Agent Skill, including the BL1–BL8 ownership architecture, live-law authority resolution, shared legal work state, per-action readiness, and adversarial evaluation contracts.
