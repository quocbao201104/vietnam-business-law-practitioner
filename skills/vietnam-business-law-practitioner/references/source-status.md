# Source / Authority Status v0.4

Use four separate dimensions to prevent authority inflation and temporal drift.

## 1. Source provenance

Where did the material come from?

Examples:

- official legislation database;
- government/ministry/regulator site;
- court/judiciary source;
- treaty/official trade repository;
- business association;
- academic publication;
- law firm / secondary legal database;
- repository / skill / AI output.

Provenance describes origin. It does not by itself determine legal force.

## 2. Authority / legal force

Classify the legal character of the material, for example:

- statute / ordinance / regulation / implementing instrument;
- treaty / international commitment;
- authoritative judicial instrument / binding precedent where applicable;
- official administrative guidance;
- ordinary court/arbitral/practice material;
- academic / practitioner interpretation;
- research-only lead.

An official webpage may host both binding instruments and non-binding explanations. Do not conflate hosting source with legal force.

## 3. Lifecycle / temporal status

Recommended labels:

- `CURRENT_BINDING`
- `FUTURE_EFFECTIVE`
- `HISTORICAL`
- `AMENDED`
- `PARTIALLY_EFFECTIVE`
- `SUPERSEDED`
- `SUSPENDED`
- `UNCERTAIN`

`PARTIALLY_EFFECTIVE` means document-level effect is mixed or some provisions have been amended/repealed/superseded while others remain operative. It requires proposition/provision-level resolution rather than treating the entire instrument as uniformly current or historical.

Lifecycle describes the instrument/version at the relevant time. It does not prove the instrument applies to the specific case.

## 4. Case applicability

Applicability is decided by the accountable proposition owner, not automatically by the resolver.

Canonical runtime states:

- `APPLICABLE_TO_CASE`
- `NOT_APPLICABLE_TO_CASE`
- `APPLICABILITY_CONDITIONAL`
- `APPLICABILITY_UNRESOLVED`

These are the state values used by `../schemas/legal-work-state.md` and `../schemas/runtime-trace.md`. Human-facing prose may say "applies", "applies if condition C is satisfied", or "does not apply", but those phrases are aliases only and must not introduce a second machine/runtime vocabulary.

A currently effective rule may be inapplicable because of scope, transaction classification, treaty interaction, or transition provisions. A historical rule may remain the governing rule for a past event.

## Freshness metadata

Material authority results should preserve:

- `authority_id` or `authority_result_id` as appropriate;
- `verified_at`;
- temporal anchor(s);
- effective period;
- source version/amendment context;
- freshness requirement where material.

Before a material irreversible/current action, stale authority must be re-resolved when freshness could affect readiness.

## Secondary/research material

Academic work, VCCI/business-association materials, law-firm analysis, legal databases, repositories, skills, and AI outputs may discover, explain, or challenge propositions. They must not silently become binding authority.

## Core invariant

```text
source provenance
≠ legal force
≠ lifecycle status
≠ case applicability
```
