# Authority Resolver — Service Contract v0.3

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

## Result

A resolver result must separate:

### Source provenance

Examples: official legal database, competent regulator, court/judiciary, treaty repository, official guidance, practitioner/academic/secondary source.

### Legal force / authority type

Examples: legislation/regulation, treaty, binding judicial authority where applicable, official interpretive/administrative guidance, non-binding practice material, secondary research.

### Lifecycle

Use as applicable:

- `DRAFT`
- `FUTURE_EFFECTIVE`
- `CURRENT_BINDING`
- `HISTORICAL`
- `AMENDED`
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
- `INSUFFICIENT_AUTHORITY`
- `TEMPORAL_SCOPE_UNRESOLVED`

### Source set

Return the **minimum sufficient authority set**, not a citation quota. A proposition may require one controlling instrument or a coordinated set such as base law + amendment + implementing instrument + transition rule.

## Applicability boundary

The resolver may report lifecycle, scope text, transition text, and source context. It does **not** decide `APPLICABLE_TO_CASE` as a substantive legal conclusion.

The accountable BL proposition owner must decide case applicability and record that decision separately.

`CURRENT_BINDING` therefore never means `APPLICABLE_TO_CASE` by itself.

## Failure and fallback behavior

### Official source unavailable

If the preferred official source cannot be accessed:

1. record `SOURCE_UNAVAILABLE` for that source ID;
2. follow the official fallback route in `../references/source-registry.md` where possible;
3. if only secondary material is available, use it only as a discovery/interpretive lead and mark the proposition unresolved or conditional if primary authority is material;
4. do not silently downgrade the authority requirement.

### Conflicting authority

If authoritative sources conflict:

1. preserve both sources;
2. compare legal force, scope, temporal status, amendment/replacement, and transition rules;
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

with `proposition_id`, owner, temporal anchors, resolution status, source IDs/authority IDs, and freshness data where material.