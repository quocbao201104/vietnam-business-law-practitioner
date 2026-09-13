# BL6 JIT Fixtures v0.1

**Semantic candidate:** `1c199a5771a1f22f38285bff1ebee84785c25786`

Purpose: test the BL6 knowledge-synthesis claims introduced in v0.1. These fixtures test observable routing/read/ownership behavior, not whether a model can produce plausible employment-law prose.

Use the runtime protocol and walker/checker contracts already defined in this repository. Each fixture should run in a fresh session/process against the bound candidate.

## BL6-JIT-01 — Relationship classification only

### Scenario

The contract calls Worker W a `freelancer`. The business supplies the work account and equipment, fixes the regular schedule, assigns tasks through a manager, requires approval for absences, evaluates W's performance, and can remove W from the role. The user asks only:

> Is the label enough to treat W as a contractor, or does the relationship classification need to be resolved from the actual work facts?

### Expected path

```text
SKILL
→ INDEX
→ BL6 core
→ relationship-classification
```

### Required behavior

- activate BL6;
- keep `freelancer` as evidence, not the classification;
- open/resolve the relationship proposition under BL6 ownership;
- do not load terms, performance/action, or separation units merely because they could become relevant later.

### Forbidden

```text
engagement-terms-work-state
performance-conduct-employer-action
restructuring-separation-protection
```

Also forbid classification based only on label/payment format or on a tax result.

---

## BL6-JIT-02 — Current employment terms/change only

### Scenario

Employee/employer state is already committed and not disputed. The employer proposes changing Employee E's workplace and remuneration. The user asks only whether the proposed change can be made lawfully and what current term/state must be established first.

### Expected path

```text
SKILL
→ INDEX
→ BL6 core
→ engagement-terms-work-state
```

### Required behavior

- consume the committed relationship/employer proposition without reopening it;
- distinguish current term/state from the proposed change;
- do not infer unlimited unilateral-change power from managerial authority;
- keep tax consequences in BL5 and privacy issues in BL7 if they later become material.

### Forbidden

```text
relationship-classification
performance-conduct-employer-action
restructuring-separation-protection
```

unless new material evidence actually contradicts the committed relationship or the requested action changes.

### Perturbation — current vs post-employment confidentiality

Current employee question:

> Does Employee E currently owe confidentiality duties concerning dataset X?

Expected:

```text
BL6 core
→ engagement-terms-work-state
```

Do not load separation/protection merely because the word `confidentiality` appears.

Then assume that current confidentiality proposition is committed and the question changes to:

> Does that duty survive after E leaves?

Expected:

```text
BL6 core
→ restructuring-separation-protection
```

Consume the committed current-term proposition. Do not reopen `engagement-terms-work-state` unless the current term itself becomes unresolved, disputed, stale, or contradictory.

---

## BL6-JIT-03 — Poor performance with desired dismissal

### Scenario

Employee E is underperforming against documented role expectations. There is no committed misconduct proposition. The employer says, "We want E gone — can we dismiss for misconduct?"

### Expected initial path

```text
SKILL
→ INDEX
→ BL6 core
→ performance-conduct-employer-action
```

### Required behavior

- classify the issue from facts rather than desired outcome;
- preserve `performance ≠ misconduct`;
- do not promote misconduct merely because dismissal is preferred;
- commit/condition the performance/action-path proposition under the performance unit.

If the user then asks whether final separation can lawfully proceed, late-load:

```text
→ restructuring-separation-protection
```

and that unit must consume the committed performance/action-path proposition rather than inventing a new ground.

### Perturbation — employment-action timing vs dispute timing

When the question is:

> Under the committed termination pathway, what employment-path notice/process timing must be satisfied before the employer acts?

Expected owner:

```text
BL6 / restructuring-separation-protection
```

If the termination later occurs and is challenged, and the question becomes:

> What is the filing/challenge/limitation deadline for the worker's dispute?

Expected:

```text
BL6 committed employment merits/pathway
→ late-route BL4
→ BL4 timing/procedure unit(s) as material
```

BL6 must not retain claim/dispute-preservation timing merely because the underlying dispute is employment-related.

### Forbidden

- separation unit before final separation becomes material;
- separation unit assigning its own performance/misconduct ground;
- `poor performance → misconduct → dismissal` shortcut;
- BL4 claim/dispute deadline treated as a BL6 employment-action deadline.

---

## BL6-JIT-04 — Controlled reclassification and exact invalidation

### Initial state

Committed state:

```text
P-BL6-REL-OLD
classification: NON_EMPLOYEE
status: RESOLVED
```

Exact dependency:

```text
P-BL5-TAX
DEPENDS_ON → P-BL6-REL-OLD
```

Unrelated current propositions exist under BL2/BL3/BL6 and do **not** depend on `P-BL6-REL-OLD`.

A new non-tax operational evidence set materially contradicts the contractor classification: direct supervision, fixed work schedule, integrated internal role and employer-controlled performance management. Separately, BL5 has already reported that employee treatment would be more expensive.

### Review-stage expected path

```text
SKILL
→ INDEX
→ BL6 core
→ relationship-classification

CLASSIFICATION_SIGNAL / CONTRADICTION_SIGNAL
→ RECLASSIFICATION_REVIEW
→ old classification remains current
→ competing candidate explicit
→ exact dependent action VERIFY_BEFORE_ACTION where material
```

Tax-cost `FEEDBACK` is not classification evidence and cannot trigger automatic invalidation.

### Commit-stage expected behavior

If BL6 resolves and commits the new classification:

```text
RECLASSIFICATION_COMMITTED
old classification → SUPERSEDED
new classification → RESOLVED
P-BL5-TAX → STALE / INVALIDATE
→ BL5 RECOMPUTE
```

Only exact `DEPENDS_ON` dependents may be invalidated/recomputed.

### Forbidden

- reclassification because employee treatment costs more tax/contributions;
- old classification disappearing during review;
- global invalidation of BL2/BL3/unrelated BL6 state;
- `SIGNALS` or `FEEDBACK` treated as automatic invalidation edges;
- BL5 committing the employment classification.

## Gate interpretation

The gate contains exactly four probes: BL6-JIT-01 through BL6-JIT-04. Temporal confidentiality routing is a perturbation of JIT-02; employment-action versus dispute timing is a perturbation of JIT-03.

A correct final employment answer reached by loading the wrong sibling unit, back-solving classification from tax, globally invalidating state, or collapsing employment-action timing into dispute timing is a path failure.
