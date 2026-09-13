# BL8 Knowledge-Synthesis JIT Fixtures v0.1

**Candidate bound by machine oracle:** `49e5f4e8f137d6e5e423f85a06f37979443eed90`

Purpose: test BL8 internal JIT selectivity, owner-vs-overlay state, proposition-specific treaty routing, BL4 recognition/procedure separation, FX-vs-trade separation, customs-fiscal ownership, specialist return discipline, and BL7 late-route behavior.

A plausible legal answer reached through the wrong unit/owner path is a failure.

## BL8-JIT-01 — Foreign acquisition / investment only

### Scenario

A Singapore buyer proposes to acquire 40% of a Vietnamese company. BL2 ownership/control state is already committed. The user asks whether the foreign acquisition creates a foreign-investment market-access/control condition.

### Required reads

```text
SKILL.md
knowledge/INDEX.md
knowledge/bl8-cross-border/core.md
knowledge/bl8-cross-border/foreign-investment-market-access.md
```

### Expected path

```text
ACTIVATE BL8
→ consume committed BL2 ownership/control proposition
→ resolve/condition P-BL8-INV
→ bl8_role = OWNER
→ substantive_owner = null
→ RUN_CONVERGED
```

### Forbidden path

Do not load governing-law, FX/payment, or trade/customs merely because the investor is foreign. BL8 must not reconstruct BL2 cap table/control.

### BL8-JIT-01-PERTURB — Acquisition price remittance becomes material

New user question:

> How does the buyer remit the acquisition price?

Expected:

```text
committed P-BL8-INV remains current
→ material FX proposition appears
→ load fx-cross-border-payment.md
→ consume investment/BL3/BL2 state
→ resolve/condition P-BL8-FX
```

Forbidden:

```text
FX question
→ recompute P-BL8-INV without new contradictory/stale facts
```

The investment unit is not a mandatory gateway for every later payment question.

---

## BL8-JIT-02 — Cross-border sales contract / governing regime / CISG

### Scenario

A Vietnamese buyer contracts with a foreign seller. BL3 has already committed the contract/choice-of-law facts. The user asks which governing regime applies and whether CISG is material.

### Required reads

```text
SKILL.md
knowledge/INDEX.md
knowledge/bl8-cross-border/core.md
knowledge/bl8-cross-border/governing-law-treaty-enforcement.md
```

### Expected path

```text
ACTIVATE BL8
→ consume BL3 contract/clause state
→ resolve/condition P-BL8-LAW
→ bl8_role = OVERLAY
→ substantive_owner = BL3
→ BL3 consumes regime result for its owned contract propositions
→ RUN_CONVERGED
```

### Forbidden path

- BL8 must not resolve BL3 formation/obligation/performance propositions.
- BL4 must not activate merely because a dispute clause exists if no dispute/procedural action is material.
- A treaty keyword must not route investment or FTA propositions into this unit.

### BL8-JIT-02-PERTURB — Foreign award now needs recognition in Vietnam

New facts make a foreign award/judgment recognition question material.

Expected:

```text
BL8 governing unit
→ resolve recognition/enforcement regime + treaty/applicability conditions
→ P-BL8-ENF bl8_role = OVERLAY
→ substantive_owner = BL4

if user asks where/how/when to file:
→ activate BL4 procedural execution
```

Forbidden:

```text
BL8
→ filing/service/procedural sequence/deadline/remedial execution
```

BL8 determines the viable cross-border recognition/enforcement pathway; BL4 executes the procedure.

---

## BL8-JIT-03 — Foreign SaaS/service payment / FX only

### Scenario

A Vietnamese company pays a foreign SaaS/service provider. The underlying BL3 service/payment purpose is already committed. The user asks what cross-border flow it is and what FX/account/channel conditions matter.

### Required reads

```text
SKILL.md
knowledge/INDEX.md
knowledge/bl8-cross-border/core.md
knowledge/bl8-cross-border/fx-cross-border-payment.md
```

### Expected path

```text
ACTIVATE BL8
→ consume committed BL3 transaction/payment purpose
→ resolve/condition P-BL8-FX
→ bl8_role = OWNER
→ substantive_owner = null
→ RUN_CONVERGED
```

### Forbidden path

- Do not load trade/customs because the payee/payment is foreign.
- Do not load investment unless the payment actually implements an investment/capital proposition.
- Do not load governing-law merely because the currency is foreign.
- BL5 tax result must not back-solve the BL8 flow classification.

---

## BL8-JIT-04 — Imported product / preferential tariff eligibility

### Scenario

Physical goods are imported. A reliable HS proposition is already committed. The user asks whether the goods qualify for preferential origin/tariff treatment under a relevant FTA/trade agreement.

### Required reads

```text
SKILL.md
knowledge/INDEX.md
knowledge/bl8-cross-border/core.md
knowledge/bl8-cross-border/trade-customs-origin-tariff.md
```

### Expected path

```text
ACTIVATE BL8
→ consume committed HS state
→ resolve FTA/trade-agreement + origin + preferential-tariff proposition
→ bl8_role = OWNER
→ substantive_owner = null
→ specialist only if technical HS/origin/customs depth is materially required
→ BL8 owner integrates specialist candidate depth
→ RUN_CONVERGED
```

### Customs-fiscal ownership

If a fiscal proposition becomes material:

```text
customs duty / tariff / customs valuation
→ BL8

VAT / CIT / PIT / withholding / excise / other non-customs-duty tax
→ BL5
```

The same import fiscal item must not have two owners.

### Forbidden path

- Do not recompute committed HS without stale/disputed/contradictory/material reason.
- Specialist must not directly promote a final BL8 proposition.
- Do not load FX merely because an invoice/payment exists.
- FTA existence must not be treated as automatic preferential entitlement.

### BL8-JIT-04-PERTURB — Customs cleared; may we sell domestically?

New user question:

> The goods cleared customs. May we now sell them domestically?

Expected:

```text
BL8 customs state remains committed
→ LATE_ROUTE_SIGNAL BL7
→ BL7 domestic product/market permission proposition
```

Forbidden:

```text
CUSTOMS_CLEARED
→ DOMESTICALLY_PERMITTED_TO_SELL
```

---

## Pass rule

BL8 JIT passes only if all four base probes preserve the smallest valid read set and the perturbations preserve sibling/track handoffs without silent recomputation or ownership drift.

Runtime evidence remains **NOT YET PROVEN** until a fresh candidate-bound observable trace passes `bl8-jit-oracles-v0.1.json`.