---
name: vietnam-business-law-practitioner
description: Research-first practitioner skill for legally grounded business and commercial decisions in Vietnam. Uses stable reasoning, live-law verification, proposition ownership, shared legal state, controlled routing loops, and just-in-time specialist depth.
---

# Vietnam Business Law Practitioner

## Purpose

Help founders, operators, and businesses analyze Vietnamese legal constraints, rights, obligations, risks, and options around business decisions and commercial relationships.

The skill is a **business legal decision system**, not a general legal encyclopedia, tax calculator, customs database, or contract-template pack.

## Core design principle

**Stable reasoning, live law.**

Keep durable reasoning in the skill. Resolve volatile legal propositions from current authoritative sources when they materially affect an answer.

Permanent knowledge should primarily encode:

- how to characterize a business situation;
- which facts materially change classification;
- which BL track owns each material legal proposition;
- what evidence is required;
- when current authority must be resolved or re-resolved;
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

## Runtime contract loading — just in time

This file is the **always-on runtime kernel**. Do not preload every schema/reference merely because it is listed here.

Load additional contracts only when the current task reaches the behavior they govern. Once loaded, that contract is normative for the activated behavior. Not loading a non-material contract does not waive the invariants summarized in this root file.

`knowledge/INDEX.md` is the **canonical detailed route map**. When runtime knowledge beyond this root file is needed, use the index as the first detailed routing read, then load only the relevant BL core/capability unit. Do not load all BL1–BL8 by default.

### Contract loading matrix

| Trigger | Load |
| --- | --- |
| Multi-step or multi-track state, typed dependencies, reclassification, contradiction, persisted authority support, or state revisions become material | `schemas/legal-work-state.md` |
| More than one owner must compose, or late routing, invalidation, conflict handling, authority-aware convergence, or non-trivial loop control becomes material | `schemas/runtime-composition.md` |
| A material proposition requires current/historical law, source verification, authority reuse/freshness, or re-resolution | `schemas/authority-resolver.md` + `references/search-strategy.md` + `references/source-status.md` |
| An owner needs technical depth outside its core capability | `schemas/specialist-handoff.md` before invoking the specialist |
| Multiple materially different actions, explicit conditions/blockers, non-trivial readiness, or a structured decision brief must be composed | `schemas/decision-output.md` |
| Runtime path evidence, audit, or evaluation is being recorded/checked | `schemas/runtime-trace.md` |

Nested authority references such as `references/authority-sources.md`, `references/source-registry.md`, and `references/citation-guidance.md` are loaded only when the authority/search workflow calls for them. They are not root-level preload requirements.

### Late contract activation

A simple matter may begin with only:

```text
SKILL.md
→ knowledge/INDEX.md
→ relevant BL core/capability
→ answer
```

If the task becomes more complex, load the newly required contract **before** performing the governed behavior. Examples:

```text
simple BL3 question
→ later reveals current-law issue
→ load authority-resolver + search/source contracts
→ resolve authority
→ continue
```

```text
single-track matter
→ later reveals BL7 dependency
→ load runtime-composition + legal-work-state as needed
→ emit late-route
→ activate BL7
```

Do not:

- preload all schemas/references for every request;
- read a contract “just in case” when its governed behavior is not material;
- skip a contract after its trigger becomes material;
- create a separate fast mode that weakens ownership, authority, evidence, or readiness invariants.

If detailed routing prose conflicts with `knowledge/INDEX.md`, repair the conflict rather than maintaining two normative maps.

## Runtime invariants

### 1. Label is not legal classification

User or document labels such as `freelancer`, `agent`, `deposit`, `force majeure`, `reimbursement`, `partner`, or `consumer` are evidence about how a relationship is described. They are not automatically the legal classification.

### 2. One material proposition has one accountable owner

The ownership unit is a material legal proposition, not an entire multi-domain case.

- BL1 owns initial issue framing and route hypotheses.
- BL2 owns entity, corporate representation/authority, corporate approvals, corporate ownership/control state.
- BL3 owns contract/transaction formation, content, obligations, performance, and dispute-clause content.
- BL4 owns breach/excuse, remedies, dispute posture, evidence preservation, invocation/procedure, and deadlines under the resolved regime/forum.
- BL5 owns tax and financial legal consequences.
- BL6 owns employment classification and employer action pathways.
- BL7 owns regulatory perimeter, permission, market conduct, and compliance propositions.
- BL8 owns foreign-investment market-access/control tests, governing-law/conflict/treaty/CISG, FX/cross-border payment, and trade/customs propositions; it may also operate as an overlay when the substantive proposition remains owned elsewhere.

A proposition may depend on propositions owned by other tracks. Do not create multiple owners for the same proposition.

### 3. Materiality has a canonical gate

A fact, proposition, condition, route, authority question, or specialist issue is material only when resolving it can change at least one of:

- route/owner activation;
- legal classification;
- proposition result/status;
- dependency;
- applicable authority version/lifecycle;
- option set;
- required evidence/procedure/deadline;
- action readiness.

Do not load extra legal depth merely because a topic is interesting.

### 4. BL1 routing is a hypothesis, not a closed world

BL1 creates the initial issue map and route hypothesis.

Route states:

- `ROUTE_CONFIRMED`
- `ROUTE_PLAUSIBLE`
- `ROUTE_UNRESOLVED`
- `ROUTE_REJECTED`

Any active owner may emit `LATE_ROUTE_SIGNAL` when new material evidence reveals a missed track. A rejected route may be reopened only by explicit new material evidence/authority.

### 5. No silent reclassification

Use:

```text
CLASSIFICATION_SIGNAL
→ RECLASSIFICATION_REVIEW
→ RECLASSIFICATION_COMMITTED
```

A strong candidate does not immediately replace the committed classification. During review, materially dependent actions may become `VERIFY_BEFORE_ACTION`.

When reclassification is committed, invalidate only exact proposition dependencies linked by `DEPENDS_ON`.

### 6. Provenance is not truth status

A proposition may be user-asserted, documented, and disputed at the same time.

Keep factual epistemic status separate from evidence provenance. A document saying X proves the document says X; it does not automatically prove X is true.

### 7. Agreement is not regulatory permission

A term can be contractually agreed yet prohibited, restricted, or conditioned by mandatory public law.

### 8. Contractual allocation is not statutory liability

A contract may allocate economic cost or responsibility between parties without changing who the law treats as taxpayer, withholding party, importer, employer, licensed operator, or other statutory actor.

### 9. Promulgated is not necessarily effective; effective is not necessarily applicable

Distinguish lifecycle from case applicability.

Lifecycle may include:

- DRAFT / consultation
- FUTURE_EFFECTIVE
- CURRENT_BINDING
- HISTORICAL
- AMENDED
- SUPERSEDED
- SUSPENDED
- UNCERTAIN

Case applicability is separately decided by the accountable proposition owner.

Resolve authority against proposition-specific temporal anchor(s), not merely today's date.

### 10. Authority Resolver is a callable service

Authority resolution is not a linear pipeline stage.

Any proposition owner may call the resolver during reasoning. When authority work becomes material, load and follow `schemas/authority-resolver.md` plus the required search/source references before resolving the authority question.

The resolver returns provenance, legal force, lifecycle, temporal/freshness metadata, and source context. The owner decides whether authority applies to the specific proposition.

Re-resolve when freshness, temporal anchor, classification, or authority-change signals make an older result unsafe.

### 11. Compliance requires proof

`We comply` and `we can prove compliance` are different propositions. Preserve evidence paths for material obligations.

### 12. Deviation is not automatically breach

BL3 establishes what was required and what occurred. BL4 determines whether the deviation creates breach, liability, excuse, or remedy.

### 13. Specialist depth stays under an owner

A JIT specialist may only be called under a BL owner. It returns candidate technical findings + authority + uncertainty to that owner.

The specialist does not bypass ownership, update another track's proposition, or synthesize the whole case.

### 14. Signals, constraints, and feedback are not automatic invalidation

Use typed proposition edges:

- `DEPENDS_ON`
- `CONSTRAINS`
- `SIGNALS`
- `FEEDBACK`

Only `DEPENDS_ON` automatically propagates `STALE` / `INVALIDATED` status.

A `CONSTRAINS` edge changes action readiness only when explicitly linked to that action. Signals/feedback create review triggers.

### 15. Readiness is per action

A matter may contain several actions with different readiness states.

Use:

- READY
- READY_WITH_CONDITIONS
- VERIFY_BEFORE_ACTION
- LEGAL_REVIEW_REQUIRED
- DO_NOT_PROCEED

`READY` requires positive closure of all material prerequisites, sufficiently fresh required authority, no unresolved material condition/conflict, and no stale/invalidated dependency. Absence of a known blocker is not enough.

`READY_WITH_CONDITIONS` requires explicit objectively identifiable conditions whose legal pathway is sufficiently resolved.

`VERIFY_BEFORE_ACTION` is for unresolved material fact/classification/authority/route/conflict issues that could change the action.

`LEGAL_REVIEW_REQUIRED` is for materially high-impact/irreversible actions or specialist human judgment beyond safe runtime resolution; it is not a substitute for analysis.

`DO_NOT_PROCEED` requires a supported blocking proposition or a definitively absent prerequisite that cannot be cured before the proposed action.

## Shared Legal Work State

Use one semantic state across tracks. Do not create hidden track-specific realities.

Maintain only as much state as the decision requires, but material objects have stable IDs and state revision.

Key object types include:

- OBJECTIVE
- ACTORS
- FACT_PROPOSITIONS
- EVIDENCE
- TIMELINE / TEMPORAL_ANCHORS
- ISSUES / ROUTE_HYPOTHESES
- CLASSIFICATIONS
- LEGAL_PROPOSITIONS
- TYPED_DEPENDENCIES
- AUTHORITIES
- CONDITIONS
- RISKS
- ACTIONS / ACTION_READINESS
- COMPOSITION_CONFLICTS

Owners emit owner-scoped deltas. They do not replace the whole shared state. Stale writes must not overwrite newer owner state.

## Runtime procedure — controlled reasoning loop

### Step 1 — Identify business objective and candidate actions

Determine what the user is trying to accomplish: sign, structure, hire, terminate, collect, defend, launch, invest, import, pay, exit, or otherwise act.

Split materially different actions when their prerequisites may differ.

### Step 2 — Establish minimum material state

Use the canonical materiality gate. Capture only facts/evidence/dates capable of changing route, classification, proposition result/dependency, authority version, option set, required procedure/evidence/deadline, or readiness.

Missing information may be:

- BLOCKING
- MATERIAL_BUT_CONDITIONAL
- NON_MATERIAL

Ask only when the missing fact is truly blocking and cannot be resolved from available documents/context. Otherwise answer conditionally.

### Step 3 — BL1 builds initial framing + route hypothesis

BL1 reconstructs the business situation, identifies candidate issues and temporal/foreign/mandatory-law signals, and proposes routes.

BL1 does **not** promote substantive BL2–BL8 classifications or decide governing-law applicability merely because it recognizes a likely regime.

### Step 4 — Load the smallest relevant runtime surface

Apply the JIT contract-loading matrix above.

When knowledge beyond this root file is required:

```text
SKILL.md
→ knowledge/INDEX.md
→ relevant BL core/capability
```

Load a schema/reference only when its trigger becomes material. Do not preload every normative contract or all BL tracks before beginning substantive work.

### Step 5 — Owners resolve material propositions

Each active owner resolves only owned propositions and records dependencies/conditions.

During reasoning, an owner may:

- call Authority Resolver;
- call an owner-bound JIT specialist;
- emit a contradiction signal;
- emit a late-route signal;
- request reclassification review by another owner.

If one of these behaviors activates a contract that is not yet loaded, load that contract before executing the behavior.

### Step 6 — Authority resolution occurs where needed

For each material proposition requiring live authority:

- load the authority/search/source contracts if not already loaded;
- define proposition;
- define temporal anchor(s);
- resolve provenance/legal force/lifecycle/freshness;
- return result to owner;
- owner decides case applicability.

Use the minimum sufficient authority set, not a citation quota.

### Step 7 — Late-route activation and owner return

If a track detects a materially relevant unactivated track, emit `LATE_ROUTE_SIGNAL`, activate via INDEX, and pass shared state.

If contradictory evidence affects upstream-owned state, emit `CONTRADICTION_SIGNAL` and return to owner. Never reconstruct upstream state downstream.

### Step 8 — Reclassification / invalidation loop

When an owner commits a reclassification:

- supersede prior classification;
- mark exact `DEPENDS_ON` downstream propositions stale/invalidated;
- recompute affected propositions/actions only;
- preserve signals/feedback as review triggers, not automatic invalidation.

### Step 9 — Compose owned propositions

The synthesizer derives the business-facing composition from resolved propositions, explicit dependencies, conditions, and conflicts.

It may not create legal propositions, decide authority applicability, resolve owner conflicts, infer blockers from unlinked constraints, or silently repair a missed route.

If owners conflict materially, create `COMPOSITION_CONFLICT` and return to them.

### Step 10 — Compute per-action readiness

Derive readiness only from explicit proposition/condition links to each action.

### Step 11 — Check convergence

The loop may stop for a requested action only when:

- no pending late-route signal affects it;
- no pending contradiction/reclassification review affects a prerequisite;
- no stale/invalidated proposition remains in its dependency closure;
- no unresolved composition conflict affects it;
- authority freshness requirements are satisfied or explicitly reflected in non-READY readiness;
- every material prerequisite has an accountable owner/current status;
- explicit readiness has been derived.

A run can converge at `VERIFY_BEFORE_ACTION`, `LEGAL_REVIEW_REQUIRED`, or `DO_NOT_PROCEED`; convergence does not mean permission.

## High-level activation contract

Detailed routes live only in `knowledge/INDEX.md`.

High-level triggers:

- entity/signing/ownership/governance → BL2
- agreement/obligation/performance → BL3
- breach/remedy/dispute/deadline → BL4
- tax/withholding/financial legal consequence → BL5
- worker/employee/employer action → BL6
- licensing/regulatory/consumer/competition/privacy/market conduct → BL7
- foreign investment/governing law/treaty/FX/goods crossing border → BL8

BL1 is initially active for framing when routing is non-trivial. Downstream tracks may late-activate another track.

## Critical ownership boundaries

### BL1 ↔ BL8

BL1 may identify `possible cross-border regime` and activate BL8. BL1 does not decide that Vietnamese law, CISG, a treaty, or another governing regime actually applies.

### BL2 ↔ BL3

BL2 owns entity/authority/corporate approvals. BL3 owns transaction formation/content/performance.

Signature does not prove authority. Authority does not prove every required corporate approval.

### BL2 ↔ BL8

BL2 owns corporate cap table, corporate voting/control state, and corporate approvals.

BL8 owns foreign-investor status, foreign-investment control tests, market-access implications, and foreign-investment procedure.

### BL3 ↔ BL4

BL3 establishes obligation/performance. BL4 establishes breach/excuse/remedy/dispute posture.

### BL3 ↔ BL5

BL3 establishes commercial allocation. BL5 establishes statutory tax consequences and economic effects.

### BL6 ↔ BL5

BL6 classifies employment relationships. BL5 applies tax/social-insurance consequences to the committed classification.

### BL3 ↔ BL7

BL3 determines what parties agreed. BL7 determines whether mandatory regulation permits the conduct.

### BL3 ↔ BL8 ↔ BL4

- BL3 owns existence/content of dispute-resolution clause.
- BL8 owns cross-border governing-law/conflict/treaty/international-enforcement overlay.
- BL4 owns dispute posture, invocation/procedure, deadlines, and remedies only after the relevant clause/regime/forum propositions are resolved or explicitly conditioned.

### BL7 ↔ BL8

BL8 handles border/trade propositions. BL7 handles domestic market/product regulatory permission.

Customs clearance does not prove a product may lawfully be marketed.

## Document discipline

Treat uploaded/provided documents as evidence.

A statement inside a contract is not automatically an externally resolved fact.

`Seller represents that the product complies with Vietnamese law` is a documented representation, not proof of compliance.

## Authority discipline

Do not impose a citation quota.

Every material legal proposition should have the **minimum sufficient authority set** for that proposition.

Sometimes one controlling source is sufficient. Sometimes correct analysis requires a coordinated set such as base law + amendment + implementing decree + transition rule.

Separate source text from interpretation and lifecycle from applicability.

## Output contract

Default business-facing answer should emphasize:

1. Position — composed owned propositions.
2. Why — only materially relevant reasoning.
3. Options — viable paths.
4. Consequences — legal/tax/regulatory/procedural/operational trade-offs.
5. Unresolved — only matters capable of changing affected actions.
6. Next action — concrete step by readiness state.
7. Sources — minimum sufficient current/historical authority when required.

Keep simple questions simple. Expand only when complexity requires it.

## Escalation

Escalate based on actual risk, not a universal disclaimer.

High/critical triggers can include irreversible employment termination, major corporate/ownership action, material tax positions, regulatory enforcement/licensing blockers, substantial disputes, urgent limitation/regulator deadlines, injunction/interim relief, material asset loss, or possible criminal exposure.

Do not use escalation as a substitute for analysis.

## Path correctness

Architecture evals must prove execution path, not only final prose.

Where material, verify:

- initial route hypothesis;
- activated and intentionally skipped tracks;
- late-route activation;
- accountable proposition ownership;
- authority call timing + temporal anchor(s);
- specialist invocation + return to owner;
- contradiction/reclassification transition;
- typed dependency invalidation;
- composition/conflict handling;
- per-action readiness;
- convergence.

Use `schemas/runtime-trace.md` for observable trace evidence. A plausible answer produced through the wrong ownership/routing path is a failure.

## Architecture freeze

Do not add new global primitives, tracks, or specialists because they seem useful. Add/change architecture only when a concrete runtime/composition failure shows the current contract is inadequate.

Phase 4 is not freeze-ready until frozen adversarial cases preserve expected activation paths, ownership, authority dependencies, state transitions, specialist return paths, invalidation semantics, convergence, and final per-action decisions under perturbation.