# Contributing

Thanks for contributing to Vietnam Business Law Practitioner.

This repository is a research-first legal decision skill. Contributions should improve correctness, maintainability, routing, evidence discipline, or runtime behavior without turning the repository into a static legal database.

## Before you contribute

Please read the repository architecture first:

- `skills/vietnam-business-law-practitioner/SKILL.md`
- `skills/vietnam-business-law-practitioner/knowledge/INDEX.md`
- `skills/vietnam-business-law-practitioner/schemas/`
- `skills/vietnam-business-law-practitioner/references/`

The core design principle is:

```text
Stable reasoning, live law.
```

Keep durable reasoning in the skill. Resolve volatile law live when it materially affects the answer.

## Good contribution areas

Useful contributions include:

- correcting or strengthening practitioner reasoning;
- improving proposition ownership or handoff clarity;
- improving JIT routing/selectivity;
- adding or repairing adversarial evaluation cases;
- improving runtime traceability or checker behavior;
- fixing source/authority handling defects;
- documenting a concrete runtime failure and the smallest repair that fixes it;
- improving public documentation and contributor usability.

## Architecture rules

Please preserve these invariants unless a concrete failure proves they are insufficient:

- one material legal proposition has one accountable owner;
- BL1 frames and routes but does not silently own downstream substantive conclusions;
- sibling knowledge units are not mandatory pipelines;
- downstream tracks do not reconstruct upstream-owned state;
- `DEPENDS_ON`, `CONSTRAINS`, `SIGNALS`, and `FEEDBACK` remain distinct;
- only exact `DEPENDS_ON` edges automatically propagate stale/invalidation state;
- Authority Resolver resolves authority, not substantive case applicability;
- specialists return candidate depth to an owning BL track and do not become hidden owners;
- readiness is per action, not global to the matter;
- the synthesizer composes owned propositions and does not become a hidden BL9.

Do not add a new BL track, primitive, controller, dependency type, or infrastructure layer merely because it appears cleaner. Show the concrete failure that cannot be repaired locally under the existing architecture.

## Legal knowledge and authority changes

For material legal corrections or additions, make the proposition under review explicit.

Where relevant, include:

- the legal proposition being corrected or supported;
- the accountable BL owner;
- the relevant temporal anchor or `as_of` date;
- the authority or source used;
- document identity and lifecycle/currentness considerations;
- the exact provision or locator when material;
- whether the change affects reasoning, routing, evidence requirements, or only current law.

Do not treat a search result, summary article, law-firm post, or database snippet as controlling authority merely because it is recent.

Do not hardcode volatile values such as current rates, thresholds, forms, permit mechanics, fines, tariff schedules, or filing details into durable knowledge unless they are clearly dated examples and there is a strong reason to keep them.

## Retrieval/search changes

The current legal-source retrieval architecture is treated as stable.

Do not redesign it around a crawler, vector database, graph database, or custom API client without a recurring concrete failure that the current discovery → identity → lifecycle/currentness → provision → owner-applicability flow cannot represent or solve.

A failed source adapter or API path is not automatically a failed Authority Resolver result when sufficient official fallback authority resolves the proposition.

## Runtime and state changes

For runtime behavior changes:

- preserve stable object IDs and `state_revision` semantics;
- keep writes owner-scoped;
- do not allow stale writes to overwrite newer shared state;
- make material path behavior externally observable through runtime events;
- prefer exact recomputation over global reset;
- do not claim path correctness from plausible final prose alone.

If you change an observable runtime contract, update the relevant trace/checker/evaluation artifacts when needed.

## Evaluation changes

Prefer small adversarial cases with an explicit oracle over broad random test suites.

A useful evaluation should make clear:

- what failure class it targets;
- expected reads and intentional skips where routing matters;
- expected owner/state transitions;
- forbidden paths or conclusions;
- the candidate SHA when the evaluation is candidate-bound.

Passing CI or mechanical validation is not, by itself, evidence that ownership, routing, authority handling, composition, or readiness are semantically correct.

## Pull requests

Keep pull requests narrow enough to review independently.

A strong PR description usually includes:

1. the problem or observed failure;
2. the affected invariant or contract;
3. the minimum proposed repair;
4. files intentionally changed;
5. files intentionally not changed;
6. evaluation or evidence used;
7. known limitations or unresolved questions.

Avoid mixing unrelated architecture, knowledge, retrieval, and documentation changes in one PR unless the change genuinely requires them to move together.

## Sensitive and proprietary material

Do not commit confidential client information, personal data, private legal documents, credentials, proprietary databases, or material you do not have the right to redistribute.

When reporting a real legal scenario, reduce it to the minimum facts needed to reproduce the architecture or reasoning issue.

## Licensing

By contributing to this repository, you agree that your contributions are licensed under the repository's MIT License.
