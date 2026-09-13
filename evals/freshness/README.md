# Freshness Evaluation

Freshness tests should prove that runtime authority handling distinguishes legal lifecycle states rather than rewarding memorized current-law answers.

Initial classes:

1. **Future-effective** — promulgated rule takes effect after the action date.
2. **Historical** — transaction occurred under an earlier version.
3. **Amended/replaced** — cached proposition must be invalidated.
4. **Suspended** — implementing rule exists but is not operative for the relevant period.
5. **Draft/consultation** — proposal must not be presented as current law.
6. **Threshold/rate drift** — volatile numeric rule changes while reasoning structure remains stable.

Each fixture should bind:

- proposition;
- relevant event/action date;
- authority lifecycle state;
- expected runtime behavior;
- forbidden stale behavior.
