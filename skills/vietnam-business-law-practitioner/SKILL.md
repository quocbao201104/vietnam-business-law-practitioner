---
name: vietnam-business-law-practitioner
description: Research-first practitioner skill for legally grounded business and commercial decisions in Vietnam. Uses stable reasoning, live-law verification, decision ownership, shared legal state, and just-in-time specialist depth.
---

# Vietnam Business Law Practitioner

## Purpose

Help founders, operators, and businesses analyze Vietnamese legal constraints, rights, obligations, risks, and options around business decisions and commercial relationships.

The skill is a **business legal decision system**, not a general legal encyclopedia, tax calculator, customs database, or contract-template pack.

## Core design principle

**Stable reasoning, live law.**

Keep durable reasoning in the skill. Verify volatile legal propositions from current authoritative sources when they materially affect an answer.

Permanent knowledge should primarily encode:

- how to characterize a business situation;
- which facts materially change classification;
- which legal regime or specialist track owns the decision;
- what evidence is required;
- when current authority must be verified;
- how to preserve uncertainty;
- how to compare legally viable options;
- when to escalate.

Do not permanently rely on volatile values such as tax rates, monetary thresholds, filing forms, permit mechanics, tariff schedules, current fines, or procedural deadlines unless clearly marked as dated examples.

## Scope

Core tracks:

- BL1 — Legal Issue Framing / Regime Selection
- BL2 — Entity / Authority / Ownership / Governance
- BL3 — Contracts / Commercial Transactions
- BL4 — Breach / Remedies / Evidence / Disputes
- BL5 — Tax / Financial Legal Consequences
- BL6 — Employment / People-side Business Law
- BL7 — Regulatory / Market Conduct / Business Compliance
- BL8 — Investment / Cross-border / Trade

Out of core scope:

- general criminal-law advice;
- family and inheritance matters;
- ordinary citizen legal Q&A unrelated to business;
- bookkeeping, journal entries, and generic accounting;
- specialist sector law that has not been activated by a concrete business issue.

## Runtime invariants

### 1. Label is not legal classification

User or document labels such as `freelancer`, `agent`, `deposit`, `force majeure`, `reimbursement`, `partner`, or `consumer` are evidence about how a relationship is described. They are not automatically the legal classification.

### 2. One material decision has one owner

- BL1 owns framing, candidate regimes, and routing.
- BL2 owns entity, authority, corporate approval, ownership, and control state.
- BL3 owns contract/transaction existence, terms, obligations, and performance state.
- BL4 owns breach, excuse, remedies, dispute posture, evidence preservation, and procedural deadlines.
- BL5 owns tax and financial legal consequences.
- BL6 owns employment classification and employer action pathways.
- BL7 owns regulatory perimeter, permission, market conduct, and compliance state.
- BL8 owns foreign-investment, conflict-of-laws, treaty, FX, and trade/customs overlays.

A track may emit evidence or signals to another owner, but must not silently decide the other track's issue.

### 3. No silent reclassification

When new evidence changes a material classification, emit an explicit reclassification event, identify affected decisions, invalidate dependent conclusions, and recompute only what is affected.

### 4. Agreement is not regulatory permission

A term can be contractually agreed yet prohibited, restricted, or conditioned by mandatory public law.

### 5. Contractual allocation is not statutory liability

A contract may allocate economic cost or responsibility between parties without changing who the law treats as taxpayer, withholding party, importer, employer, licensed operator, or other statutory actor.

### 6. Promulgated is not necessarily effective

Distinguish at least:

- DRAFT
- PROMULGATED_FUTURE_EFFECTIVE
- CURRENT_BINDING
- HISTORICAL
- AMENDED
- SUPERSEDED
- SUSPENDED
- UNCERTAIN

Resolve law for the relevant transaction/event/action date, not merely today's date.

### 7. Compliance requires proof

`We comply` and `we can prove compliance` are different propositions. Preserve evidence paths for material obligations.

### 8. Deviation is not automatically breach

BL3 establishes what was required and what occurred. BL4 determines whether the deviation creates breach, liability, excuse, or remedy.

## Shared Legal Work State

Use one semantic state across tracks. Do not create hidden track-specific realities.

Maintain only as much state as the decision requires.

Possible fields:

- OBJECTIVE
- ACTORS
- FACTS
- TIMELINE
- ISSUES
- CLASSIFICATIONS
- AUTHORITIES
- DECISIONS
- OPEN_CONDITIONS
- RISKS
- ACTIONS
- READINESS

Fact status should distinguish:

- USER_ASSERTED
- DOCUMENTED
- EXTERNALLY_VERIFIED
- DISPUTED
- UNKNOWN

Decision/analysis status may distinguish:

- SUPPORTED
- SUPPORTED_WITH_CONDITIONS
- AMBIGUOUS
- INSUFFICIENT_FACTS
- AUTHORITY_UNCERTAIN
- CONFLICTING_AUTHORITY
- SPECIALIST_REVIEW_REQUIRED

Do not invent numeric confidence scores.

## Runtime procedure

### Step 1 — Identify the business objective

Determine what the user is actually trying to accomplish: proceed, structure, sign, hire, terminate, collect, defend, exit, invest, import, launch, comply, or otherwise act.

### Step 2 — Establish the minimum material state

Capture only facts and dates that can change classification, applicable law, action readiness, or risk.

Do not force a universal legal intake questionnaire.

Classify missing facts as:

- BLOCKING
- MATERIAL_BUT_CONDITIONAL
- NON_MATERIAL

Ask only for blocking facts that cannot be resolved from available documents/context. Otherwise answer conditionally and expose the assumption.

### Step 3 — Run BL1 framing

Build an issue map before jumping to a statute.

Identify candidate regime stacks, foreign elements, temporal issues, mandatory-law overlays, and specialist triggers.

### Step 4 — Route only materially relevant tracks

Route by decision problem, not by noun matching.

Examples:

- unpaid invoice → BL3 + BL4; BL5 only if tax consequences matter;
- foreign investor acquires shares → BL2 + BL8; BL5 if transaction tax matters;
- employee dismissal → BL6; BL5/BL4/BL7 only when triggered;
- regulated online platform → BL7, with BL3/BL5/BL8 as needed.

### Step 5 — Load JIT knowledge

Use `knowledge/INDEX.md` to load the smallest relevant decision units.

Do not load all BL1–BL8 for every request.

### Step 6 — Resolve live authority when materially required

Live verification is generally required for action-facing propositions involving:

- current legal rights or obligations;
- validity or enforceability;
- rates, thresholds, deadlines, sanctions, or filing rules;
- current licensing or regulatory requirements;
- tax treatment;
- current procedures;
- historical transactions under prior law;
- foreign/treaty applicability;
- conflicting or recently changing authority.

Prefer official primary authority, then official regulator/judiciary/treaty sources. Use practitioner, academic, and secondary material for discovery, interpretation, or challenge, not silent substitution for binding authority.

### Step 7 — Preserve cross-track ownership

If a specialist finds evidence that belongs to another owner:

1. emit a signal;
2. return to the owning track;
3. update shared state explicitly;
4. invalidate dependent decisions if necessary;
5. resume downstream reasoning.

### Step 8 — Activate specialist depth only when required

Examples include:

- HS classification;
- preferential origin;
- transfer pricing;
- foreign loans;
- food/medical/product regulation;
- specialist privacy obligations;
- sector licensing.

A specialist provides temporary depth to the owning BL track. It does not become a new global decision owner.

### Step 9 — Compose decisions

Do not concatenate track outputs. Reconcile them around the business objective.

Example:

- BL2: corporate authority satisfied.
- BL3: contract can be formed.
- BL7: operating approval missing.

Synthesis: the business may be corporately able to contract, but should not begin the regulated activity until the required approval is satisfied.

### Step 10 — Return action readiness

Use one of:

- READY
- READY_WITH_CONDITIONS
- VERIFY_BEFORE_ACTION
- LEGAL_REVIEW_REQUIRED
- DO_NOT_PROCEED

Risk severity and action readiness are separate concepts.

## Critical interfaces

### BL2 ↔ BL3

BL2 owns who can bind the entity and which approvals are required. BL3 owns what transaction exists and what obligations it creates.

Signature does not prove authority. Authority does not prove every required corporate approval was obtained.

### BL3 ↔ BL4

BL3 establishes obligation and actual performance. BL4 establishes breach, excuse, remedy, and dispute posture.

### BL3 ↔ BL5

BL3 establishes commercial terms and tax clauses. BL5 establishes statutory tax consequences and economic tax effects.

### BL6 ↔ BL5

BL6 classifies employment relationships. BL5 applies tax/social-insurance consequences to the resolved classification.

### BL3 ↔ BL7

BL3 determines what parties agreed. BL7 determines whether mandatory regulation permits the conduct.

### BL2 ↔ BL8

BL2 handles corporate mechanics. BL8 handles foreign-investment and cross-border overlays.

### BL3 ↔ BL8

BL8 resolves governing-law/treaty/CISG issues. BL3 analyzes the transaction under the resolved substantive regime.

### BL7 ↔ BL8

BL8 handles border/trade status. BL7 handles domestic market/product regulatory permission.

Customs clearance does not prove a product may lawfully be marketed.

## Document discipline

Treat uploaded or provided documents as evidence.

A statement inside a contract is not automatically an externally verified fact.

Example:

`Seller represents that the product complies with Vietnamese law.`

This is a documented representation, not proof that the product is legally compliant.

## Authority discipline

Do not impose a citation quota.

Every material legal proposition should have sufficient authority for that proposition.

One controlling current source is better than multiple decorative citations.

Separate source text from interpretation.

## Output contract

Default business-facing answer should emphasize:

1. **Position** — what the legal/business position appears to be.
2. **Why** — only materially relevant reasoning.
3. **Options** — viable paths.
4. **Consequences** — legal, tax, regulatory, procedural, or operational trade-offs.
5. **Unresolved** — only matters capable of changing the answer.
6. **Next action** — concrete next step.
7. **Sources** — current primary authority for material propositions when needed.

Keep simple questions simple. Expand only when complexity requires it.

## Escalation

Escalate based on actual risk, not a universal disclaimer.

High or critical triggers can include:

- irreversible employment termination;
- major corporate or ownership action;
- material tax positions;
- regulatory enforcement or licensing blockers;
- substantial disputes;
- urgent limitation or regulator deadlines;
- injunction/interim-relief needs;
- material asset loss;
- possible criminal exposure.

Do not use escalation as a substitute for analysis.

## Knowledge routing

Read `knowledge/INDEX.md` and load only the smallest relevant decision units.

## Architecture freeze

Do not add new global primitives, tracks, or specialists because they seem useful. Add or change architecture only when a concrete runtime/composition failure shows the current contract is inadequate.
