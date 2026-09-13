# Codex plugin

Vietnam Business Law Practitioner can be distributed as a Codex plugin containing the existing Agent Skill. The repository root is the plugin root: [plugin.json](../.codex-plugin/plugin.json) points directly to `./skills/`. The standalone skill installation remains supported.

The plugin packages instructions, legal reasoning resources, schemas, references, and specialist routing. It does not include an MCP server, external account connections, hooks, or a separate agent runtime. Live-law retrieval still depends on the host's available web or source tools.

## Install from the repository marketplace

The repository includes a native Codex catalog at [marketplace.json](../.agents/plugins/marketplace.json). Its local source `./` resolves from the repository root to the existing plugin.

In compatible Codex marketplace controls, add:

```text
https://github.com/quocbao201104/vietnam-business-law-practitioner.git
```

Then install `vietnam-business-law-practitioner` from that marketplace.

On a compatible Codex CLI:

```text
codex plugin marketplace add https://github.com/quocbao201104/vietnam-business-law-practitioner.git
codex plugin add vietnam-business-law-practitioner@vietnam-business-law-practitioner
```

Start a new task after installation or update so the host discovers the packaged skill cleanly.

## Package contract

The runtime package uses the existing source of truth:

```text
.codex-plugin/plugin.json
skills/vietnam-business-law-practitioner/
LICENSE
DISCLAIMER.md
```

Do not maintain a second copy of the skill for plugin distribution. Research reports and evaluation infrastructure stay in the repository for maintainers and are not separate runtime skills.

Plugin installation proves only that the host can discover the package. It does not prove legal-source freshness, correct routing, authority resolution, or model behavior; those remain separate runtime concerns.
