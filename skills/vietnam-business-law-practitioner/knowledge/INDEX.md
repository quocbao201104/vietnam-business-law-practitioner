# Knowledge Routing Index

Load the smallest decision unit that owns the issue. Do not load all tracks by default.

## BL1 — Legal Issue Framing / Regime Selection

Use BL1 whenever the legal characterization, applicable regime, temporal scope, authority status, or routing itself is unresolved.

- `bl1-issue-framing/framing-and-routing.md` — turn a business situation into an issue map and route owners.
- `bl1-issue-framing/regime-selection.md` — build the applicable-law stack and resolve overlaps.
- `bl1-issue-framing/temporal-authority.md` — determine which version of law applies to the relevant event/action date.
- `bl1-issue-framing/authority-classification.md` — distinguish binding authority, official guidance, practice evidence, and secondary material.

## BL2 — Entity / Authority / Ownership / Governance

Activate for questions about who the legal actor is, who can bind it, internal approval, ownership/control, or corporate-state change.

- `bl2-corporate/entity-and-role.md`
- `bl2-corporate/authority-and-representation.md`
- `bl2-corporate/approvals-and-conflicts.md`
- `bl2-corporate/ownership-and-control.md`

Typical triggers:

- who may sign or authorize;
- legal representative vs owner/director;
- related-party transaction;
- board/member/shareholder approval;
- share/capital transfer;
- ownership/control change.

## BL3 — Contracts / Commercial Transactions

Activate to establish what deal legally exists, which documents/terms govern, what obligations exist, and what performance occurred.

- `bl3-contracts/formation.md`
- `bl3-contracts/document-stack.md`
- `bl3-contracts/obligation-and-proof.md`
- `bl3-contracts/variation-and-performance.md`

Do not use BL3 to decide breach remedies, tax liability, regulatory permission, or signatory authority.

## BL4 — Breach / Remedies / Evidence / Disputes

Activate after BL3 has established obligation/performance state or whenever an existing dispute, deadline, notice, or urgent evidence issue exists.

- `bl4-remedies-disputes/breach-and-excuse.md`
- `bl4-remedies-disputes/remedy-selection.md`
- `bl4-remedies-disputes/damages-and-evidence.md`
- `bl4-remedies-disputes/dispute-and-deadlines.md`

Typical triggers:

- non-performance or defective performance;
- force majeure/hardship/excuse;
- penalty, damages, interest;
- suspension/termination/cancellation;
- evidence preservation;
- negotiation, arbitration, litigation, limitation.

## BL5 — Tax / Financial Legal Consequences

Activate when a business decision may create tax, withholding, invoicing/documentation, deductibility, contribution, or tax-structuring consequences.

- `bl5-tax/tax-characterization.md`
- `bl5-tax/transaction-triggers.md`
- `bl5-tax/evidence-and-timing.md`
- `bl5-tax/structuring-consequences.md`

BL5 is not an accounting handbook and should not produce bookkeeping entries.

## BL6 — Employment / People-side Business Law

Activate for employee/contractor classification and employer decisions across the relationship lifecycle.

- `bl6-employment/relationship-classification.md`
- `bl6-employment/employment-lifecycle.md`
- `bl6-employment/discipline-and-exit.md`
- `bl6-employment/business-protection.md`

Typical triggers:

- freelancer/employee ambiguity;
- hiring/probation/terms;
- performance vs misconduct;
- discipline;
- restructuring/termination;
- confidentiality, trade secrets, post-employment restrictions.

## BL7 — Regulatory / Market Conduct / Business Compliance

Activate when private agreement is not enough to establish that the business may lawfully operate, market, process data, sell a product, or engage in conduct.

- `bl7-regulatory/regulatory-perimeter.md`
- `bl7-regulatory/market-entry.md`
- `bl7-regulatory/market-conduct.md`
- `bl7-regulatory/compliance-lifecycle.md`

Typical triggers:

- conditional business activity;
- licensing/registration/notification;
- consumer protection;
- advertising;
- e-commerce/platform role;
- competition;
- data/privacy;
- sector/product regulation.

## BL8 — Investment / Cross-border / Trade

Activate when a foreign element changes the applicable investment, governing-law, treaty, FX, payment, or trade/customs regime.

- `bl8-cross-border/foreign-element.md`
- `bl8-cross-border/investment-and-market-access.md`
- `bl8-cross-border/governing-law-and-treaty.md`
- `bl8-cross-border/trade-customs-interface.md`

Do not route every foreign transaction to customs. Cross-border services, investment, payments, and goods trade are separate modes.

## Specialist depth

If a core track detects a specialist issue that cannot be handled safely with generic reasoning plus live research, emit `SPECIALIST_DEPTH_REQUIRED`.

Examples:

- HS classification;
- preferential origin;
- transfer pricing;
- foreign borrowing;
- food/medical/product regulation;
- specialist privacy obligations;
- sector-specific licensing.

A specialist returns depth to the owning BL track. It does not become a new global decision owner.

## Composition reminders

- BL2 → BL3: authority before binding transaction conclusions.
- BL3 → BL4: obligation/performance before breach/remedy.
- BL6 → BL5: employment classification before employment-tax consequence.
- BL8 → BL3: governing-law/treaty resolution before cross-border contract analysis where material.
- BL3 ↔ BL7: contractual agreement never replaces mandatory regulatory analysis.
- BL8 ↔ BL7: customs/border status never proves domestic product/market permission.
