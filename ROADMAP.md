# Vietnam Business Law Practitioner — Roadmap

> This roadmap describes possible directions for the project. It is **not a delivery commitment** and it is not a promise that every listed capability will be implemented.
>
> The project follows an evidence-first rule: **map broadly, build narrowly**. New capabilities, specialists, or architecture primitives should be added only when real use, dogfooding, evaluation, or contributor demand shows that they are worth maintaining.

## Project direction

Vietnam Business Law Practitioner is intended to grow from a research-first legal reasoning skill into a broader **business-law practitioner system** for founders, operators, and businesses working in Vietnam.

The long-term shape is not “more Markdown about more laws.” The intended stack is:

```text
LEGAL REASONING KERNEL
BL1 → BL8
        ↓
DOMAIN DEPTH
specialist legal areas when evidence shows core depth is insufficient
        ↓
PRACTITIONER CAPABILITIES
review / draft / negotiate / audit / investigate / comply / dispute / monitor
        ↓
WORK PRODUCTS
contracts / redlines / notices / resolutions / policies / DD / checklists / evidence packs
        ↓
WORK EPISODES
real business matters from decision through action, monitoring, change, and closure
```

The core architecture should stay relatively small even if the useful surface becomes large.

---

## Status legend

| Status | Meaning |
| --- | --- |
| **Current** | Core architecture/capability already exists in the repository. |
| **Near-term candidate** | High-value extension that fits the current architecture and is a strong dogfooding target. |
| **Research candidate** | Worth investigating before implementation. |
| **Specialist candidate** | Add only if recurring cases show BL1–BL8 cannot safely provide enough depth. |
| **Architecture question** | Do not solve by adding a new primitive until a concrete ownership/composition failure is demonstrated. |
| **Deferred / demand-driven** | Useful but not currently prioritized; contributor, user, or sponsor demand may change priority. |

---

# 1. Current foundation

## Legal reasoning kernel — Current

The current core is organized around proposition ownership rather than a giant subject-matter handbook:

- **BL1** — issue framing / regime selection / routing
- **BL2** — entity / authority / ownership / governance
- **BL3** — contracts / commercial transactions
- **BL4** — breach / remedies / evidence / disputes
- **BL5** — tax / financial legal consequences
- **BL6** — employment / people-side business law
- **BL7** — regulatory / market conduct / business compliance
- **BL8** — investment / cross-border / trade

Key architectural foundations already include:

- one material proposition → one accountable owner;
- stable shared legal work state;
- typed dependencies;
- controlled late routing and reclassification;
- live authority resolution with lifecycle/freshness separation;
- proposition-specific temporal anchors;
- per-action readiness;
- bounded specialist handoff;
- composition-conflict lifecycle and convergence;
- JIT contract/knowledge loading;
- semantic ownership independent of single-agent vs multi-agent deployment topology;
- observable runtime/path contracts for evaluation.

The goal of future work is to **reuse this substrate**, not replace it every time a new legal domain appears.

---

# 2. Practitioner capability roadmap

These are capabilities that transform legal reasoning into actual legal work.

## Contract lifecycle — Near-term candidate

Potential capabilities:

- contract review / issue spotting;
- clause-by-clause review;
- risk and negotiation position extraction;
- redline generation;
- clean revised draft generation;
- contract drafting from committed facts/terms;
- clause alternatives and fallback positions;
- version comparison;
- amendment / addendum drafting;
- termination / non-renewal / cure notices;
- obligation extraction;
- renewal / milestone / condition tracking.

Likely ownership substrate: primarily BL3, with BL2/BL4/BL5/BL6/BL7/BL8 contributing owned propositions where material.

Important boundary:

> Drafting is an expression/work-product capability. It must not invent commercial terms, decide authority applicability, silently choose between conflicting legal positions, or convert unresolved law into confident clause text.

## Debt, claim, and dispute workflow — Near-term candidate

Potential capabilities:

- debt/claim viability assessment;
- demand-letter preparation;
- notice / cure / reservation-of-rights workflow;
- evidence preservation and evidence map;
- limitation/deadline tracking;
- settlement options;
- negotiation posture;
- arbitration/litigation preparation pack;
- enforcement-readiness analysis.

Likely substrate: BL3 → BL4, with BL2/BL5/BL7/BL8 where material.

## Corporate actions and governance work — Near-term candidate

Potential capabilities:

- board/member/shareholder resolutions;
- corporate approvals;
- delegation / authorization / power-of-attorney support;
- share issuance / transfer / capital-contribution workflow;
- founder/shareholder changes;
- corporate housekeeping checklists;
- signing authority and approval packs;
- restructuring/dissolution work products.

Likely substrate: BL2, with BL3/BL5/BL8 overlays where material.

## Legal due diligence — Near-term candidate

Potential scopes:

- corporate DD;
- contract DD;
- licensing/compliance DD;
- employment DD;
- tax-law issue spotting;
- dispute/claim DD;
- foreign-investment/cross-border DD;
- vendor/customer/partner DD;
- transaction target DD.

Possible output:

```text
issue
→ owner
→ evidence
→ authority
→ severity/materiality
→ missing information
→ remediation
→ action readiness / deal consequence
```

## Compliance implementation — Near-term candidate

Move beyond “is this compliant?” toward operational legal work:

- applicability assessment;
- compliance gap analysis;
- requirement-to-control mapping;
- policy / SOP generation;
- evidence requirements;
- license/approval/notification checklist;
- recurring obligation register;
- remediation plan;
- audit evidence pack;
- change-impact review.

Likely substrate: BL7 with BL2/BL3/BL6/BL8 depending on the proposition.

## Legal policy and communication drafting — Research candidate

Potential work products:

- internal policies;
- customer-facing terms/policies;
- privacy/data notices;
- employee communications;
- counterpart legal communications;
- complaint responses;
- regulator-response drafts;
- settlement / reservation / breach correspondence.

Legal owners determine substance; the drafting layer expresses the committed position without silently changing it.

## Legal negotiation support — Research candidate

Potential capabilities:

- negotiation issue map;
- mandatory-law constraints;
- negotiable vs non-negotiable terms;
- fallback positions;
- reciprocal concessions;
- clause alternatives;
- legal/commercial trade-off map;
- stop / escalate conditions.

This capability must not turn legal uncertainty into artificial confidence or use generic “closing tricks.”

---

# 3. Business work-episode roadmap

A mature practitioner should be able to carry a business matter through a bounded episode rather than answer one isolated question.

Candidate episodes include:

- form or restructure a company;
- add/remove a shareholder/member;
- raise a seed/venture round;
- enter a distributor/agency/franchise arrangement;
- negotiate and sign a major vendor/customer agreement;
- launch a SaaS/digital service in Vietnam;
- hire, manage, restructure, or terminate employees;
- collect an overdue commercial debt;
- respond to a breach or claim;
- settle a commercial dispute;
- import/export a product;
- take foreign investment;
- make a cross-border payment/loan;
- apply for or maintain a material business permission;
- respond to a regulator/customer/employee complaint;
- acquire/invest in/divest a business;
- close or wind down a business activity.

A work episode may activate several BL owners, practitioner capabilities, artifacts, and specialist depth, but it should preserve the same ownership/state/readiness architecture.

---

# 4. Domain-depth and specialist landscape

The following areas may eventually justify specialist modules. Listing them here does **not** pre-approve implementation.

## Finance / secured transactions — Research / specialist candidate

Possible depth:

- lending;
- guarantees;
- security/collateral;
- perfection/registration;
- priority;
- project finance;
- foreign borrowing;
- banking regulatory overlays.

## Intellectual property — Research / specialist candidate

Possible depth:

- trademark/copyright/patent/right existence and ownership;
- assignment/licensing;
- employee/contractor-created IP;
- technology transfer;
- R&D collaborations;
- IP due diligence;
- enforcement;
- security over IP.

## Real estate / land / construction — Research / specialist candidate

Possible depth:

- land-use/property rights;
- title/encumbrance;
- transfer/lease/development;
- planning/permission;
- construction/EPC;
- project transfer;
- foreign ownership/investment overlay.

## Capital markets / securities — Deferred / demand-driven

Potential areas:

- securities issuance;
- public-company obligations;
- private placements;
- IPO/listing;
- disclosure;
- market conduct.

## Restructuring / insolvency — Research candidate

Potential areas:

- distressed company posture;
- creditor rights;
- restructuring options;
- insolvency proceedings;
- transaction unwind/priority effects;
- distressed M&A.

## Investigations / anti-bribery / fraud — Research candidate

Potential areas:

- internal investigations;
- whistleblowing;
- fraud response;
- anti-bribery controls;
- evidence handling;
- employee/regulatory/dispute composition.

## Sector specialists — Deferred / evidence-gated

Possible future areas:

- logistics / shipping / transport / aviation;
- energy / infrastructure / PPP;
- pharmaceutical / healthcare;
- food / product safety;
- insurance;
- fintech / payments;
- telecommunications;
- cybersecurity;
- environmental regulation;
- specialist privacy/data;
- customs HS classification;
- preferential origin;
- transfer pricing.

A specialist should be added only when recurring runtime/evaluation evidence shows that the responsible BL owner cannot safely resolve the proposition with core reasoning + live authority research.

---

# 5. Architecture research questions

These are deliberately **not** roadmap commitments to add BL9/BL10/etc.

## Property / proprietary-right ownership gap — Architecture question

Several future domains share a pattern:

```text
right exists
→ who owns/holds it?
→ validity
→ priority
→ transferability
→ encumbrance
```

Examples:

- IP rights;
- land/property rights;
- security interests/collateral rights.

These propositions do not always map cleanly to existing BL ownership.

Research path:

```text
adversarial cases
→ freeze ownership oracle
→ try BL1–BL8 composition
→ concrete ownership/composition failure?
   NO  → keep current architecture
   YES → apply the smallest boundary repair justified by evidence
```

Do not create a new global “asset/property” owner merely because the taxonomy looks attractive.

## Specialist threshold — Architecture question

Research when a domain should remain:

- core owner reasoning + live law;
- a new JIT capability inside an existing BL track;
- a specialist depth module;
- an external human-review boundary.

## Artifact correctness — Architecture question

Future drafting/redline/policy capabilities need evaluation beyond “good prose.”

Potential invariants:

- every material clause maps to committed propositions/conditions;
- unresolved legal effects remain visible;
- no invented facts/terms;
- no unsupported blocker/permission;
- no clause silently changes owner conclusions;
- artifact version changes remain traceable to decision changes.

---

# 6. Legal operations roadmap

This is separate from substantive business law. It concerns keeping legal work usable over time.

## Matter and obligation management — Research candidate

Potential capabilities:

- matter registry;
- contract registry;
- entity registry;
- obligation register;
- license/permission register;
- deadline/renewal tracking;
- evidence register;
- action/readiness history.

## Legal-change monitoring — Research candidate

Potential capability:

```text
new/amended authority
→ identify affected authority results
→ identify dependent propositions
→ mark exact support stale/review-required
→ identify affected actions/contracts/policies
→ re-resolve only what is material
```

This should be impact-aware, not a generic “law changed” newsletter.

## Playbooks / self-service legal workflows — Deferred / demand-driven

Examples:

- hire employee;
- sign NDA;
- onboard vendor;
- approve discount/distributor terms;
- respond to overdue invoice;
- process a contract amendment;
- launch a promotion;
- import a product.

Playbooks should route into the same BL ownership/authority system rather than becoming independent rule silos.

## Knowledge and precedent management — Deferred / demand-driven

Possible future support:

- approved clause/playbook knowledge;
- prior matter lessons;
- evidence-backed precedent reuse;
- freshness/version rules;
- organization-specific policy/approval constraints.

---

# 7. Suggested priority bands

These bands are intentionally flexible.

## Foundation / current

- stabilize BL1–BL8 ownership and composition;
- live authority retrieval/freshness;
- JIT loading;
- conflict/convergence semantics;
- single-runtime semantic ownership;
- targeted runtime/path validation.

## High-value next candidates

- contract review / redline;
- contract drafting;
- debt / demand / dispute workflow;
- corporate document generation;
- legal due diligence;
- compliance → checklist / SOP / policy;
- legal-change impact monitoring.

## Research before build

- IP ownership/right lifecycle;
- land/property/right lifecycle;
- secured-transactions priority;
- insolvency/restructuring;
- finance/project finance;
- investigations;
- artifact correctness contracts;
- long-running legal work episodes.

## Demand-driven specialist expansion

- capital markets;
- energy/projects;
- construction;
- pharma/healthcare;
- insurance;
- logistics/shipping;
- fintech;
- telecom;
- environmental;
- specialist privacy;
- HS/origin/transfer-pricing depth.

---

# 8. How roadmap items become real work

A roadmap item should not enter the core simply because it appears useful.

Preferred progression:

```text
user/contributor need
→ concrete scenario(s)
→ research
→ ownership/routing hypothesis
→ adversarial review
→ minimal implementation
→ targeted evaluation/dogfooding
→ local repair
→ only then broader rollout
```

Signals that can justify prioritization include:

- repeated real-world user need;
- recurring runtime/evaluation failure;
- clear missing practitioner capability;
- strong contributor interest;
- domain expert contribution;
- sponsorship/funding for a well-scoped capability;
- maintainability benefit to the wider project.

Funding or sponsorship can influence **priority**, but should not override architecture, evidence, safety, or legal-source standards.

---

# 9. Contributing or sponsoring a direction

If you want to help move an item forward, useful contributions include:

- real anonymized business scenarios;
- adversarial fixtures;
- Vietnamese legal-source research;
- domain-expert review;
- implementation work;
- evaluation/oracle design;
- documentation;
- sponsorship for a clearly scoped research/capability track.

A sponsored feature is still expected to follow the repository's evidence, ownership, authority, and review standards.

The maintainer may reprioritize, defer, narrow, reject, or redesign a proposed roadmap item when research shows that the original idea is unsafe, redundant, poorly scoped, or incompatible with the architecture.

---

# 10. What this roadmap does not mean

This roadmap does **not** mean:

- every legal field will become core knowledge;
- every domain gets a new BL track;
- every candidate specialist will be implemented;
- the repository will become a static encyclopedia of Vietnamese law;
- sponsorship guarantees a requested legal conclusion or architectural design;
- listed future work is legally or technically complete.

The intended discipline remains:

> **Stable reasoning, live law. Map broadly, build narrowly. Expand when evidence shows the expansion is worth owning.**
