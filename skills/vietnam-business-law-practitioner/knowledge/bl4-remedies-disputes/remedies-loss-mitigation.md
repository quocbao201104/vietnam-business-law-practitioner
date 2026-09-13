# BL4 — Remedies / Loss / Mitigation

## Owns

Determining which remedies are legally available after the relevant breach/liability state is established, what loss/causation/proof is required, how mitigation affects recovery, and how penalty, damages, interest, performance, termination, restitution, or other remedy categories differ.

This unit owns **remedy availability and loss/recovery analysis**. It does not establish the underlying BL3 obligation/performance state or reconstruct the breach proposition.

## Does not own

- transaction formation/terms/obligations/performance — BL3;
- breach/excuse/liability proposition or an exclusion/limitation clause's effect on whether liability exists — `breach-excuse-liability.md`;
- notice/evidence-preservation/limitation workflow — `notice-evidence-deadlines.md`;
- forum/invocation/procedure/dispute posture — `dispute-posture-procedure-settlement.md`;
- statutory tax consequences — BL5;
- public-law sanctions/permission — BL7;
- governing-law/treaty/cross-border enforcement overlay — BL8.

## Activate when

Use when the user needs to know what can be done about an established or conditioned BL4 breach/liability state, including:

- preserve/compel performance;
- suspend or withhold where legally available;
- terminate/cancel/exit;
- claim penalty/liquidated amount/interest;
- claim damages/loss;
- seek restitution/return/payment;
- reduce loss or preserve recovery;
- compare remedies or determine whether they can coexist;
- quantify or evidence a recovery position;
- determine the effect of a contractual cap/exclusion/limitation on available remedy or recoverable quantum after liability is otherwise established.

Skip when remedy choice is not material to the current action or already committed in shared state.

## Required state

Where material, consume:

- committed/conditioned BL4 breach/liability/excuse proposition;
- BL3 term/obligation/change propositions relevant to remedy rights;
- contractual remedy/limitation/exclusion/penalty/interest terms;
- loss events and evidence;
- causation facts;
- mitigation actions/opportunities;
- amounts paid/received/saved or avoided where relevant;
- temporal anchors;
- notice/deadline state where remedy preservation depends on it;
- forum/regime proposition where remedy availability depends on it;
- BL8 cross-border overlay where material.

Do not load sibling units merely to consume already reliable propositions from shared state.

## Core distinctions

### Breach/liability ≠ remedy availability

A supported liability proposition does not automatically create every requested remedy.

Resolve each material remedy independently under the applicable contractual/legal regime.

### Termination ≠ generic response to any breach

Do not infer:

```text
BREACH
→ TERMINATE
```

Termination/avoidance/cancellation may depend on breach type/materiality, contractual trigger, notice/cure, timing, election, or other conditions.

### Penalty ≠ damages ≠ interest

Keep separate where material:

- contractual penalty or agreed sanction;
- compensatory damages/loss;
- late-payment/default interest;
- restitution/return;
- price reduction or other adjustment;
- performance/specific relief.

Do not merge calculation bases or availability rules.

### Contract amount ≠ recoverable loss

A claimed amount is not recoverable merely because it appears on an invoice, spreadsheet, budget, forecast, or internal estimate.

Resolve causation, legal recoverability, proof, duplication, mitigation, and contractual/statutory limits where material.

### Loss occurred ≠ caused by breach

Keep the causation link explicit. Multiple events may contribute to the loss.

### Gross loss ≠ net recoverable loss

Where material, identify avoided costs, substitute performance, recoveries, insurance/third-party payments, savings, offsets, or other factors relevant under the applicable regime.

### Mitigation ≠ duty to accept unreasonable sacrifice

Mitigation analysis should ask what reasonable steps were available and what consequence follows from not taking them under the applicable regime. Do not invent a universal obligation or hindsight standard.

### Remedy right ≠ correct exercise

Even a legally available remedy may require notice, timing, cure opportunity, election, procedural step, or evidence preservation. Coordinate with `notice-evidence-deadlines.md` and dispute-procedure state where material.

### Exclusion / limitation ownership follows effect, not clause label

BL3 owns the clause content.

`breach-excuse-liability.md` owns the clause's effect on **whether or to what scope liability exists**.

This unit owns the clause's effect on **available remedy, recoverable amount, damages cap, or recovery limitation after liability is otherwise established**.

Examples:

```text
Seller bears no liability for delay caused by event X.
→ breach-excuse-liability.md
```

```text
Total damages recoverable are capped at amount X.
→ remedies-loss-mitigation.md
```

If one clause has both effects, represent them as separate propositions with separate owners. Do not let both units decide one proposition.

### Contractual limitation ≠ automatically effective

Do not assume a limitation/exclusion/penalty clause has the asserted recovery effect merely because BL3 established its text. Resolve its remedy/recovery effect under the applicable regime within this unit; liability-existence effects remain with `breach-excuse-liability.md`.

## Employment remedy basis

For an employment claim, accept the committed/conditioned BL6 merits proposition
as the upstream substantive basis. A BL3 contract source or a duplicate BL4
breach proposition is not mandatory. Record the BL6 source ID in the remedy's
upstream basis; identify any remaining BL4 claim-liability question explicitly.
Resolve remedy availability, scope and amount using the employment-specific
current/historical authority. Do not apply commercial penalty/damages rules by
analogy or reopen the BL6 ground merely because a remedy depends on it.

## Decision procedure

1. **State the objective.** Preserve performance, obtain payment, exit, recover loss, reduce exposure, protect assets, or settle.
2. **Consume breach/liability state.** Do not reconstruct breach/excuse here.
3. **Inventory candidate remedies.** Include only remedies plausibly supported by contract/current authority.
4. **Resolve prerequisites for each remedy.** Materiality, notice, cure, deadline, election, contractual trigger, forum, or other conditions.
5. **Check coexistence/election issues.** Do not stack remedies automatically.
6. **For monetary recovery, build a loss ledger.** Separate claimed item, amount, causal link, evidence, mitigation, duplication, and uncertainty.
7. **Apply contractual/statutory recovery limits live where material.** Resolve only remedy/quantum effects here; return liability-existence effects to `breach-excuse-liability.md`.
8. **Assess mitigation.** Record reasonable steps taken/not taken and the legal consequence, if any.
9. **Commit remedy status.** Available, available-with-conditions, unavailable, disputed, unresolved, or preserved-but-not-yet-exercisable.
10. **Hand procedural execution to dispute/notice units where needed.** Remedy existence and remedy exercise are not the same proposition.

## Remedy-state pattern

```text
P-BL4-REM-01
remedy: TERMINATION / PERFORMANCE / PENALTY / DAMAGES / INTEREST / RESTITUTION / OTHER
upstream_basis: <committed BL4 liability or BL6 employment merits ID>
term_source: <BL3 commercial term or BL6 employment term ID, if material>
prerequisites: [...]
notice_deadline_dependency: <if any>
status: AVAILABLE / CONDITIONAL / UNAVAILABLE / DISPUTED / UNRESOLVED
```

For damages/loss:

```text
LOSS_ITEM
- amount / range
- causal event
- evidence
- mitigation
- duplication/offset issue
- recoverability status
```

Do not force speculative precision.

## Evidence requirements

Potential evidence includes:

- contracts and remedy clauses resolved by BL3;
- invoices/payment records;
- replacement transaction evidence;
- lost-sales/profit records where legally material;
- operational cost records;
- repair/rework costs;
- expert/technical evidence where needed;
- communications showing mitigation attempts;
- market quotes/substitute offers;
- records of amounts saved/recovered/offset;
- notices preserving or exercising remedies.

Evidence strength must track the specific remedy/loss proposition. `notice-evidence-deadlines.md` may preserve and map the evidence, but this unit owns whether it is sufficient to resolve the remedy/loss proposition.

## Live authority triggers

Use Authority Resolver where the result depends on:

- remedy availability or prerequisites;
- termination/cancellation rights;
- penalty/liquidated-damages treatment;
- damages categories/causation/proof;
- interest rules;
- mitigation consequences;
- effect of exclusion/limitation clauses on remedy/recovery/quantum;
- historical remedy rules at the relevant event date.

Do not hardcode penalty ceilings, damage formulas, default interest, limitation bases, or statutory remedy lists as stable knowledge.

## Cross-track handoffs

### From breach/excuse/liability

Consume the committed liability/materiality/excuse proposition. If new remedy evidence contradicts that upstream state, emit `CONTRADICTION_SIGNAL` rather than rewriting it.

If an exclusion/limitation term may eliminate or narrow liability itself, return that effect to the breach/liability owner. Keep only remedy/recovery effects here.

### From BL3

Consume remedy clauses, limitation/exclusion terms, payment terms, termination clauses, and changed transaction state. BL4 decides their remedy consequence according to the ownership-by-effect rule.

### To notice/evidence/deadlines

Send exact remedy prerequisites requiring notice, cure, evidence preservation, election, or deadline tracking. This unit retains ownership of whether preserved evidence proves the remedy/loss proposition.

### To dispute posture/procedure

Provide available/conditioned remedies and unresolved procedural prerequisites. That unit owns how/where the claim is pursued under the resolved forum/regime; deadline timing propositions remain owned by `notice-evidence-deadlines.md`.

### To BL5

Provide settlement/recovery/payment facts only when tax consequences are material. BL5 owns statutory tax treatment.

### To BL8

Consume cross-border regime/enforcement constraints where they change remedy availability or realization. BL8 owns the overlay, not the BL4 remedy proposition.

## Failure modes

- every breach treated as termination right;
- remedy selected before breach/liability is resolved;
- penalty, damages, and interest collapsed;
- claimed invoice amount accepted as recoverable loss;
- causation skipped;
- mitigation ignored or applied as hindsight punishment;
- liability-existence effect and recovery-cap effect of one clause collapsed into one proposition;
- contractual cap/exclusion assumed effective from text alone;
- penalty ceiling/base guessed from memory;
- stacking mutually inconsistent remedies without analysis;
- BL4 rewriting BL3 term/change state to make a remedy fit;
- remedy availability confused with procedural ability to exercise it now.

## Escalation

Increase verification for termination, high-value damages, lost-profit claims, penalty/limitation clauses, urgent asset-protection needs, disputed causation, uncertain mitigation, or remedies whose exercise would materially worsen the user's position if wrong.
