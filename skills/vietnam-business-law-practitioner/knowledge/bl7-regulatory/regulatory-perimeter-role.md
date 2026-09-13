# BL7 — Regulatory Perimeter / Role / Regime Trigger

## Owns

Determining which public-law regulatory perimeter(s) are materially triggered by an already described business model, activity, product/service, customer relationship, channel, data flow, market position, and geography, including the regulated role that BL7 should use for downstream permission or conduct analysis.

This unit owns **regulatory-perimeter, regulated-role and regime-trigger propositions**. It does not decide private contract formation, tax, employment classification, border/customs status, or a sector specialist's technical question by itself.

## Does not own

- corporate entity/authority/ownership state — BL2;
- contract formation/content/obligations — BL3;
- breach/remedies/dispute procedure — BL4;
- tax/contribution consequences — BL5;
- employment relationship/action pathway — BL6;
- foreign-investment, border/customs, trade and cross-border payment classification — BL8;
- specialist technical propositions merely because a regulatory noun appears.

## Activate when

Use when the decision depends on:

- whether an activity/product/service/channel/data practice/market role falls within a regulated perimeter;
- which actor is the regulated actor for the proposition;
- whether the business acts as seller, platform/intermediary, advertiser, data actor, producer/importer/distributor, service provider, dominant/market participant, or another legally material role;
- whether several regulatory regimes may overlap;
- whether a specialist regime should be invoked under BL7 ownership;
- whether a change in business model, customer, channel, product, data flow, market position, or geography creates a new regulatory route.

Skip or compress when the material BL7 regime and regulated role are already reliably committed and the user only asks about a specific permission, conduct, privacy, or compliance proposition.

## Required state

Where material, consume or capture:

- legal actor/entity state from BL2;
- business activity and transaction facts from BL3 where relevant;
- product/service description and actual functionality;
- customer type and relationship;
- channel/platform/intermediary structure;
- advertising/claims/sales practices;
- data collection/use/sharing/monitoring flows;
- market position and counterparties;
- geography and domestic versus cross-border elements;
- BL8 border/trade or foreign-operator facts where already resolved;
- relevant temporal anchors;
- current/historical regulatory authority where perimeter depends on law.

Do not infer the complete regulatory perimeter from a company name, business-line registration label, product nickname, website category, or contract title alone.

## Core distinctions

### Business registration ≠ regulatory perimeter resolved

A registered business line or general company registration may be relevant evidence but does not prove the activity is unrestricted, all required permissions exist, a specialist regime does not apply, or every channel/customer/product variation is permitted.

### Noun match ≠ specialist activation

Do not invoke a food, medical, privacy, competition, finance, education, telecom, advertising, product-safety, or other specialist merely because a noun appears.

Use:

```text
concrete material fact
→ candidate regulatory trigger
→ BL7 owner decides specialist depth is needed
→ specialist returns candidate finding to BL7
```

not:

```text
word appears
→ load entire sector handbook
```

### Actor identity ≠ regulated role

The legal entity from BL2 may play several regulatory roles depending on the activity. Resolve the role per proposition rather than assigning one global regulatory identity.

### B2B ≠ no mandatory regulation

A business-to-business relationship may change some consumer-oriented propositions, but it does not imply the activity is outside licensing, competition, advertising, data, product, sector, or other public-law regulation.

### Contract label ≠ regulatory classification

BL3 may establish a contractual role such as `service provider`, `agent`, `reseller`, or `platform`. BL7 still decides the relevant public-law role under the regulatory regime.

### Border status ≠ domestic regulatory permission

BL8 may establish import/customs/trade status. That does not establish that a product/service may lawfully be placed on, marketed in, or operated in the domestic market.

### Foreign element ≠ BL7 loses ownership

A foreign operator or cross-border flow may activate BL8 for foreign-investment/trade/payment propositions while BL7 still owns domestic regulatory permission or conduct.

## Decision procedure

1. State the regulatory question.
2. Map actor, activity, product/service, customer, channel, data, market position, and geography.
3. Consume upstream state from BL2/BL3/BL6/BL8; do not reconstruct it inside BL7.
4. Identify candidate regime triggers: prohibition, permission/entry, product/service rules, customer/consumer rules, advertising/claims, competition/market conduct, privacy/data, platform/e-commerce, or another concrete trigger.
5. Assign regulated role per proposition.
6. Apply the canonical materiality gate before loading extra depth.
7. Resolve authority live where perimeter is legally defined.
8. Commit perimeter/role state as confirmed, plausible, unresolved, or rejected.
9. Route JIT depth: permission/ongoing compliance → `permission-entry-ongoing-compliance.md`; market/consumer/claims/competition → `market-conduct-consumer-claims.md`; privacy/data/digital operations → `data-privacy-digital-operations.md`; specialist only when a concrete trigger requires it.

## Proposition pattern

```text
P-BL7-PERIM-01
actor: <resolved entity/actor>
activity: <...>
product_service: <...>
customer: <...>
channel: <...>
data_role: <if material>
market_position: <if material>
geography: <...>
regulated_role: <candidate/resolved>
regime_trigger: <candidate/resolved>
status: CONFIRMED / PLAUSIBLE / UNRESOLVED / REJECTED
```

## Evidence requirements

Potential evidence includes corporate/entity records, product/service specifications, user/customer journeys, sales/channel evidence, platform arrangements, claims/advertising materials, data-flow maps, BL3/BL8 transaction/trade facts, market-position evidence, licenses/registrations/notifications, and authoritative scope definitions.

Preserve evidence provenance separately from the regulatory conclusion.

## Live authority triggers

Use Authority Resolver where the perimeter depends on regulated activity/product/service definitions, regulated actor/role definitions, current prohibited/conditional/notification categories, consumer/B2B scope, platform/intermediary/data-role classifications, competition thresholds/market-role definitions, sector-specific triggers, or historical rules.

Do not hardcode current regulated-activity lists, thresholds, product lists, actor definitions, permit lists, forms, or article numbers.

## Cross-track handoffs

- BL2 → BL7: consume entity/actor identity; BL7 decides public-law role.
- BL3 → BL7: consume contractual/activity facts; agreement or contractual role does not substitute for regulatory classification or permission.
- BL6 → BL7: consume employment facts only where monitoring/data/sector propositions become material; BL6 retains employment merits ownership.
- BL8 → BL7: consume border/trade/foreign-operator facts; BL7 owns domestic market/product/service permission and conduct.
- BL7 siblings consume committed perimeter/role propositions from shared state; reopen only when unresolved, disputed, stale, contradictory, or materially changed.
- Specialists return candidate findings to BL7 for owner review.

## Failure modes

- registered business line treated as complete permission analysis;
- noun-based checklist dumping;
- specialist loaded because a keyword appears rather than a material trigger;
- contractual role treated as public-law regulatory role;
- B2B treated as unregulated;
- customs/import clearance treated as domestic market permission;
- foreign element used to hand every regulatory question to BL8;
- one global regulatory role assigned to all propositions;
- stale conditional-business/product/threshold list used as current law;
- perimeter speculation loaded despite no effect on the requested action.

## Escalation

Increase verification for novel business models, platforms/intermediaries, regulated products/services, mixed B2B/B2C channels, cross-border operators, sensitive data/monitoring, concentrated markets, high-impact advertising/claims, or any activity where an incorrect perimeter classification could change whether the business may operate at all.