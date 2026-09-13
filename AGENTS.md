# Repository instructions

## Scope and purpose

These instructions apply throughout this repository. Read any applicable nested
`AGENTS.md` or `AGENTS.override.md` before editing its target paths. Explicit user
instructions take precedence over repository defaults.

This repository develops the Vietnam Business Law Practitioner Agent Skill for
business decisions involving Vietnamese law. Its main artifacts are Markdown
reasoning guidance, semantic runtime contracts, and evaluation fixtures. Python
scripts support observable runtime evaluation; they do not run an LLM.

The governing design principle is **stable reasoning, live law**: retain durable
legal reasoning here and resolve material, time-sensitive law from authoritative
sources at runtime.

## Read according to the task

- Start with `README.md` for purpose, structure, and scope.
- For skill behavior, read `skills/vietnam-business-law-practitioner/SKILL.md`.
- For routing and ownership, use
  `skills/vietnam-business-law-practitioner/knowledge/INDEX.md` as the canonical
  detailed route map, then read the relevant BL core and only the capability units
  needed for the task. Do not preload all units in a track.
- For state, composition, authority resolution, handoffs, output, or trace
  changes, read the corresponding files in
  `skills/vietnam-business-law-practitioner/schemas/`.
- For research and legal sources, read `research/README.md` and the relevant
  files in `skills/vietnam-business-law-practitioner/references/`.
- For evaluation work, start with `evals/composition/README.md` and, where
  relevant, `evals/freshness/README.md`.
- For packaging, read `docs/plugin.md` and `docs/claude-code-plugin.md`.
- For source-retrieval design, also read `research/legal-source-retrieval/README.md`;
  the runtime authority contracts remain normative.

This file governs repository work. It does not replace the skill's runtime
contracts or define a second routing map. Resolve inconsistencies in their
canonical source and update affected consumers within the requested scope.

## Architecture invariants

- Preserve BL1–BL8 boundaries. Each material legal proposition has exactly one
  accountable owner; a multi-domain matter can involve several owners.
- Ownership is semantic, not tied to an agent/process. One runtime may execute
  several owners sequentially while preserving ownership and state boundaries.
  Do not introduce mandatory multi-agent orchestration.
- Follow the JIT contract-loading matrix in `SKILL.md`. Load coupled contracts
  before their governed behavior, including shared-state support for authority
  resolution and specialist handoffs. Do not impose blanket schema preloading.
- BL1 proposes initial framing and routes. It does not decide substantive
  classifications owned by BL2–BL8. New material evidence can activate a late route.
- Keep factual truth status separate from evidence provenance. User labels and
  document statements are not automatically established legal classifications.
- Preserve one shared legal state, stable material object IDs, revisions, and
  owner-scoped updates. Downstream work must return contradictions to the owner.
- Reclassification requires signal, review, and committed change. Only explicit
  proposition-level `DEPENDS_ON` edges automatically propagate invalidation.
  `SIGNALS` and `FEEDBACK` trigger review; constraints affect readiness through
  explicit action links.
- Authority Resolver is callable by owners as needed. Keep provenance, legal
  force, lifecycle, freshness, and case applicability distinct. The owner decides
  applicability using proposition-specific temporal anchors.
- Specialist findings return to an accountable BL owner for integration.
- Synthesis derives the answer from owned propositions; it cannot invent legal
  conclusions, resolve owner conflicts, or silently repair missing routes.
- Preserve the `ACTIVE`, `RESOLVED`, and `TERMINAL_UNRESOLVED` conflict lifecycle.
  Status and affected-action scope changes require revision-safe state deltas.
  Terminalization requires exhausted material internal resolution steps and explicit
  remaining external needs. Reopening requires new material input and an explicit
  transition for the same conflict ID at a newer committed revision.
- Recompute readiness for every affected action after conflict transitions or scope
  changes. Active or terminal unresolved conflicts cannot support `READY` or
  `READY_WITH_CONDITIONS`. `DO_NOT_PROCEED` requires an independently supported
  blocker; unresolved conflict alone is insufficient.
- Readiness is per action. `READY` requires positive closure of material
  prerequisites and sufficiently fresh authority. Convergence may end in a
  non-READY state.

Consult the schemas for exact definitions rather than extending these summaries
into new rules. Add architecture, tracks, or specialist modules only when concrete
runtime/composition evidence demonstrates a gap, consistent with `SKILL.md`.

## Knowledge and research changes

- Keep knowledge focused on decision procedures, material facts, distinctions,
  evidence needs, ownership boundaries, and failure modes.
- Do not encode volatile rates, thresholds, forms, fines, or deadlines as timeless
  knowledge. Clearly label dated examples and their sources when needed.
- Verify material legal claims against appropriate current or historical authority.
  Source-routing documents are discovery guidance, not legal authority themselves.
- Separate discovery from verification. Lock instrument identity, lifecycle, and
  provision currentness before relying on controlling text; retain provision locators
  and source context rather than treating search snippets as authority.
- Keep source-attempt failures separate from proposition-level resolution. Record
  source drift/unavailability and use official fallback paths; one failed source does
  not invalidate a sufficient result obtained elsewhere.
- Reuse authority only when identity/version, temporal scope, and freshness remain
  suitable. Do not reuse another proposition's applicability decision automatically.
- Preserve useful research provenance, contradictory findings, uncertainty, and
  reasons for rejecting claims. Do not fabricate sources or research results.
- Maintain the minimum sufficient authority set; do not impose citation quotas.
- Keep simple user-facing answers proportionate to the actual decision.

## Documentation conventions

- Follow the existing English documentation style and preserve exact schema/event
  identifiers.
- Keep repository references relative to the repository or containing document.
  Do not embed personal tool configuration or machine-specific paths.

## Plugin packaging

- Codex and Claude Code share `skills/vietnam-business-law-practitioner/` as the
  runtime source of truth. Do not duplicate skill files for distribution.
- Keep `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`,
  `.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json` consistent with
  their respective package documentation when packaging changes are requested.
- Packaging does not supply a separate LLM runtime, retrieval service, or legal
  database. Research and eval artifacts are maintainer resources, not extra skills.
- For manifest changes, validate JSON and referenced local paths. Keep package
  identity/version claims consistent across affected manifests and documentation.

## Verification and evaluation evidence

- For documentation-only changes, inspect the full diff, validate referenced paths
  and identifiers, and check consistency with the canonical contracts. No build is
  required merely for editing Markdown.
- For Python changes, run the affected CLI's `--help` and focused behavioral checks
  for the changed behavior, including relevant failure cases. A help invocation
  alone does not prove runtime correctness.
- For runtime semantics changes, identify affected CT/RF, BL JIT, and freshness cases.
  Run the applicable evaluation where feasible; otherwise state the evidence gap.
- Read `evals/composition/runtime-agent-protocol-v0.3.md` before cold-start runs.
  Obtain the frozen candidate and oracle from the evaluation documents rather than
  assuming the working HEAD is the candidate.
- Select the candidate-bound oracle for the layer under test. The older RF oracle
  does not prove BL1–BL8 internal capability routing; each track has its own JIT
  fixtures and oracle listed in `evals/composition/README.md`.
- A PASS against a historical candidate does not validate later semantic edits.
  Report the evaluated candidate and scope explicitly; do not silently rebind a
  frozen oracle or imply coverage of current HEAD.
- During a cold-start fixture, use walker-mediated candidate reads, a fresh session
  per fixture, and the protocol's context-isolation requirements. Do not substitute
  direct skill-file reads or preloaded architecture context.
- `scripts/runtime_walker.py` records candidate file reads and semantic events;
  `scripts/check_runtime_trace.py` checks traces against the oracle. Semantic event
  logging must not expose private chain-of-thought.
- Do not fabricate traces, replay expected events as evidence of an actual run, or
  weaken the oracle to obtain PASS. Review unexpected behavior and checker limits.
- Keep manual traces, observable cold-start evidence, and held-out/independent review
  distinct. Follow the freeze gate in `evals/composition/README.md`; a manual pass
  count or plausible final answer does not establish freeze readiness.
- Finish by reporting what changed, what was actually checked, and any limitations.
  Never claim checks passed or a phase is complete without supporting evidence.
