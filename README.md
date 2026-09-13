# Vietnam Business Law Practitioner

Research-first practitioner skill for legally grounded business and commercial decisions in Vietnam.

> **Status:** architecture preflight. The repository is intentionally not a legal encyclopedia and does not yet contain a production-ready legal knowledge base.

## Design principle

**Stable reasoning, live law.**

The repository should preserve durable decision methods: issue framing, legal characterization, authority discipline, evidence handling, cross-domain routing, uncertainty, and escalation. Volatile law — rates, thresholds, forms, filing mechanics, permit procedures, tariffs, deadlines, and current implementing rules — should be verified from current authoritative sources at runtime when materially relevant.

## Intended scope

The skill focuses on business and commercial legal decisions in Vietnam:

- entity, authority, ownership, governance;
- contracts and commercial transactions;
- breach, remedies, evidence, and disputes;
- tax and financial legal consequences of business decisions;
- employment and people-side business law;
- licensing, regulatory perimeter, market conduct, and compliance;
- investment, cross-border transactions, and trade interfaces.

Import/export and customs are specialist branches, not the identity of the skill.

## Out of scope

This is not a general Vietnamese-law encyclopedia. Criminal law, family law, inheritance, ordinary citizen disputes, bookkeeping, and generic accounting are outside the core scope unless they materially intersect a business-law decision.

## Architecture

The runtime is organized into eight decision tracks:

1. **BL1 — Legal Issue Framing / Regime Selection**
2. **BL2 — Entity / Authority / Ownership / Governance**
3. **BL3 — Contracts / Commercial Transactions**
4. **BL4 — Breach / Remedies / Evidence / Disputes**
5. **BL5 — Tax / Financial Legal Consequences**
6. **BL6 — Employment / People-side Business Law**
7. **BL7 — Regulatory / Market Conduct / Business Compliance**
8. **BL8 — Investment / Cross-border / Trade**

Each material decision has one owner. Cross-track state is shared rather than silently reinterpreted.

## Current phase

The repository is being built in this order:

`scope freeze → source mapping → deep research → composition contract → runtime architecture → adversarial evaluation → practitioner knowledge synthesis`

The current implementation is the **runtime architecture preflight**. It intentionally keeps substantive law thin until routing, ownership, authority resolution, and composition survive evaluation.

## Provenance

The project is developed from multi-source research. Third-party skills, repositories, practitioner materials, academic work, and legal-tech systems may be studied as research inputs, but no single external package is treated as the architectural source of truth.
