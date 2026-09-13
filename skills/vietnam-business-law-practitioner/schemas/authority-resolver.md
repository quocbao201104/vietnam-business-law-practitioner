# Authority Resolver — Service Contract v0.5

This contract defines the callable authority-resolution service used by proposition owners. It does not decide substantive case applicability.

## Request

Each request must identify:

- `request_id`
- `proposition_id`
- accountable BL owner
- exact legal proposition/question to verify
- jurisdiction(s)
- temporal anchor(s)
- required authority class if known
- freshness requirement
- known candidate sources/authorities, if any

The request must be proposition-specific. Do not search for a whole case in one undifferentiated call when different propositions have different temporal anchors or authority needs.

## Materiality gate

Call the resolver when the authority result can change at least one of:

- route or owner activation;
- legal classification;
- proposition result/status;
- proposition dependency;
- authority version/lifecycle applicable to a proposition;
- available option set;
- action readiness;
- required evidence/procedure/deadline.

Do not call merely to decorate an answer with citations.

## Resolution stages

The resolver must not collapse these states:

```text
DISCOVERED
→ IDENTIFIED
→ LIFECYCLE_RESOLVED
→ PROVISION_RESOLVED
```

`APPLICABLE_TO_CASE` remains owned by the accountable BL proposition owner.

### Discovery

Discovery may fan out across official and reputable secondary sources to maximize recall and speed.

A search hit is only a candidate.

### Document identity lock

Before a material provision is relied on, lock the instrument identity using stable attributes where available:

- number/symbol;
- title;
- instrument type;
- issuer;
- promulgation date;
- canonical official record/locator.

Portal/internal IDs may be retained for retrieval but do not replace the legal identity fields.

### Optional machine-readable acceleration

Official machine-readable portal access may be used to accelerate metadata, relationship, lifecycle, or structural lookup after a candidate document/locator is known.

Such transport is optional unless an official stable interface is explicitly required by the proposition. An undocumented endpoint, frontend Server Action, backend UUID route, or catalog is not a hard dependency merely because it is convenient.

If machine-readable access fails, drifts, or appears stale, preserve that source-attempt condition and continue through appropriate official web/publication fallbacks. Absence from a machine-readable catalog is not proof that an instrument or later change does not exist.

### Lifecycle/currentness resolution

Resolve, as material:

- effective-from / effective-to;
- future effect;
- amendment;
- partial effect;
- replacement/repeal;
- suspension/resumption;
- consolidation;
- transition rules;
- historically applicable version for the temporal anchor.

Do not infer provision-level currentness solely from a document-level status when partial effect or amendment is material.

### Provision resolution

Resolve the controlling provision at the narrowest useful legal locator, for example Article/Clause/Point.

Prefer official structural data when available. If structure is deterministically derived, preserve that fact in provenance.

## Result

A resolver result must separate:

### Source provenance

Examples: official legal database, competent regulator, court/judiciary, treaty repository, official guidance, practitioner/academic/secondary source.

### Legal force / authority type

Examples: legislation/regulation, treaty, binding judicial authority where applicable, official interpretive/administrative guidance, non-binding practice material, secondary research.

### Document identity

Record stable identity fields actually verified, plus any retrieval locator used. Do not treat a backend ID alone as sufficient legal identity.

### Provision locator

When the proposition depends on a specific provision, record the resolved Article/Clause/Point or equivalent locator and whether the structure is official or derived.

### Lifecycle

Use as applicable:

- `DRAFT`
- `FUTURE_EFFECTIVE`
- `CURRENT_BINDING`
- `HISTORICAL`
- `AMENDED`
- `PARTIALLY_EFFECTIVE`
- `SUPERSEDED`
- `SUSPENDED`
- `UNCERTAIN`

### Temporal scope

Record the anchor(s) against which the result was resolved, such as formation, closing, performance, breach, notice, tax event, customs entry, or planned action date.

### Freshness

Record:

- `verified_at`
- `source_version` or amendment/consolidation context where material
- `fresh_until` or a semantic freshness requirement when determinable
- authority-change signals, if any

### Resolution status

Use one of:

- `RESOLVED`
- `PARTIALLY_RESOLVED`
- `CONFLICTING_AUTHORITY`
- `SOURCE_UNAVAILABLE`
- `SOURCE_DRIFT`
- `DOCUMENT_IDENTITY_UNRESOLVED`
- `CURRENTNESS_UNRESOLVED`
- `PROVISION_UNRESOLVED`
- `CONSOLIDATION_UNRESOLVED`
- `INSUFFICIENT_AUTHORITY`
- `TEMPORAL_SCOPE_UNRESOLVED`

`SOURCE_UNAVAILABLE` and `SOURCE_DRIFT` may describe a failed source/adapter attempt in the trace. They do not force the final proposition-level resolver status to remain unresolved if an official fallback establishes a sufficient authority result. For example, a VBPL backend adapter may emit `SOURCE_DRIFT` while the final resolver result is `RESOLVED` from an official Government publication plus the controlling text.

### Source set

Return the **minimum sufficient authority set**, not a citation quota. A proposition may require one controlling instrument or a coordinated set such as base law + amendment + implementing instrument + transition rule.

## Applicability boundary

The resolver may report lifecycle, scope text, transition text, source context, document identity, and provision locator. It does **not** decide `APPLICABLE_TO_CASE` as a substantive legal conclusion.

The accountable BL proposition owner must decide case applicability and record that decision separately.

`CURRENT_BINDING` therefore never means `APPLICABLE_TO_CASE` by itself.

## Failure and fallback behavior

### Official source unavailable

If the preferred official source cannot be accessed:

1. record `SOURCE_UNAVAILABLE` for that source ID/attempt;
2. follow the official fallback route in `../references/source-registry.md` where possible;
3. continue resolution if another sufficient official source can establish the needed authority;
4. if only secondary material is available, use it only as a discovery/interpretive lead and mark the proposition unresolved or conditional if primary authority is material;
5. do not silently downgrade the authority requirement.

### Source drift

If an undocumented endpoint, frontend action, HTML layout, or expected payload changes shape:

1. record `SOURCE_DRIFT` for that adapter/source attempt;
2. do not reinterpret the unexpected response as an empty legal result;
3. use an official fallback route where possible;
4. continue resolution if fallback authority is sufficient;
5. return final `SOURCE_DRIFT`/unresolved authority only when the drift prevents the proposition from being resolved to the required level after fallback attempts;
6. require re-resolution before a dependent material proposition can be `READY` only when the final authority result remains insufficient/stale.

### Source/index lag

If a machine-readable catalog, portal index, or cached corpus lacks a recent instrument/change that is found on another official source:

1. preserve the lag signal in provenance/trace;
2. do not treat catalog absence as negative legal evidence;
3. verify the newer instrument/change against the best available official publication/source;
4. use the proposition-level result established by sufficient authority rather than forcing the lagging source to agree.

### Document identity unresolved

If a candidate instrument cannot be reliably matched to an official record, return `DOCUMENT_IDENTITY_UNRESOLVED`. Do not retrieve a same-numbered/similarly titled provision from another document and continue silently.

### Currentness unresolved

If amendment, replacement, partial effect, consolidation, or temporal applicability cannot be resolved to the level needed by the proposition, return `CURRENTNESS_UNRESOLVED` or `TEMPORAL_SCOPE_UNRESOLVED` rather than assuming the discovered text is current.

### Provision unresolved

If the correct instrument/version is known but the exact controlling provision cannot be reliably located, return `PROVISION_UNRESOLVED` and identify what is missing.

### Conflicting authority

If authoritative sources conflict:

1. preserve both sources;
2. compare legal force, identity, scope, temporal status, amendment/replacement, and transition rules;
3. return `CONFLICTING_AUTHORITY` if the conflict remains material;
4. the owner may not force `READY` for an affected action merely by choosing the more convenient source.

### Partial resolution

If only part of a proposition is resolved, return `PARTIALLY_RESOLVED` and identify the unresolved sub-proposition or missing temporal/factual input.

### Freshness failure

If a material action depends on an authority result whose freshness requirement is no longer satisfied, the dependent proposition becomes review-required/stale until re-resolution and owner review occur.

## Source routing

Use:

- `../references/source-registry.md` for stable source IDs and fallback routes;
- `../references/authority-sources.md` for source-family/authority guidance;
- `../references/source-status.md` for source/force/lifecycle distinctions;
- `../references/search-strategy.md` for proposition-specific search procedure.

The source-routing files are not themselves authority.

## Trace events

An instrumented runtime should emit:

- `AUTHORITY_CALL`
- `AUTHORITY_RESULT`
- `AUTHORITY_RERESOLVE`
- `AUTHORITY_CHANGE_SIGNAL`
- `AUTHORITY_IDENTITY_LOCK`
- `AUTHORITY_SOURCE_DRIFT`

with `proposition_id`, owner, temporal anchors, resolution status, source IDs/authority IDs, resolved document identity, provision locator, and freshness data where material.

When one source/adapter attempt fails but fallback resolution succeeds, the trace should preserve both facts rather than collapsing them, for example:

```text
AUTHORITY_SOURCE_DRIFT source=VN-VBPL transport=machine-readable
→ official fallback
→ AUTHORITY_RESULT status=RESOLVED
```
