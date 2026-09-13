# Freshness Evaluation v0.2

Freshness tests should prove that runtime authority handling distinguishes source provenance, legal force, lifecycle, temporal anchors, freshness, and case applicability rather than rewarding memorized current-law answers.

## Initial classes

1. **Future-effective** — promulgated rule takes effect after the action date.
2. **Historical** — transaction occurred under an earlier version.
3. **Amended/replaced** — cached authority may no longer support dependent propositions.
4. **Suspended** — implementing rule exists but is not operative for the relevant period.
5. **Draft/consultation** — proposal must not be presented as current law.
6. **Threshold/rate drift** — volatile numeric rule changes while reasoning structure remains stable.
7. **Transition applicability** — current law exists but transition provisions preserve another regime for the proposition.
8. **Multi-anchor matter** — formation, breach, tax event, customs entry, and action date may require different authority versions.
9. **Freshness expiry / authority-change signal** — authority verified earlier must be re-resolved before material irreversible/current action when freshness is no longer satisfied.

## Fixture contract

Each fixture should bind:

- `proposition_id`;
- accountable BL owner;
- temporal anchor(s), not one global date;
- source provenance;
- legal-force type;
- lifecycle state;
- `verified_at` / freshness requirement;
- expected owner decision about case applicability;
- expected typed dependency/invalidation behavior;
- affected action readiness;
- forbidden stale behavior.

## Core oracle

```text
CURRENT_BINDING
≠ APPLICABLE_TO_CASE

verified yesterday
≠ automatically fresh enough for today's irreversible action
```

Authority Resolver returns lifecycle/freshness metadata. The accountable proposition owner decides applicability.