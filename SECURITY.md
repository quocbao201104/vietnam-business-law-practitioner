# Security Policy

## Supported versions

This repository is under active development. Security fixes are applied to the current `main` branch unless a release explicitly states otherwise.

## Reporting a security issue

Please do not publish sensitive exploit details, credentials, private data, or a working attack against users in a public issue.

If GitHub private vulnerability reporting is available for this repository, use **Report a vulnerability** in the repository's Security tab.

If private reporting is not available, open a minimal public issue asking the maintainer for a private reporting channel. Do not include exploit details or sensitive material in that issue.

Please include, where possible:

- affected file, script, workflow, or runtime behavior;
- impact and realistic attack scenario;
- reproduction steps that do not expose third-party secrets;
- affected commit or version;
- any proposed mitigation.

## Security scope

Security reports may include issues such as:

- unintended command or code execution in repository tooling;
- unsafe file/path handling;
- secret or credential exposure;
- unsafe handling of untrusted repository/runtime input;
- trace or artifact behavior that leaks sensitive information;
- a runtime path that allows untrusted content to bypass an explicit security boundary.

Legal-analysis disagreements, stale law, ownership/routing bugs, or incorrect legal conclusions are important correctness issues but are normally not security vulnerabilities. Report those through ordinary issues with enough evidence to reproduce the problem.

## Sensitive legal material

Do not attach confidential client documents, privileged communications, personal data, credentials, or private business records to a security report unless a private channel has been established and the material is strictly necessary.

Prefer a reduced synthetic reproduction whenever possible.
