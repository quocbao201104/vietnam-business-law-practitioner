# BL4 JIT Selectivity Fixtures v0.1

**Semantic candidate:** `bd456e45ab50c72e7a073c91d7120979312a50e5`

Purpose: test the BL4 knowledge-synthesis claim that `core.md` routes to the smallest material BL4 capability, sibling units are not a mandatory pipeline, and BL4 internal ownership remains deterministic.

These fixtures test execution path, not merely final legal plausibility.

## BL4-JIT-01 — Late delivery: breach characterization only

### Input state

BL3 has already committed:

- Seller had a delivery obligation due on D;
- delivery occurred on D+10;
- the relevant obligation/performance proposition is current and undisputed.

User asks: **Does the 10-day delay constitute breach?**

### Expected path

```text
SKILL.md
→ knowledge/INDEX.md
→ bl4-remedies-disputes/core.md
→ breach-excuse-liability.md
```

### Required behavior

- activate BL4;
- consume committed BL3 performance state;
- resolve a BL4 breach/liability proposition;
- do not choose remedy merely because breach is analyzed.

### Forbidden reads

- `remedies-loss-mitigation.md`
- `notice-evidence-deadlines.md`
- `dispute-posture-procedure-settlement.md`

unless the fixture itself introduces a new material dependency (it does not).

### Failure examples

- `late → breach` without BL4 characterization;
- loading all four BL4 units;
- jumping directly to penalty/termination.

---

## BL4-JIT-02 — Liability committed: damages proof only

### Input state

A current BL4 proposition already establishes liability. The user now asks only:

**Can the claimed damages be supported by the available invoice, replacement-cost records, and mitigation evidence?**

The liability proposition is not disputed, stale, or contradictory.

### Expected path

```text
SKILL.md
→ knowledge/INDEX.md
→ bl4-remedies-disputes/core.md
→ remedies-loss-mitigation.md
```

### Required behavior

- consume the committed liability proposition from shared state;
- build/assess the loss/recovery proposition;
- keep causation, mitigation, duplication and proof distinct;
- do not reopen breach merely because damages depend on liability.

### Forbidden reads

- `breach-excuse-liability.md`
- `notice-evidence-deadlines.md`
- `dispute-posture-procedure-settlement.md`

### Failure examples

- reconstructing breach from BL3 facts;
- treating invoice amount as recoverable damages;
- using the evidence-preservation unit as the damages merits owner.

---

## BL4-JIT-03 — Remedy committed: timing/deadline only

### Input state

A remedy proposition is already committed. The user asks:

**Is the contractual notice / claim-filing window about to expire?**

No filing mechanics are requested yet.

### Expected path

```text
SKILL.md
→ knowledge/INDEX.md
→ bl4-remedies-disputes/core.md
→ notice-evidence-deadlines.md
```

### Required behavior

Resolve only the temporal/preservation proposition:

```text
trigger
→ clock
→ tolling/suspension/extension
→ expiry / filing window
→ preservation state
```

### Forbidden reads

- `breach-excuse-liability.md`
- `remedies-loss-mitigation.md`
- `dispute-posture-procedure-settlement.md`

### Failure examples

- resolving forum filing mechanics when only the deadline is asked;
- treating negotiation as automatic tolling;
- one global dispute deadline.

---

## BL4-JIT-03-PERTURB — Deadline committed, now ask how to commence arbitration

### Input state

The preceding timing proposition is supplied as reliable shared state:

```text
P-BL4-DEADLINE-01
status: OPEN
expiry_or_window: committed
```

The user now asks:

**How do we commence arbitration under the already committed dispute-resolution clause before that deadline?**

The timing proposition itself is not disputed, stale, contradictory, or material to recalculate.

### Expected path

```text
SKILL.md
→ knowledge/INDEX.md
→ bl4-remedies-disputes/core.md
→ dispute-posture-procedure-settlement.md
```

The dispute unit consumes `P-BL4-DEADLINE-01` from shared state.

### Forbidden read

`notice-evidence-deadlines.md`

The deadline unit may reopen only if timing itself becomes unresolved, stale, contradictory, or materially changes.

### Required behavior

```text
committed deadline proposition
→ procedural dependency
→ invocation / filing mechanics / sequence
```

Do not duplicate or recompute the clock merely because procedure consumes it.

---

## BL4-JIT-04 — Settlement posture returns changed contract state to BL3

### Input state

A dispute exists and BL4 is managing settlement posture. The parties then actually agree a new payment schedule that changes contractual obligations.

### Expected path

```text
SKILL.md
→ knowledge/INDEX.md
→ bl4-remedies-disputes/core.md
→ dispute-posture-procedure-settlement.md
→ settlement terms actually agreed
→ BL3 activation / return
→ bl3-contracts/core.md
→ bl3-contracts/variation-waiver-settlement.md
→ BL3 commits changed contractual state
→ BL4 consumes committed new state for remaining claim/remedy/procedure questions
```

### Required behavior

- BL4 owns settlement posture;
- once contractual terms are actually agreed, BL3 owns formation/content/change state;
- BL4 may resume only from the committed BL3 state.

### Forbidden behavior

```text
BL4 settlement posture
→ BL4 rewrites payment obligation directly
```

### Failure examples

- BL4 creating the new contract state itself;
- treating a settlement discussion as a formed settlement;
- failing to return changed obligations to BL3.

---

## Gate interpretation

A fixture passes only if the observable `READ`/event path matches the candidate-bound oracle. A legally plausible answer reached by loading forbidden sibling units or assigning the proposition to the wrong unit is a failure.

Passing these fixtures would establish BL4 internal JIT/path evidence for this candidate; it would not replace the broader architecture RF/held-out gate.
