# BL1 — Authority Applicability

## Owns

Framing authority-status/applicability problems that materially affect BL1 issue framing or routing, distinguishing source status from legal force and lifecycle, and identifying when a proposition owner must resolve live authority before the route or action-facing conclusion can be trusted.

BL1 may classify an **authority problem** and route it. It does not become owner of the substantive legal proposition merely because it finds or reads the source.

## Does not own

- routine current-law verification for a narrow proposition whose accountable owner is already clear;
- final case applicability of corporate, contract, remedy, tax, employment, regulatory, or cross-border authority;
- choosing a business-friendly interpretation between conflicting substantive owner conclusions;
- promoting official guidance into binding law;
- treating official source provenance as proof of legal force.

## Activate when

Load this BL1 unit only when the **authority problem itself changes or may change framing/routing**, for example when:

- source provenance versus legal force must be distinguished before selecting the correct route/owner;
- lifecycle, amendment, suspension, replacement, transition, or temporal status makes the route unclear;
- conflicting authority or unresolved final authority support prevents BL1 from trusting the current route hypothesis;
- several authority types/instruments must be distinguished to know which owner or regime must be activated;
- authority freshness/status creates a meta-level routing problem rather than merely an owner-specific verification task.

A single unavailable/drifting/lagging source attempt does **not** by itself activate or keep BL1 unresolved if the Authority Resolver reaches a sufficient final result through fallback.

Do **not** load this unit merely because a downstream legal proposition depends on current or historical law.

For a narrow owner-specific proposition, the accountable BL owner should call Authority Resolver directly:

```text
BL5 proposition
→ BL5 calls Authority Resolver
→ BL5 decides case applicability
```

not:

```text
BL1
→ authority-applicability
→ Authority Resolver
→ BL5
```

unless the authority-status problem is itself material to BL1 framing/routing.

## Required state

When this unit is activated, capture:

- exact framing/routing question affected by authority status;
- candidate accountable BL owner(s);
- jurisdiction(s);
- temporal anchor(s);
- materiality reason;
- known candidate sources if any;
- action(s) whose route/readiness may be affected;
- required freshness or urgency.

## Core distinctions

### Source provenance ≠ legal force

A source hosted by a government body may contain legislation, guidance, Q&A, announcement, administrative practice, or explanatory material. Identify what the source legally is.

### Source-attempt status ≠ resolver outcome

Individual retrieval attempts may have:

- `SUCCEEDED`
- `SOURCE_UNAVAILABLE`
- `SOURCE_DRIFT`
- `SOURCE_LAGGING`

These are `source_attempt.attempt_status` values only.

A failed/lagging adapter may coexist with a final resolver `RESOLVED` result when another sufficient official route succeeds.

Do not promote an attempt-local state such as `SOURCE_UNAVAILABLE` into the proposition-level resolver outcome.

### Legal force ≠ lifecycle

A binding instrument can be future-effective, historical, amended, superseded, suspended, or uncertain for the relevant period.

### Lifecycle ≠ case applicability

`CURRENT_BINDING` means the authority currently has binding status within its scope. It does not automatically mean it governs the facts or temporal anchor of the proposition.

### Official guidance ≠ legislation

Official guidance can be highly relevant to interpretation or administrative practice without having the same force as legislation.

### Secondary material ≠ final authority

Practitioner, academic, database, repository, or AI material may discover, explain, or challenge a proposition. It must not silently substitute for material primary authority when primary authority is available/required.

### One source ≠ sufficient authority set in every case

Some propositions are controlled by one instrument. Others require coordinated reading of base law, amendment, implementing instrument, transition provision, treaty, or authoritative interpretation.

## Decision procedure

1. **Confirm BL1 activation is justified.** Ask whether authority status/lifecycle can change framing, route, owner, or another BL1-owned meta proposition. If not, skip this unit and let the accountable owner call Authority Resolver directly.
2. **Define the authority-status question.** Do not search a whole case as one undifferentiated query.
3. **Identify candidate owner(s).** Authority resolution supports proposition ownership; it does not replace it.
4. **Bind temporal anchors.** Ask what authority status matters at the relevant event/action date(s).
5. **Identify required authority class.** Determine whether routing depends on binding law, treaty, judicial authority, regulator guidance, or explanatory material.
6. **Call Authority Resolver when the BL1 meta question is material.** Use `../../schemas/authority-resolver.md`.
7. **Separate result dimensions.** Preserve source-attempt status separately from source provenance, legal force, lifecycle, temporal scope, freshness, source version/amendment context, and final `resolution_status`.
8. **Return route-relevant status to BL1 and substantive authority result to the owner.** The owner decides `APPLICABLE_TO_CASE` or records uncertainty.
9. **Use minimum sufficient authority set.** Stop when the framing/routing question is adequately supported; do not collect decorative citations.
10. **Re-resolve when necessary.** Authority changes, stale freshness, changed temporal anchors, or reclassification can reopen a previously settled route.

## Authority resolution states

The final resolver `resolution_status` uses the canonical proposition-level outcomes from `../../schemas/authority-resolver.md`:

- `RESOLVED`
- `PARTIALLY_RESOLVED`
- `CONFLICTING_AUTHORITY`
- `DOCUMENT_IDENTITY_UNRESOLVED`
- `CURRENTNESS_UNRESOLVED`
- `PROVISION_UNRESOLVED`
- `CONSOLIDATION_UNRESOLVED`
- `INSUFFICIENT_AUTHORITY`
- `TEMPORAL_SCOPE_UNRESOLVED`

Do not place `SOURCE_UNAVAILABLE`, `SOURCE_DRIFT`, or `SOURCE_LAGGING` in this final-result layer; those describe individual source attempts.

Do not coerce unresolved authority into a binary route or legal conclusion.

## Source routing discipline

Prefer the strongest appropriate source for the authority-status question, typically:

1. competent primary/official legal authority;
2. official regulator/judiciary/treaty material appropriate to the issue;
3. official guidance/practice material where interpretation/administration matters;
4. practitioner/academic/secondary material for discovery, explanation, challenge, or unresolved interpretation.

Use `../../references/authority-sources.md` and `../../references/source-registry.md` for source routing. These files are routing infrastructure, not legal authority themselves.

## Applicability questions for the owner

After authority resolution, the substantive owner should ask:

- Is the actor/activity/object within the authority's scope?
- Does a special rule displace a general rule?
- Does the relevant temporal anchor fall within the authority's effective/transition period?
- Is a factual classification prerequisite resolved?
- Is there an exception, exclusion, condition, or implementing rule?
- Does another mandatory regime constrain the result?
- Is the authority sufficient alone or only as part of a coordinated set?

BL1 may surface these questions only when they affect framing/routing. It must not answer owner-specific propositions.

## Freshness and action-facing burden

Freshness normally belongs inside the accountable owner's authority call. BL1 should reason about freshness only when freshness itself changes route or framing.

Re-resolution may be route-relevant when:

- an authority-change signal exists;
- the source version may have changed;
- the action date moved across a legal transition;
- a material classification changed the candidate regime;
- a transition provision opens/closes a route;
- a previously rejected route may need explicit reopening.

A stale authority result cannot support `READY`; but BL1 does not become the readiness owner by detecting that issue.

## Conflicting authority

When material sources conflict at the routing level:

1. preserve both;
2. compare legal force;
3. compare scope;
4. compare temporal status;
5. check amendment/replacement/transition context;
6. distinguish source text from interpretation;
7. return `CONFLICTING_AUTHORITY` if conflict remains material;
8. keep the substantive proposition with its accountable owner.

Do not resolve conflict by source count or convenience.

## Evidence requirements

Record enough provenance to reconstruct why the authority affected routing:

- source identity and link/reference;
- source-attempt status where material;
- authority type/legal force;
- relevant passage;
- lifecycle/effective period;
- verified time;
- source version/amendment context when material;
- framing/route question and temporal anchor supported.

## Cross-track handoffs

A BL1 authority handoff should contain only route-relevant authority state:

- proposition/question;
- candidate accountable owner;
- authority requirement;
- temporal anchor(s);
- final authority resolution status;
- material source-attempt condition where relevant;
- unresolved authority issue;
- freshness requirement where it affects routing;
- affected action(s).

The accountable owner then calls or consumes Authority Resolver as needed and records substantive case applicability.

## Failure modes

- loading this unit for every action-facing legal proposition;
- turning BL1 into an authority gateway;
- `official website = binding law`;
- `current law = applicable law`;
- `one recent article = authority`;
- decorative citation accumulation;
- secondary source silently replacing primary authority;
- resolver deciding substantive case applicability;
- searching after a conclusion only to confirm memory;
- treating one `SOURCE_UNAVAILABLE` / `SOURCE_DRIFT` / `SOURCE_LAGGING` attempt as the final resolver outcome;
- ignoring final authority conflict/partial resolution;
- letting BL1 become a hidden substantive owner because it found the source.

## Escalation

Escalate BL1 authority framing only when authority uncertainty can change routing/ownership or prevents a material action from reaching the correct substantive owner. Owner-specific legal uncertainty should escalate within the accountable BL track.
