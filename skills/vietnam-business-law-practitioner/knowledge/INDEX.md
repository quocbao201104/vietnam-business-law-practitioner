# Knowledge Routing Index — Canonical Detailed Route Map v0.3

This file is the **single canonical detailed route map** for BL1–BL8. `SKILL.md` contains only high-level activation rules.

Load the smallest relevant owner(s) and knowledge unit(s). Do not load all tracks or all units by default.

## Route status

For each materially relevant track record one of:

- `ROUTE_CONFIRMED`
- `ROUTE_PLAUSIBLE`
- `ROUTE_UNRESOLVED`
- `ROUTE_REJECTED`

BL1 creates the initial route hypothesis. Any active owner may emit `LATE_ROUTE_SIGNAL` to activate another track when new evidence makes it material.

## BL1 — Legal Issue Framing / Regime Selection

Start with:

`bl1-issue-framing/core.md`

Then JIT-load only the capability needed:

- `bl1-issue-framing/issue-framing.md` — convert a business story into candidate actions, material legal questions, owners, fact/evidence state, and missing conditions;
- `bl1-issue-framing/regime-routing.md` — candidate regime stacks, special/mandatory layers, cross-track routing, foreign-element detection, substantive/procedural separation;
- `bl1-issue-framing/temporal-applicability.md` — proposition-specific temporal anchors, historical/current/future-effective regimes, amendment/replacement/suspension/transition issues;
- `bl1-issue-framing/authority-applicability.md` — source provenance, legal force, lifecycle, applicability, freshness, conflicting authority, and minimum sufficient authority set.

Activate BL1 for non-trivial framing, route hypotheses, temporal/foreign/mandatory-law detection, and reclassification orchestration.

BL1 does **not** promote substantive BL2–BL8 classifications or decide that a candidate governing regime actually applies.

Do not load all four BL1 units by default.

## BL2 — Entity / Authority / Ownership / Governance

Start with:

`bl2-corporate/core.md`

Then JIT-load only the capability needed:

- `bl2-corporate/entity-actor-state.md` — resolve legal entity identity, actor role/state, group/branch/business-unit distinctions, and historical/current corporate identity;
- `bl2-corporate/authority-representation.md` — representation/signing authority, delegation scope, disputed authority, ratification/acceptance/course-of-dealing effects;
- `bl2-corporate/approval-conflict-governance.md` — reserved matters, corporate approvals, conflicts/related-party governance, quorum/voting/disclosure/approval defects;
- `bl2-corporate/ownership-control-state-change.md` — legal ownership, cap table, voting/control, transfer/subscription/contribution completion, and corporate-state changes.

Activate BL2 when a decision depends on who the legal actor is, who may bind it, what internal approval is required, who owns/controls it, or whether corporate state changed.

BL2 does **not** decide foreign-investor status, foreign-investment control tests, market access, or investment procedures. Route those propositions to BL8 using BL2's resolved corporate facts.

Do not load all four BL2 units by default.

## BL3 — Contracts / Commercial Transactions

`bl3-contracts/core.md`

Activate for:

- formation/assent;
- contract/document stack;
- transaction terms;
- contractual obligations;
- performance state;
- variation/settlement effect on transaction state;
- existence/content of dispute-resolution clauses.

Does not decide signatory authority (BL2), breach/remedies (BL4), tax liability (BL5), regulatory permission (BL7), or cross-border governing-law/treaty applicability (BL8).

## BL4 — Breach / Remedies / Evidence / Disputes

`bl4-remedies-disputes/core.md`

Activate after BL3 has established a material obligation/performance proposition for:

- breach/excuse/materiality;
- remedy availability;
- loss/proof/mitigation;
- notice/evidence preservation;
- limitation/deadline;
- dispute posture;
- invocation/procedure/remedies under a resolved forum/regime.

For cross-border disputes, BL8 owns governing-law/treaty/international-enforcement overlay; BL3 owns the dispute-clause content.

## BL5 — Tax / Financial Legal Consequences

`bl5-tax/core.md`

Activate for:

- tax characterization;
- taxpayer/withholder propositions;
- VAT/CIT/PIT/withholding or other tax consequences when material;
- documentary/timing conditions;
- tax-aware transaction economics/structuring feedback.

BL5 consumes upstream transaction/employment/ownership classifications. It may signal contradictions but must not reconstruct those classifications.

Tax economics that make a structure unattractive are normally `FEEDBACK`, not automatic invalidation of BL2/BL3 state.

## BL6 — Employment / People-side Business Law

`bl6-employment/core.md`

Activate for:

- employee/contractor classification;
- hiring/probation/employment terms;
- performance vs misconduct;
- discipline;
- restructuring/termination;
- confidentiality/business protection and post-employment issues.

BL6 owns employment classification. BL5 applies tax/BHXH consequences only after the classification is committed or clearly conditioned.

## BL7 — Regulatory / Market Conduct / Business Compliance

`bl7-regulatory/core.md`

Activate for:

- licensing/conditional business/market entry;
- product/service operating permission;
- consumer protection;
- advertising/claims;
- e-commerce/platform role;
- competition/market conduct;
- privacy/data and other public-law compliance triggers;
- domestic market permission after import/customs.

Agreement/consent in BL3 never substitutes for BL7 regulatory permission.

## BL8 — Investment / Cross-border / Trade

`bl8-cross-border/core.md`

Activate when a foreign element can materially change the legal position.

BL8 may be an accountable owner for:

- foreign-investor status / market access / foreign-investment control tests;
- governing-law/conflict/treaty/CISG propositions;
- FX/cross-border payment classification;
- trade/customs/HS/origin/tariff propositions.

BL8 may also operate only as an overlay where the underlying proposition remains owned elsewhere.

Foreign element does not automatically mean import/export.

## Late-route examples

- BL3 receives evidence of missing signing authority → signal/late-return BL2.
- BL5 sees payroll-style evidence contradicting contractor classification → `CONTRADICTION_SIGNAL` to BL6; do not classify employee itself.
- BL7 discovers foreign platform/operator facts → late-route BL8.
- BL8 discovers domestic product approval is material → late-route BL7.
- BL3 identifies non-performance → activate BL4 only after obligation/performance state is established.

## Specialist depth

A specialist is never a top-level sibling route.

Only an accountable BL owner may invoke specialist depth via `../schemas/specialist-handoff.md`.

Examples:

- BL8 → HS classification / preferential origin specialist;
- BL5 → transfer-pricing specialist;
- BL7 → privacy / food / medical / sector-licensing specialist.

The specialist returns candidate depth to the owner; the owner promotes/conditions/rejects the result.

## Composition reminders

- BL2 → BL3: authority/approval propositions condition binding transaction conclusions.
- BL3 → BL4: obligation/performance propositions precede breach/remedy.
- BL6 → BL5: employment classification precedes employment-tax consequences.
- BL8 → BL3: governing-law/treaty proposition precedes cross-border contract reasoning where material.
- BL3 ↔ BL7: agreement never replaces mandatory regulatory analysis.
- BL8 ↔ BL7: customs/border status never proves domestic market permission.
- BL3 ↔ BL8 ↔ BL4: clause content / cross-border overlay / dispute procedure have separate owners.

## Invalidation reminder

This routing map is **not** an executable dependency graph.

Only explicit proposition-level `DEPENDS_ON` edges propagate automatic invalidation. `SIGNALS` and `FEEDBACK` create review triggers.