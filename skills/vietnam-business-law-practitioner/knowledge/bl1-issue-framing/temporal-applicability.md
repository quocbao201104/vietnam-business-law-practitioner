# BL1 — Temporal Applicability

## Owns

Identifying which event dates matter, constructing proposition-specific temporal anchors, and determining when historical, current, future-effective, transition, amendment, replacement, or suspension analysis must be activated.

BL1 owns the **temporal question map**. The accountable BL owner decides the substantive proposition under the resolved temporal authority.

## Does not own

- substantive application of corporate, contract, remedy, tax, employment, regulatory, or cross-border law;
- case applicability merely because an instrument is current;
- authority lifecycle determination without live verification when the proposition is time-sensitive.

## Activate when

Use when:

- the relationship spans more than one legal period;
- the transaction, performance, breach, notice, tax event, customs event, or planned action occurs on different dates;
- a law was amended, replaced, suspended, or became effective during the matter;
- an enacted rule will take effect before a planned future action;
- a transition clause may preserve an older regime;
- the user asks which temporal authority version governs analysis of a past event;
- current consolidated text may not represent the historical rule.

## Required state

Record only temporal anchors capable of changing the proposition or action. Typical anchors include:

- formation/signing date;
- corporate approval/closing date;
- performance/delivery/payment date;
- breach/default date;
- notice/termination date;
- tax recognition/payment/filing event;
- employment action date;
- regulatory launch/operation/change date;
- customs entry/export/import date;
- dispute filing/claim date;
- planned future action date.

A case may require several anchors. Do not force one global `RELEVANT_DATE`.

## Core distinctions

### Publication/promulgation ≠ effectiveness

An instrument may exist publicly before it governs the relevant action.

### Current/effective ≠ applicable to every historical relationship

A current rule may not govern rights or classifications fixed under an earlier regime.

### Future-effective ≠ current law

An enacted future rule may matter for planning but must not be presented as currently operative before its effective date.

### Historical ≠ obsolete for the case

A superseded rule can still be the correct authority candidate for an event that occurred while it governed.

### Lifecycle ≠ case applicability

The Authority Resolver may determine `CURRENT_BINDING`, `HISTORICAL`, `SUPERSEDED`, or another lifecycle state. The proposition owner still decides whether/how that authority governs the specific legal proposition.

### One relationship ≠ one temporal regime

Formation may require one authority version, later performance or breach another, and present-day procedure a third depending on transition rules and proposition type.

## Temporal-anchor procedure

1. **Identify the proposition.** Temporal reasoning is proposition-specific, not case-wide.
2. **Identify legally relevant events.** Ask which event can change the authority version/lifecycle relevant to this proposition.
3. **Create explicit temporal anchor(s).** Name the anchor by event, not merely `date`.
4. **Detect lifecycle uncertainty.** Determine whether amendment, replacement, suspension, repeal, future effectiveness, or transition may matter.
5. **Call Authority Resolver when material.** Request authority against each relevant anchor.
6. **Preserve transition provisions.** Do not use only the latest consolidated text when the relationship crosses a legal change.
7. **Return authority lifecycle/transition data to the proposition owner.** The owner resolves substantive case applicability.
8. **Re-evaluate future actions.** If a planned action moves to a different date, authority/version dependencies may need re-resolution.
9. **Invalidate only exact temporal dependents.** A changed date should not rerun unrelated propositions.

## Temporal state pattern

A useful representation is:

```text
PROPOSITION: P-BL3-FORMATION
TEMPORAL_ANCHOR: FORMATION_DATE
DATE: <known or unresolved>
AUTHORITY_REQUIRED: yes/no
LIFECYCLE_STATUS: resolver result
CASE_APPLICABILITY: owner result
```

For multi-event matters:

```text
P-BL3-FORMATION → FORMATION_DATE
P-BL4-BREACH    → BREACH_DATE
P-BL4-NOTICE    → NOTICE_DATE
P-BL5-TAX       → TAX_EVENT_DATE
ACTION-LAUNCH   → PLANNED_ACTION_DATE
```

Do not collapse these anchors unless the governing rules genuinely use the same temporal event.

## Live authority triggers

Live resolution is generally required when:

- the answer depends on whether a rule was effective on a specific date;
- a law changed between formation and current action;
- transition provisions may preserve the old regime;
- the user asks about a historical transaction;
- an instrument was suspended/replaced/amended;
- a future-effective rule may govern analysis by the planned action date;
- a deadline or procedural right depends on date-sensitive current authority.

## Evidence requirements

Temporal facts may require evidence such as:

- executed agreement/date/time records;
- corporate resolutions or closing records;
- delivery/performance logs;
- invoices/payment records;
- notices/communications;
- employment decisions/records;
- customs declarations;
- filings/regulator correspondence.

Document date ≠ event date automatically. Preserve disputes over when the legal event actually occurred.

## Cross-track handoffs

BL1 should pass only temporal metadata and unresolved signals, for example:

```text
TEMPORAL_ANCHOR: FORMATION_DATE
LIFECYCLE_STATUS: CURRENT_BINDING | HISTORICAL | ...
TRANSITION_SIGNAL: YES | NO | UNRESOLVED
CASE_APPLICABILITY: UNRESOLVED → accountable owner
```

A handoff may include:

- proposition ID/question;
- temporal anchor name;
- event date or unresolved status;
- lifecycle uncertainty requiring resolution;
- transition/amendment signal;
- affected owner/action.

BL1 should not state that a substantive law/regime `applies` to the case. That conclusion remains with the accountable BL owner.

## Failure modes

- one global relevant date;
- using today's law for every event;
- assuming publication date equals effective date;
- applying future-effective law as current;
- treating superseded law as irrelevant to historical events;
- using a current consolidated text without checking historical version/transition;
- changing an action date without rechecking authority dependencies;
- invalidating an entire case when only one temporal proposition changed;
- letting lifecycle status substitute for case applicability;
- BL1 describing a substantive regime as `applicable` instead of handing lifecycle/transition state to its owner.

## Escalation

Escalate temporal verification when a change in law could alter validity, ownership, permission, tax liability, remedy, deadline, enforcement, or readiness for a material action.