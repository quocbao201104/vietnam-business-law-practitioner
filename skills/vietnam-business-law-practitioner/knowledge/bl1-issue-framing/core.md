# BL1 — Legal Issue Framing / Regime Selection

## Owns

Initial framing of the business situation into legal issues; route hypotheses; detection of temporal, foreign-element, mandatory-law, and specialist signals; orchestration of explicit late routing and reclassification review.

BL1 owns the **question map**, not every substantive legal classification.

## Does not own

- BL2–BL8 substantive propositions;
- final governing-law/treaty applicability (BL8 where cross-border);
- corporate authority/ownership (BL2);
- contract formation/content (BL3);
- breach/remedies (BL4);
- tax treatment (BL5);
- employment classification (BL6);
- regulatory permission (BL7).

## Activate when

The business objective, issue map, route, temporal anchors, foreign element, mandatory-law overlay, or specialist trigger is non-trivial or unresolved.

## Required state

Business objective; candidate actions; material actors; relationship; object/activity; material timeline; available documents/evidence; desired action.

## Core distinctions

- user label ≠ legal classification;
- route hypothesis ≠ substantive classification;
- one situation may require several proposition owners;
- general law ≠ special law;
- substantive law ≠ procedure/forum;
- promulgated ≠ effective;
- effective/current ≠ applicable to every case;
- official provenance ≠ binding legal force.

## Route states

Use:

- `ROUTE_CONFIRMED`
- `ROUTE_PLAUSIBLE`
- `ROUTE_UNRESOLVED`
- `ROUTE_REJECTED`

BL1 is allowed to say `possible cross-border sales regime → activate BL8`.

BL1 is not allowed to promote `Vietnamese Commercial Law applies` or `CISG applies` before the accountable owner resolves that proposition.

## Decision procedure

1. Reconstruct the business situation without accepting legal labels as conclusions.
2. Identify candidate material propositions/questions.
3. Assign candidate owners using `knowledge/INDEX.md`.
4. Detect special-law, mandatory-law, foreign-element, temporal, and specialist signals.
5. Create route hypotheses, not closed-world routing conclusions.
6. Identify volatile propositions that an owner will need to resolve through Authority Resolver.
7. Activate only materially relevant tracks initially.
8. Accept `LATE_ROUTE_SIGNAL` from downstream owners and update the route map explicitly.
9. If new evidence challenges a classification, open reclassification review; do not silently commit the change.

## Authority behavior

BL1 may request authority for meta-routing/temporal propositions when necessary, but the Authority Resolver is a callable service available to all owners.

BL1 does not become the legal owner merely because it found the source.

## Failure modes

- keyword-to-statute routing;
- treating initial routing as closed world;
- one-law collapse;
- BL1 promoting BL8/BL6/BL2 classifications itself;
- current-law bias for historical/future events;
- draft/future law treated as current;
- official source treated as automatically applicable;
- silent route repair or silent reclassification.
