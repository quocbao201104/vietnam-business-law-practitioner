# BL3 JIT Fixtures v0.1

**Semantic candidate:** `1ce89ad5f624d541b8ebeb4673b10b0ef4ae95ba`

Purpose: test BL3 internal JIT selectivity and the repaired BL3↔BL4 / BL3↔BL8 ownership boundaries. These fixtures test execution path, not just final prose.

## BL3-JIT-01 — unsigned PO + email acceptance

### Scenario

Buyer sends an unsigned purchase order. Seller replies by email: `Accepted. We will deliver on 30 September.` The user asks only whether a transaction was formed. Signatory authority, governing law, performance, and later changes are not disputed or material in the fixture.

### Expected path

```text
READ SKILL.md
READ INDEX.md
ACTIVATE BL3
READ bl3-contracts/core.md
READ bl3-contracts/formation-transaction-state.md
→ resolve formation proposition
→ RUN_CONVERGED
```

### Forbid

Do not load:

- `document-stack-terms.md`
- `obligations-conditions-performance.md`
- `variation-waiver-settlement.md`

unless the fixture is materially changed.

Do not infer `no signature → no contract`.

---

## BL3-JIT-02 — executed MSA + Order Form conflict

### Scenario

Formation is undisputed. The parties have one executed MSA and one executed Order Form. They contain inconsistent payment timing provisions. The user asks which contractual payment term governs. There is no later amendment and no performance dispute.

### Expected path

```text
READ SKILL.md
READ INDEX.md
ACTIVATE BL3
READ bl3-contracts/core.md
READ bl3-contracts/document-stack-terms.md
→ resolve incorporation/precedence/term proposition
→ RUN_CONVERGED
```

Formation state is already reliably established in shared state and must be consumed without loading `formation-transaction-state.md`.

### Forbid

- `formation-transaction-state.md`
- `obligations-conditions-performance.md`
- `variation-waiver-settlement.md`

The existence of a current-law question inside BL3 does not route substantive domestic contract-law applicability to BL1; BL3 calls Authority Resolver directly if live authority becomes material.

---

## BL3-JIT-03 — fixed term, due/performed question

### Scenario

A single executed contract is undisputed. The governing term is already established: delivery is due on 1 September. The only question is whether delivery became due and whether delivery occurred by that date. There is no dispute about formation, document stack, or later variation.

### Expected path

```text
READ SKILL.md
READ INDEX.md
ACTIVATE BL3
READ bl3-contracts/core.md
READ bl3-contracts/obligations-conditions-performance.md
→ resolve due/performance state
→ RUN_CONVERGED
```

### Forbid

- `formation-transaction-state.md`
- `document-stack-terms.md`
- `variation-waiver-settlement.md`

A performance state such as `LATE`, `DEFECTIVE`, or `NON_PERFORMED` is still a BL3 proposition. Do not promote it to `BREACH` inside BL3.

### BL3-JIT-03-PERTURB — delivery 10 days late

Change only one fact: delivery occurred 10 days after the due date, and the user now asks whether there is a breach/remedy consequence.

Expected path:

```text
BL3 obligations/performance
→ commit performance state = LATE
→ LATE_ROUTE_SIGNAL BL4
→ ACTIVATE BL4
→ READ bl4-remedies-disputes/core.md
→ BL4 resolves breach/excuse/remedy proposition
→ RUN_CONVERGED
```

Forbid:

```text
BL3 obligations
→ PROPOSITION_STATUS = BREACH
```

The perturbation proves the internal BL3 unit stops at performance state and hands the legal consequence to BL4.

---

## BL3-JIT-04 — settlement changes payment schedule after dispute

### Scenario

A payment dispute already exists. BL4 owns the dispute/settlement posture. The parties then reach a written settlement changing the payment schedule. The user asks what obligations now govern and what happens to the existing claim posture.

### Expected composition

```text
READ SKILL.md
READ INDEX.md
ACTIVATE BL3
READ bl3-contracts/core.md
READ bl3-contracts/variation-waiver-settlement.md
ACTIVATE BL4
READ bl4-remedies-disputes/core.md

BL4: current dispute/settlement posture
→ settlement terms reached
→ BL3 commits changed contractual obligation state
→ BL4 consumes committed BL3 state
→ BL4 resolves remaining claim/remedy/procedure consequence
→ RUN_CONVERGED
```

### Forbid

- BL4 rewriting BL3 transaction/obligation state;
- BL3 deciding that a damages claim, limitation right, arbitration objection, or other procedural/remedy right is waived merely because BL3 resolved settlement/change text;
- unrelated BL3 formation/document units unless a real material dependency is introduced.

---

## Shared pass rule

A fixture passes only if:

1. required file reads are observable against the bound candidate;
2. forbidden sibling units remain unread;
3. sibling propositions already committed in shared state are consumed without reopening their knowledge unit;
4. proposition ownership matches BL3/BL4 boundaries;
5. final prose does not rescue an incorrect execution path.
