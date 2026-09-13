# BL1 — Legal Issue Framing / Regime Selection

BL1 frames the business problem, creates the initial route hypothesis, and detects temporal, authority, foreign-element, mandatory-law, and reclassification signals.

BL1 owns the **question map and route hypothesis**. It does not own substantive BL2–BL8 conclusions.

## Owns

- business-objective and candidate-action framing;
- material legal question/proposition map;
- initial route hypotheses, initial route state, and route-map orchestration;
- detection of temporal, mandatory-law, foreign-element, and specialist signals;
- orchestration of late routing and reclassification review;
- meta-level authority/temporal questions needed to route safely.

## Does not own

- corporate authority/ownership/control — BL2;
- contract formation/content/performance — BL3;
- breach/remedies/dispute posture — BL4;
- tax consequences — BL5;
- employment classification — BL6;
- regulatory permission/compliance — BL7;
- governing-law/treaty/foreign-investment/trade propositions — BL8;
- final case applicability of authority owned by BL2–BL8;
- route-state decisions that the runtime contract assigns to a newly activated accountable owner.

## Activate when

Activate BL1 when framing or routing is non-trivial, including when:

- the user gives a business story rather than a narrow legal proposition;
- several BL tracks may interact;
- route, owner, temporal anchor, foreign element, or mandatory-law overlay is unresolved;
- downstream evidence may trigger late routing or reclassification.

Compress or skip deep BL1 loading for a narrow proposition whose owner and scope are already clear.

## JIT capability map

Load only the BL1 unit needed for the current framing problem.

### `issue-framing.md`

Load when the main task is to convert a business situation into material legal questions, candidate actions, owners, facts/evidence, and missing conditions.

### `regime-routing.md`

Load when multiple legal regimes/owners may interact, a special or mandatory layer may matter, a foreign element may change routing, or substantive/procedural regimes are being collapsed.

### `temporal-applicability.md`

Load when legal treatment may change across formation, performance, breach, notice, tax/customs events, current action, amendment, transition, replacement, or future-effective law.

### `authority-applicability.md`

Load only when authority status/applicability is itself part of the BL1 framing/routing problem — for example when provenance, legal force, lifecycle, transition, conflicting authority, or source unavailability must be distinguished before the correct owner/route can be trusted.

Do **not** load this unit merely because a downstream owner needs current law. For a narrow owner-specific proposition, that owner should call Authority Resolver directly.

Do not load all four by default.

## Core invariants

- user label ≠ legal classification;
- route hypothesis ≠ substantive classification;
- one matter may require several proposition owners;
- route map ≠ executable dependency graph;
- general rule ≠ special/mandatory rule;
- private agreement ≠ public-law permission;
- substantive law ≠ procedure/forum;
- promulgated ≠ effective;
- current/effective ≠ applicable to every case;
- source provenance ≠ legal force;
- legal force ≠ lifecycle;
- lifecycle ≠ case applicability.

## Route states

Use:

- `ROUTE_CONFIRMED`
- `ROUTE_PLAUSIBLE`
- `ROUTE_UNRESOLVED`
- `ROUTE_REJECTED`

BL1 may identify `possible cross-border sales regime → activate BL8`.

BL1 may not promote `Vietnamese law applies`, `CISG applies`, `employee`, `taxpayer`, `licensed activity`, or another BL2–BL8 conclusion before the accountable owner resolves it.

A rejected route may reopen only when new material evidence or authority change affects the route basis. Reopening must be explicit.

## Minimum execution procedure

1. Identify business objective and split materially different actions.
2. Capture only material facts/evidence and temporal anchors.
3. Convert the story into material legal questions/propositions.
4. Assign candidate owners using `../INDEX.md`.
5. Detect temporal, foreign, mandatory-law, authority, and specialist signals.
6. Create route hypotheses rather than closed-world conclusions.
7. Load only the needed BL1 capability unit(s) and downstream owner(s).
8. Accept explicit `LATE_ROUTE_SIGNAL` or contradiction/reclassification return from downstream owners.
9. Update the route map without silently rewriting substantive state or overriding an activated owner's own route confirmation/rejection.
10. Stop BL1 expansion when framing is sufficient for accountable owners to resolve the requested action(s).

## Live authority behavior

Authority Resolver is a callable service available to proposition owners.

BL1 should call or request live authority only when a meta-level authority/temporal fact is itself material to safe framing or routing. Owner-specific current-law verification goes directly from the accountable owner to Authority Resolver and does not require `authority-applicability.md`.

Finding a source does not transfer substantive ownership to BL1.

## Handoff contract

A BL1 handoff should contain only what the owner needs:

- objective/action;
- proposition/question;
- candidate owner;
- route state;
- material facts/evidence status;
- temporal anchor(s);
- unresolved conditions;
- activation reason;
- authority-resolution need where material.

Do not attach an unearned substantive conclusion.

## Failure modes

- keyword-to-statute or keyword-to-track routing;
- universal intake/checklist dumping;
- treating route hypotheses as legal conclusions;
- one-law collapse;
- treating initial routing as a closed world;
- BL1 promoting BL2–BL8 classifications itself;
- BL1 acting as a mandatory authority gateway for owner-specific propositions;
- one global relevant date;
- current-law bias for historical/future events;
- official source treated as automatically binding/applicable;
- loading every plausible track instead of applying materiality;
- silent route repair or silent reclassification.