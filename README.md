<div align="center">

# Vietnam Business Law Practitioner

**Stable reasoning. Live law.**

A research-first Agent Skill for legally grounded business decisions in Vietnam — built to separate durable legal reasoning from rules that must be verified against current authority.

[![Version: v0.1.0](https://img.shields.io/badge/version-v0.1.0-0a7.svg)](#status-and-scope)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Jurisdiction: Vietnam](https://img.shields.io/badge/jurisdiction-Vietnam-da251d.svg)](#scope)
[![Format: Agent Skill](https://img.shields.io/badge/format-Agent%20Skill-6f42c1.svg)](skills/vietnam-business-law-practitioner/SKILL.md)

**[What it can help with](#what-it-can-help-with) · [Quick start](#quick-start) · [How it works](#how-it-works) · [Live-law verification](#live-law-verification) · [Research & evaluation](#research-and-evaluation)**

<sub><strong>Business decisions · Legal propositions · Authority · Evidence · Action readiness</strong></sub>

</div>

---

Vietnam Business Law Practitioner is a decision-support skill for founders, operators, and businesses working through Vietnamese business and commercial legal questions.

It is designed for questions where a useful answer requires more than recalling a rule. The runtime first reconstructs the business situation, separates the legal propositions that actually need resolution, assigns each material proposition to an accountable legal track, verifies current or historically applicable authority when required, and then composes the result back into business-facing options, consequences, unresolved issues, and next actions.

The project is intentionally **not** a static encyclopedia of Vietnamese law. Rules that can change — rates, thresholds, forms, deadlines, filing mechanics, penalties, permit requirements, tariff treatment, current administrative guidance, and similar details — should be resolved from current authority when they materially affect the decision.

## What it can help with

| Bring a business question | Work toward a useful result |
| --- | --- |
| Who can bind or act for a company? | Entity, representation, authority, approval, ownership, and governance analysis |
| What do the parties actually owe each other? | Contract formation, document stack, terms, obligations, performance state, and transaction analysis |
| What happens after non-performance or a dispute? | Breach, excuse, remedy, evidence posture, deadline, and dispute-path analysis |
| What tax or financial-law consequences follow from a business choice? | Legally relevant tax/financial consequences, dependencies, and unresolved authority |
| Can an employer take a proposed action? | Employment relationship, employer-side constraints, process, evidence, and consequence analysis |
| Is a business model, activity, claim, or market behavior permitted? | Regulatory perimeter, licensing/permission, market conduct, consumer, competition, data, and compliance analysis |
| What changes when foreign investment or cross-border activity is involved? | Investment, conflict-of-laws, treaty, foreign-exchange, customs, and trade overlays |
| Which legal regime even governs the problem? | Issue framing, candidate regimes, route selection, temporal applicability, and proposition ownership |

These are supported decision areas, not guarantees of a legal outcome. The quality of a result still depends on the facts, documents, timing, available authority, host tools, and model behavior.

## Quick start

The repository can be used as a standalone Agent Skill or installed as a repository-backed plugin. Claude and Codex packages share the same runtime files under `skills/vietnam-business-law-practitioner/`; there is no duplicate copy of the legal knowledge.

### Claude Code

```text
/plugin marketplace add quocbao201104/vietnam-business-law-practitioner
/plugin install vietnam-business-law-practitioner@vietnam-business-law-practitioner
```

See [Claude Code marketplace setup](docs/claude-code-plugin.md).

### Codex

Add this repository as a marketplace in compatible Codex plugin controls:

```text
https://github.com/quocbao201104/vietnam-business-law-practitioner.git
```

On a compatible Codex CLI:

```text
codex plugin marketplace add https://github.com/quocbao201104/vietnam-business-law-practitioner.git
codex plugin add vietnam-business-law-practitioner@vietnam-business-law-practitioner
```

See [Codex plugin setup](docs/plugin.md).

### Repository / standalone skill

```bash
git clone https://github.com/quocbao201104/vietnam-business-law-practitioner.git
```

The governing runtime instructions are in [`skills/vietnam-business-law-practitioner/SKILL.md`](skills/vietnam-business-law-practitioner/SKILL.md).

### Your first task

You do not need to know the internal BL track names. Give the agent the business situation in ordinary language and include the facts, documents, dates, intended action, and decision you actually need when available.

```text
Use Vietnam Business Law Practitioner.

A Vietnamese company wants to terminate a commercial agreement after repeated delivery failures.
The contract, latest amendment, notices, and delivery timeline are attached.

Determine what facts and legal propositions materially control the decision,
verify current authority where required,
and give me the viable options, consequences, unresolved issues,
and the next actions I should consider before acting.
```

For historical matters, include the relevant transaction or event date. A rule that is current today may not have governed the earlier event.

> **Important:** installing the skill does not install an authoritative Vietnamese legal database. Current-law verification depends on the host's available retrieval tools and access to suitable sources.

## Why it exists

A legal answer can sound precise and still be wrong for the decision in front of you.

| Failure to avoid | Design response |
| --- | --- |
| Treat the user's label as the legal classification | Reconstruct the relationship from legally material facts |
| Find a matching article and stop | Lock the instrument identity, lifecycle, temporal applicability, and controlling provision |
| Use a current rule for a historical event | Resolve the authority version applicable to the relevant date |
| Let one legal domain silently decide another | Give each material proposition one accountable owner |
| Treat contractual agreement as regulatory permission | Keep private-law validity and public-law permission separate |
| Treat a search result as verified authority | Separate discovery from verification |
| Hide missing facts behind confident prose | Preserve uncertainty and state what remains unresolved |
| Return a legal conclusion with no decision path | Translate the legal position into options, consequences, readiness, and next actions |

The core preserves distinctions that can change the legal result:

```text
user label ≠ legal classification
search hit ≠ verified authority
current text ≠ historically applicable text
contractual permission ≠ regulatory permission
fact ≠ allegation ≠ inference ≠ verified evidence
instrument identity ≠ provision text
source availability ≠ source authority
legal possibility ≠ action readiness
one case ≠ one legal owner
```

## How it works

The runtime starts from the **business decision**, not from a legal topic list.

```text
BUSINESS SITUATION
        ↓
MATERIAL FACTS + TIME ANCHOR
        ↓
LEGAL PROPOSITIONS
        ↓
ACCOUNTABLE BL OWNERS
        ↓
JUST-IN-TIME SPECIALIST DEPTH
        ↓
CURRENT / HISTORICAL AUTHORITY RESOLUTION
        ↓
CROSS-TRACK COMPOSITION
        ↓
POSITION · OPTIONS · CONSEQUENCES · GAPS · NEXT ACTIONS
```

A simple matter can stay simple. A multi-domain matter can activate several tracks, but activation does not give every track permission to decide everything.

The key composition rule is:

```text
ONE MATERIAL PROPOSITION
→ ONE ACCOUNTABLE OWNER
```

Other tracks may supply facts, constraints, dependencies, or specialist input. They do not silently overwrite the proposition owned elsewhere.

### Core tracks

| Track | Accountable area |
| --- | --- |
| **BL1** | Legal issue framing, candidate regimes, routing, and temporal applicability |
| **BL2** | Entity, representation, authority, corporate approval, ownership, and control |
| **BL3** | Contract/transaction existence, terms, obligations, and performance state |
| **BL4** | Breach, excuse, remedy, evidence posture, disputes, and deadline state |
| **BL5** | Tax and financial legal consequences |
| **BL6** | Employment relationship and employer action pathway |
| **BL7** | Regulatory perimeter, permission, market conduct, and compliance state |
| **BL8** | Foreign investment, conflict-of-laws, treaty, FX, trade, and customs overlay |

[`knowledge/INDEX.md`](skills/vietnam-business-law-practitioner/knowledge/INDEX.md) is the canonical detailed route map. Specialist depth is loaded only when an already-open issue requires it; the repository does not route into customs, transfer pricing, sector regulation, privacy, or another specialist area merely because a related noun appears in the prompt.

## Live-law verification

The project's central operating principle is:

> **Keep stable reasoning in the skill. Resolve volatile law from current authority when it matters.**

Current-law work therefore separates **discovery** from **verification**.

```text
PROPOSITION
    ↓
DISCOVER CANDIDATE AUTHORITY
    ↓
LOCK DOCUMENT IDENTITY
    ↓
CHECK LIFECYCLE + EFFECTIVE DATE + AMENDMENT / REPLACEMENT
    ↓
READ THE CONTROLLING PROVISION IN CONTEXT
    ↓
RECORD SOURCE / VERSION / VERIFICATION STATE
    ↓
RETURN THE AUTHORITY RESULT TO THE PROPOSITION OWNER
```

Search engines, legal databases, commentary, and secondary legal sites can be useful for discovering document numbers, candidate provisions, amendments, replacement instruments, or official locators. Discovery does not by itself establish the controlling legal proposition.

The authority resolver is designed to preserve distinctions such as:

- whether a candidate source was available or unavailable;
- whether the source identity was established;
- whether the applicable version and lifecycle were resolved;
- whether the controlling provision was read in context;
- whether a proposition is resolved, partially resolved, ambiguous, or unresolved;
- when freshness or a new fact requires re-resolution.

This matters because a phrase match can come from the wrong instrument, an older version, a future-effective amendment, or an unofficial reproduction whose text is not enough to establish temporal applicability.

See [`references/search-strategy.md`](skills/vietnam-business-law-practitioner/references/search-strategy.md), [`references/source-status.md`](skills/vietnam-business-law-practitioner/references/source-status.md), and [`schemas/authority-resolver.md`](skills/vietnam-business-law-practitioner/schemas/authority-resolver.md).

## Shared legal state and composition

A multi-domain case should not become eight independent mini-answers stitched together at the end.

The runtime carries shared state for material facts, classifications, proposition results, dependencies, authority versions, option sets, evidence/procedure/deadline state, and action readiness. A later track can consume an earlier result without silently changing its meaning or evidence status.

Examples:

- BL3 may determine what a contract requires; BL4 then evaluates breach and remedies without rewriting the contract terms.
- BL2 may determine who had authority to act for an entity; BL3 may use that result when assessing the transaction without taking ownership of the corporate-authority proposition.
- BL7 may determine that an activity requires regulatory permission even where BL3 finds a valid private agreement.
- BL8 may add a cross-border overlay without replacing the domestic proposition owner unless the governing-law or treaty question actually changes ownership.

The normative composition contracts live under [`schemas/`](skills/vietnam-business-law-practitioner/schemas/).

## Scope

The project focuses on **business and commercial legal decisions in Vietnam**, including cross-border overlays where they materially affect the matter.

Core scope includes:

- corporate entity, authority, ownership, governance, and approvals;
- contracts and commercial transactions;
- breach, remedies, evidence, and disputes;
- tax and financial legal consequences of business decisions;
- employment and employer-side actions;
- licensing, regulatory perimeter, market conduct, consumer, competition, data, and compliance questions;
- foreign investment, FX, trade, customs, treaty, and conflict-of-laws overlays when activated by the matter.

It is not intended to be:

- a general Vietnamese-law encyclopedia;
- a criminal, family, inheritance, or ordinary citizen legal Q&A system;
- an accounting or bookkeeping engine;
- a tax-rate, tariff, penalty, form, or deadline database;
- a contract-template pack;
- a substitute for professional legal advice or representation.

## Host compatibility and tools

The skill packages instructions, schemas, practitioner knowledge, source discipline, and specialist routing. It does **not** create capabilities the host does not have.

A host may need web search, browser access, official-document retrieval, file reading, or other tools to verify a material proposition. If those tools are unavailable, the correct behavior is to preserve the limitation rather than fabricate current authority.

Likewise, plugin installation does not create access to private legal databases, government systems, filing portals, client documents, or confidential business records.

The host also controls context persistence. Material facts, dates, adopted classifications, authority status, and unresolved dependencies should remain in the active task or an accessible project record when a matter spans multiple sessions.

## Under the hood

```text
skills/vietnam-business-law-practitioner/
├── SKILL.md              governing runtime instructions and invariants
├── knowledge/
│   ├── INDEX.md          canonical detailed route map
│   └── bl*/              practitioner reasoning by accountable legal track
├── references/           authority, source, search, and citation guidance
├── schemas/              shared state, composition, resolver, handoff, and output contracts
└── specialist/           bounded specialist depth loaded only when justified

research/                 provenance, research questions, synthesis, and repair history
evals/                    composition, freshness, routing, and runtime evaluation artifacts
scripts/                  supporting runtime and evaluation utilities

.claude-plugin/           Claude plugin and marketplace manifests
.codex-plugin/            Codex plugin manifest
.agents/plugins/          Codex marketplace catalog
```

The repository deliberately keeps **research provenance** separate from **runtime practitioner knowledge**. Research files explain why a mechanism exists; runtime knowledge contains the bounded material the agent should use during work.

No external repository, legal-tech product, commentary site, or single source package is treated as the architectural source of truth.

## Research and evaluation

Research is first-class provenance rather than discarded after synthesis. Where useful, a research track preserves its question, source map, findings, contradictory evidence, rejected folklore, architecture implications, unresolved questions, and repair history.

The current dedicated research area includes [`research/legal-source-retrieval/`](research/legal-source-retrieval/), which pressure-tests how current legal authority should be discovered, identified, versioned, and verified before a proposition is treated as resolved.

Evaluation artifacts under [`evals/`](evals/) test the architecture at several boundaries, including:

- just-in-time track routing;
- cross-track composition;
- authority freshness and temporal applicability;
- source drift and source unavailability;
- preservation of ownership and legal state across runtime steps;
- whether a runtime path actually read the required contract and knowledge surfaces.

Passing a mechanical evaluation does not establish that a generated legal answer is correct. Repository checks, routing evidence, authority verification, model behavior, and real legal correctness remain separate claims.

## Status and scope

Current plugin manifest version: **v0.1.0**.

The repository is ready for **early dogfooding**. The core practitioner architecture, BL1–BL8 ownership model, just-in-time specialist routing, live-law authority resolution, shared legal state, composition contracts, and action-readiness model are in place.

Runtime validation is ongoing. Real usage may still expose routing failures, missing authority dependencies, composition defects, stale source assumptions, or cases where the current abstractions are too broad or too narrow.

The project favors **local repair over architecture expansion**: a new track, primitive, specialist module, or shared state field should be added only when a concrete decision-relevant failure cannot be repaired cleanly within the existing ownership model.

## Responsible use

Vietnam Business Law Practitioner is an open-source research and decision-support project. It is **not a law firm**, does not provide legal representation, and does not create a lawyer-client or attorney-client relationship.

Material legal propositions should be independently verified before action, especially for decisions that are high-impact, irreversible, deadline-sensitive, regulated, disputed, or cross-border.

Do not submit confidential client information, privileged communications, credentials, personal data, or sensitive business records to a runtime or third-party service unless you understand and accept how that system handles the data.

Read the full [Disclaimer](DISCLAIMER.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

Contributions should correct a demonstrated problem with the smallest justified surface. Do not add a legal domain, specialist module, state field, or architecture primitive merely for coverage completeness.

Research inputs may include official law and government sources, legal databases, practitioner material, academic work, legal-tech systems, and third-party repositories. Source breadth is useful; no single external source becomes the runtime architecture by default.

Community participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). Security reports should follow [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).
