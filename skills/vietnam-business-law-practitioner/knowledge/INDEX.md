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

Activate BL4 after the substantive owner has established the relevant merits/state (BL3 commercial obligations or BL6 employment merits), or when remedy preservation, claim procedure, or invocation under a committed dispute-resolution clause is material.

BL4 sibling units are not a mandatory pipeline. Consume already committed sibling propositions from shared state without loading the sibling unit unless that proposition is unresolved, disputed, stale, contradictory, or material to reopen.

BL4 does **not** reconstruct transaction/obligation/change state (BL3), dispute-clause contractual existence/content/effect (BL3), statutory tax consequences (BL5), public-law permission/compliance/enforcement (BL7), or governing-law/treaty/international-enforcement overlay (BL8).

Within BL4:

- deadline/timing ownership is singular: `notice-evidence-deadlines.md` owns trigger, clock, tolling/suspension/extension, expiry/filing-window, and preservation state;
- `dispute-posture-procedure-settlement.md` consumes that timing proposition and owns how/where/what procedural sequence to pursue;
- evidence preservation/mapping belongs to the notice/evidence unit, while evidentiary sufficiency remains with the proposition owner;
- exclusion/limitation ownership follows effect: liability-existence/scope → breach unit; remedy/recovery/quantum → remedies unit. If both effects matter, create two propositions.

For dispute-resolution clauses:

- BL3 owns clause existence/content and contract-law formation/incorporation/validity/effect as a contractual term;
- BL8 owns cross-border governing-law/private-law treaty/recognition-enforcement-regime overlay;
- BL4 owns invocation, dispute posture, filing/service/procedural sequence, deadlines and remedies under the resolved/conditioned clause/forum.

For settlement:

- BL4 owns settlement posture, claim/remedy preservation, and procedural consequences;
- when parties agree commercial contractual changes, BL3 owns formation/content/changed transaction state; employment-specific changes remain BL6-owned;
- BL4 then consumes the committed BL3 or BL6 state, according to substantive ownership, for remaining claims/remedies/procedure.

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
- customs duty/tariff propositions explicitly owned by BL8 remain BL8; BL5 owns VAT/CIT/PIT/withholding/excise and other non-customs-duty statutory tax consequences;
- invoice validity, VAT credit, tax deductibility, and accounting recognition are separate propositions;
- tax-document defects do not silently erase BL3 transaction/payment state;
- tax economics that make an option unattractive normally create `FEEDBACK` to BL2/BL3/BL6/BL8, not automatic invalidation or reclassification;
- tax economics alone never justify changing a factual/legal classification; reopening classification requires new non-tax facts/evidence and remains owned by the upstream track.

BL5 does **not** own bookkeeping/accounting entries, general financial reporting, or full financial analysis.

Do not load all four BL5 units by default.

### BL5 compulsory contribution routing

After BL6 relationship/employer state is committed or conditioned:

- `bl5-tax/characterization-events-roles.md` owns scheme-specific compulsory
  social-insurance/contribution coverage, exclusions, participant and liable
  contributor roles. Employment status alone does not settle scheme coverage.
- `bl5-tax/base-method-rate-timing.md` owns the contribution base, included pay
  components, caps/floors, allocation, applicable rate and participation/payment
  period under live authority; a taxable base is not a contribution base.
- `bl5-tax/documentation-invoice-evidence.md` owns registration, declaration,
  payroll, payment and coverage evidence needed for the contribution position.
- `bl5-tax/incentives-structuring-economics.md` is needed only for a separately
  claimed preferential relief or a comparison of lawful options, not routine
  coverage exclusions or a contribution-only calculation.

Keep scheme-specific coverage and contribution propositions separate from PIT
and other tax propositions. Load only units needed for the unresolved question.

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

Start with:

`bl7-regulatory/core.md`

Then JIT-load only the capability needed:

- `bl7-regulatory/regulatory-perimeter-role.md` — regulatory perimeter plus **coarse BL7 routing role/regime trigger** sufficient to decide which BL7 capability is material; it does not pre-decide operation-specific data roles or proposition-specific competition status;
- `bl7-regulatory/permission-entry-ongoing-compliance.md` — prohibition, market-entry/operating permission, license/approval/registration/notification, product/service domestic market placement, permission scope/lifecycle, and **permission-maintenance** conditions such as renewal or permission-linked reporting/records/inspection/event duties;
- `bl7-regulatory/market-conduct-consumer-claims.md` — consumer/customer mandatory protections, advertising/claims/promotions/pricing, e-commerce selling conduct, unfair/deceptive practices, and competition/market-conduct propositions including proposition-specific competition status where material;
- `bl7-regulatory/data-privacy-digital-operations.md` — personal-data processing, monitoring/tracking/profiling, employee/customer data, operation-specific controller/processor or other data-role propositions, vendor/group sharing, retention/security/access, and other privacy/digital-operation propositions.

Activate BL7 when a decision depends on a material public-law regulatory perimeter, permission/permission-maintenance state, market/customer conduct, privacy/data/digital operation, or sector specialist finding.

BL7 sibling units are not a mandatory pipeline. Consume already committed sibling propositions from shared state without loading the sibling unit unless that proposition is unresolved, disputed, stale, contradictory, or material to reopen.

Within BL7:

- `regulatory-perimeter-role.md` owns only BL7 perimeter plus coarse routing-role/regime-trigger propositions; dependent siblings consume that state and resolve their own proposition-specific data/competition roles where needed;
- business registration/registered business line never substitutes for activity/product/service permission;
- `permission-entry-ongoing-compliance.md` owns recurring duties only when they maintain/renew/amend/preserve or materially condition the permission state; ongoing claim/consumer/competition duties stay market-conduct, and ongoing processing/retention/sharing/security duties stay data/privacy;
- permission to operate/place a product does not establish that every claim, promotion, customer practice or competition restriction is lawful;
- BL3 owns private contract/consent content; BL7 separately resolves mandatory public-law permission, conduct and data propositions;
- BL8 owns border/customs/trade/foreign-investment propositions; BL7 owns domestic product/service market permission and domestic conduct after/beside those results;
- BL6 owns employment merits/pathway; BL7 owns privacy/data/monitoring legality even when the same evidence is relevant to employment action;
- market-conduct and privacy/data propositions may coexist for one digital practice and must not be collapsed into one generic `digital compliance` result;
- **any active BL7 capability that owns the material proposition** may invoke specialist depth after the materiality gate; perimeter is not a specialist gateway. Specialist findings remain candidate depth until the same owning BL7 capability accepts/conditions/rejects them.

BL7 does **not** own private contract formation/content (BL3), private dispute remedies/procedure (BL4), tax (BL5), employment merits/classification (BL6), or foreign-investment/trade/customs/payment classification (BL8).

Do not load all four BL7 units by default.

## BL8 — Investment / Cross-border / Trade

Start with:

`bl8-cross-border/core.md`

Then JIT-load only the capability needed:

- `bl8-cross-border/foreign-investment-market-access.md` — foreign-investor status, foreign-investment market access/control, acquisition/subscription/project entry/change triggers, and investment/market-access treaty commitments/schedules using committed BL2 corporate facts;
- `bl8-cross-border/governing-law-treaty-enforcement.md` — governing law/conflict-of-laws, CISG/private-law treaty applicability, mandatory-law interaction, and cross-border recognition/enforcement-regime overlay while BL3/BL4 retain substantive/procedural ownership;
- `bl8-cross-border/fx-cross-border-payment.md` — cross-border payment/capital-flow classification, FX/account/channel/registration/reporting conditions, and foreign-payment state consumed by BL5;
- `bl8-cross-border/trade-customs-origin-tariff.md` — goods trade/customs, HS, origin, FTA/trade-agreement origin/tariff propositions, customs valuation/customs duty/tariff/preference, clearance state, and owner-bound HS/origin/customs specialist depth.

Activate BL8 only when a foreign element can materially change a proposition. A foreign element is an activation/materiality signal, **not** a rule assigning the whole case to BL8.

BL8 sibling units are not a mandatory pipeline. Consume already committed sibling propositions from shared state without loading the sibling unit unless that proposition is unresolved, disputed, stale, contradictory, or material to reopen.

Every committed BL8 proposition/handoff must make dual role explicit where material:

```text
bl8_role: OWNER | OVERLAY
substantive_owner: BL2 | BL3 | BL4 | BL5 | BL6 | BL7 | null
```

`OVERLAY` conditions another owner's proposition/action; it never transfers that substantive proposition to BL8.

Within BL8:

- BL2 owns corporate identity/cap table/voting/control/approval; `foreign-investment-market-access.md` owns the separate foreign-investment consequence of those committed facts;
- treaty ownership follows proposition, not the noun: investment/market-access treaty commitments → investment unit; private-law governing/CISG/conflict or recognition-enforcement treaty overlay → governing-law unit; FTA/trade-agreement origin/tariff → trade unit;
- BL3 owns contract formation/content/obligations and dispute-clause contractual content/effect as a term; `governing-law-treaty-enforcement.md` may overlay governing law/CISG/private-law treaty state but must not resolve BL3 obligations;
- BL8 owns whether a cross-border recognition/enforcement regime/pathway is available and its treaty/recognition conditions; BL4 owns filing, service, procedural sequence, deadlines, interim/remedial posture and execution of that pathway;
- `fx-cross-border-payment.md` owns foreign payment/capital-flow classification; BL5 owns resulting non-customs-duty tax/withholding consequences;
- `trade-customs-origin-tariff.md` owns customs classification, customs valuation, tariff/preferential tariff, customs duty, and only border/customs charges intrinsically part of that trade/customs proposition; BL5 owns VAT/CIT/PIT/withholding/excise and other non-customs-duty statutory tax consequences;
- BL5 and BL8 must not independently own/calculate the same import fiscal item;
- BL7 owns domestic product/service market placement, operating permission and conduct; BL8 border/customs or foreign-investment status does not substitute for BL7;
- `fx-cross-border-payment.md` does not activate goods/customs merely because a payment/counterparty is foreign;
- within trade/customs reasoning, product name does not determine HS, shipment country does not determine preferential origin, and FTA existence does not determine preferential tariff entitlement;
- a specialist is owner-bound candidate depth only. BL8 accepts/conditions/rejects before committing an HS/origin/customs proposition.

Do not load all four BL8 units by default.

## Employment claims, settlement and cross-border terms

BL4 consumes committed BL6 employment merits/state for employment claims and
remedies; BL3 commercial obligation/performance state is not a prerequisite for
that handoff. BL4 owns claim/remedy/procedure, while BL6 retains the underlying
employment ground, term and separation state.

A settlement that changes employment terms or mutual separation goes to BL6:
ongoing terms to `bl6-employment/engagement-terms-work-state.md`, separation/end
state to `bl6-employment/restructuring-separation-protection.md`. BL4 consumes the
committed change for remaining claims and procedural consequences. Ordinary
commercial settlement terms go to BL3. Split mixed settlements by proposition.

A cross-border regime overlay affecting an employment term uses BL8 `OVERLAY`
with `substantive_owner: BL6`. BL6 supplies the employment term/choice-of-law
content; BL8 resolves its conflict-law effect and returns it to BL6 for merits.

## Late-route examples

- BL3 receives evidence of missing signing authority → signal/late-return BL2.
- BL5 sees payroll-style evidence contradicting contractor classification → `CONTRADICTION_SIGNAL` to BL6; do not classify employee itself.
- BL6 finds monitoring/employee-data evidence material to an employer action → late-route BL7 for privacy/regulatory legality; BL6 retains employment merits ownership.
- BL6 employment action becomes challenged → late-route BL4 for claim/remedy/dispute-preservation timing and procedure; BL6 retains employment merits/pathway ownership.
- BL7 discovers foreign platform/operator facts → late-route BL8 for the exact foreign/cross-border proposition while BL7 retains domestic regulatory ownership.
- BL8 investment/trade analysis discovers domestic sector/product approval is material → late-route BL7; foreign-investment/customs state does not prove domestic permission.
- BL8 payment evidence contradicts the committed BL3 transaction purpose → `CONTRADICTION_SIGNAL` to BL3; BL8 must not rewrite transaction state.
- BL8 investment evidence contradicts committed BL2 ownership/control → `CONTRADICTION_SIGNAL` to BL2; BL8 must not reconstruct cap table/control.
- BL8 recognition/enforcement regime becomes actionable → BL4 executes filing/service/procedure/deadline pathway; BL8 does not execute it.
- BL3 obligations unit establishes material non-performance/deviation → activate BL4; BL3 does not label the state breach itself.

## Specialist depth

A specialist is never a top-level sibling route.

Only an accountable BL owner may invoke specialist depth via `../schemas/specialist-handoff.md`.

Examples:

- BL8 active owning capability → HS classification / preferential origin / customs technical specialist;
- BL5 → transfer-pricing specialist;
- BL7 active owning capability → privacy / food / medical / product-safety / competition / sector-licensing specialist.

The specialist returns candidate depth to the owner; the owner promotes/conditions/rejects the result. BL8 must not let an HS/origin specialist directly commit a legal proposition or final readiness state.

## Composition reminders

- BL2 → BL3: authority/approval propositions condition binding transaction conclusions.
- BL3 → BL4: obligation/performance propositions precede breach/remedy.
- BL6 → BL5: employment classification precedes employment-tax/contribution consequences.
- BL6 ↔ BL7: employment merits/pathway and privacy/monitoring legality have separate owners.
- BL6 ↔ BL4: substantive employment-action timing stays BL6; claim/dispute-preservation timing and procedure stay BL4.
- BL2 ↔ BL8: corporate ownership/control state and foreign-investment control/market-access consequence have separate owners.
- BL8 → BL3: governing-law/CISG/private-law treaty overlay precedes cross-border contract reasoning where material; BL3 remains contract owner.
- BL8 ↔ BL4: recognition/enforcement regime/pathway belongs to BL8; procedural execution belongs to BL4.
- BL3 ↔ BL7: agreement never replaces mandatory regulatory analysis.
- BL8 ↔ BL7: customs/border/foreign-investment state never proves domestic market permission.
- BL3 ↔ BL8 ↔ BL4: clause contractual existence/effect / cross-border regime-recognition overlay / dispute invocation-procedural execution have separate owners.
- BL8 → BL5: foreign payment/investment/trade classification and explicitly BL8-owned customs-duty state may be consumed for tax/economic consequences; BL5 retains non-customs-duty tax ownership and tax economics do not back-solve BL8 classification.

## Invalidation reminder

This routing map is **not** an executable dependency graph.

Only explicit proposition-level `DEPENDS_ON` edges propagate automatic invalidation. `SIGNALS` and `FEEDBACK` create review triggers.
