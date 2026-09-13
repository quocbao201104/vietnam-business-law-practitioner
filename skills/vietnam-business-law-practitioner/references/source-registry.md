# Authority Source Registry v0.3

This registry gives stable source IDs and fallback roles for runtime authority discovery. It is not a legal database and does not imply that every statement on an official site is binding law.

Use together with `../schemas/authority-resolver.md`, `authority-sources.md`, `source-status.md`, and `search-strategy.md`.

## Registry principles

- Source identity/provenance is separate from legal force.
- **Discovery may be multi-source; verification requirements depend on the proposition.**
- Prefer the source that actually publishes the controlling instrument or official record.
- If one official source is unavailable or appears stale/incomplete, use another official source where the same instrument/record can be independently verified.
- Practitioner/academic/secondary sources may discover or interpret but do not silently replace primary authority when primary authority is material.
- Record the actual URL/document identity used at runtime; registry IDs are routing aids only.
- Portal backend IDs, `ItemID`s, UUIDs, frontend action hashes, and undocumented API routes are transport/locator details, not legal authority by themselves.
- Machine-readable official access is an optional accelerator, not a mandatory verification path.
- If an undocumented adapter changes shape, becomes unavailable, or appears stale, record the source-attempt condition and continue through an official fallback instead of treating the legal result as empty.

## General legal instruments

### `VN-VBPL`

Role: national/competent-authority legal-document databases under `vbpl.vn` and official Ministry of Justice VBPL services.

Use for: official text, legal-document identity/metadata, lifecycle/history, amendment/replacement/consolidation relationships, and provision structure where available.

Runtime note: portal frontend/backend endpoints may be useful as accelerators, but undocumented endpoint shapes or Next.js action identifiers are not stable contracts. Research has observed a document-detail transport shaped like `https://vbpl-bientap-gateway.moj.gov.vn/api/qtdc/public/doc/{id}`. Treat the route as implementation transport, not a guaranteed developer API. Cross-check returned instrument identity, tolerate catalog/index lag, and fall back to official web/publication sources when the transport fails or drifts.

Fallback: `VN-GOV-LAW`, original official attachment/publication, or competent ministry/regulator legal-document portal.

### `VN-GOV-LAW`

Role: Government legal-document publication portal under `vanban.chinhphu.vn` / official Government domains.

Use for: promulgated laws/decrees/resolutions/circular metadata, official text/attachments, and independent identity/effective-date verification where available.

Fallback: `VN-VBPL` or competent issuing authority.

### `VN-SECONDARY-LEGAL-INDEX`

Role: reputable non-official Vietnamese legal indexes/search services, for example Thư Viện Pháp Luật or LuatVietnam.

Use for: fast discovery, keyword search, candidate instrument/provision identification, and navigation to likely primary authority.

Constraint: discovery/interpretive aid only for material binding-law propositions. Verify controlling text, lifecycle, and amendment state against appropriate official authority before treating the proposition as resolved.

Fallback: direct web search plus `VN-VBPL`, `VN-GOV-LAW`, or the competent regulator.

## Corporate / investment

### `VN-BUSINESS-REGISTRY`

Role: National Business Registration Portal / competent business-registration authority (`dangkykinhdoanh.gov.vn` and successor official services).

Use for: business-registration procedures/forms/official registration guidance, current implementing materials, and domain-specific change signals.

Fallback: competent provincial/ministerial official source plus governing legal instrument.

### `VN-INVESTMENT-AUTH`

Role: competent investment authority / Ministry of Finance successor functions and official investment portals.

Use for: investment procedures, official market-access/implementation material where authoritative.

Fallback: governing law/decree on `VN-VBPL` / `VN-GOV-LAW`.

## Tax / customs / finance

### `VN-MOF`

Role: Ministry of Finance official portal and official policy/Q&A systems.

Use for: tax/customs/financial legal instruments and official administrative guidance.

Fallback: `VN-VBPL`, `VN-GOV-LAW`, competent tax/customs authority.

### `VN-TAX-AUTH`

Role: competent tax authority official services/portals.

Use for: official tax administration guidance, filing/implementation materials, taxpayer procedures.

Fallback: `VN-MOF` + governing legal instrument.

### `VN-CUSTOMS-AUTH`

Role: competent customs authority official portal/services.

Use for: customs procedures, classification/origin/administrative implementation material.

Fallback: `VN-MOF` + governing customs/trade instruments.

## Labour / social insurance

### `VN-LABOUR-AUTH`

Role: competent labour authority / ministry successor official portal.

Use for: labour implementing rules, official guidance, work-permit/employment procedures.

Fallback: `VN-VBPL` / `VN-GOV-LAW` + governing labour instrument.

### `VN-SOCIAL-INSURANCE`

Role: Vietnam Social Security official portal.

Use for: official social-insurance implementation/guidance and contribution procedures.

Fallback: governing law/decree/circular from official legal sources.

## Regulatory / competition / consumer / e-commerce

### `VN-MOIT`

Role: Ministry of Industry and Trade official portal.

Use for: trade, e-commerce, competition/consumer, advertising/market-conduct material within competence.

Fallback: `VN-VBPL` / `VN-GOV-LAW` + competent regulator.

### `VN-COMPETITION-CONSUMER`

Role: competent competition/consumer regulator official source.

Use for: regulatory decisions/guidance/market-conduct implementation within competence.

Fallback: `VN-MOIT` + governing legal instrument.

## Judiciary / disputes

### `VN-COURTS`

Role: Supreme People's Court / official court and precedent publication systems.

Use for: binding precedent where applicable, official judicial instruments, published judgments/decisions where relevant.

Fallback: official legal instrument source; practitioner summaries only as secondary discovery.

### `VIAC-PRACTICE`

Role: Vietnam International Arbitration Centre materials.

Status: practitioner/arbitral practice material, not automatically binding precedent.

Use for: practical dispute patterns, case summaries, arbitration procedure materials; verify controlling law separately.

## Treaties / trade

### `VNTR`

Role: Vietnam National Trade Repository (`vntr.moit.gov.vn`).

Use for: tariff schedules, rules of origin, non-tariff measures, trade procedures, treaty/FTA discovery.

Fallback: original treaty/FTA text and implementing instrument from official treaty/trade sources.

### `UNCITRAL-CISG`

Role: official UNCITRAL treaty/status materials.

Use for: CISG text/status and treaty discovery.

Fallback: official treaty publication/contracting-state materials.

## Official convergence rule

For a material binding-law proposition:

1. secondary/web discovery may nominate candidate instruments;
2. resolve the instrument against an appropriate official source;
3. optionally use official machine-readable transport when it speeds metadata/relationship/structure lookup;
4. check lifecycle and later-change signals;
5. when the rule is recent, disputed, high-consequence, or one official index may lag, use another appropriate official source or original official attachment as a cross-check;
6. preserve conflicts instead of averaging sources.

`Official convergence` is a verification discipline, not a fixed two-source quota.

## Registry fallback rule

When a registry source or transport is unavailable, stale, or drifting:

1. record `SOURCE_UNAVAILABLE` or `SOURCE_DRIFT` for the attempted source/adapter as appropriate;
2. follow the stated official fallback where possible;
3. preserve the source actually used and its provenance/legal force;
4. do not treat failure of one API, portal adapter, or index as failure of the Authority Resolver if another sufficient official route resolves the proposition;
5. if only non-primary material remains for a material binding proposition, return partial/unresolved authority rather than silently treating the secondary source as controlling.

## Maintenance

This registry routes source discovery and verification. It may be updated when official portals, transport mechanisms, or institutional responsibilities change without changing the BL1–BL8 ownership architecture.
