# BL2 — Corporate Approval / Conflict / Governance

## Owns

Determining whether a corporate action or transaction requires an internal approval, reserved-matter decision, conflict process, or related-party governance step, and whether that requirement has been satisfied.

This unit owns **internal corporate decision validity/state**. It is separate from representation/signing authority and separate from the contract's substantive terms.

## Does not own

- external representation/signing authority — `authority-representation.md`;
- corporate ownership/cap-table/voting/control state — `ownership-control-state-change.md`;
- contract formation/content/performance or disputed agreement interpretation — BL3;
- tax consequences — BL5;
- market/sector regulatory permission — BL7;
- foreign-investment approval/market-access procedures — BL8.

## Activate when

Use when a material action may involve:

- a reserved matter;
- board/member/shareholder/owner approval;
- significant asset/financing/corporate action;
- related-party or conflict-of-interest transaction;
- self-dealing or overlapping interests;
- corporate approval thresholds/conditions;
- approval timing, quorum, voting, abstention, disclosure, or documentation questions;
- transaction validity or action readiness that depends on internal governance.

## Required state

Where material, capture:

- entity/corporate form and relevant date;
- proposed action/transaction;
- transaction parties and relationships;
- decision-maker(s);
- representation/authority proposition if already resolved;
- charter/governance documents;
- **committed ownership/voting state** relevant to approval, or an explicit unresolved dependency on `ownership-control-state-change.md`;
- conflict/related-party facts;
- resolutions/minutes/consents/approvals;
- conditions, quorum/voting or procedural facts where material;
- any post-transaction confirmation/ratification evidence if relevant;
- resolved BL3 proposition for any shareholder/member agreement term whose existence/content/interpretation is material.

## Core distinctions

### Representation ≠ corporate approval

A person may be authorized to represent/sign for the entity while the transaction still requires a separate internal approval.

Do not infer:

```text
signatory authority satisfied
→ internal corporate approval satisfied
```

### Approval requirement ≠ approval obtained

First determine whether an approval is required; then separately determine whether the approval was validly obtained and remained effective for the action taken.

### Conflict signal ≠ invalid transaction

A related-party relationship, shared ownership, family relationship, management overlap, personal interest, or other conflict signal activates governance analysis. It does not itself establish invalidity, prohibition, or remedy.

### Voting/ownership input ≠ governance-owned state

Governance may need ownership/voting state to determine quorum, voting entitlement, abstention, or approval outcome. That does not make governance the owner of the cap table or corporate-control proposition.

If the relevant ownership/voting state is unresolved:

```text
governance question
→ activate ownership-control-state-change.md
→ consume committed ownership/voting proposition
→ apply governance rule
```

Do not reconstruct the cap table or control state inside this unit.

### Governance source ≠ contract reconstruction

A shareholder/member agreement may contain governance-related commitments, but its existence, content, formation, interpretation, and contractual effect belong to BL3 when disputed or material.

Use:

```text
BL3 resolves contractual proposition
→ BL2 governance asks what corporate-governance consequence follows, if any
```

Do not read a disputed agreement and simultaneously resolve both its contractual meaning and the governance result inside BL2.

### Economic importance ≠ legal reserved matter

A transaction can be commercially important without triggering a particular statutory/charter approval, and a legally reserved matter may be triggered even when management views the transaction as routine.

Resolve the actual governance source rather than using intuition about importance.

### Corporate approval ≠ regulatory approval

Board/member/shareholder/owner consent does not establish that a regulator, licensing authority, competition authority, investment authority, or other public body permits the action.

Route public-law questions to BL7/BL8.

### Corporate approval ≠ transaction effect

BL2 resolves:

- whether approval was required;
- whether it was obtained;
- whether a governance defect exists;
- the **corporate-law status/consequence of that defect within BL2 ownership**.

BL3 resolves what that BL2 proposition means for transaction formation, binding effect, content, performance, or other contract/transaction consequences under the applicable regime.

Do not infer:

```text
approval defective
→ contract automatically invalid / non-binding
```

## Decision procedure

1. **Define the exact corporate action.** Avoid asking abstractly whether `the company approved the deal`.
2. **Consume upstream BL2 state.** Do not reconstruct entity identity, signing authority, or ownership/voting state here. If ownership/voting state material to approval is unresolved, activate `ownership-control-state-change.md` first and consume its committed proposition.
3. **Identify candidate governance source.** Law, charter, board/member rules, reserved-matter list, prior resolution, transaction-specific governance document, or a **resolved BL3 proposition** about a shareholder/member agreement term where legally relevant.
4. **Detect conflict/related-party signals.** Map relationships and interests without pre-judging legal consequence.
5. **Resolve whether approval is required.** Bind the proposition to the relevant date and committed corporate state.
6. **Resolve the proper approving body/person and procedure.** Verify current/historical authority where procedure is material.
7. **Evaluate evidence that approval occurred.** Resolution, consent, minutes, written decision, voting evidence, disclosure/abstention evidence, or other applicable proof.
8. **Separate procedural defect from downstream transaction effect.** Resolve only the corporate-law status/consequence of the governance defect within BL2. Hand transaction-effect questions to BL3.
9. **Commit the approval proposition.** Supported, supported with conditions, unresolved, disputed, or defective subject to the resolved corporate-law consequence.
10. **Hand off downstream.** BL3 consumes approval/defect state for transaction conclusions; BL8 consumes corporate facts when foreign-investment procedures are separately triggered.

## Conflict / related-party analysis

Do not use a single label `related party` as the conclusion.

Separate at least:

- factual relationship between actors;
- legal definition/test applicable to the proposition;
- disclosure requirement;
- participation/abstention restriction if any;
- approving body/process;
- effect of non-compliance within corporate-governance ownership;
- downstream transaction consequence owned by BL3 where material.

Different regimes may define related/conflicted actors differently. Verify the definition relevant to the exact governance proposition.

## Approval proposition design

Prefer explicit propositions such as:

- `P-BL2-GOV-01: Transaction T required approval by corporate body B at date D.`
- `P-BL2-GOV-02: Required approval was documented before execution.`
- `P-BL2-GOV-03: Conflict procedure remains unresolved because relationship R may trigger disclosure/abstention rules.`
- `P-BL2-GOV-04: Governance defect D has corporate-law consequence C; downstream transaction effect remains for BL3.`

Avoid broad statements like `the board approved everything`, `related-party deal is invalid`, or `approval defect means the contract is void`.

## Evidence requirements

Potential evidence includes:

- charter/bylaws/governance rules;
- **shareholder/member agreement terms already resolved by BL3 when contractual content/interpretation is material or disputed**;
- board/member/shareholder resolutions;
- written owner decisions;
- meeting notices, minutes, attendance/quorum/voting records;
- committed ownership/voting proposition for the relevant meeting/action date;
- conflict disclosures;
- abstention/participation records;
- transaction schedules/materials presented for approval;
- post-action confirmation/ratification evidence where legally relevant.

Use only evidence needed for the proposition. Do not demand a corporate-data room for routine questions.

## Live authority triggers

Live authority is normally required when the result depends on:

- current statutory reserved matters;
- approval thresholds;
- quorum/voting/procedure;
- related-party/conflict definitions;
- disclosure/abstention rules;
- corporate-law consequence of missing/defective approval;
- historical governance rules at the transaction date.

Do not hardcode numeric thresholds, voting percentages, current procedural formalities, or article numbers as stable knowledge.

## Cross-track handoffs

### From authority / representation

Consume the resolved signatory/representation proposition. Do not treat it as internal approval.

### From ownership / control

Consume the committed ownership/voting/control proposition for the relevant date when quorum, voting entitlement, abstention, approving body, or outcome depends on it.

If that state is unresolved, return to `ownership-control-state-change.md`; governance must not reconstruct it.

### From BL3

Consume resolved contractual propositions when a shareholder/member agreement or other contract term is material to the governance question.

BL2 does not resolve disputed contractual existence/content/interpretation itself.

### To BL3

Provide:

- whether approval was required;
- whether it was obtained;
- unresolved conditions/defects;
- corporate-law status/consequence of any governance defect within BL2 ownership;
- temporal anchor;
- authority/evidence support.

BL3 decides what that BL2 proposition means for transaction formation, binding effect, content, performance, or other transaction consequences under the applicable regime.

### To BL5

If tax consequences depend on related-party/ownership facts, provide only committed facts/classifications from the owning BL2 unit. BL5 owns tax treatment.

### To BL7

Send competition/market-conduct/regulatory conflict issues only when the facts trigger a public-law proposition.

### To BL8

Provide only governance/approval propositions owned by this unit plus ownership/control facts already resolved by `ownership-control-state-change.md` when needed.

BL8 separately owns foreign-investment market-access/control tests and investment procedures.

## Failure modes

- signature treated as sufficient corporate approval;
- legal representative treated as unlimited corporate decision-maker;
- governance reconstructing cap table/voting/control state instead of consuming ownership unit;
- BL2 governance reconstructing disputed shareholder/member agreement content instead of consuming BL3;
- conflict/related-party status treated as automatic invalidity;
- approval defect promoted directly into contract invalidity/non-binding conclusion;
- commercial materiality substituted for actual reserved-matter rule;
- board/member/shareholder approval treated as regulatory permission;
- current governance rule applied to historical transaction without temporal check;
- voting/threshold numbers recalled from memory;
- BL3 silently deciding internal corporate approval itself;
- foreign-investment approval conflated with ordinary corporate approval.

## Escalation

Increase verification for major ownership/asset/financing actions, conflicted or related-party transactions, disputed approvals, defective minutes/resolutions, minority-owner disputes, transactions already signed without clear approval, or actions whose validity/remedy exposure materially depends on governance procedure.