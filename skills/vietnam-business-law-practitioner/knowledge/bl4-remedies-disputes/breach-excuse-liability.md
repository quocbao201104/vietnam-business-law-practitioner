# BL4 — Breach / Excuse / Liability

## Owns

Determining whether a committed BL3 obligation/performance deviation supports a breach/liability proposition, including materiality, attribution, contractual/statutory excuse, force-majeure/hardship-type issues, risk allocation, and other defenses that affect whether or to what scope liability exists.

For a commercial claim, this unit starts **after BL3 has established the relevant obligation, due state, and performance state**. For an employment claim, consume BL6 employment merits/state instead; resolve only any still-open claim-liability consequence, without reconstructing BL6 grounds or terms. It does not reconstruct the contract or decide the remedy merely because breach is established.

## Does not own

- contract formation, term content, obligation, due state, or performance state — BL3;
- remedy selection, damages quantum, penalty, interest, mitigation consequence, recovery caps/quantum limits — `remedies-loss-mitigation.md`;
- notice/evidence preservation/limitation workflow — `notice-evidence-deadlines.md`;
- forum/procedure/dispute posture — `dispute-posture-procedure-settlement.md`;
- employment classification — BL6;
- regulatory legality — BL7;
- governing-law/treaty/cross-border enforcement overlay — BL8.

## Activate when

Use for a material commercial breach/liability question from committed BL3 deviation, or a still-open employment claim-liability consequence from committed BL6 merits. Do not repeat the upstream merits.

Typical triggers:

- late, partial, defective, refused, or non-performance;
- anticipatory/threatened non-performance where legally material;
- dispute about whether the obligation was actually due;
- force majeure, hardship, impossibility, changed circumstances, third-party failure, government action, or other excuse/risk-allocation argument;
- dispute about causation/attribution of the non-performance;
- contractual exclusion/limitation/risk-allocation term that may affect **whether or to what scope liability exists**.

Skip when breach/liability is not material to the requested action or already reliably committed in shared state.

## Required state

Where material, consume from shared state:

- BL3 obligation proposition;
- source term/document proposition;
- due/condition state;
- actual performance/deviation state;
- variation/waiver/change proposition where relevant;
- relevant BL2 authority/approval state if the disputed act depends on it;
- BL7 public-law state where legality materially affects the liability proposition;
- BL8 governing-law/treaty proposition where cross-border law is material;
- temporal anchor(s);
- evidence supporting and disputing the deviation/excuse.

A sibling BL3/BL4 knowledge unit need not be loaded merely because its proposition is consumed. Load it only when the owned proposition is unresolved, disputed, stale, contradictory, or material to reopen.

## Core distinctions

### Deviation ≠ breach

`Late`, `partial`, `defective`, `not received`, or `not accepted` are BL3 performance states. BL4 asks whether the applicable contractual/legal regime treats that committed state as breach.

Do not infer:

```text
DELIVERY_LATE
→ BREACH
```

without resolving the BL4 proposition.

### Breach ≠ liability

A breach proposition may still be subject to excuse, attribution, exclusion, limitation, or another rule affecting liability.

Keep separate where material:

```text
BREACH
ATTRIBUTION
EXCUSE / DEFENSE
LIABILITY
```

### Liability ≠ remedy

Liability does not prove that every requested remedy is legally available, proportionate, preserved, or procedurally exercisable.

Remedy analysis belongs to `remedies-loss-mitigation.md`.

### Exclusion / limitation ownership follows effect, not clause label

BL3 owns what the clause says.

This unit owns the clause's legal effect on **whether liability exists or the scope/type of liability itself**, for example:

```text
Seller bears no liability for delay caused by event X.
→ liability-effect proposition
→ breach-excuse-liability.md
```

`remedies-loss-mitigation.md` owns the effect on **available remedy, recoverable quantum, or recovery cap after liability is otherwise established**, for example:

```text
Total damages recoverable are capped at amount X.
→ recovery-effect proposition
→ remedies-loss-mitigation.md
```

If one clause has both effects, create two explicit propositions with separate owners. Do not let both units decide the same proposition.

### Materiality ≠ commercial annoyance

A commercially serious problem is not automatically a legally material/fundamental breach. Resolve materiality under the applicable contract/legal regime rather than intuition.

### Force majeure ≠ generic bad event

Do not keyword-match pandemic, flood, war, outage, supplier failure, government action, or other event into a force-majeure conclusion.

Resolve at least where material:

- applicable source of the excuse;
- event and scope;
- foreseeability/control/avoidance requirements under the applicable regime;
- causal connection to the affected obligation;
- notification/mitigation requirements where they affect the defense;
- duration/scope of relief;
- contractual risk allocation.

### Hardship ≠ force majeure

Economic difficulty, increased cost, or changed circumstances may involve a different legal mechanism from impossibility/prevention. Do not collapse them.

### Third-party failure ≠ automatic excuse

A subcontractor, supplier, platform, carrier, bank, or other third party failing does not automatically shift contractual risk.

Resolve risk allocation and applicable excuse rules.

### Contractual allocation ≠ statutory conclusion

A force-majeure, exclusion, limitation, indemnity, risk-transfer, or warranty clause is BL3 content. BL4 determines the relevant liability/remedy consequence under the applicable regime using the ownership-by-effect rule above.

Private allocation does not displace mandatory public-law obligations owned elsewhere.

## Decision procedure

1. **State the BL4 proposition.** Example: `Does Seller's committed 10-day late-delivery state constitute a breach for which Seller is liable?`
2. **Consume substantive owner state.** Use BL3 obligation/performance/change state for commercial claims or BL6 employment merits/state for employment claims. Do not reconstruct the upstream proposition. If the relevant liability basis is already resolved, pass it to remedies without repeating it.
3. **Resolve breach characterization.** Determine whether the deviation violates the obligation under the applicable regime.
4. **Resolve legal materiality where relevant.** Do not equate severity with a termination/remedy right.
5. **Resolve attribution.** Identify whose conduct/event caused or is legally assigned the deviation where material.
6. **Test excuse/defense/risk allocation.** Resolve only effects on breach/liability here; send remedy/quantum effects to `remedies-loss-mitigation.md`.
7. **Separate defense scope from total immunity.** An excuse may affect only a period, obligation, remedy, or liability component.
8. **Commit BL4 status.** Supported, conditional, disputed, excused in scope, not established, or unresolved.
9. **Hand off remedy questions.** If remedy/recovery becomes material, `remedies-loss-mitigation.md` consumes the committed proposition.
10. **Preserve notice/evidence/deadline needs.** Activate `notice-evidence-deadlines.md` only when those propositions are unresolved/material.

## Liability-state pattern

A useful representation:

```text
P-BL4-BREACH-01
substantive_basis: <BL3 obligation/performance or BL6 merits proposition ID>
upstream_obligation: <P-BL3-OBL-01 for a commercial claim, if material>
upstream_performance: <P-BL3-PERF-01 for a commercial claim, if material>
breach_status: SUPPORTED / NOT_ESTABLISHED / DISPUTED / CONDITIONAL
materiality_status: <if material>
attribution: <resolved / disputed>
excuse_status: NONE / PARTIAL / SUPPORTED / DISPUTED / UNRESOLVED
liability_status: SUPPORTED / LIMITED / NOT_ESTABLISHED / UNRESOLVED
```

These are reasoning states, not statutory labels.

## Evidence requirements

Potential evidence includes:

- committed BL3 obligation/performance evidence;
- notices explaining delay/non-performance;
- event records for alleged excuse;
- operational logs and communications;
- third-party failure evidence;
- mitigation/avoidance efforts relevant to the defense;
- contemporaneous reservation/objection records;
- authority supporting the applicable excuse/liability rule.

Evidence that an event occurred is separate from evidence that it legally excuses the performance.

Evidence sufficiency for the breach/excuse/liability proposition remains owned here even if preservation/mapping is handled by `notice-evidence-deadlines.md`.

## Live authority triggers

Use Authority Resolver where current/historical law materially determines:

- breach/materiality classification;
- force-majeure/hardship/changed-circumstance standards;
- mandatory liability rules;
- legal effect of exclusion/limitation/risk-allocation terms **on breach/liability existence or scope**;
- historical rules at the breach/event date.

Do not hardcode current statutory breach categories, force-majeure elements, penalty/remedy consequences, or article numbers.

## Cross-track handoffs

### From BL3

Consume committed:

- obligation;
- due/condition state;
- performance state;
- variation/waiver state;
- relevant clause content.

If any of these is contradicted by new evidence, emit `CONTRADICTION_SIGNAL` to BL3 rather than rewriting BL3 state.

### To remedies/loss

Provide breach/liability/materiality/excuse status plus the exact upstream obligation and temporal anchor. If a limitation/exclusion clause has a separate recovery/quantum effect, hand that proposition to the remedies unit rather than resolving it here.

### To notice/evidence/deadlines

Provide the evidence items/propositions that require preservation or timing tracking. This unit retains ownership of whether that evidence is sufficient to resolve breach/excuse/liability.

### To BL7

If the dispute reveals a public-law violation/permission question, late-route BL7. BL4 does not convert private breach into regulatory illegality or vice versa.

### To BL8

Use BL8 for governing-law/treaty/cross-border enforcement propositions where material. BL4 owns breach/liability under the resolved or conditioned regime.

## Failure modes

- late/defective performance directly labeled breach without BL4 analysis;
- breach and liability collapsed;
- one exclusion/limitation clause proposition decided by both liability and remedies units;
- recovery cap treated as a liability-existence proposition;
- commercial severity treated as legal materiality;
- force majeure decided by event keyword;
- hardship and force majeure collapsed;
- supplier/third-party failure automatically treated as excuse;
- remedy selected before liability/defense state is resolved;
- BL4 reconstructing BL3 obligation/performance/change state;
- contractual allocation treated as overriding mandatory law;
- current breach law applied to historical event without temporal verification.

## Escalation

Increase verification for termination-sensitive breaches, high-value loss, disputed causation, force majeure/hardship claims, exclusions/limitations, urgent threatened non-performance, repeated breaches, or cases where a liability conclusion would trigger irreversible action.
