# BL7 — Permission / Market Entry / Ongoing Compliance

## Owns

Determining whether a business may lawfully commence or continue a regulated activity, product/service operation, market entry, or other public-law activity, including prohibition, license/approval, registration/notification, qualifying conditions, ongoing conditions, event-triggered duties, and compliance-state propositions.

This unit owns **public-law permission and ongoing-compliance propositions** after the relevant regulatory perimeter/role is sufficiently resolved.

## Does not own

- regulatory-perimeter/role discovery when still unresolved — `regulatory-perimeter-role.md`;
- private contract formation/content — BL3;
- breach/remedies/dispute procedure — BL4;
- tax treatment — BL5;
- employment relationship/pathway — BL6;
- advertising/consumer/competition conduct propositions — `market-conduct-consumer-claims.md`;
- privacy/data/digital-operation propositions — `data-privacy-digital-operations.md`;
- border/customs/trade or foreign-investment permission — BL8;
- specialist technical findings before BL7 owner integration.

## Activate when

Use when the decision depends on:

- whether an activity is prohibited, conditional, licensed, approved, registered, notified, certified, declared, or otherwise gated;
- whether a product/service may be placed on or remain in the domestic market;
- whether an existing permission remains current and sufficient for the actual activity;
- whether conditions must be satisfied before launch/operation;
- whether an ongoing condition, renewal, reporting, inspection, recordkeeping, or event-triggered obligation affects readiness;
- whether a change in facts may require amendment, new approval/notification, or re-evaluation of permission state.

Skip when the question is only about market conduct, advertising/claims, consumer duties, competition, privacy/data, or a BL8 border/trade proposition.

## Required state

Where material, consume:

- committed BL7 perimeter/regulated-role proposition;
- entity/authority facts from BL2;
- actual business/activity/product/service facts;
- geography and channel;
- existing license/approval/registration/notification/certificate records;
- current conditions attached to those permissions;
- product/service status and material changes;
- BL8 import/customs/trade state where relevant to domestic post-border permission;
- relevant action and temporal anchors;
- authoritative current/historical permission rules.

Do not reconstruct a missing perimeter/role merely to reach a permission result. Return to `regulatory-perimeter-role.md` if the trigger itself is unresolved.

## Core distinctions

### Company exists ≠ activity may commence

Corporate formation and business registration from BL2 do not establish public-law operating permission.

### Registered business line ≠ conditions satisfied

A registered line may coexist with separate sector, product, facility, personnel, technical, notification, approval, certification, or ongoing requirements.

### Permit exists ≠ permit covers this activity

Check scope, actor, product/service, location, facility, channel, duration, conditions, and relevant changes. Do not treat one permission as global permission for the whole business.

### Entry compliance ≠ ongoing compliance

A business that lawfully entered the market may later become non-compliant because conditions changed, expired, were not maintained, or event-triggered duties arose.

### License status ≠ evidence of all conditions

A license/certificate can prove a permission status, but not every ongoing factual condition unless the authority and evidence actually support that proposition.

### Customs clearance ≠ domestic market permission

BL8 may resolve import/customs entry. BL7 separately decides post-border domestic product/service permission and ongoing regulatory conditions.

### Contract permission ≠ public-law permission

A customer, supplier, landlord, platform, or counterparty may contractually agree to an activity. That does not establish statutory permission.

### Permission ≠ conduct safe

A business may have permission to operate while a specific advertisement, consumer practice, data use, or competitive conduct remains unlawful or conditioned.

## Decision procedure

1. **State the action.** Example: `May Entity E launch/continue Activity A on date D?`
2. **Consume perimeter/role state.** Use the committed BL7 regulatory role/regime trigger.
3. **Classify the regulatory gate.** Prohibited, permission/approval, registration/notification, qualifying conditions, ongoing conditions, or no material gate established.
4. **Resolve scope.** Actor, activity, product/service, location, facility/channel, duration and conditions.
5. **Resolve authority live.** Verify current/historical requirements and lifecycle state.
6. **Separate permission record from condition evidence.** Identify what the document proves and what still needs factual evidence.
7. **Check change events.** New product, location, channel, ownership/control, facility, process, customer class, data use or another material fact may trigger re-evaluation.
8. **Commit compliance state.** `PERMITTED`, `PERMITTED_WITH_CONDITIONS`, `VERIFY`, `BLOCKED`, `UNRESOLVED`, or another compatible reasoning status.
9. **Link action readiness explicitly.** A missing or unresolved permission affects readiness only when it is a prerequisite for the requested action.
10. **Route conduct/privacy/trade consequences to the correct owner.** Permission does not absorb sibling or BL8 propositions.

## Permission-state pattern

```text
P-BL7-PERM-01
regulated_role_dependency: P-BL7-PERIM-...
action: <launch / operate / place product / continue / change>
gate_type: PROHIBITION / APPROVAL / LICENSE / REGISTRATION / NOTIFICATION / CONDITION / OTHER
scope: <actor/activity/product/location/channel/time>
permission_record: <if any>
ongoing_conditions: [...]
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
- facility/personnel/product/process evidence where conditions depend on them;
- renewal/change filings;
- inspection/reporting/compliance records;
- product/label/technical records where market placement is material;
- BL8 border/customs state where imported goods are involved;
- current official authority for the permission proposition.

`COMPLIANT` is never inferred merely from document possession. Preserve what each artifact actually proves.

## Live authority triggers

Use Authority Resolver for current prohibition/conditional status, permit/approval/notification requirements, scope and exemptions, renewal/lifecycle, ongoing conditions, event-triggered obligations, product/service market-placement rules, change-of-fact consequences, historical permission status, and current procedure where it materially affects action readiness.

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

Return regulated-role/activity state where privacy/digital obligations depend on it. Permission does not itself prove compliant data processing.

### To specialists

Invoke a sector specialist only when the permission proposition requires technical depth beyond the stable BL7 reasoning layer. BL7 retains owner review.

## Failure modes

- company registration treated as permission to operate;
- business-line registration treated as all conditions satisfied;
- permit title treated as proof of scope;
- expired/stale license treated as current;
- entry permission treated as permanent ongoing compliance;
- one license treated as permission for every product/location/channel;
- customs clearance treated as domestic market permission;
- contract consent treated as statutory permission;
- permit possession treated as proof of every factual compliance condition;
- stale procedural checklist used for an irreversible launch.

## Escalation

Increase verification before launch, market entry, material business-model change, regulated product/service placement, expansion to new locations/channels, ownership/control changes that can affect permission, or any irreversible action where missing permission would create a hard legal blocker.