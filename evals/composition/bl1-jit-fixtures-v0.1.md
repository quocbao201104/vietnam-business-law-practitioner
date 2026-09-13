# BL1 JIT Selectivity Fixtures v0.1

**Frozen semantic candidate:** `af030a3b491c078c2e278f5a1b2f0ce718090892`

These fixtures test the new BL1 knowledge decomposition and JIT selectivity claim. They are path oracles, not substantive Vietnamese-law tests.

A fixture fails if the answer is plausible but BL1 loads unnecessary capability units, becomes an authority gateway, decides substantive applicability, or skips a unit whose capability is materially required.

---

## BL1-JIT-01 — Messy business story → issue framing only

### Scenario

A founder provides a messy account of a business disagreement involving several people, documents, dates, labels, and desired outcomes, but there is not yet enough structure to know which legal propositions matter. No concrete competing legal regime, historical-law transition, or authority-status ambiguity is yet material.

### Expected path

```text
READ SKILL.md
→ READ knowledge/INDEX.md
→ READ bl1-issue-framing/core.md
→ READ bl1-issue-framing/issue-framing.md
→ frame candidate actions / facts / evidence / questions / owners
→ stop BL1 depth
```

### Forbidden BL1 reads

- `regime-routing.md`
- `temporal-applicability.md`
- `authority-applicability.md`

### Failure oracle

- all BL1 units are loaded “for completeness”;
- authority unit is loaded merely because law will eventually be needed;
- story labels are promoted to downstream classifications.

---

## BL1-JIT-02 — Clear proposition with competing regime → regime routing, not authority gateway

### Scenario

The user asks a reasonably clear contract proposition. The accountable downstream owner is identifiable, but a special/mandatory regime may displace or constrain the ordinary contract route. There is no source-status conflict, lifecycle ambiguity, or transition issue at the BL1 layer.

### Expected path

```text
READ SKILL.md
→ READ knowledge/INDEX.md
→ READ bl1-issue-framing/core.md
→ READ bl1-issue-framing/regime-routing.md
→ create/adjust route hypothesis
→ activate accountable downstream owner
→ downstream owner calls Authority Resolver if current law is needed
```

### Forbidden BL1 reads

- `authority-applicability.md`
- `temporal-applicability.md`
- `issue-framing.md` unless the proposition becomes materially underframed

### Failure oracle

- `authority-applicability.md` loads just because the downstream owner will need live law;
- BL1 calls Authority Resolver as a mandatory gateway for the owner's proposition;
- BL1 decides the substantive regime actually applies.

---

## BL1-JIT-03 — Historical transaction crossing amendment → temporal unit

### Scenario

A transaction formed before a legal amendment; performance/breach occurs after the change. The case requires proposition-specific temporal anchors and transition analysis.

### Expected path

```text
READ SKILL.md
→ READ knowledge/INDEX.md
→ READ bl1-issue-framing/core.md
→ READ bl1-issue-framing/temporal-applicability.md
→ identify FORMATION and BREACH/PERFORMANCE anchors
→ Authority Resolver called against the required anchors
→ lifecycle / transition state recorded
→ CASE_APPLICABILITY remains UNRESOLVED → accountable owner
```

### Forbidden behavior

- one global relevant date;
- BL1 states that a substantive law/regime `applies`;
- authority unit is loaded automatically unless a separate source-status/force ambiguity becomes material.

### Failure oracle

- current consolidated law is used for every event;
- multiple anchors are not preserved;
- BL1 converts lifecycle into substantive applicability.

---

## BL1-JIT-04 — Official guidance vs binding instrument ambiguity → authority applicability unit

### Scenario

The route depends on whether an official-looking source is binding law, non-binding guidance, or an explanation of a separate controlling instrument. This source-status/force ambiguity must be resolved before BL1 can trust the route.

### Expected path

```text
READ SKILL.md
→ READ knowledge/INDEX.md
→ READ bl1-issue-framing/core.md
→ READ bl1-issue-framing/authority-applicability.md
→ distinguish provenance / force / lifecycle
→ call Authority Resolver for the BL1 meta-level authority question
→ update route state as supported
→ substantive applicability remains with downstream owner
```

### Forbidden BL1 reads

- unrelated BL1 units unless a new material signal appears.

### Failure oracle

- official provenance is treated as binding force;
- BL1 becomes substantive applicability owner;
- source ambiguity is ignored and route is confirmed from appearance alone.

---

## Pass rule

Each fixture passes only when observable `READ` order and semantic events preserve the expected JIT path. The claim under test is:

```text
BL1 core
→ smallest material capability unit(s)
→ accountable downstream owner
```

not:

```text
BL1 core
→ load all BL1 knowledge
→ authority gateway
→ downstream owner
```
