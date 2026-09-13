# Knowledge Routing Index

This preflight intentionally implements one thin `core.md` per BL track. Split a core into deeper decision units only after runtime/eval evidence shows the boundary is stable and recurring depth is needed.

Load the smallest relevant track. Do not load all tracks by default.

## BL1 — Legal Issue Framing / Regime Selection

`bl1-issue-framing/core.md`

Owns issue framing, candidate regime stack, temporal applicability, authority classification, routing, and reclassification orchestration.

## BL2 — Entity / Authority / Ownership / Governance

`bl2-corporate/core.md`

Owns entity identity, representation/authority, required corporate approval, conflict/related-party state, ownership/control, and corporate-state change.

## BL3 — Contracts / Commercial Transactions

`bl3-contracts/core.md`

Owns formation, document stack, contractual obligations, performance state, variation, and transaction evidence. Does not decide remedies, regulatory permission, tax liability, or signatory authority.

## BL4 — Breach / Remedies / Evidence / Disputes

`bl4-remedies-disputes/core.md`

Owns breach/excuse, remedy availability, loss/proof, notice, evidence preservation, limitation/deadline, and dispute posture after BL3 has established obligation/performance state.

## BL5 — Tax / Financial Legal Consequences

`bl5-tax/core.md`

Owns tax characterization, taxpayer/withholder consequences, documentation/timing, and tax-aware transaction consequences. Not bookkeeping/accounting.

## BL6 — Employment / People-side Business Law

`bl6-employment/core.md`

Owns employee/contractor classification and lawful employer pathways across hiring, management, discipline, restructuring, termination, and post-employment protection.

## BL7 — Regulatory / Market Conduct / Business Compliance

`bl7-regulatory/core.md`

Owns regulatory perimeter, entry/operating conditions, market conduct, compliance lifecycle, and specialist regulatory triggers.

## BL8 — Investment / Cross-border / Trade

`bl8-cross-border/core.md`

Owns foreign-investment, governing-law/treaty, FX/payment, and trade/customs overlays. Foreign element does not automatically mean import/export.

## Specialist depth

If a core track cannot safely resolve a recurring specialist issue using stable reasoning plus live authority, emit `SPECIALIST_DEPTH_REQUIRED` and use the protocol in `../schemas/specialist-handoff.md`.

Examples: HS classification, preferential origin, transfer pricing, foreign borrowing, food/medical regulation, specialist privacy, sector licensing.

## Composition reminders

- BL2 → BL3: authority before binding transaction conclusions.
- BL3 → BL4: obligation/performance before breach/remedy.
- BL6 → BL5: employment classification before employment-tax consequence.
- BL8 → BL3: governing-law/treaty resolution before cross-border contract analysis where material.
- BL3 ↔ BL7: agreement never replaces mandatory regulatory analysis.
- BL8 ↔ BL7: border/customs status never proves domestic market permission.
