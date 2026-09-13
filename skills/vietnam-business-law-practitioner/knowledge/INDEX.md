# Knowledge Routing Index — Canonical Detailed Route Map v0.3

This file is the **single canonical detailed route map** for BL1–BL8. `SKILL.md` contains only high-level activation rules.

Load the smallest relevant owner(s) and knowledge unit(s). Do not load all tracks or all units by default.

## Route status

For each materially relevant track record one of:

- `ROUTE_CONFIRMED`
- `ROUTE_PLAUSIBLE`
- `ROUTE_UNRESOLVED`
- `ROUTE_REJECTED`

BL1 creates the initial route hypothesis. Any active owner may emit `LATE_ROUTE_SIGNAL` to activate another track when new evidence makes it material. A newly activated accountable owner may confirm or reject its own route under the runtime contract.

## BL1 — Legal Issue Framing / Regime Selection

Start with:

`bl1-issue-framing/core.md`

Then JIT-load only the capability needed:

- `bl1-issue-framing/issue-framing.md` — convert a business story into candidate actions, material legal questions, owners, fact/evidence state, and missing conditions;
- `bl1-issue-framing/regime-routing.md` — candidate regime stacks, special/mandatory layers, cross-track routing, foreign-element detection, substantive/procedural separation;
- `bl1-issue-framing/temporal-applicability.md` — proposition-specific temporal anchors, historical/current/future-effective regimes, amendment/replacement/suspension/transition issues; returns lifecycle/transition state to the accountable owner rather than deciding substantive applicability;
- `bl1-issue-framing/authority-applicability.md` — load only when authority provenance/force/lifecycle/conflict/source availability is itself material to BL1 framing/routing. Do not load it merely because a downstream owner needs current law; the accountable owner calls Authority Resolver directly.

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

Start with:

`bl3-contracts/core.md`

Then JIT-load only the capability needed:

- `bl3-contracts/formation-transaction-state.md` — agreement/assent, draft/offer/order/acceptance sequence, formation versus effectiveness/conditions, electronic/form issues, and formation/effectiveness state only;
- `bl3-contracts/document-stack-terms.md` — document/version stack, incorporation, precedence, negotiated/standard terms, material clause interpretation, and dispute-resolution clause existence/content plus contract-law formation/incorporation/validity/effect as a contractual term;
- `bl3-contracts/obligations-conditions-performance.md` — obligations, triggers/conditions, due state, performance/acceptance state, and performance evidence;
- `bl3-contracts/variation-waiver-settlement.md` — amendment, contractual waiver, later agreement, course of dealing/conduct, and settlement terms that change contractual transaction/obligation state.

Activate BL3 when a decision depends on what transaction exists, what terms/documents govern, what each party must do, what performance state exists, whether the deal changed, or what a dispute-resolution clause contractually says/does.

BL3 sibling units are not a mandatory pipeline. Consume already committed sibling propositions from shared state without loading the sibling unit unless that proposition is unresolved, disputed, stale, contradictory, or material to reopen.

BL3 does **not** decide entity/signatory authority or corporate approval (BL2), breach/remedies/claim consequences/dispute invocation or procedure (BL4), statutory tax liability (BL5), public-law permission/compliance (BL7), or governing-law/treaty/CISG/cross-border overlay (BL8).

For domestic BL3 propositions, BL3 remains the substantive owner and resolves applicable contract-law authority using Authority Resolver where required. BL1 only routes candidate regimes.

Do not load all four BL3 units by default.

## BL4 — Breach / Remedies / Evidence / Disputes

Start with:

`bl4-remedies-disputes/core.md`

Then JIT-load only the capability needed:

- `bl4-remedies-disputes/breach-excuse-liability.md` — breach/materiality/attribution, excuse/defense, force-majeure/hardship-type questions, liability state after committed BL3 performance state, and exclusion/limitation effects on whether/to what scope liability exists;
- `bl4-remedies-disputes/remedies-loss-mitigation.md` — remedy availability, termination/performance/payment relief, penalty/damages/interest, loss/causation/proof/mitigation, and exclusion/limitation effects on remedy/recovery/quantum after liability is established;
- `bl4-remedies-disputes/notice-evidence-deadlines.md` — notice/cure/objection/reservation, evidence preservation/mapping, limitation/time bars, trigger/clock/tolling/expiry/filing-window state, and preservation of claims/options;
- `bl4-remedies-disputes/dispute-posture-procedure-settlement.md` — invocation under a committed dispute-resolution clause/forum, filing mechanics/procedural sequence, dispute posture, urgent protection, and settlement posture using committed timing state.

Activate BL4 after BL3 has established a material obligation/performance proposition, or when remedy preservation, claim procedure, or invocation under a committed dispute-resolution clause is material.

BL4 sibling units are not a mandatory pipeline. Consume already committed sibling propositions from shared state without loading the sibling unit unless that proposition is unresolved, disputed, stale, contradictory, or material to reopen.

BL4 does **not** reconstruct transaction/obligation/change state (BL3), dispute-clause contractual existence/content/effect (BL3), statutory tax consequences (BL5), public-law permission/compliance/enforcement (BL7), or governing-law/treaty/international-enforcement overlay (BL8).

Within BL4:

- deadline/timing ownership is singular: `notice-evidence-deadlines.md` owns trigger, clock, tolling/suspension/extension, expiry/filing-window, and preservation state;
- `dispute-posture-procedure-settlement.md` consumes that timing proposition and owns how/where/what procedural sequence to pursue;
- evidence preservation/mapping belongs to the notice/evidence unit, while evidentiary sufficiency remains with the proposition owner;
- exclusion/limitation ownership follows effect: liability-existence/scope → breach unit; remedy/recovery/quantum → remedies unit. If both effects matter, create two propositions.

For dispute-resolution clauses:

- BL3 owns clause existence/content and contract-law formation/incorporation/validity/effect as a contractual term;
- BL8 owns cross-border governing-law/treaty/international-enforcement overlay;
- BL4 owns invocation, dispute posture, filing mechanics/procedural sequence, and remedies under the resolved/conditioned clause/forum; timing/deadline propositions remain with `notice-evidence-deadlines.md`.

For settlement:

- BL4 owns settlement posture, claim/remedy preservation, and procedural consequences;
- when parties actually agree terms that create/change contractual obligations, BL3 owns formation/content/changed transaction state;
- BL4 then consumes the committed BL3 state for remaining claims/remedies/procedure.

Do not load all four BL4 units by default.

## BL5 — Tax / Financial Legal Consequences

Start with:

`bl5-tax/core.md`

Then JIT-load only the capability needed:

- `bl5-tax/characterization-events-roles.md` — map already-resolved business events to tax significance, statutory taxpayer/payer/recipient/withholder roles, candidate tax regimes, taxable-scope/non-taxable characterization, and scope exclusions integral to the regime;
- `bl5-tax/base-method-rate-timing.md` — taxable base, computation/withholding method, current rate/band/threshold, proposition-specific tax timing, and historical/current rule differences;
- `bl5-tax/documentation-invoice-evidence.md` — invoice/document/payment/evidence conditions for a specific tax position, including VAT-credit/deduction/deductibility support without collapsing them into accounting recognition;
- `bl5-tax/incentives-structuring-economics.md` — preferential incentive/exemption/holiday/preference entitlement after taxable scope is resolved and bounded tax-economic `FEEDBACK` across already lawful prospective options.

Activate BL5 when a decision depends on statutory tax characterization/role, tax computation/timing, documentary eligibility, preferential incentive entitlement, or tax consequences that materially change the economics of an upstream business option.

BL5 sibling units are not a mandatory pipeline. Consume already committed sibling propositions from shared state without loading the sibling unit unless that proposition is unresolved, disputed, stale, contradictory, or material to reopen.

BL5 consumes upstream corporate/transaction/employment/cross-border events and classifications. It must not reconstruct whether those business events occurred or reclassify them merely to reach a tax result.

Within BL5:

- business-event occurrence is owned upstream; `characterization-events-roles.md` maps the committed event to tax significance/trigger;
- taxable scope/non-taxable characterization and regime-integral exclusions belong to `characterization-events-roles.md`;
- preferential exemption/holiday/incentive entitlement after taxable scope is established belongs to `incentives-structuring-economics.md`;
- contractual tax allocation remains BL3 content; statutory taxpayer/withholder/tax treatment is BL5;
- employee/contractor and employment-law employer classification remain BL6; BL5 consumes committed/conditioned state for tax/withholding/contribution consequences only;
- foreign-payment/investment/trade classification remains BL8; BL5 consumes it for tax consequences;
- invoice validity, VAT credit, tax deductibility, and accounting recognition are separate propositions;
- tax-document defects do not silently erase BL3 transaction/payment state;
- tax economics that make an option unattractive normally create `FEEDBACK` to BL2/BL3/BL6/BL8, not automatic invalidation or reclassification;
- tax economics alone never justify changing a factual/legal classification; reopening classification requires new non-tax facts/evidence and remains owned by the upstream track.

BL5 does **not** own bookkeeping/accounting entries, general financial reporting, or full financial analysis.

Do not load all four BL5 units by default.

## BL6 — Employment / People-side Business Law

Start with:

`bl6-employment/core.md`

Then JIT-load only the capability needed:

- `bl6-employment/relationship-classification.md` — employee/contractor/work-relationship classification, employment-law employer identity, actual-work facts versus labels, and controlled reclassification review;
- `bl6-employment/engagement-terms-work-state.md` — employment-specific hiring/probation/onboarding terms, role/remuneration/workplace/schedule/current work state, changes to ongoing employment terms, and confidentiality duty/content/current effect during ongoing employment;
- `bl6-employment/performance-conduct-employer-action.md` — performance versus misconduct/conduct/attendance/capability classification, evidence, investigation/management action, and lawful employer-action pathway;
- `bl6-employment/restructuring-separation-protection.md` — restructuring/organizational change, unilateral or mutual separation, substantive employment-action notice/process/consultation timing, final employment state, and post-employment survival/effect of confidentiality plus other business protection.

Activate BL6 when a decision depends on employment relationship/employer classification, employment terms/current state, employer management action, restructuring/separation, substantive employment-action timing, or employment-specific post-employment protection.

BL6 sibling units are not a mandatory pipeline. Consume already committed sibling propositions from shared state without loading the sibling unit unless that proposition is unresolved, disputed, stale, contradictory, or material to reopen.

Within BL6:

- relationship/employer classification belongs to `relationship-classification.md`; downstream BL6/BL5 units consume committed or conditioned state rather than reconstructing it;
- where separation relies on performance or misconduct, `performance-conduct-employer-action.md` owns that issue/action-path proposition and `restructuring-separation-protection.md` consumes it;
- current confidentiality duty/content/effect during ongoing employment belongs to `engagement-terms-work-state.md`; post-employment survival/effect belongs to `restructuring-separation-protection.md`;
- substantive timing required to lawfully take the employment action belongs to BL6; claim/dispute-preservation timing such as limitation, filing, challenge and procedural deadlines belongs to BL4;
- desired employer outcome never creates a legal ground/pathway;
- restructuring, poor performance and misconduct remain separate propositions;
- BL5 owns tax/withholding/BHXH/contribution consequences after BL6 relationship state; tax economics alone never justify reclassification;
- BL7 owns privacy/data/monitoring legality even when monitoring evidence is relevant to BL6 merits;
- reclassification follows signal → review → commit; prior state remains current during review, the competing candidate and exact dependents remain explicit, and affected actions may require verification;
- on reclassification commit, prior classification becomes `SUPERSEDED`, new classification becomes `RESOLVED`, and only exact `DEPENDS_ON` dependents are invalidated/recomputed; `SIGNALS`/`FEEDBACK` never cause global invalidation.

BL6 does **not** own corporate decision-maker authority (BL2), tax/contribution consequences (BL5), privacy/data/monitoring compliance (BL7), or claim/dispute remedies, preservation deadlines and procedure (BL4).

Do not load all four BL6 units by default.

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

BL8 may also operate only as a cross-border overlay when the underlying proposition remains owned elsewhere.

Foreign element does not automatically mean import/export.

## Late-route examples

- BL3 receives evidence of missing signing authority → signal/late-return BL2.
- BL5 sees payroll-style evidence contradicting contractor classification → `CONTRADICTION_SIGNAL` to BL6; do not classify employee itself.
- BL6 finds monitoring/employee-data evidence material to an employer action → late-route BL7 for privacy/regulatory legality; BL6 retains employment merits ownership.
- BL6 employment action becomes challenged → late-route BL4 for claim/remedy/dispute-preservation timing and procedure; BL6 retains employment merits/pathway ownership.
- BL7 discovers foreign platform/operator facts → late-route BL8.
- BL8 discovers domestic product approval is material → late-route BL7.
- BL3 obligations unit establishes material non-performance/deviation → activate BL4; BL3 does not label the state breach itself.

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
- BL6 → BL5: employment classification precedes employment-tax/contribution consequences.
- BL6 ↔ BL7: employment merits/pathway and privacy/monitoring legality have separate owners.
- BL6 ↔ BL4: substantive employment-action timing stays BL6; claim/dispute-preservation timing and procedure stay BL4.
- BL8 → BL3: governing-law/treaty proposition precedes cross-border contract reasoning where material.
- BL3 ↔ BL7: agreement never replaces mandatory regulatory analysis.
- BL8 ↔ BL7: customs/border status never proves domestic market permission.
- BL3 ↔ BL8 ↔ BL4: clause contractual existence/effect / cross-border overlay / dispute invocation-procedure have separate owners.

## Invalidation reminder

This routing map is **not** an executable dependency graph.

Only explicit proposition-level `DEPENDS_ON` edges propagate automatic invalidation. `SIGNALS` and `FEEDBACK` create review triggers.
