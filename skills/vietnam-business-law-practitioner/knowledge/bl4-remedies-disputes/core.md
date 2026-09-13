# BL4 — Breach / Remedies / Evidence / Disputes

BL4 resolves what follows after BL3 has established a material obligation/performance state: breach/liability, excuse, available remedies, preservation/deadlines, and dispute posture/procedure under the resolved or explicitly conditioned regime/forum.

This `core.md` is a **JIT router**, not the full BL4 handbook. Load only the capability unit needed for the material proposition.

## Owns

BL4 owns propositions about:

- breach, materiality, attribution, excuse, and liability;
- remedy availability and exercise conditions;
- damages/loss/causation/mitigation, penalty, interest, and other recovery questions;
- notice, objection, reservation of rights, evidence preservation, limitation/deadline state;
- dispute posture, invocation, procedure, urgent protection, and settlement posture under a resolved/conditioned forum/regime;
- claim/remedy/procedural consequences of contractual changes/waivers already committed by BL3.

BL4 does **not** own the whole dispute merely because performance went wrong.

## Does not own

- transaction formation/content/obligations/performance/change state — BL3;
- dispute-resolution clause existence/content and contract-law formation/incorporation/validity/effect as a contractual term — BL3;
- statutory tax consequences — BL5;
- employment classification/pathway — BL6;
- regulatory permission/compliance/enforcement — BL7;
- governing-law/treaty/CISG/international-enforcement overlay — BL8.

## Core distinctions

- deviation ≠ breach;
- breach ≠ liability;
- liability ≠ remedy availability;
- remedy availability ≠ correct exercise;
- commercial seriousness ≠ legal materiality;
- force majeure ≠ generic bad event;
- hardship ≠ force majeure;
- penalty ≠ damages ≠ interest;
- claimed amount ≠ recoverable loss;
- loss ≠ causation;
- negotiation ≠ deadline suspension;
- evidence exists ≠ fact resolved;
- contractual waiver/change (BL3) ≠ claim/remedy/procedural consequence (BL4);
- dispute-clause contractual existence/effect (BL3) ≠ cross-border overlay (BL8) ≠ invocation/procedure/remedies (BL4).

## JIT capability routing

### Breach / excuse / liability

Load `breach-excuse-liability.md` when the question depends on:

- whether a BL3 performance deviation is breach;
- materiality/attribution;
- force majeure, hardship, changed circumstances, third-party failure, or another defense/excuse;
- contractual/statutory risk allocation affecting liability.

### Remedies / loss / mitigation

Load `remedies-loss-mitigation.md` when the question depends on:

- termination/cancellation/performance/payment or another remedy;
- penalty, damages, interest, restitution, or monetary recovery;
- loss, causation, proof, mitigation, duplication, or remedy limits;
- whether several remedies can coexist or require election/conditions.

### Notice / evidence / deadlines

Load `notice-evidence-deadlines.md` when the question depends on:

- notice/default/cure/objection/reservation;
- evidence preservation;
- limitation/prescription/contractual time bars;
- filing/escalation windows;
- preserving a remedy or procedural option while negotiating.

### Dispute posture / procedure / settlement

Load `dispute-posture-procedure-settlement.md` when the question depends on:

- invoking a committed dispute-resolution clause;
- arbitration/court/other forum procedure under the resolved regime;
- dispute escalation/defense/urgent protection;
- settlement posture;
- procedural consequences of a committed BL3 waiver/change/settlement.

Do not load all four units by default.

## Sibling JIT rule

BL4 sibling units are **not a mandatory pipeline**.

A proposition owned by another BL4 unit may be consumed directly from shared state when it is already reliably established and is not material to reopen.

Load the sibling capability only when its owned proposition is unresolved, disputed, stale, contradictory, or material to the current decision.

Examples:

```text
Breach/liability already committed; user asks only about damages evidence
→ remedies-loss-mitigation
```

```text
Remedy already known; user asks whether a notice deadline expires tomorrow
→ notice-evidence-deadlines
```

Do not force:

```text
breach
→ remedies
→ notice
→ dispute procedure
```

for every BL4 question.

## Typical compositions

```text
Supplier delivered 10 days late. Is that legally a breach?
→ breach-excuse-liability
```

```text
Breach already established. Can we terminate and claim damages?
→ remedies-loss-mitigation
→ notice-evidence-deadlines only if exercise/preservation depends on notice/deadline
```

```text
We are negotiating but limitation may expire.
→ notice-evidence-deadlines
→ dispute-posture-procedure-settlement only if filing/escalation decision becomes material
```

```text
Settlement terms were agreed and changed payment obligations.
→ dispute-posture-procedure-settlement for posture
→ BL3 variation-waiver-settlement commits changed contractual state
→ BL4 consumes new state for remaining claim/remedy/procedure questions
```

## Upstream dependency rules

BL4 consumes upstream propositions rather than reconstructing them.

- BL3 resolves transaction, term, obligation, due/performance, contractual waiver/change, and dispute-clause contractual propositions.
- BL8 resolves governing-law/treaty/cross-border enforcement overlay where material.
- BL7 resolves public-law permission/compliance/enforcement propositions.

If new evidence contradicts upstream state, emit `CONTRADICTION_SIGNAL` to the owner. Do not silently rewrite it inside BL4.

## Live authority behavior

Stable BL4 knowledge defines decision structure and proof paths. Use Authority Resolver when current/historical law materially determines:

- breach/materiality/liability/excuse;
- remedy availability/prerequisites;
- penalty/damages/interest/mitigation;
- limitation/deadline/notice requirements;
- arbitration/court/forum procedure;
- urgent/interim relief;
- historical rules at the relevant event/action date.

Do not hardcode penalty ceilings, interest rates, limitation periods, filing windows, remedy lists, forum procedures, or current article numbers.

## Handoff rules

- BL3 → BL4: committed/conditioned obligation, performance, change/waiver, and dispute-clause contractual propositions.
- BL4 → BL3: candidate settlement/amendment/waiver terms only when they may change contractual state; BL3 owns formation/content/change.
- BL4 → BL5: recovery/settlement/payment facts only; BL5 owns statutory tax consequences.
- BL4 ↔ BL7: private breach/remedy does not replace regulatory legality/enforcement analysis.
- BL8 → BL4: governing-law/treaty/international-enforcement overlay where material; BL4 owns dispute posture/procedure/remedies under the resolved or conditioned regime.

## Failure modes

- BL3 performance deviation labeled breach without BL4 analysis;
- every breach treated as termination right;
- force-majeure keyword matching;
- penalty, damages, and interest collapsed;
- claimed loss accepted without causation/proof;
- mitigation ignored;
- notice treated as paperwork;
- negotiation assumed to suspend deadlines;
- dispute-clause content reconstructed inside BL4;
- governing law/forum/procedure/enforcement collapsed;
- BL4 rewriting BL3 obligations during settlement;
- loading all dispute/remedy knowledge for a narrow deadline or evidence question.
