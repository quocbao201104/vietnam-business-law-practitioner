# BL7 — Data / Privacy / Digital Operations

## Owns

Determining the public-law legality and compliance state of material personal-data, monitoring, tracking, profiling, employee/customer data, digital-platform, device/access, and other data-processing operations after the relevant BL7 route/perimeter trigger is sufficiently resolved.

This unit owns **privacy/data/digital-operation propositions, including operation-specific data-role propositions** such as controller/processor/platform/intermediary or another legally material privacy/data role derived from the actual processing operation/data flow.

It does not decide whether an employee committed misconduct, whether a contract was formed, or whether a cross-border payment/trade flow is lawful merely because data or a platform is involved.

## Does not own

- coarse BL7 regulatory-perimeter/routing-role discovery when unresolved — `regulatory-perimeter-role.md`;
- operating permission unrelated to the data/digital proposition — `permission-entry-ongoing-compliance.md`;
- advertising/consumer/competition conduct except the distinct data proposition — `market-conduct-consumer-claims.md`;
- private contract formation/content — BL3;
- employment merits/pathway — BL6;
- dispute remedies/procedure — BL4;
- foreign-investment/trade/customs/payment classification — BL8;
- specialist privacy/technical finding before BL7 owner integration.

## Activate when

Use when the decision depends on:

- collection, recording, monitoring, tracking, profiling, analysis, use, storage, sharing, disclosure, transfer, retention, deletion, or another processing operation;
- employee monitoring, biometrics, CCTV, device/system access, background checks, location or productivity tracking;
- customer/lead data, advertising audiences, personalization, cookies/tracking, messaging, loyalty, reviews or platform data flows;
- operation-specific controller/processor/platform/intermediary or another legally material data role;
- third-party/vendor or group-company data sharing;
- cross-border data movement where the data proposition itself is material;
- security/access/retention/deletion obligations where public-law compliance affects the business action.

Skip when data is incidental and cannot change the route, legal proposition, required evidence/procedure, option set, or action readiness.

## Required state

Where material, consume:

- committed BL7 perimeter/coarse routing state sufficient to establish that a privacy/data route is material;
- data subjects/actors and data categories actually involved;
- processing purpose(s) and operation(s);
- source and collection method;
- systems/vendors/recipients and access paths;
- retention/deletion logic;
- monitoring/device/platform context;
- employee relationship facts from BL6 where relevant to merits but not privacy legality;
- contract/consent/terms from BL3 as evidence, not automatic legal basis;
- domestic/cross-border geography and recipients;
- security/access-control facts where material;
- current/historical privacy/data authority.

Do not require `regulatory-perimeter-role.md` to pre-resolve controller/processor or another operation-specific privacy/data role. This unit owns that role proposition from the actual processing operation.

Do not accept a privacy policy, click-through consent, employee acknowledgement, vendor agreement, or platform setting as conclusive proof of lawful processing.

## Core distinctions

### Route-level privacy trigger ≠ operation-specific data role

`regulatory-perimeter-role.md` may establish that a privacy/data regime is materially triggered and provide a coarse route-level actor context.

This unit separately resolves the operation-specific role for the actual processing proposition.

Example:

```text
Business performs customer analytics
→ perimeter: privacy/data route is material

Who is controller/processor for Processing Operation O?
→ data-privacy-digital-operations
```

Do not let both units own the same data-role proposition.

### Consent ≠ complete privacy compliance

Consent/acknowledgement may be one fact or legal mechanism where applicable. It does not by itself resolve purpose limitation, transparency, data-role allocation, necessity, retention, security, transfer, data-subject rights, or another mandatory proposition.

### Contract permission ≠ public-law data permission

BL3 may establish that a worker/customer/vendor agreed to data use. BL7 still resolves the public-law legality and conditions of the processing.

### Evidence usefulness ≠ lawful collection/use

BL6 or BL4 may consider a monitoring record relevant to employment/dispute merits. BL7 separately decides whether the collection/use/retention/sharing of that evidence creates a privacy/data compliance issue.

Do not infer:

```text
evidence is useful
→ monitoring was lawful
```

### Privacy notice exists ≠ processing lawful

A notice proves, at most, that certain information was communicated if supported. It does not establish that the described processing is lawful, proportionate, accurate, current, secure, or actually implemented as stated.

### Data stored ≠ unlimited retention right

Retention must be tied to the legally relevant purpose, duty, dispute/evidence need, security requirement, or other supportable basis. Do not default to `keep forever just in case`.

### Platform feature ≠ regulatory permission

A platform providing a targeting, tracking, review, messaging, identity, analytics, or monitoring feature does not establish that using it is lawful for this business/context.

### Group company ≠ unrestricted data sharing

Corporate relationship from BL2 does not itself establish privacy/data permission between entities.

### Employee relationship ≠ unlimited monitoring

BL6 relationship/employer status does not automatically authorize every monitoring or data-processing method.

### Cross-border data element ≠ BL8 owns privacy

BL8 may own foreign-investment/payment/trade propositions. BL7 owns the privacy/data proposition, including cross-border data-specific requirements where those are part of the domestic regulatory regime.

## Decision procedure

1. **State the data proposition.** Example: `May Business B collect/use/share Data D for Purpose P in Operation O?`
2. **Consume route/perimeter state.** Use the committed coarse BL7 route trigger; do not reconstruct employment, contract, corporate, or trade state inside BL7.
3. **Map the data flow.** Data subject → collection/source → purpose → processing → system/vendor → recipient → location → retention/deletion.
4. **Identify the operation-specific legally material data role(s).** This unit owns that proposition. Do not assign one global role if roles differ across operations.
5. **Separate claimed legal mechanism from full compliance.** Consent/contract/notice/legitimate business purpose may require additional conditions.
6. **Resolve current authority.** Verify current/historical requirements for the specific operation and temporal anchor.
7. **Identify evidence/operational controls.** Notice, consent/record, access control, vendor terms, retention settings, security/process records, transfer records, rights handling, or other material evidence.
8. **Commit data-operation state.** Supported, conditional, verification-required, blocked, disputed, or unresolved.
9. **Link action readiness.** `DEPLOY MONITORING`, `SHARE DATA`, `LAUNCH TRACKING`, `RETAIN RECORD`, etc. only where the proposition is an explicit prerequisite.
10. **Return merits/contract/dispute questions to their owners.** Data legality does not absorb BL3/BL4/BL6.
11. **Invoke specialist depth directly if this data proposition requires it.** Apply the materiality gate, call specialist with `owner=BL7`, integrate candidate depth here, and do not reload perimeter solely to authorize the call.

## Data-state pattern

```text
P-BL7-DATA-01
data_subject: <...>
data_category: <...>
operation: <collect/use/share/monitor/retain/delete/transfer/etc.>
purpose: <...>
source: <...>
recipient_vendor: <if any>
location: <...>
data_role: <operation-specific legally material role(s)>
claimed_mechanism: <consent/contract/statutory/other if material>
retention_security_dependencies: [...]
temporal_anchor: <...>
status: SUPPORTED / CONDITIONAL / VERIFY / BLOCKED / DISPUTED / UNRESOLVED
```

## Evidence requirements

Potential evidence includes:

- actual data-flow maps/system architecture at the level needed for the proposition;
- privacy notices and communication records;
- consent/acknowledgement records where material;
- contracts/data-processing/vendor terms from BL3;
- system access/role/retention settings;
- logs showing actual collection/use/sharing;
- monitoring/device/CCTV/biometric configurations;
- data-subject request/complaint records;
- security/incident records where relevant;
- cross-border recipient/location evidence;
- authoritative current privacy/data rules.

Do not infer actual operational compliance solely from a policy document.

## Live authority triggers

Use Authority Resolver for current operation-specific data-role definitions, legal grounds/conditions, transparency/consent/notice requirements, employee/customer monitoring rules, sensitive/special data treatment, data-subject rights, retention/deletion/security requirements, vendor/recipient obligations, cross-border data requirements, breach/incident duties, or historical rules at the processing date.

Do not hardcode current consent wording, notice fields, retention periods, filing/assessment requirements, transfer procedures, thresholds, forms, or article numbers.

## Cross-track handoffs

### From perimeter unit

Consume only the committed coarse route/regime trigger needed to establish that the privacy/data capability is material. Resolve controller/processor or other operation-specific data roles here.

Reopen perimeter only when the route/regime trigger itself becomes unresolved, disputed, stale, contradictory, or materially changed.

### From BL6

BL6 provides employment merits and monitoring/evidence context. BL7 owns privacy/data legality. A BL7 problem may constrain an employer action but does not itself decide performance/misconduct.

### From BL3

Consume consent/contract/vendor terms as private-law content. They do not replace mandatory privacy/data analysis.

### To BL4

If a privacy/data issue becomes a concrete claim/dispute, return committed regulatory propositions for BL4 remedy/procedure ownership while BL7 retains regulator-facing compliance/enforcement propositions.

### To market-conduct unit

Targeting, personalization, reviews, advertising audiences or customer messaging may create both data and market-conduct propositions. Use separate owners within BL7 and do not collapse them into one `digital compliance` result.

### To specialists

If this data proposition materially requires privacy/security/sector technical depth, this active owning BL7 capability may invoke the specialist directly. Specialist findings return as candidate depth and must be accepted/conditioned/rejected here before shared-state promotion.

Do not reload perimeter solely to authorize specialist depth.

## Failure modes

- perimeter/coarse routing role treated as the operation-specific controller/processor conclusion;
- consent treated as complete privacy compliance;
- contract clause treated as statutory data permission;
- useful employment evidence treated as lawfully collected by default;
- privacy notice treated as proof of actual compliance;
- platform feature treated as legal permission;
- group-company relationship treated as unrestricted sharing right;
- employee status treated as unlimited monitoring authority;
- indefinite retention recommended without a supported purpose/duty;
- cross-border data automatically handed to BL8;
- perimeter reloaded solely to authorize specialist depth;
- privacy specialist bypassing BL7 owner review;
- hardcoded forms/thresholds/retention periods used as current law.

## Escalation

Increase verification for sensitive/high-impact data, employee monitoring, biometrics, profiling/automated decisions, children/vulnerable persons, large-scale tracking, cross-border data, security incidents, data sharing across multiple entities/vendors, or any irreversible deployment where a privacy/data defect could block launch or create material enforcement exposure.