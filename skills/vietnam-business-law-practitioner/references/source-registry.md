# Authority Source Registry v0.1

This registry gives stable source IDs and fallback roles for runtime authority discovery. It is not a legal database and does not imply that every statement on an official site is binding law.

Use together with `../schemas/authority-resolver.md`, `authority-sources.md`, `source-status.md`, and `search-strategy.md`.

## Registry principles

- Source identity/provenance is separate from legal force.
- Prefer the source that actually publishes the controlling instrument or official record.
- If one official source is unavailable, use another official source where the same instrument/record can be independently verified.
- Practitioner/academic/secondary sources may discover or interpret but do not silently replace primary authority when primary authority is material.
- Record the actual URL/document identity used at runtime; registry IDs are routing aids only.

## General legal instruments

### `VN-VBPL`

Role: national/competent-authority legal-document databases under `vbpl.vn`.

Use for: official text, historical versions, legal-document metadata, consolidation/replacement research where available.

Fallback: `VN-GOV-LAW` or competent ministry/regulator legal-document portal.

### `VN-GOV-LAW`

Role: Government legal-document publication portal under `vanban.chinhphu.vn` / official Government domains.

Use for: promulgated laws/decrees/resolutions/circular metadata and official text where available.

Fallback: `VN-VBPL` or competent issuing authority.

## Corporate / investment

### `VN-BUSINESS-REGISTRY`

Role: National Business Registration Portal / competent business-registration authority (`dangkykinhdoanh.gov.vn` and successor official services).

Use for: business-registration procedures/forms/official registration guidance and current implementing materials.

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

## Registry fallback rule

When a registry source is unavailable:

1. log `SOURCE_UNAVAILABLE` for the attempted source ID;
2. follow the stated official fallback where possible;
3. preserve the source actually used and its provenance/legal force;
4. if only non-primary material remains for a material binding proposition, return partial/unresolved authority rather than silently treating the secondary source as controlling.

## Maintenance

This registry routes source discovery. It may be updated when official portals or institutional responsibilities change without changing the BL1–BL8 ownership architecture.