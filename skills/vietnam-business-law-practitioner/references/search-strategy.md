# Search Strategy v0.2

Search is a designed runtime dependency for volatile legal authority. The Authority Resolver is a **callable service**, not a fixed pipeline stage.

Any accountable BL owner may call it while resolving a proposition. Composition may request re-resolution when temporal anchors, authority freshness, or downstream reclassification changes.

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

## Search sequence

1. Define the exact proposition requiring verification.
2. Identify its temporal anchor(s).
3. Identify jurisdiction and likely authority/legal-force type.
4. Locate the highest appropriate official source for the proposition.
5. Record source provenance separately from legal force.
6. Check lifecycle: effective date, amendment, replacement, suspension, repeal, consolidation, future effect.
7. Check transition rules and whether multiple versions are needed for different anchors.
8. Read the controlling passage in context.
9. Record `verified_at`, source/version context, and freshness requirement.
10. Return the authority result to the accountable owner.
11. The owner decides **case applicability**; the resolver does not silently promote `CURRENT_BINDING` to `APPLICABLE_TO_CASE`.
12. Reuse the resolved authority across tracks when the proposition, temporal anchor, and freshness remain valid.

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
- superseded/repealed;
- suspended;
- uncertain/transitioning.

A current law may still be inapplicable to a pre-effective transaction because of a transition rule. A past law may still govern a historical proposition.

## Authority freshness

An authority result is not permanently fresh merely because it was correct when retrieved.

For material irreversible/current actions, re-resolve authority when:

- its freshness requirement has expired;
- a known authority-change signal exists;
- a relevant effective date has passed;
- the temporal anchor changed;
- a reclassification changes the proposition being supported;
- the applicable regime becomes uncertain.

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
2. compare lifecycle/effective period;
3. compare scope and case applicability;
4. check amendment/replacement/transition context;
5. preserve ambiguity if conflict remains material.

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

Stop when the accountable owner has enough fresh, applicable authority to support the material proposition at the level needed for the action.

Do not continue collecting sources merely to make the answer look researched.