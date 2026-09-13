# BL7 — Permission / Market Entry / Ongoing Compliance

## Owns

Determining whether a business may lawfully commence or continue a regulated activity, product/service operation, market entry, or other public-law activity, including prohibition, license/approval, registration/notification, qualifying conditions, **permission-maintenance conditions**, and event-triggered duties that affect permission status or action readiness.

This unit owns **public-law permission and permission-maintenance propositions** after the relevant regulatory perimeter/role is sufficiently resolved. It does not own every ongoing compliance duty merely because the duty recurs over time.

## Does not own

- regulatory-perimeter/coarse routing-role discovery when still unresolved — `regulatory-perimeter-role.md`;
- private contract formation/content — BL3;
- breach/remedies/dispute procedure — BL4;
- tax treatment — BL5;
- employment relationship/pathway — BL6;
- advertising/consumer/competition conduct propositions, including ongoing claim/pricing/customer-practice duties — `market-conduct-consumer-claims.md`;
- privacy/data/digital-operation propositions, including ongoing processing/retention/sharing/security duties — `data-privacy-digital-operations.md`;
- border/customs/trade or foreign-investment permission — BL8;
- specialist technical findings before BL7 owner integration.

## Activate when

Use when the decision depends on:

- whether an activity is prohibited, conditional, licensed, approved, registered, notified, certified, declared, or otherwise gated;
- whether a product/service may be placed on or remain in the domestic market;
- whether an existing permission remains current and sufficient for the actual activity;
- whether conditions must be satisfied before launch/operation;
- whether a **permission-linked** condition, renewal, notification/registration maintenance duty, reporting/recordkeeping/inspection obligation, or event-triggered duty affects permission status or readiness;
- whether a change in facts may require amendment, new approval/notification, or re-evaluation of permission state.

Skip when the question is only about market conduct, advertising/claims, consumer duties, competition, privacy/data, or a BL8 border/trade proposition.

## Required state

Where material, consume:

- committed BL7 perimeter/coarse routing-role proposition;
- entity/authority facts from BL2;
- actual business/activity/product/service facts;
- geography and channel;
- existing license/approval/registration/notification/certificate records;
- current conditions attached to those permissions;
- product/service status and material changes;
- BL8 import/customs/trade state where relevant to domestic post-border permission;
- relevant action and temporal anchors;
- authoritative current/historical permission rules.

Do not reconstruct a missing perimeter/role merely to reach a permission result. Return to `regulatory-perimeter-role.md` only if the route-level trigger itself is unresolved, disputed, stale, contradictory, or materially changed.

## Core distinctions

### Company exists ≠ activity may commence

Corporate formation and business registration from BL2 do not establish public-law operating permission.

### Registered business line ≠ conditions satisfied

A registered line may coexist with separate sector, product, facility, personnel, technical, notification, approval, certification, or permission-maintenance requirements.

### Permit exists ≠ permit covers this activity

Check scope, actor, activity, product/service, location, facility, channel, duration, conditions, and relevant changes. Do not treat one permission as global permission for the whole business.

### Entry compliance ≠ permission maintained

A business that lawfully entered the market may later lose or condition its permission/readiness because a permission-linked requirement expired, changed, was not maintained, or an event-triggered duty arose.

This unit owns that **permission-maintenance** state, not generic ongoing compliance across all BL7 propositions.

Examples:

```text
license requires annual report / renewal / notification
→ permission-entry-ongoing-compliance

advertisement must continue to satisfy substantiation/disclosure rules
→ market-conduct-consumer-claims

customer data retention/sharing/security duty continues over time
→ data-privacy-digital-operations
```

The word `ongoing` is not an ownership criterion. Proposition type is.

### License status ≠ evidence of all conditions

A license/certificate can prove a permission status, but not every permission-linked factual condition unless the authority and evidence actually support that proposition.

### Customs clearance ≠ domestic market permission

BL8 may resolve import/customs entry. BL7 separately decides post-border domestic product/service permission and permission-maintenance conditions.

### Contract permission ≠ public-law permission

A customer, supplier, landlord, platform, or counterparty may contractually agree to an activity. That does not establish statutory permission.

### Permission ≠ conduct safe

A business may have permission to operate while a specific advertisement, consumer practice, data use, or competitive conduct remains unlawful or conditioned.

## Decision procedure

1. **State the action.** Example: `May Entity E launch/continue Activity A on date D?`
2. **Consume perimeter/route state.** Use the committed BL7 regulatory trigger/coarse routing role.
3. **Classify the regulatory gate.** Prohibited, permission/approval, registration/notification, qualifying conditions, permission-maintenance conditions, or no material gate established.
4. **Resolve scope.** Actor, activity, product/service, location, facility/channel, duration and conditions.
5. **Resolve authority live.** Verify current/historical requirements and lifecycle state.
6. **Separate permission record from condition evidence.** Identify what the document proves and what permission-linked condition still needs factual evidence.
7. **Check change events.** New product, location, channel, ownership/control, facility, process, customer class, data use or another material fact may trigger re-evaluation of permission state.
8. **Commit permission state.** `PERMITTED`, `PERMITTED_WITH_CONDITIONS`, `VERIFY`, `BLOCKED`, `UNRESOLVED`, or another compatible reasoning status.
9. **Link action readiness explicitly.** A missing or unresolved permission/maintenance prerequisite affects readiness only when it is linked to the requested action.
10. **Route other recurring duties to the correct owner.** Market-conduct and data/privacy duties do not become this unit's merely because they are ongoing.
11. **Invoke specialist depth directly if this permission proposition requires it.** Apply the materiality gate, call specialist with `owner=BL7`, integrate the candidate finding here, and do not reload perimeter merely to authorize the call.

## Permission-state pattern

```text
P-BL7-PERM-01
perimeter_dependency: P-BL7-PERIM-...
action: <launch / operate / place product / continue / change>
gate_type: PROHIBITION / APPROVAL / LICENSE / REGISTRATION / NOTIFICATION / CONDITION / OTHER
scope: <actor/activity/product/location/channel/time>
permission_record: <if any>
permission_maintenance_conditions: [...]
change_trigger: <if any>
authority_freshness: <...>
status: PERMITTED / CONDITIONAL / VERIFY / BLOCKED / UNRESOLVED
```

These are reasoning states, not statutory labels.

## Evidence requirements

Potential evidence includes:

- licenses/approvals/certificates/registrations/notifications;
- scope/annex/condition documents;
- authority decisions and official records;
- facility/personnel/product/process evidence where permission conditions depend on them;
- renewal/change filings;
- permission-linked inspection/reporting/recordkeeping records;
- product/label/technical records where market placement is material;
- BL8 border/customs state where imported goods are involved;
- current official authority for the permission proposition.

`COMPLIANT` is never inferred merely from document possession. Preserve what each artifact actually proves.

## Live authority triggers

Use Authority Resolver for current prohibition/conditional status, permit/approval/notification requirements, scope and exemptions, renewal/lifecycle, permission-maintenance conditions, permission-linked event-triggered obligations, product/service market-placement rules, change-of-fact consequences, historical permission status, and current procedure where it materially affects action readiness.

Do not use this unit's authority resolution to absorb ongoing advertising/consumer/competition or data/privacy duties owned by sibling units.

Do not hardcode permit lists, thresholds, validity periods, forms, filing sequences, agency names, fees, or current conditions as stable knowledge.

## Cross-track handoffs

### From BL2

Consume entity/authority state. BL2 corporate existence/approval does not replace BL7 permission.

### From BL3

Consume activity/product/service/contract facts. Contractual allocation or consent does not create statutory permission.

### From BL8

Consume import/customs/trade status. Border clearance does not prove domestic market permission.

### To market-conduct unit

Return permission/activity state if the conduct proposition depends on what the business is allowed to offer or how it is regulated. Do not decide the conduct proposition here.

### To data/privacy unit

Return permission/activity state where a data proposition depends on it. Permission does not itself prove compliant data processing.

### To specialists

If this permission proposition requires sector/product technical depth, this active owning BL7 capability may invoke the specialist directly after the materiality gate. Specialist findings return as candidate depth; this unit accepts/conditions/rejects them before BL7 commits the permission proposition.

Do not reload `regulatory-perimeter-role.md` solely to authorize a specialist call.

## Failure modes

- company registration treated as permission to operate;
- business-line registration treated as all conditions satisfied;
- permit title treated as proof of scope;
- expired/stale license treated as current;
- generic `ongoing compliance` used to absorb advertising/consumer/data propositions;
- permission-maintenance duty confused with ongoing conduct/privacy duty;
- one license treated as permission for every product/location/channel;
- customs clearance treated as domestic market permission;
- contract consent treated as statutory permission;
- permit possession treated as proof of every factual compliance condition;
- perimeter reloaded solely to authorize specialist depth;
- specialist directly committing the final BL7 permission proposition;
- stale procedural checklist used for an irreversible launch.

## Escalation

Increase verification before launch, market entry, material business-model change, regulated product/service placement, expansion to new locations/channels, ownership/control changes that can affect permission, or any irreversible action where missing permission would create a hard legal blocker.