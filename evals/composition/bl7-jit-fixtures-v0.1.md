# BL7 JIT Fixtures v0.1

**Semantic candidate:** `2d07f0b6917fedc522532a07a789b2696bf9090a`

Purpose: test the BL7 knowledge-synthesis claims introduced in v0.1. These fixtures test observable routing/read/ownership behavior, not whether a model can produce plausible regulatory prose.

Use the runtime protocol and walker/checker contracts already defined in this repository. Each fixture should run in a fresh session/process against the bound candidate.

## BL7-JIT-01 — Novel platform role / perimeter only

### Scenario

A novel platform connects business sellers and customers. The contractual labels are clear, but the relevant public-law role/regime trigger is not. The user asks only which BL7 regulatory route is materially triggered before any specific license, claim, competition, or data-processing question is analyzed.

### Expected path

```text
SKILL
→ INDEX
→ BL7 core
→ regulatory-perimeter-role
```

### Required behavior

- activate BL7;
- resolve or condition the coarse BL7 routing role/regime trigger;
- keep contractual role from BL3 as evidence rather than the public-law conclusion;
- do not decide an operation-specific controller/processor role or proposition-specific competition status inside perimeter;
- do not invoke specialist depth unless a concrete material technical issue actually emerges.

### Forbidden reads

```text
permission-entry-ongoing-compliance
market-conduct-consumer-claims
data-privacy-digital-operations
```

Also forbid specialist activation based only on the noun `platform`.

---

## BL7-JIT-02 — Permission coverage with role already committed

### Scenario

The BL7 route and coarse regulated role are already committed and not disputed. The user asks whether an existing license/approval covers a newly proposed Activity A at a specific location/channel.

### Expected path

```text
SKILL
→ INDEX
→ BL7 core
→ permission-entry-ongoing-compliance
```

### Required behavior

- consume committed perimeter/route state without reopening it;
- resolve permission scope by actor/activity/product/location/channel/time as material;
- distinguish permission-maintenance obligations from generic recurring conduct/privacy duties;
- do not load market-conduct or data/privacy merely because they might matter for a future action.

### Forbidden reads

```text
regulatory-perimeter-role
market-conduct-consumer-claims
data-privacy-digital-operations
```

unless the route-level proposition itself becomes unresolved, disputed, stale, contradictory, or materially changed.

### Perturbation — technical product-safety depth discovered inside permission

While resolving the same permission proposition, the permission unit encounters a concrete technical product-safety classification issue that is material to whether the approval covers Activity A.

Expected:

```text
permission-entry-ongoing-compliance remains active owner
→ MATERIALITY_DECISION material=true
→ SPECIALIST_CALL owner=BL7
→ specialist returns candidate depth
→ permission unit accepts / conditions / rejects candidate finding
→ BL7 permission proposition committed
```

Forbidden:

```text
reload regulatory-perimeter-role solely to authorize specialist
specialist directly commits final BL7 proposition
specialist becomes top-level owner
```

The specialist call must remain proposition-bound under BL7 ownership.

---

## BL7-JIT-03 — Claim publication / market conduct only

### Scenario

Domestic product permission is already committed and current. The business wants to publish factual Claim C to customers. No material tracking, profiling, personalization, or other data operation is involved in executing the claim.

### Expected path

```text
SKILL
→ INDEX
→ BL7 core
→ market-conduct-consumer-claims
```

### Required behavior

- consume permission state without reopening the permission unit;
- separate claim wording/content from substantiation and mandatory public-law consequence;
- preserve consumer/advertising/competition ownership in the market-conduct unit;
- do not infer that permission to sell authorizes Claim C.

### Forbidden reads

```text
permission-entry-ongoing-compliance
data-privacy-digital-operations
regulatory-perimeter-role
```

unless the current proposition actually introduces a new material permission/data/perimeter issue.

---

## BL7-JIT-04 — Employee monitoring / data legality only

### Scenario

BL6 has already committed the employment relationship and the employment merits/action-path proposition. The employer now asks whether it may deploy a new monitoring system that records worker activity and stores the resulting data.

### Expected path

```text
SKILL
→ INDEX
→ BL7 core
→ data-privacy-digital-operations
```

### Required behavior

- consume BL6 employment context without reconstructing employment merits;
- map the actual processing operation/data flow;
- resolve any operation-specific data role in the data/privacy unit rather than perimeter;
- keep `worker consent/acknowledgement ≠ complete privacy compliance`;
- keep evidence usefulness separate from lawful collection/use.

### Forbidden reads / ownership

```text
market-conduct-consumer-claims
permission-entry-ongoing-compliance
regulatory-perimeter-role
```

unless a distinct route/gate becomes material.

Also forbid BL7 from reopening or replacing the committed BL6 performance/misconduct proposition.

## Gate interpretation

A correct regulatory answer reached through the wrong BL7 sibling path is a failure.

The gate must prove, where applicable:

- perimeter is route-level rather than a universal role owner;
- permission-maintenance does not absorb ongoing conduct/privacy duties;
- active sibling owners can invoke specialists directly under `owner=BL7`;
- specialist findings remain candidate depth until the owning BL7 capability integrates them;
- committed sibling/upstream propositions are consumed without gratuitous reloads.
