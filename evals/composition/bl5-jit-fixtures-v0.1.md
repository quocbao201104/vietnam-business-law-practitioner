# BL5 JIT Selectivity Fixtures v0.1

**Purpose:** Test the BL5 knowledge-synthesis claim that internal tax capabilities are loaded selectively, upstream classifications remain owned upstream, and tax economics produce bounded `FEEDBACK` rather than silent rewrite/invalidation.

**Semantic candidate:** `108d7292df27aeec9fbc265a2a224a900cf7178c`

These fixtures test execution path, not whether a final tax number is correct.

---

## BL5-JIT-01 — Characterization only

### User situation

A resolved contract/payment record describes a payment as `reimbursement`. The business event and payment occurrence are already committed by BL3. The user asks what statutory tax role/treatment follows from that event.

### Expected reads

```text
SKILL.md
→ knowledge/INDEX.md
→ bl5-tax/core.md
→ bl5-tax/characterization-events-roles.md
```

### Must skip

```text
base-method-rate-timing.md
documentation-invoice-evidence.md
incentives-structuring-economics.md
```

unless the fixture is materially changed.

### Required behavior

- activate BL5;
- consume the resolved BL3 business/payment event rather than reconstructing whether it occurred;
- treat `reimbursement` as a business label, not the tax conclusion;
- resolve/condition the tax characterization/statutory role proposition;
- converge without loading computation, documentation, or incentives units.

### Forbidden behavior

- `business label = tax characterization`;
- BL5 changing the underlying BL3 payment/transaction fact;
- loading all BL5 units merely because downstream tax questions could exist.

---

## BL5-JIT-01-PERTURB — Foreign payment mode unresolved

### Changed fact

The payment is cross-border, but it is unresolved whether the flow is a service payment, loan, capital contribution, investment flow, or another BL8-owned mode. That classification is material to BL5 treatment.

### Expected path

```text
BL5 core
→ characterization-events-roles
→ LATE_ROUTE_SIGNAL BL8
→ BL8 resolves/conditions cross-border payment mode
→ BL5 consumes BL8 proposition
→ BL5 commits/conditions tax characterization
```

### Required behavior

- BL5 must not guess the foreign-payment mode;
- BL8 owns the cross-border classification;
- BL5 owns only the tax consequence after consuming BL8 state.

### Forbidden behavior

```text
foreign supplier/payment
→ BL5 invents one fixed foreign-tax treatment
```

or BL5 assigning itself ownership of the BL8 payment-mode proposition.

---

## BL5-JIT-02 — Computation only

### User situation

Tax characterization, taxpayer/withholder role, and relevant regime are already committed and fresh. The user asks for the currently applicable base/method/rate/timing proposition.

### Expected reads

```text
SKILL.md
→ knowledge/INDEX.md
→ bl5-tax/core.md
→ bl5-tax/base-method-rate-timing.md
```

### Must skip

```text
characterization-events-roles.md
documentation-invoice-evidence.md
incentives-structuring-economics.md
```

unless an upstream proposition becomes stale/disputed/material to reopen.

### Required behavior

- consume committed characterization/role state;
- resolve current/historical computation authority with the correct temporal anchor;
- keep base, method, rate/threshold, and timing as distinct propositions where material;
- do not reopen characterization merely because computation depends on it.

### Forbidden behavior

- current rate recalled from memory;
- payment date treated as universal tax date;
- contract amount automatically treated as tax base;
- recomputing committed characterization without a concrete trigger.

---

## BL5-JIT-03 — Documentation only

### User situation

Tax treatment is already committed. The user asks whether the available invoice/payment evidence satisfies the documentary conditions for a specific deductibility position.

### Expected reads

```text
SKILL.md
→ knowledge/INDEX.md
→ bl5-tax/core.md
→ bl5-tax/documentation-invoice-evidence.md
```

### Must skip

```text
characterization-events-roles.md
base-method-rate-timing.md
incentives-structuring-economics.md
```

unless a dependency actually becomes material.

### Required behavior

- analyze only the documentary/evidence proposition;
- distinguish invoice validity from VAT credit, deductibility, and accounting recognition;
- preserve any evidence uncertainty;
- leave BL3 transaction/payment occurrence intact even if a tax document is defective.

### Forbidden behavior

```text
invoice exists
→ deductible
```

or:

```text
tax-document defect
→ underlying transaction did not occur
```

---

## BL5-JIT-04 — Structuring feedback only

### User situation

Two prospective upstream options are already committed as lawful/supportable. Their relevant BL5 characterization, computation, and documentary states are already known. The user asks whether the tax consequences materially change which option deserves owner review.

### Expected reads

```text
SKILL.md
→ knowledge/INDEX.md
→ bl5-tax/core.md
→ bl5-tax/incentives-structuring-economics.md
```

### Must skip

```text
characterization-events-roles.md
base-method-rate-timing.md
documentation-invoice-evidence.md
```

because those propositions are already committed and fresh.

### Required behavior

```text
committed upstream OPTION-A / OPTION-B
→ consume committed BL5 consequences
→ compare on like-for-like assumptions
→ FEEDBACK to owning track
→ owner may review prospective option
```

Tax feedback may recommend review of a prospective lawful option. It must not silently rewrite the option.

### Anti-reclassification requirement

Tax economics alone may **not** cause:

- employee → contractor;
- sale → loan;
- payment → capital contribution;
- domestic → cross-border reclassification;
- ownership/residency change;
- any other upstream factual/legal classification change.

Reclassification may be reopened only when new **non-tax facts/evidence** independently make it reviewable by its accountable owner.

### Forbidden behavior

- automatic `INVALIDATE` of an upstream option because tax is expensive;
- `RECLASSIFICATION_COMMITTED` based only on tax economics;
- inventing a third structure/label to manufacture a tax result;
- lowest nominal tax treated as automatically best;
- sham/artificial/fake facts or documents.

---

## Pass condition

BL5 synthesis passes this targeted JIT gate only when all four base fixtures and the foreign-payment perturbation show the expected observable path, reads/skips, owner boundaries, and convergence against `bl5-jit-oracles-v0.1.json`.

A plausible tax answer reached through the wrong internal path is a failure.