# BL1 — Authority Applicability

## Owns

Framing authority questions, distinguishing source status from legal force and lifecycle, and identifying when proposition owners must resolve live authority before an action-facing conclusion can be trusted.

BL1 may classify an authority problem and route it. It does not become owner of the substantive legal proposition merely because it finds or reads the source.

## Does not own

- final case applicability of corporate, contract, remedy, tax, employment, regulatory, or cross-border authority;
- choosing a business-friendly interpretation between conflicting substantive owner conclusions;
- promoting official guidance into binding law;
- treating official source provenance as proof of legal force.

## Activate when

Use when:

- a material proposition depends on current/historical legal authority;
- source status or legal force is unclear;
- an official page, guidance, circular, decree, statute, treaty, precedent, or secondary source may be misunderstood;
- several instruments must be read together;
- authority may be amended, suspended, replaced, or transition-sensitive;
- a proposition is action-facing and stale authority would change readiness;
- sources conflict or primary authority is unavailable.

## Required state

- exact proposition/question;
- accountable BL owner;
- jurisdiction(s);
- temporal anchor(s);
- materiality reason;
- known candidate sources if any;
- action(s) depending on the proposition;
- required freshness or urgency.

## Core distinctions

### Source provenance ≠ legal force

A source hosted by a government body may contain legislation, guidance, Q&A, announcement, administrative practice, or explanatory material. Identify what the source legally is.

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

1. **Define the proposition before searching.** Do not search a whole case as one undifferentiated query.
2. **Identify the owner.** Authority resolution supports the proposition owner; it does not replace ownership.
3. **Bind temporal anchors.** Ask what authority status matters at the relevant event/action date(s).
4. **Identify required authority class.** Determine whether the proposition requires binding law, treaty, judicial authority, regulator guidance, or only explanatory material.
5. **Call Authority Resolver when material.** Use `../../schemas/authority-resolver.md`.
6. **Separate result dimensions.** Preserve source provenance, legal force, lifecycle, temporal scope, freshness, source version/amendment context, and resolution status.
7. **Return the result to the owner.** The owner decides `APPLICABLE_TO_CASE` or records uncertainty.
8. **Use minimum sufficient authority set.** Stop when the proposition is adequately supported; do not collect decorative citations.
9. **Re-resolve when necessary.** Authority changes, stale freshness, changed temporal anchors, or reclassification can invalidate an earlier authority result.
10. **Propagate only exact dependencies.** If authority supporting one proposition becomes stale, mark that proposition/dependent actions for review rather than invalidating unrelated state.

## Authority resolution states

The resolver may return states such as:

- `RESOLVED`
- `PARTIALLY_RESOLVED`
- `CONFLICTING_AUTHORITY`
- `SOURCE_UNAVAILABLE`
- `INSUFFICIENT_AUTHORITY`
- `TEMPORAL_SCOPE_UNRESOLVED`

Do not coerce unresolved authority into a binary legal conclusion.

## Source routing discipline

Prefer the strongest appropriate source for the proposition, typically:

1. competent primary/official legal authority;
2. official regulator/judiciary/treaty material appropriate to the issue;
3. official guidance/practice material where interpretation/administration matters;
4. practitioner/academic/secondary material for discovery, explanation, challenge, or unresolved interpretation.

Use `../../references/authority-sources.md` and `../../references/source-registry.md` for source routing. These files are routing infrastructure, not legal authority themselves.

## Applicability questions for the owner

After authority resolution, the owner should ask:

- Is the actor/activity/object within the authority's scope?
- Does a special rule displace a general rule?
- Does the relevant temporal anchor fall within the authority's effective/transition period?
- Is a factual classification prerequisite resolved?
- Is there an exception, exclusion, condition, or implementing rule?
- Does another mandatory regime constrain the result?
- Is the authority sufficient alone or only as part of a coordinated set?

BL1 may surface these questions but must not answer owner-specific propositions.

## Freshness and action-facing burden

The closer a conclusion is to an irreversible or current business action, the stronger the freshness requirement.

Re-resolve when:

- an authority-change signal exists;
- the source version may have changed;
- the action date moved;
- a material classification changed;
- a transition provision becomes relevant;
- the prior result is too stale to support readiness.

A stale authority result cannot support `READY` merely because it was correct when first retrieved.

## Conflicting authority

When material sources conflict:

1. preserve both;
2. compare legal force;
3. compare scope;
4. compare temporal status;
5. check amendment/replacement/transition context;
6. distinguish source text from interpretation;
7. return `CONFLICTING_AUTHORITY` if conflict remains material.

Do not resolve conflict by source count or convenience.

## Evidence requirements

Record enough provenance to reconstruct why the source was used:

- source identity and link/reference;
- authority type/legal force;
- relevant passage;
- lifecycle/effective period;
- verified time;
- source version/amendment context when material;
- proposition and temporal anchor supported.

## Cross-track handoffs

A BL1 authority handoff should contain:

- proposition ID/question;
- accountable owner;
- authority requirement;
- temporal anchor(s);
- candidate authority/source status;
- unresolved authority issue;
- freshness requirement;
- affected action(s).

The owner then calls/consumes Authority Resolver and records case applicability.

## Failure modes

- `official website = binding law`;
- `current law = applicable law`;
- `one recent article = authority`;
- decorative citation accumulation;
- secondary source silently replacing primary authority;
- resolver deciding substantive case applicability;
- searching after a conclusion only to confirm memory;
- ignoring source unavailability/conflict/partial resolution;
- using stale authority to keep an action `READY`;
- letting BL1 become a hidden substantive owner because it found the source.

## Escalation

Escalate verification when authority uncertainty can change legality, validity, ownership/control, tax liability, regulatory permission, remedy, deadline, enforcement, or readiness for a high-impact action.