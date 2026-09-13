# BL7 — Regulatory Perimeter / Role / Regime Trigger

## Owns

Determining which public-law regulatory perimeter(s) are materially triggered by an already described business model, activity, product/service, customer relationship, channel, data flow, market position, and geography, including the **coarse BL7 routing role/regime trigger** needed to decide which BL7 capability becomes material.

This unit owns **regulatory-perimeter, coarse routing-role, and regime-trigger propositions**. It does not own operation-specific privacy/data roles, proposition-specific competition status, private contract formation, tax, employment classification, border/customs status, or a sector specialist's technical proposition by itself.

## Does not own

- corporate entity/authority/ownership state — BL2;
- contract formation/content/obligations — BL3;
- breach/remedies/dispute procedure — BL4;
- tax/contribution consequences — BL5;
- employment relationship/action pathway — BL6;
- foreign-investment, border/customs, trade and cross-border payment classification — BL8;
- operation-specific controller/processor/platform/intermediary or other privacy/data role — `data-privacy-digital-operations.md`;
- proposition-specific market-power/competition status where deeper conduct analysis is material — `market-conduct-consumer-claims.md`;
- specialist technical propositions merely because a regulatory noun appears.

## Activate when

Use when the decision depends on:

- whether an activity/product/service/channel/data practice/market position falls within a regulated perimeter;
- which coarse public-law role/regime trigger is sufficient to route the material BL7 proposition;
- whether the business acts, at a routing level, as seller, platform/intermediary, advertiser, producer/importer/distributor, service provider, data actor, market participant, or another materially different public-law role;
- whether several regulatory regimes may overlap;
- whether this **perimeter proposition itself** requires specialist depth;
- whether a change in business model, customer, channel, product, data flow, market position, or geography creates a new regulatory route.

Skip or compress when the material BL7 regime and coarse routing role are already reliably committed and the user only asks about a specific permission, conduct, privacy/data, or compliance proposition.

## Required state

Where material, consume or capture:

- legal actor/entity state from BL2;
- business activity and transaction facts from BL3 where relevant;
- product/service description and actual functionality;
- customer type and relationship;
- channel/platform/intermediary structure;
- advertising/claims/sales practices;
- data collection/use/sharing/monitoring flows at the level needed to identify the BL7 route, not to resolve operation-specific data roles;
- market position and counterparties at the level needed to identify a conduct/competition route, not to decide the final competition proposition;
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

Any active BL7 capability that owns the material proposition may decide specialist depth is required after applying the materiality gate.

Use:

```text
material BL7 proposition
→ owning BL7 capability
→ materiality gate
→ SPECIALIST_CALL owner=BL7
→ specialist returns candidate finding
→ owning BL7 capability accepts / conditions / rejects
→ BL7 commits owned proposition
```

For a perimeter proposition specifically, this unit may make that call itself. It is **not** a central specialist gateway for sibling propositions.

Do not use:

```text
word appears
→ reload perimeter
→ load entire sector handbook
```

### Actor identity ≠ coarse routing role ≠ operation-specific role

The legal entity from BL2 may play several public-law roles depending on the activity.

This unit resolves only the coarse role/regime trigger needed for BL7 routing. Where the final proposition depends on an operation-specific role, the owning sibling resolves that role from the relevant facts.

Examples:

```text
customer analytics creates a material privacy/data route
→ perimeter confirms DATA_PRIVACY route

who is controller/processor for Processing Operation O?
→ data-privacy-digital-operations
```

```text
market arrangement creates a material competition route
→ perimeter confirms MARKET_CONDUCT route

whether Actor A has the proposition-specific market status/power relevant to Conduct C
→ market-conduct-consumer-claims
```

Do not assign one global regulatory role to all propositions.

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
5. Resolve only the **coarse routing role/regime trigger** needed to select the accountable BL7 capability. Do not pre-decide operation-specific data or competition roles here.
6. Apply the canonical materiality gate before loading extra depth.
7. Resolve authority live where the perimeter itself is legally defined.
8. Commit perimeter/routing-role state as confirmed, plausible, unresolved, or rejected.
9. Route JIT depth: permission/permission-maintenance → `permission-entry-ongoing-compliance.md`; market/consumer/claims/competition → `market-conduct-consumer-claims.md`; privacy/data/digital operations → `data-privacy-digital-operations.md`.
10. If this perimeter proposition itself requires specialist depth, this unit may call a specialist under BL7 ownership. Sibling proposition owners do not need to reload this unit merely to authorize their own specialist call.

## Proposition pattern

```text
P-BL7-PERIM-01
actor: <resolved entity/actor>
activity: <...>
product_service: <...>
customer: <...>
channel: <...>
market_context: <if material>
geography: <...>
routing_role: <coarse candidate/resolved BL7 role>
regime_trigger: <candidate/resolved>
status: CONFIRMED / PLAUSIBLE / UNRESOLVED / REJECTED
```

Operation-specific data roles and proposition-specific competition status are separate sibling-owned propositions, not fields to be decided here.

## Evidence requirements

Potential evidence includes corporate/entity records, product/service specifications, user/customer journeys, sales/channel evidence, platform arrangements, claims/advertising materials, high-level data-flow maps, BL3/BL8 transaction/trade facts, market-position evidence, licenses/registrations/notifications, and authoritative scope definitions.

Preserve evidence provenance separately from the regulatory conclusion.

## Live authority triggers

Use Authority Resolver where the perimeter depends on regulated activity/product/service definitions, coarse regulated actor/role definitions needed for routing, current prohibited/conditional/notification categories, consumer/B2B scope, platform/intermediary regime triggers, competition-regime triggers, privacy/data-regime triggers, sector-specific triggers, or historical rules.

Operation-specific privacy/data-role definitions are resolved by `data-privacy-digital-operations.md`; proposition-specific competition status/depth is resolved by `market-conduct-consumer-claims.md` where material.

Do not hardcode current regulated-activity lists, thresholds, product lists, actor definitions, permit lists, forms, or article numbers.

## Cross-track handoffs

- BL2 → BL7: consume entity/actor identity; BL7 decides public-law consequence.
- BL3 → BL7: consume contractual/activity facts; agreement or contractual role does not substitute for regulatory classification or permission.
- BL6 → BL7: consume employment facts only where monitoring/data/sector propositions become material; BL6 retains employment merits ownership.
- BL8 → BL7: consume border/trade/foreign-operator facts; BL7 owns domestic market/product/service permission and conduct.
- BL7 siblings consume committed coarse perimeter/routing-role propositions from shared state; they resolve their own proposition-specific roles where needed and reopen this unit only when the perimeter itself is unresolved, disputed, stale, contradictory, or materially changed.
- Any active BL7 capability owning a material proposition may invoke specialist depth under BL7 ownership; specialist findings remain candidate depth until that capability accepts/conditions/rejects them.

## Failure modes

- registered business line treated as complete permission analysis;
- noun-based checklist dumping;
- perimeter treated as the exclusive specialist gateway;
- specialist loaded because a keyword appears rather than a material trigger;
- coarse routing role treated as an operation-specific controller/processor or competition conclusion;
- contractual role treated as public-law regulatory role;
- B2B treated as unregulated;
- customs/import clearance treated as domestic market permission;
- foreign element used to hand every regulatory question to BL8;
- one global regulatory role assigned to all propositions;
- stale conditional-business/product/threshold list used as current law;
- perimeter speculation loaded despite no effect on the requested action.

## Escalation

Increase verification for novel business models, platforms/intermediaries, regulated products/services, mixed B2B/B2C channels, cross-border operators, sensitive data/monitoring, concentrated markets, high-impact advertising/claims, or any activity where an incorrect perimeter classification could change whether the business may operate at all.