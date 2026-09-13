# Vietnam Business Law Practitioner

Research-first practitioner skill for legally grounded business and commercial decisions in Vietnam.

> **Status:** architecture repair / runtime preflight. The repository is intentionally not a legal encyclopedia and does not yet contain a production-ready legal knowledge base.

## Design principle

**Stable reasoning, live law.**

The repository preserves durable decision methods: issue framing, legal characterization, proposition ownership, authority discipline, evidence handling, cross-domain routing, uncertainty, invalidation, and escalation. Volatile law — rates, thresholds, forms, filing mechanics, permit procedures, tariffs, deadlines, and current implementing rules — is resolved from current authoritative sources at runtime when materially relevant.

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

The runtime uses eight BL tracks:

1. **BL1 — Legal Issue Framing / Regime Selection**
2. **BL2 — Entity / Authority / Ownership / Governance**
3. **BL3 — Contracts / Commercial Transactions**
4. **BL4 — Breach / Remedies / Evidence / Disputes**
5. **BL5 — Tax / Financial Legal Consequences**
6. **BL6 — Employment / People-side Business Law**
7. **BL7 — Regulatory / Market Conduct / Business Compliance**
8. **BL8 — Investment / Cross-border / Trade**

The accountable unit is a **material legal proposition**, not the whole case. A proposition has one owner and may depend on propositions owned by other tracks.

The runtime is a controlled reasoning loop rather than a linear pipeline: BL1 proposes initial routes; owners may call live authority or owner-bound specialists; downstream evidence may trigger late activation or reclassification review; exact dependencies are invalidated explicitly; final readiness is computed per user action.

## Current phase

The repository is being built in this order:

`scope freeze → source mapping → deep research → composition contract → runtime architecture → adversarial evaluation → practitioner knowledge synthesis`

The current implementation is the **Phase 4 architecture-repair preflight**. Substantive law remains intentionally thin until routing, proposition ownership, authority-as-service, state semantics, specialist return paths, invalidation, and per-action synthesis survive adversarial evaluation.

Canonical architecture evals:

- `evals/composition/ct-v0.2.md`
- `evals/composition/runtime-fixtures-v0.2.md`

## Provenance

The project is developed from multi-source research. Third-party skills, repositories, practitioner materials, academic work, and legal-tech systems may be studied as research inputs, but no single external package is treated as the architectural source of truth.
