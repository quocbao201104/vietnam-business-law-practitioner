# Legal Source Retrieval — Adversarial Matrix v0.1

**Fixture freeze date:** 2026-09-13

Purpose: test whether Authority Resolver preserves the distinction between discovery, document identity, lifecycle/currentness, provision resolution, and case applicability.

These tests are not scored by whether the model memorizes the legal answer. They are scored by whether it follows the source-resolution contract and fails closed when proof is insufficient.

## LSR-01 — Clean current instrument

**Setup:** user asks a current business-law proposition where one clearly identified current instrument and provision are sufficient.

**Oracle:** broad discovery is allowed; resolver locks official document identity, resolves current lifecycle, retrieves the exact provision, records freshness, and returns `RESOLVED`.

**Forbidden:** citation decoration without identity/currentness checks.

## LSR-02 — Partially effective base law

**Setup:** candidate base law has document-level partial-effect/amendment state, e.g. Law 59/2020/QH14 at the fixture date.

**Oracle:** resolver does not infer every provision is current from the document-level status; it checks the targeted provision and later-change context.

**Forbidden:** `document exists/current-ish → provision current`.

## LSR-03 — Later amendment discovered after the base instrument

**Setup:** discovery first finds a familiar base instrument, but a later amendment exists, e.g. Law 76/2025/QH15 in the enterprise-law chain.

**Oracle:** freshness/later-change search finds the amendment and updates the minimum sufficient authority set before a current-law answer is finalized.

**Forbidden:** stop after the familiar base law because it still exists.

## LSR-04 — Replacement plus subsequent amendment

**Setup:** a historical implementing decree has been replaced, and the replacement has itself been amended by the fixture date; enterprise-registration chain may be used as the fixture family.

**Oracle:** resolver detects replacement and then checks the replacement for later changes. Historical text remains available only for historical anchors.

**Forbidden:** `replacement found → freshness complete` without checking later change signals.

## LSR-05 — Official consolidation available

**Setup:** a current-law proposition has an appropriate official consolidated text.

**Oracle:** resolver prefers the official consolidated wording when it is current and sufficient, while preserving amendment/provenance context where material.

**Failure:** if the candidate consolidation cannot be proven current/appropriate, return `CONSOLIDATION_UNRESOLVED` rather than silently choosing it.

## LSR-06 — Historical as-of question

**Setup:** user asks what the law provided at a past date before later amendments.

**Oracle:** resolver anchors to the historical date, includes amendments effective by that date, excludes later changes, and checks transition rules where material.

**Forbidden:** quote today's consolidated wording as if it governed the historical event.

## LSR-07 — Search result matches the provision number but the wrong document

**Setup:** generic search such as an Article number + legal phrase returns a different or older instrument before the intended one.

**Oracle:** resolver treats the hit as `DISCOVERED` only, locks document identity first, then retrieves the provision inside that instrument/version.

**Failure:** if identity cannot be locked, return `DOCUMENT_IDENTITY_UNRESOLVED`.

## LSR-08 — Portal/API source-shape drift

**Setup:** an adapter depending on an undocumented endpoint, frontend action, or HTML selector receives an unexpected shape after deployment.

**Oracle:** emit `SOURCE_DRIFT`; do not treat missing expected fields as evidence that no provision/amendment exists; follow an official fallback path.

**Forbidden:** empty payload → `RESOLVED: no amendment`.

## LSR-09 — Secondary index discovers, official source verifies

**Setup:** a reputable secondary legal index quickly surfaces a candidate current instrument/provision.

**Oracle:** use the secondary source for discovery, then verify identity/text/lifecycle against appropriate official authority before resolving a material binding-law proposition.

**Forbidden:** promote the secondary page to controlling authority solely because it is easier to search.

## LSR-10 — Official-source disagreement or index lag

**Setup:** two official portals surface different apparent freshness states or one has not yet surfaced a recent instrument.

**Oracle:** compare instrument identity, legal force, publication/effective dates, source role, and later-change context; use original official publication/issuing authority as needed; preserve `CONFLICTING_AUTHORITY` or unresolved status if material conflict remains.

**Forbidden:** choose the result with more citations or the most convenient portal.

## Minimum trace oracle

A passing instrumented run should make it possible to reconstruct:

```text
AUTHORITY_CALL
→ discovery candidates
→ AUTHORITY_IDENTITY_LOCK
→ lifecycle/currentness resolution
→ provision locator
→ AUTHORITY_RESULT
```

When source drift occurs:

```text
AUTHORITY_SOURCE_DRIFT
→ fallback attempt
→ resolved or typed unresolved result
```

The trace must not make `CURRENT_BINDING` indistinguishable from `APPLICABLE_TO_CASE`.
