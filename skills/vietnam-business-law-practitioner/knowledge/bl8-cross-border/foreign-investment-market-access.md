# BL8 — Foreign Investment / Market Access / Control

## Owns

Determining foreign-investment propositions that arise because an investor, owner, acquirer, project, transaction, or controlled entity has a foreign element, including foreign-investor status, market-access conditions, foreign-investment control tests, investment-entry/change triggers, **investment/market-access treaty commitments and schedules relevant to those propositions**, and investment-law consequences that depend on committed corporate facts.

This unit owns **foreign-investment status, market-access, foreign-investment control, and investment-treaty/market-access propositions**. It does not reconstruct corporate ownership/control, private transaction formation, domestic operating permission, or tax treatment merely because a foreign investor is involved.

## Does not own

- entity identity, cap table, voting/control, corporate approvals, transfer/subscription completion — BL2;
- private contract formation/content/closing obligations — BL3;
- breach/remedies/dispute procedure — BL4;
- tax/contribution treatment — BL5;
- domestic sector/product/service operating permission — BL7;
- private-law governing-law/conflict/CISG or recognition-enforcement treaty propositions — `governing-law-treaty-enforcement.md`;
- FTA/trade-agreement origin/tariff propositions — `trade-customs-origin-tariff.md`;
- FX/payment propositions — `fx-cross-border-payment.md`.

## Activate when

Use when a material decision depends on:

- whether an actor is a foreign investor or another investment-law category;
- whether a proposed acquisition/subscription/project/investment is permitted or conditioned for the foreign investor;
- foreign-investment market-access conditions or restrictions;
- **whether an investment/market-access treaty commitment, schedule, reservation or investor-treatment rule affects entry/control**;
- whether a transaction crosses an investment-law control/approval/registration threshold or trigger;
- whether a change in ownership/control, investor identity, sector/activity, project, location, or other investment fact changes the foreign-investment state;
- whether committed BL2 ownership/control facts create a distinct foreign-investment consequence.

Skip when the matter is merely a domestic corporate ownership/approval question, ordinary contract issue, domestic operating license, private-law treaty/CISG question, FTA-origin/tariff question, tax treatment, payment classification, or trade/customs question.

## Required state

Where material, consume:

- committed BL2 entity/actor identity;
- committed BL2 cap-table, voting/control, ownership-change and approval state;
- investor nationality/status and relevant legal characteristics;
- target/project/business activity and sector facts;
- transaction type: acquisition, subscription, contribution, project entry, restructuring, transfer, or another mode;
- pre- and post-transaction ownership/control state;
- domestic regulatory/sector facts from BL7 where relevant to market access but not owned here;
- contractual/closing facts from BL3 where needed as inputs, not as foreign-investment conclusions;
- investment treaty/special investor status facts where material;
- relevant temporal anchors;
- current/historical investment authority.

Do not reconstruct BL2 corporate state merely because a foreign-investment test depends on it.

## Core distinctions

### Corporate ownership/control ≠ foreign-investment control test

BL2 owns the underlying corporate proposition:

```text
who owns/votes/controls Entity E?
```

BL8 owns the separate foreign-investment proposition:

```text
given committed corporate state,
what foreign-investment consequence follows?
```

Do not collapse the two tests.

### Foreign ownership percentage ≠ complete market-access analysis

A percentage can be material but does not by itself resolve every foreign-investment question. Market access may also depend on activity/sector, investor category, investment treaty/special regime, transaction form, project facts, control features, timing, or another current legal condition.

Do not infer:

```text
foreign ownership = X%
→ transaction automatically permitted / prohibited
```

unless current authority makes that fact dispositive for the exact proposition.

### Treaty noun ≠ governing-law-unit ownership

Investment/market-access treaty propositions stay here when they affect investor treatment, entry, ownership/control or market-access conditions.

```text
investment treaty / market-access schedule
→ foreign-investment-market-access

private-law conflict / CISG / award-recognition treaty
→ governing-law-treaty-enforcement

FTA / preferential-origin / tariff treaty
→ trade-customs-origin-tariff
```

Do not route a treaty question by the noun `treaty`; route by the legal proposition it changes.

### Corporate validity ≠ foreign-investment compliance

A share transfer/subscription may be valid as a corporate/private-law transaction while a separate foreign-investment permission/registration/control proposition remains unresolved.

BL2/BL3 completion does not silently satisfy BL8.

### Foreign-investment permission ≠ domestic operating permission

BL8 may resolve foreign-investor market-access or investment-entry status. BL7 separately owns domestic activity/product/service operating permission and ongoing public-law compliance.

```text
foreign investor may enter structure
≠ business may commence regulated service
```

### Investor label ≠ legal investor status

`foreign company`, `Vietnam company with foreign shareholders`, `offshore fund`, `nominee`, `foreign-owned`, or similar labels are evidence/context, not the final legal classification.

Resolve the proposition from committed actor/ownership/control facts and current authority.

### Investment consequence ≠ tax consequence

BL8 classifies the investment structure/status where owned here. BL5 owns resulting tax/withholding/incentive consequences.

## Decision procedure

1. **State the foreign-investment proposition.** Example: `Does Acquisition A by Investor I trigger a foreign-investment market-access/control condition on closing date D?`
2. **Consume BL2 corporate state.** Entity identity, current ownership/control, proposed ownership/control change and required corporate approval where material.
3. **Classify the investment mode.** Acquisition, subscription/contribution, project/investment entry, restructuring, transfer, or another mode.
4. **Resolve investor status.** Determine the legally material investor category from current facts/authority without replacing BL2 actor identity.
5. **Identify the exact legal source family.** Domestic investment rule, market-access schedule, investment treaty/special investor regime, or another investment-specific source as material; do not route private-law/FTA treaty propositions here.
6. **Resolve market-access/control tests live.** Bind to actual activity/sector, investor status, transaction mode, pre/post state, treaty/special-regime facts if material, and temporal anchor.
7. **Separate investment-state consequence from corporate mechanics.** Return corporate implementation questions to BL2 and private closing/contract questions to BL3.
8. **Separate investment permission from domestic operating permission.** Late-route/consume BL7 where the business activity itself requires a domestic regulatory gate.
9. **Commit BL8 investment state with explicit BL8 role marker.** Supported, conditional, approval/registration-required, verify, blocked, disputed, or unresolved as appropriate.
10. **Hand consequences outward.** BL5 receives investment classification for tax consequence; BL2/BL3 receive owned implementation dependencies; BL7 receives domestic operating questions.

## Investment-state pattern

```text
P-BL8-INV-01
bl8_role: OWNER / OVERLAY
substantive_owner: BL2 / BL3 / BL4 / BL5 / BL6 / BL7 / null
investor: <actor>
target_or_project: <entity/project>
mode: ACQUISITION / SUBSCRIPTION / CONTRIBUTION / PROJECT / TRANSFER / RESTRUCTURE / OTHER
bl2_state_dependencies: [...]
pre_state: <ownership/control if material>
post_state: <ownership/control if material>
activity_sector: <...>
investment_treaty_or_schedule_state: <if material>
market_access_state: <...>
control_trigger_state: <...>
temporal_anchor: <...>
status: SUPPORTED / CONDITIONAL / APPROVAL_REQUIRED / VERIFY / BLOCKED / DISPUTED / UNRESOLVED
```

For the foreign-investment proposition itself, `bl8_role` will normally be `OWNER` and `substantive_owner` `null`. Use `OVERLAY` only where the BL8 state is explicitly conditioning another owner's substantive proposition/action; the marker never transfers that owner's proposition to BL8.

These are reasoning states, not hardcoded statutory labels.

## Evidence requirements

Potential evidence includes:

- BL2 entity/cap-table/voting/control propositions;
- investor identity/nationality/ownership records;
- transaction structure and pre/post ownership/control table;
- corporate resolutions/approvals where relevant as BL2 state;
- project/activity/sector description;
- investment/transaction documents from BL3;
- existing investment approvals/registrations or official records;
- current official market-access/investment authority;
- evidence of investment treaty/special investor status where material.

Preserve what each document actually proves. A corporate filing does not automatically prove the foreign-investment consequence.

## Live authority triggers

Use Authority Resolver where current/historical law materially determines:

- foreign-investor/investment-law actor definitions;
- market-access conditions/restrictions;
- foreign-ownership/control tests;
- acquisition/subscription/project approval or registration triggers;
- sector/activity restrictions affecting foreign investment;
- investment treaty/market-access commitments, schedules, reservations or investor-treatment conditions;
- change-of-investor/control consequences;
- transition/historical rules for the relevant investment/closing date.

Do not hardcode current ownership thresholds, restricted-sector lists, approval triggers, filing forms, agency names, procedures, treaty schedules, or article numbers.

## Cross-track handoffs

### From BL2

Consume corporate identity, cap table, voting/control, transfer/subscription completion and approval propositions. If new investment evidence contradicts BL2 corporate state, emit `CONTRADICTION_SIGNAL` to BL2 rather than rewriting the cap table/control.

### To BL2

Return foreign-investment condition/status. BL2 still owns corporate mechanics needed to implement the structure.

### From / to BL3

Consume transaction/closing facts when material. BL3 owns agreement/conditions/closing obligations; BL8 owns the foreign-investment proposition. A foreign-investment condition may become an explicit BL3 closing dependency without BL8 rewriting the contract.

### To governing-law unit

Only route a treaty proposition to `governing-law-treaty-enforcement.md` when it is a private-law governing-regime/CISG/conflict or recognition-enforcement proposition. Investment/market-access treaty commitments remain here.

### To BL7

If foreign-investment status is resolved but the activity/product/service still needs domestic permission, late-route/hand off to BL7. Investment access is not operating permission.

### To BL5

Provide committed investment/status/flow facts. BL5 owns tax/withholding/incentive consequences and must not back-solve the investment classification from tax economics.

## Failure modes

- BL8 reconstructing cap table/control rather than consuming BL2;
- foreign ownership percentage treated as complete market-access analysis;
- treaty keyword routed automatically to governing-law unit despite an investment/market-access proposition;
- corporate validity treated as foreign-investment compliance;
- foreign-investment approval treated as domestic operating license;
- foreign investor label treated as dispositive legal status;
- tax consequence used to choose/reclassify investment status;
- BL8 role marker omitted where owner/overlay distinction is material;
- current thresholds/restricted lists/treaty schedules recalled from memory;
- foreign element causing BL8 to absorb unrelated corporate/contract/regulatory questions.

## Escalation

Increase verification for regulated/restricted sectors, complex group ownership, indirect control, nominee/intermediary structures, multi-step acquisitions, project restructuring, treaty-dependent access, material changes before closing, or any irreversible transaction where an incorrect foreign-investment classification could block or condition closing.