# Vietnam Legal Source Retrieval — Research Freeze v0.1

**Status:** runtime/retrieval architecture research freeze candidate

**Scope:** how the practitioner discovers, identifies, verifies, and retrieves Vietnamese legal authority. This artifact does not change BL1–BL8 substantive ownership and does not replace practitioner knowledge.

## Research question

How should an agent retrieve current or historically applicable Vietnamese legal authority without turning search hits, secondary indexes, portal implementation details, or stale cached text into silent legal conclusions?

## Findings

### 1. Stable reasoning should remain in-repo; volatile law should be resolved at runtime

The practitioner handbook should own distinctions, issue routing, legal decision procedure, and composition boundaries. Time-sensitive statutory text, effective status, amendments, replacements, transition rules, and official consolidations should be verified against current authority when material.

### 2. Discovery and verification have different source requirements

Discovery benefits from broad recall and may use web search, official portals, specialist regulator portals, and reputable secondary legal indexes.

Material binding-law assertions should converge on appropriate official authority before resolution.

```text
DISCOVERY = permissive
VERIFICATION = source-aware and strict
```

### 3. Search hit is not legal identity

A result matching a provision number or phrase may belong to the wrong instrument or historical version.

Lock the document first using stable attributes such as number, title, issuer, type, date, and an official record/locator. Only then resolve the exact provision.

```text
DISCOVERED != IDENTIFIED != CURRENT != APPLICABLE_TO_CASE
```

### 4. Official sources may need fan-out

A single official search index can lag or surface poorly. Recent or high-consequence changes may require cross-checking VBPL, Government publication, a competent regulator portal, or an original official attachment.

This is not a citation-count rule. Legal force and lifecycle still control.

### 5. VBPL portal mechanics are useful but not a stable contract

Research inputs show that current VBPL frontend/backend flows expose machine-readable document metadata/relationships and provision outline data. Some routes are publicly reachable but undocumented; frontend Server Action identifiers and payload shapes may change after deployment.

Therefore:

```text
unexpected adapter/source shape
→ SOURCE_DRIFT
→ fail closed / official fallback
```

Do not interpret a changed response as proof that a provision or amendment does not exist.

### 6. Document graph and provision structure are distinct

Official systems can expose document-level relations such as amendment, replacement, repeal, consolidation, or implementing relationships while provision-level amendment/citation edges remain incomplete.

The runtime may use official document relations for candidate traversal, but must not invent clause-level amendment provenance without resolving it.

### 7. Document status is not sufficient for provision currentness

`CURRENT` or `partially effective` at document level does not prove the lifecycle of every provision. Provision-level currentness may depend on amendment, suspension, delayed commencement, transition rules, or official consolidation.

### 8. Prefer official consolidation when it actually answers the current-law wording question

For current-law questions, use an appropriate official current consolidated text when available and sufficient rather than reconstructing wording unnecessarily from multiple amendments.

Historical/as-of questions still require temporal resolution to the relevant event date.

### 9. Legal structure should be provision-addressable

Prefer stable legal locators:

```text
Document → Article → Clause → Point
```

over arbitrary vector chunks.

If structure must be parsed deterministically, mark it as derived.

## Runtime contract

```text
PROPOSITION + TEMPORAL ANCHOR
        ↓
BROAD DISCOVERY
        ↓
DOCUMENT IDENTITY LOCK
        ↓
OFFICIAL SOURCE ACQUISITION
        ↓
LIFECYCLE / LATER-CHANGE CHECK
        ↓
CONSOLIDATION / AS-OF RESOLUTION
        ↓
EXACT PROVISION RESOLUTION
        ↓
AUTHORITY RESULT
        ↓
ACCOUNTABLE BL OWNER DECIDES APPLICABILITY
```

## Failure states required by the research

- `SOURCE_UNAVAILABLE`
- `SOURCE_DRIFT`
- `DOCUMENT_IDENTITY_UNRESOLVED`
- `CURRENTNESS_UNRESOLVED`
- `PROVISION_UNRESOLVED`
- `CONSOLIDATION_UNRESOLVED`
- `TEMPORAL_SCOPE_UNRESOLVED`
- `CONFLICTING_AUTHORITY`

These are preferable to silent best-effort promotion.

## Implementation boundary

The first runtime implementation should remain thin.

It does **not** require:

- a full-corpus crawler;
- a vector database;
- a graph database;
- model fine-tuning;
- a permanent dependency on an undocumented VBPL endpoint.

A later adapter may opportunistically use official machine-readable endpoints or cached metadata for speed, but must preserve identity cross-checks, source-shape checks, official fallbacks, and freshness semantics.

## Research inputs

Architecture was pressure-tested against public legal-tech/retrieval work including:

- `th1nhng0/vietnamese-legal-documents` — current VBPL metadata/content/relationship crawling and ID handling;
- `tamnd/luatdo` — structural identities, temporal versions, provenance, amendment/citation graph concepts;
- `ngocnhat2k1/Legal-AI-Knowledge-System` — VBPL provision-tree and source-shape experiments;
- `saladnga/ISODS-PhapDien-Crawler-Semantic-Search` — older VBPL `ItemID` multi-surface crawling pattern.

These systems are research inputs, not authority and not architectural sources of truth.

## Rejected shortcuts

- first search hit = controlling law;
- one legal portal = universal discovery index;
- backend ID alone = document identity;
- document `current` status = every provision current;
- semantic similarity = legal applicability;
- cached file exists = still current;
- secondary legal index = final authority for a material binding proposition;
- unexpected API payload = no result.
