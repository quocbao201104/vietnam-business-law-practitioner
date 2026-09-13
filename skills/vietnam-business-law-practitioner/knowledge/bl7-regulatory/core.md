# BL7 — Regulatory / Market Conduct / Business Compliance

BL7 resolves public-law regulatory perimeter, permission/compliance, market-conduct, and privacy/data propositions for business activity in Vietnam, while preserving separate ownership for private contract, employment, tax, dispute, and cross-border/trade questions.

This `core.md` is a **JIT router**, not a regulatory encyclopedia. Load only the capability unit needed for the material proposition.

## Owns

BL7 owns propositions about:

- regulatory perimeter, coarse routing role, and material regime triggers;
- prohibition, market-entry permission, license/approval/registration/notification, product/service market placement, and permission-maintenance conditions;
- consumer, advertising/claims, e-commerce selling conduct, competition and other market-conduct constraints;
- privacy/data/monitoring/digital-operation legality, including operation-specific data roles;
- BL7-owned specialist activation and integration of candidate specialist findings by the active capability that owns the proposition.

BL7 does **not** own every consequence of a regulated business fact merely because public law is involved.

## Does not own

- corporate entity/authority/ownership/governance state — BL2;
- private contract formation/content/obligations — BL3;
- private dispute remedies, claim-preservation timing and procedure — BL4;
- tax/contribution consequences — BL5;
- employment relationship and employer-action merits — BL6;
- foreign-investment control, governing-law/conflict, FX/cross-border-payment, trade/customs/HS/origin propositions — BL8.

## Core distinctions

- business registration ≠ permission to operate;
- registered business line ≠ all regulatory conditions satisfied;
- absence from a remembered conditional-business list ≠ unregulated;
- contractual role ≠ public-law regulated role;
- coarse routing role ≠ operation-specific data/competition role;
- contract consent/agreement ≠ regulatory or privacy compliance;
- customs/border clearance ≠ domestic market permission;
- market-entry compliance ≠ permission maintained;
- permission-maintenance duty ≠ every recurring regulatory duty;
- permit exists ≠ permit covers every actor/activity/product/location/channel/time;
- product/service may be lawful ≠ every claim/customer practice is lawful;
- claim wording ≠ claim substantiation;
- B2B ≠ no mandatory regulation;
- small company ≠ competition-exempt;
- worker consent ≠ lawful monitoring/data processing;
- useful evidence ≠ lawfully collected evidence;
- platform feature/policy ≠ statutory permission;
- specialist keyword ≠ specialist activation;
- perimeter unit ≠ exclusive specialist gateway;
- compliance document ≠ proof of complete compliance.

## JIT capability routing

### Regulatory perimeter / role

Load `regulatory-perimeter-role.md` when the question depends on:

- whether an activity/product/service/channel/data practice/market position falls within a material regulatory perimeter;
- which coarse BL7 routing role/regime trigger is enough to decide the next BL7 capability;
- whether several regimes overlap;
- whether a material business-model/fact change activates another BL7 route;
- whether the **perimeter proposition itself** requires specialist depth.

Do not use this unit to pre-decide operation-specific controller/processor roles or proposition-specific competition status that belong to the downstream owning capability.

### Permission / entry / permission maintenance

Load `permission-entry-ongoing-compliance.md` when perimeter/route is sufficiently resolved and the question depends on:

- prohibition or permission to commence/continue an activity;
- license/approval/registration/notification/certification or similar gate;
- product/service domestic market placement;
- scope/lifecycle of a permission;
- permission-linked ongoing conditions, renewals, notification/registration maintenance, reporting, recordkeeping, inspection or event-triggered duties;
- whether a material change requires re-evaluation of permission state.

Do not route a recurring duty here merely because it is `ongoing`: recurring claim/consumer/competition duties stay market-conduct; recurring processing/retention/sharing/security duties stay data/privacy.

### Market conduct / consumer / claims / competition

Load `market-conduct-consumer-claims.md` when the question depends on:

- consumer/customer mandatory protections;
- advertising, factual claims, comparisons, endorsements, disclosures or promotions;
- pricing/sales/e-commerce conduct;
- unfair/deceptive conduct;
- exclusivity, bundling/tying, coordination, restrictions, market power or another competition/market-conduct proposition.

This unit resolves proposition-specific competition status/depth where needed rather than relying on a coarse perimeter role as the final competition conclusion.

### Data / privacy / digital operations

Load `data-privacy-digital-operations.md` when the question depends on:

- employee/customer data collection/use/sharing/retention/deletion;
- monitoring, tracking, profiling, biometrics, CCTV or device/system access;
- cookies/analytics/targeting/personalization/messaging or platform data flows;
- operation-specific controller/processor/platform/intermediary or another legally material data role;
- vendor/group-company sharing, security/access controls or cross-border data-specific compliance.

Do not load all four units by default.

## Sibling JIT rule

BL7 sibling units are **not a mandatory pipeline**.

A committed BL7 proposition may be consumed directly from shared state without loading its owning sibling when it is already reliable and not material to reopen.

Load the sibling only when the owned proposition is unresolved, disputed, stale, contradictory, or material to reopen.

Examples:

```text
Regulated route/role already committed; user asks only whether existing license covers Activity A
→ permission-entry-ongoing-compliance
```

```text
Permission to sell already committed; user asks whether Claim C may be published
→ market-conduct-consumer-claims
```

```text
Employment merits already committed; user asks whether monitoring data may lawfully be collected/used
→ data-privacy-digital-operations
```

Do not force:

```text
perimeter
→ permission
→ conduct
→ privacy/data
```

for every regulatory question.

## Internal ownership rules

### Coarse perimeter/route role ≠ proposition-specific sibling role

Where the regulatory route itself is material and unresolved:

```text
regulatory-perimeter-role
→ committed / conditioned coarse BL7 route/regime trigger
→ dependent permission / conduct / data proposition
```

The downstream owner consumes that route state, then resolves its own proposition-specific role where needed.

Examples:

```text
privacy/data route is material
→ perimeter

who is controller/processor for Operation O?
→ data-privacy-digital-operations
```

```text
competition route is material
→ perimeter

what proposition-specific market status/power is relevant to Conduct C?
→ market-conduct-consumer-claims
```

A downstream BL7 unit must not silently invent a missing **route-level** trigger merely to continue, but it also must not reload perimeter to obtain an operation-specific role that it itself owns.

### Permission ≠ market conduct

```text
May the business/product/service operate or enter/remain in market?
→ permission-entry-ongoing-compliance

May the business make/use this claim, promotion, customer practice or competition restriction?
→ market-conduct-consumer-claims
```

Permission to operate does not prove conduct legality; conduct defect does not automatically erase the underlying permission unless current authority creates that exact consequence.

### Permission maintenance ≠ generic ongoing compliance

`permission-entry-ongoing-compliance.md` owns recurring obligations only when they maintain, renew, amend, preserve, or materially condition the permission/market-entry state.

```text
license annual report / renewal / permission-linked inspection
→ permission-entry-ongoing-compliance

ongoing ad substantiation / pricing / customer practice
→ market-conduct-consumer-claims

ongoing processing / retention / sharing / security
→ data-privacy-digital-operations
```

The word `ongoing` never decides ownership; the legal proposition does.

### Agreement/consent does not replace public-law analysis

BL3 owns private contract/consent content. BL7 consumes that content as evidence where material but separately resolves mandatory public-law permission/conduct/data propositions.

### Domestic market permission ≠ BL8 border/trade status

```text
BL8
→ import/customs/trade/border proposition

BL7
→ domestic product/service market permission and conduct
```

Neither proposition substitutes for the other.

### Employment merits ≠ monitoring/data legality

BL6 owns whether worker conduct/performance supports an employer action. BL7 owns whether the monitoring/data operation is compliant where material.

Evidence relevance or usefulness does not transfer employment merits ownership to BL7.

### Market conduct and privacy/data may coexist

A single digital practice may create two separate BL7 propositions.

Example:

```text
targeted advertising claim/disclosure
→ market-conduct-consumer-claims

tracking/profile/data use supporting the targeting
→ data-privacy-digital-operations
```

Do not collapse them into one generic `digital compliance` result.

## Specialist JIT rule

A specialist is never a top-level BL7 sibling and never owns the final BL7 proposition.

**Any active BL7 capability that owns the material proposition** may determine specialist depth is required after the canonical materiality gate.

Use:

```text
material BL7 proposition
→ owning BL7 capability
→ materiality gate
→ SPECIALIST_CALL owner=BL7
→ specialist returns candidate finding / evidence / authority / uncertainty
→ same owning BL7 capability accepts / conditions / rejects
→ BL7 commits owned proposition
```

`regulatory-perimeter-role.md` may invoke a specialist when the perimeter proposition itself requires depth. It is not a central authorization gateway for permission, conduct, or data propositions.

Possible specialist areas include privacy, food, medical/health, product safety, finance, education, telecom, environmental, competition, or another sector-specific domain.

Do **not** invoke specialist depth merely because a noun appears. The trigger must be concrete and material to the requested action.

Do **not** reload perimeter solely to authorize a specialist call from another active BL7 capability.

## Compliance lifecycle and change signals

BL7 state is proposition-specific and time-bound.

A previously resolved regulatory proposition may require review when material facts change, including:

- actor/coarse routing role;
- activity/product/service functionality;
- customer class;
- channel/platform/intermediary structure;
- data flow/purpose/recipient or operation-specific data role;
- location/geography;
- market position or proposition-specific competition state;
- ownership/control where the regulatory regime makes it material;
- permission lifecycle/permission-maintenance condition;
- authority freshness/change.

Use `SIGNALS`/late-route/re-resolution as appropriate. Do not globally invalidate unrelated BL7 propositions merely because one regulatory fact changed.

## Live authority behavior

Stable BL7 knowledge defines decision structure, ownership, handoffs and proof path. Use Authority Resolver whenever current/historical law materially determines:

- regulated activity/product/service/actor definitions and route-level triggers;
- prohibited/conditional/permission/notification status;
- permit scope/lifecycle/permission-maintenance conditions;
- consumer/customer mandatory rights/duties;
- advertising/claim/promotion/pricing restrictions;
- competition tests/thresholds/exemptions and proposition-specific market status where material;
- privacy/data/monitoring operation-specific roles, duties and conditions;
- sector specialist propositions;
- historical rules at the relevant launch/conduct/processing/action date.

Do not hardcode current lists, thresholds, permit periods, mandatory wording, consumer periods, competition presumptions, consent/notice fields, data-retention periods, forms, filing steps, agency names, fees, or article numbers.

Before a material irreversible/current action, re-resolve stale authority when a changed rule could affect permission, conduct legality, evidence/procedure, option set, or action readiness.

## Handoff rules

- BL2 → BL7: committed entity/authority/ownership facts where regulatory-role or permission analysis depends on them; BL7 owns public-law consequence.
- BL3 → BL7: contract/activity/consent/claim terms as private-law facts; agreement never substitutes for mandatory permission/conduct/data analysis.
- BL6 → BL7: employment/monitoring context; BL6 retains employment merits, BL7 owns privacy/data/regulatory legality.
- BL8 → BL7: border/trade/foreign-operator facts; BL7 owns domestic market/product/service permission and domestic conduct.
- BL7 → BL4: when a resolved regulatory/consumer/data issue becomes a concrete private claim/dispute, BL4 owns claim/remedy/deadline/procedure; BL7 retains regulator-facing public-law compliance/enforcement propositions.
- BL7 specialist → active owning BL7 capability: candidate depth only; that capability reviews before shared-state promotion.

If downstream evidence contradicts an upstream-owned corporate/contract/employment/trade proposition, emit `CONTRADICTION_SIGNAL` to the accountable owner rather than rewriting it inside BL7.

## Failure modes

- business registration treated as permission to operate;
- registered business line treated as proof all conditions are met;
- coarse route role treated as operation-specific data/competition conclusion;
- noun-based checklist dumping;
- perimeter treated as exclusive specialist gateway;
- specialist activation by keyword instead of material trigger;
- contract consent treated as privacy/regulatory compliance;
- customs clearance treated as domestic market permission;
- license treated as perpetual/current universal permission;
- permission-maintenance unit absorbing all recurring conduct/privacy duties;
- permission to sell treated as permission for any claim/promotion;
- platform feature/policy treated as statutory authority;
- B2B or small-company status treated as blanket exemption;
- useful employment evidence treated as lawfully collected by default;
- privacy/data and market-conduct propositions collapsed into one generic status;
- compliance document treated as proof of all operational conditions;
- stale lists/thresholds/forms used as current law;
- loading the whole regulatory handbook for a narrow permission, claim or data question.
