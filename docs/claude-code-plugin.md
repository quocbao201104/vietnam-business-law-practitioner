# Claude Code marketplace

The repository is both a Claude Code marketplace and its single plugin. The catalog at [marketplace.json](../.claude-plugin/marketplace.json) points to the repository root, where [plugin.json](../.claude-plugin/plugin.json) declares the plugin. Claude Code discovers the existing `skills/vietnam-business-law-practitioner/SKILL.md` through its default `skills/` directory. Claude Code and Codex therefore share the same runtime skill files.

After the manifests are available from GitHub, run inside Claude Code:

```text
/plugin marketplace add quocbao201104/vietnam-business-law-practitioner
/plugin install vietnam-business-law-practitioner@vietnam-business-law-practitioner
```

Follow the installation prompt and reload plugins or restart the session if requested. Invoke the skill with:

```text
/vietnam-business-law-practitioner:vietnam-business-law-practitioner
```

For an existing marketplace installation, refresh the catalog before updating the plugin:

```text
/plugin marketplace update vietnam-business-law-practitioner
/plugin update vietnam-business-law-practitioner@vietnam-business-law-practitioner
```

For local testing, add the repository checkout path instead of the GitHub repository. Use the repository root so the catalog's relative source resolves correctly.

The plugin packages the existing reasoning system; it does not itself supply authoritative legal databases or guarantee that a host has suitable web/source tools. Current-law verification remains part of the skill's runtime contract.
