# Vietnam Business Law Practitioner

A research-first Agent Skill for analyzing Vietnamese business and commercial legal questions with current authoritative law.

It is designed for founders, operators, and businesses that need to understand legal constraints, obligations, risks, and available options around real business decisions.

## What it helps with

- company authority, ownership, governance, and approvals;
- contracts and commercial transactions;
- breach, remedies, evidence, and disputes;
- tax and financial legal consequences of business decisions;
- employment and employer-side legal issues;
- licensing, market conduct, consumer, competition, data, and regulatory compliance;
- investment, cross-border transactions, and trade-related legal issues.

It is not intended to be a general Vietnamese-law encyclopedia or an accounting/bookkeeping assistant.

## Approach

**Stable reasoning, live law.**

The skill keeps durable legal reasoning methods in the repository while resolving time-sensitive legal rules from current authoritative sources when they materially affect the answer.

In practice, it:

1. frames the actual business decision and relevant facts;
2. loads only the legal reasoning needed for that issue;
3. verifies current or historically applicable authority when required;
4. preserves uncertainty, evidence status, and cross-domain dependencies;
5. returns a business-facing position, options, consequences, unresolved issues, and next actions.

A user or document label is not automatically accepted as the legal classification, and contractual agreement does not automatically mean regulatory permission.

## Scope

The core practitioner areas are:

- legal issue framing and applicable regimes;
- corporate entity, authority, ownership, and governance;
- contracts and commercial transactions;
- breach, remedies, evidence, and disputes;
- tax consequences;
- employment;
- regulatory and market conduct;
- investment, cross-border matters, and trade.

Specialist topics such as customs classification, preferential origin, transfer pricing, sector regulation, or specialist privacy analysis are loaded only when the specific matter requires that depth.

## Repository structure

```text
skills/vietnam-business-law-practitioner/
├── SKILL.md          # runtime instructions and core invariants
├── knowledge/        # practitioner reasoning by legal decision area
├── references/       # authority, source, search, and citation guidance
├── schemas/          # shared runtime and composition contracts
└── specialist/       # specialist depth when justified

research/             # research provenance and synthesis
evals/                # adversarial and runtime evaluation
scripts/              # supporting runtime/evaluation utilities
```

## Plugin installation

The repository can be used as both a standalone Agent Skill and a repository-backed plugin. Claude Code and Codex share the same `skills/vietnam-business-law-practitioner/` runtime files; the plugin manifests do not maintain a second copy of the skill.

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

Plugin installation packages the reasoning system; it does not itself supply an authoritative legal database or guarantee current-law retrieval. Live-law verification still depends on the host's available source tools and the skill's authority-resolution contract.

## Project documents

- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Disclaimer](DISCLAIMER.md)
- [MIT License](LICENSE)

## Status

Ready for early dogfooding. Core practitioner architecture, capability routing, live-law authority resolution, shared state, composition, and action-readiness behavior are in place; runtime validation continues as real usage surfaces concrete failures.

## License

MIT. See [LICENSE](LICENSE).