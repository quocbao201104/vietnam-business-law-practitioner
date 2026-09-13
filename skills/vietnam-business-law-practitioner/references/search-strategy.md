# Search Strategy v0.4

Search is a designed runtime dependency for volatile legal authority. The Authority Resolver is a **callable service**, not a fixed pipeline stage.

Any accountable BL owner may call it while resolving a proposition. Composition may request re-resolution when temporal anchors, authority freshness, or downstream reclassification changes.

## Core resolution invariant

Keep these states separate:

```text
DISCOVERED
!= IDENTIFIED
!= CURRENT
!= APPLICABLE_TO_CASE
!= INTERPRETED
```

A search hit is a discovery lead, not proof of document identity, lifecycle, provision currentness, or case applicability.

## Search when the proposition is materially time-sensitive or action-facing

Typical triggers:

- current rights or obligations;
- validity/enforceability;
- rates, thresholds, deadlines, fines, forms, filing mechanics;
- licensing or market-entry requirements;
- tax treatment;
- current procedure;
- historical transactions governed by prior law;
- foreign/treaty applicability;
- conflicting authority;
- recently changing regulation;
- material irreversible/current actions whose prior authority check may be stale.

## Authority request

Define:

- exact proposition requiring verification;
- accountable BL owner;
- jurisdiction;
- required authority/legal-force type;
- **temporal anchor(s)** relevant to that proposition;
- freshness requirement appropriate to the action.

Do not assume one universal relevant date for the whole case.

Possible temporal anchors include formation, closing, performance, breach, notice, tax event, customs entry, and planned action date.

## Discovery may be broad; legal verification must converge

Discovery may use multiple source families when that improves recall or speed, including web search, official portals, specialist regulator portals, and reputable secondary legal indexes.

Do not force every discovery step through one portal.

For a material binding-law assertion, however, converge on appropriate official authority before treating the proposition as resolved. Secondary indexes may identify likely instruments or provisions but must not silently become the controlling source when primary authority is available and material.

For recently changing, conflicting, or high-consequence rules, fan out across appropriate official sources when useful to detect a later amendment, replacement, transition rule, or source-index lag. Source count does not determine legal force.

## Machine-readable official access is an accelerator, not a dependency

When an official portal exposes machine-readable data and the document identity/locator is sufficiently resolved, the resolver may use it to accelerate metadata, relationship, lifecycle, or structural lookup.

For VBPL, research has observed publicly reachable frontend/backend transport such as a document-detail route shaped like:

`https://vbpl-bientap-gateway.moj.gov.vn/api/qtdc/public/doc/{id}`

Treat such routes as implementation transports unless an official stable developer contract says otherwise.

Machine-readable access must not become a hard dependency:

```text
machine-readable lookup succeeds
→ use it when useful
→ cross-check material identity/currentness against official authority as needed

machine-readable lookup fails / lags / changes shape
→ record the source-attempt condition
→ continue with official webpages, original attachments, Government portal, or competent authority
→ do not block legal resolution merely because that adapter failed
```

A machine-readable catalog or dataset may lag newly promulgated instruments. Absence from that catalog is not proof that an instrument, amendment, or relationship does not exist.

## Search sequence

1. Define the exact proposition requiring verification.
2. Identify its temporal anchor(s).
3. Identify jurisdiction and likely authority/legal-force type.
4. Discover candidate instruments broadly enough to avoid single-index blind spots.
5. **Lock document identity** before relying on a provision: verify, as available, number, title, instrument type, issuer, promulgation date, and canonical official record/identifier.
6. If useful and reachable, use official machine-readable access to accelerate metadata/relationship/structure lookup; treat the transport as optional and cross-check stable legal identity.
7. Acquire the controlling text from an appropriate official source or official fallback.
8. Check lifecycle/currentness: effective date, amendment, partial effect, replacement, suspension, repeal, consolidation, future effect, and transition rules. Actively look for later changes rather than stopping at the first still-existing instrument.
9. For current-law questions, prefer an appropriate official current consolidated text where it actually resolves the wording needed; do not reconstruct consolidated wording when an official consolidation is available and sufficient.
10. For historical questions, resolve the wording and authority set **as of the proposition's temporal anchor**, not by reading today's consolidated text backward.
11. Resolve the exact provision after document identity/currentness are sufficiently controlled: Chapter/Article/Clause/Point where material.
12. Read the controlling passage in context and preserve the provenance of both document identity and provision text.
13. Record `verified_at`, source/version context, and freshness requirement.
14. Return the authority result to the accountable owner.
15. The owner decides **case applicability**; the resolver does not silently promote `CURRENT_BINDING` to `APPLICABLE_TO_CASE`.
16. Reuse the resolved authority across tracks when the proposition, temporal anchor, document/version identity, and freshness remain valid.

## Document identity before provision retrieval

Do not search a generic phrase such as `Điều 12 người đại diện` and treat the first matching page as the controlling provision.

Resolve the instrument first, then retrieve the provision inside that instrument/version.

An internal portal ID, `ItemID`, UUID, search-session token, or backend identifier is an implementation locator, not legal identity by itself. If one is used, cross-check the returned official record against stable instrument attributes such as number/title/issuer/date before locking identity.

A discovery query disappearing from the destination URL is not a legal problem if the destination instrument identity is independently resolved.

## Provision structure

Prefer official structural data for Article/Clause/Point boundaries when available and trustworthy.

If deterministic parsing is required as a fallback, mark the structure as derived rather than silently treating regex/chunk boundaries as official legal structure.

Do not use arbitrary vector chunks as legal citation identity when a provision-level locator is available or can be deterministically resolved.

## Source-shape drift and source-attempt failure

Undocumented portal endpoints, frontend Server Actions, HTML layouts, and backend payloads may change. Official indexes may also lag recently promulgated material.

If an adapter expects a field/shape and the source no longer matches it:

```text
unexpected source shape
→ record SOURCE_DRIFT for that source attempt
→ do not infer an empty legal result
→ continue through an appropriate official fallback
```

If a source is unreachable:

```text
source unavailable
→ record SOURCE_UNAVAILABLE for that source attempt
→ continue through an appropriate official fallback
```

`SOURCE_DRIFT` or `SOURCE_UNAVAILABLE` at one adapter/source attempt does **not** automatically mean the Authority Resolver failed. If another sufficient official route establishes identity, lifecycle, currentness, and the controlling provision, the final proposition-level authority result may still be `RESOLVED`.

Do **not** reinterpret a changed/missing payload, stale catalog, or failed API request as proof that no amendment, replacement, provision, or instrument exists.

## Four dimensions of authority

Keep these separate:

1. **Source provenance** — where the material came from.
2. **Authority/legal force** — statute, regulation, treaty, judicial authority, official guidance, practice, secondary material.
3. **Lifecycle/temporal status** — future-effective, current, historical, superseded, suspended, etc.
4. **Case applicability** — whether the accountable owner concludes that authority governs the specific proposition/facts/date.

Official hosting does not by itself make every statement binding law.

## Temporal checks

Do not equate publication/promulgation with effectiveness.

Distinguish at least:

- draft/consultation;
- promulgated but future-effective;
- currently binding;
- historical version;
- amended;
- partially effective;
- superseded/repealed;
- suspended;
- uncertain/transitioning.

A document-level status does not prove that every provision has the same lifecycle state. A current law may still be inapplicable to a pre-effective transaction because of a transition rule. A past law may still govern a historical proposition.

## Authority freshness

An authority result is not permanently fresh merely because it was correct when retrieved.

For material irreversible/current actions, re-resolve authority when:

- its freshness requirement has expired;
- a known authority-change signal exists;
- a relevant effective date has passed;
- the temporal anchor changed;
- a reclassification changes the proposition being supported;
- the applicable regime becomes uncertain;
- a later amendment/replacement/consolidation candidate is discovered.

Cached authority cannot support `READY` when freshness is unsatisfied.

## Historical questions

For a past transaction/event, search for the law applicable to each material event date rather than simply using the current consolidated text.

Check transition provisions when a relationship spans multiple legal regimes.

## Search terms

Search by legal proposition and transaction facts, not only by the user's noun label.

Bad: `freelancer tax Vietnam`

Better: resolve employment-vs-service classification through BL6, then verify tax/social-insurance consequences for the owned classification and relevant tax period.

Bad: `FTA Korea 0%`

Better: identify product classification/origin issue, relevant FTA, current tariff year, origin requirement, and import date.

## Conflicting sources

When sources conflict:

1. compare legal force;
2. compare document identity;
3. compare lifecycle/effective period;
4. compare scope and case applicability;
5. check amendment/replacement/transition context;
6. preserve ambiguity if conflict remains material.

Do not resolve conflict by citation count.

## Minimum sufficient authority set

Prefer the **minimum sufficient authority set** over decorative citation count.

A proposition may require one controlling instrument, or a set such as:

- base law;
- amending law;
- implementing decree;
- transition rule;
- authoritative interpretation where material.

`One source` is not a goal when the legal rule only exists correctly as a coordinated authority set.

## Search stop condition

Stop when the accountable owner has enough fresh, identified, provision-specific, applicable authority to support the material proposition at the level needed for the action.

Do not continue collecting sources merely to make the answer look researched.
