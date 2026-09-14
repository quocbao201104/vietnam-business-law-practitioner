<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo-vector-20260914/banner/readme-banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/logo-vector-20260914/banner/readme-banner-light.svg">
  <img src="assets/logo-vector-20260914/banner/readme-banner-light.svg" alt="Vietnam Business Law Practitioner" width="100%">
</picture>

# Vietnam Business Law Practitioner

**Work through the legal questions behind your next business decision in Vietnam.**

An Agent Skill for founders, operators, and businesses assessing contracts, company decisions, employment, compliance, tax consequences, and cross-border activity.

[![Version: v0.2.0](https://img.shields.io/badge/version-v0.2.0-0a7.svg)](#status)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Jurisdiction: Vietnam](https://img.shields.io/badge/jurisdiction-Vietnam-da251d.svg)](#what-it-can-help-with)
[![Format: Agent Skill](https://img.shields.io/badge/format-Agent%20Skill-6f42c1.svg)](skills/vietnam-business-law-practitioner/SKILL.md)

**[Use cases](#what-it-can-help-with) · [Quick start](#quick-start) · [How it works](#how-it-works) · [Project status](#status)**

<sub>Stable reasoning. Live law.</sub>

</div>

---

Before you sign, hire, terminate, launch, or invest, you need to understand what the law means for the action you are considering.

Vietnam Business Law Practitioner guides an AI agent through that work: establish the relevant facts, investigate the legal questions, verify the authority that matters, and explain the available options, consequences, and next steps. It is designed to make unresolved issues visible so you can distinguish a supported option from one that still needs evidence or legal review.

**Available as a skill and as a plugin for Claude Code and Codex.** The project is in early dogfooding; it supports research and decision preparation, with professional review where needed.

## What it can help with

| Your business question | What the skill helps examine |
| --- | --- |
| Can this person sign or approve the deal? | Company representation, signing authority, corporate approvals, ownership, and control |
| What have we agreed to, and can we exit? | Contract terms and amendments, obligations, performance, breach, remedies, and dispute options |
| What legal tax or financial consequences follow? | Relevant tax treatment, statutory responsibilities, and dependencies that need verification |
| Can we take this employment action? | The employment relationship, employer obligations, required process, evidence, and consequences |
| Can we launch or operate this activity? | Licensing and permissions, market conduct, consumer protection, competition, and data compliance |
| What changes with a foreign investor or overseas counterparty? | Investment restrictions, governing law, treaties, cross-border payments, trade, and customs issues |

You can describe the situation in ordinary language. The skill is designed to identify the relevant legal areas and investigate specialist questions when they could change the decision.

Its scope is business and commercial law. General criminal, family, and inheritance matters, bookkeeping, and generic accounting sit outside its core scope.

### What a useful answer looks like

For a company considering termination after repeated delivery failures, the skill should examine the contract and amendments, what was required, what occurred, and which law applies to the relevant events. It should then explain:

- **The legal position:** supported conclusions and the facts and authority behind them.
- **The options:** available courses of action and their material consequences.
- **The gaps:** missing documents, disputed facts, or unresolved law that could change the answer.
- **The next steps:** what can proceed, what needs verification, and what requires professional review.

That is an illustration of the intended workflow, not a reported case result. The answer's depth should match the decision; a straightforward question does not need a full decision brief.

## Quick start

Choose your host below. It needs access to the skill files and suitable retrieval tools to verify current or historically applicable law. Installation includes the reasoning guidance; access to legal databases, government systems, and private records depends on the host.

### Claude Code

Run inside Claude Code:

```text
/plugin marketplace add quocbao201104/vietnam-business-law-practitioner
/plugin install vietnam-business-law-practitioner@vietnam-business-law-practitioner
```

Reload plugins or restart the session if prompted, then invoke:

```text
/vietnam-business-law-practitioner:vietnam-business-law-practitioner
```

[Installation and update details →](docs/claude-code-plugin.md)

### Codex

In compatible Codex marketplace controls, add this repository and install `vietnam-business-law-practitioner`:

```text
https://github.com/quocbao201104/vietnam-business-law-practitioner.git
```

On a compatible Codex CLI:

```text
codex plugin marketplace add https://github.com/quocbao201104/vietnam-business-law-practitioner.git
codex plugin add vietnam-business-law-practitioner@vietnam-business-law-practitioner
```

Start a new task after installation so the host discovers the skill.

[Codex setup and package details →](docs/plugin.md)

### Standalone skill

Clone the repository:

```bash
git clone https://github.com/quocbao201104/vietnam-business-law-practitioner.git
```

Use [`skills/vietnam-business-law-practitioner/`](skills/vietnam-business-law-practitioner/) with a host that supports Agent Skills, following that host's skill-loading instructions. [`SKILL.md`](skills/vietnam-business-law-practitioner/SKILL.md) is the runtime entry point. Both plugin packages use these same files.

### Bring your first business decision

Provide the action you are considering, the outcome you want, and the relevant facts, documents, and dates you have. For example:

```text
Use Vietnam Business Law Practitioner.

Our Vietnamese company is considering terminating a supply agreement
because the supplier has repeatedly missed deliveries.
I have attached the agreement, amendments, notices, and delivery timeline.

Assess our options before we send a termination notice.
Identify the facts that could change the answer, verify the law applicable
to the relevant events, and explain the consequences, unresolved issues,
and next steps for each option.
```

Include transaction and event dates for historical matters: today's rule may not be the rule that governed the event. Share documents only through a host whose data handling is suitable for their sensitivity.

## How it works

**Stable reasoning. Live law.** The skill retains durable methods for analyzing a business situation and directs the agent to verify rules that can change when they materially affect the answer.

Three design choices support that approach:

- **Start with facts and the proposed action.** A label such as “freelancer” or “force majeure” is a claim to examine. The agent must establish the facts that determine the legal classification.
- **Keep related legal questions accountable.** Contract obligations, signing authority, regulatory permission, and remedies can affect the same decision. Each material legal proposition has one accountable legal role, and those roles work from shared facts and evidence.
- **Assess readiness for each action.** Different options may need different evidence, approvals, or legal review. Missing prerequisites and unresolved conflicts must remain visible in the resulting advice.

The eight legal roles span issue framing (BL1), company authority and governance (BL2), contracts (BL3), breach and disputes (BL4), tax and financial consequences (BL5), employment (BL6), regulation and compliance (BL7), and investment and cross-border matters (BL8).

One assistant can perform several roles in sequence; separate agents are optional. Knowledge and specialist guidance are loaded only when needed. See the [detailed capability and ownership map](skills/vietnam-business-law-practitioner/knowledge/INDEX.md) and [runtime contracts](skills/vietnam-business-law-practitioner/schemas/) for the exact boundaries.

## Live-law verification

When a legal rule could change the decision, the skill directs the agent to verify the relevant instrument, controlling provision, effective period, and amendments or replacements, then determine whether that authority applies to the facts and dates at hand. Owners can request this verification whenever it becomes necessary during analysis.

A search result helps locate a source; the underlying authority still needs verification. Rates, thresholds, forms, permit mechanics, penalties, and deadlines are therefore researched when needed rather than treated as timeless facts stored in the skill.

If suitable sources or retrieval tools are unavailable, the agent should explain what remains unverified and how that affects the proposed action. The package does not include a legal database or retrieval service.

For the method, see the [search strategy](skills/vietnam-business-law-practitioner/references/search-strategy.md), [source-status guidance](skills/vietnam-business-law-practitioner/references/source-status.md), and [authority-resolution contract](skills/vietnam-business-law-practitioner/schemas/authority-resolver.md).

## Status

**v0.2.0 · Early dogfooding · Runtime validation ongoing**

The repository contains the BL1–BL8 reasoning guidance, shared-state and composition contracts, authority-verification workflow, and evaluation tooling. These define intended behavior; they do not establish exhaustive legal coverage or reliable execution across every model, host, and matter.

Results depend on the facts and documents supplied, available authority, retrieval access, and model behavior. The evaluation work is intended to expose routing, verification, and composition failures so they can be repaired.

See the [release notes](docs/releases/v0.2.0.md), [Changelog](CHANGELOG.md), and [Roadmap](ROADMAP.md).

## Research and evaluation

For maintainers and contributors, the repository keeps runtime guidance, research provenance, and evaluation evidence separate:

| Location | Purpose |
| --- | --- |
| [`skills/vietnam-business-law-practitioner/`](skills/vietnam-business-law-practitioner/) | Runtime instructions, legal reasoning, specialist guidance, references, and contracts |
| [`research/`](research/README.md) | Research findings, sources, alternative explanations, and unresolved questions |
| [`research/legal-source-retrieval/`](research/legal-source-retrieval/README.md) | Research into discovering, identifying, versioning, and verifying legal authority |
| [`evals/composition/`](evals/composition/README.md) | Routing, ownership, shared state, composition, and observable runtime evaluation |
| [`evals/freshness/`](evals/freshness/README.md) | Authority freshness and temporal-scope evaluation |
| [`scripts/`](scripts/) | Utilities for recording file reads and semantic events, and checking traces; these do not run an LLM |

A passing trace check is evidence about the checked behavior and candidate. It does not establish that a generated legal answer is correct or validate later changes.

## Contributing

Useful contributions begin with a concrete problem: a missed legal issue, an unsupported conclusion, a source-verification failure, or a decision the current guidance cannot handle clearly. Include the relevant evidence and propose the smallest justified repair.

Read [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow and the [Code of Conduct](CODE_OF_CONDUCT.md) for community participation. Report security concerns through [SECURITY.md](SECURITY.md).

## Responsible use

This is an open-source research and decision-support project, not a law firm or a substitute for professional legal advice or representation. It does not create a lawyer-client relationship. Independently verify material legal conclusions before acting, especially when consequences are significant, irreversible, or deadline-sensitive.

Read the full [Disclaimer](DISCLAIMER.md).

## License

[MIT](LICENSE).
