# Adversarial Runtime Fixtures v0.2

These fixtures test **path correctness**, not Vietnamese substantive-law correctness. They are architecture preflight oracles for routing, proposition ownership, authority calls, state transitions, and readiness.

A correct-looking final answer still fails if the path violates ownership or state semantics.

---

## RF-01 — Late regulatory activation after contract framing

### Scenario

A company asks whether it may sign a SaaS distribution agreement. Initial facts look like ordinary B2B contracting. Later the agreement reveals that the distributor will collect consumer payments and process end-user personal data.

### Expected path

```text
BL1
→ ROUTE_CONFIRMED BL3
→ BL3 reads agreement
→ BL3 emits LATE_ROUTE_SIGNAL(BL7)
→ BL7 owns consumer/data/platform-regulatory propositions
→ BL3 retains contract-content ownership
→ synthesis derives separate sign/operate readiness
```

### Expected skip

BL5 and BL8 remain skipped unless additional facts make tax/foreign issues material.

### Failure oracle

- BL1 route treated as closed world;
- BL3 silently reasons privacy/consumer law itself;
- BL7 never activates because user did not say `privacy` or `consumer`.

---

## RF-02 — Authority service called during owner reasoning

### Scenario

BL6 is deciding whether a planned employer action today requires a current procedural step that may have recently changed.

### Expected path

```text
BL6 owns proposition
→ calls Authority Resolver during reasoning
→ resolver returns provenance + legal force + lifecycle + temporal anchor + verified_at
→ BL6 decides case applicability
→ proposition updates
```

### Failure oracle

- BL6 reasons from memory and only searches after conclusion;
- Authority Resolver becomes owner of applicability;
- search occurs only as a final citation stage.

---

## RF-03 — Candidate reclassification without premature invalidation

### Scenario

A service contractor has several employee-like facts, but key supervision/control evidence remains missing. Company wants to terminate tomorrow and asks PIT/BHXH treatment.

### Expected path

```text
BL6
→ CLASSIFICATION_SIGNAL
→ RECLASSIFICATION_REVIEW
→ old committed classification remains current
→ competing employment candidate explicit
→ terminate action = VERIFY_BEFORE_ACTION
→ BL5 tax result conditional; no committed employment-tax recomputation yet
```

### Failure oracle

- immediate employee classification;
- old contractor state treated as fully safe;
- all downstream propositions invalidated before owner commits reclassification.

---

## RF-04 — Committed reclassification invalidates exact dependents

### Scenario

Additional evidence resolves the RF-03 relationship as employment.

### Expected path

```text
BL6
→ RECLASSIFICATION_COMMITTED
→ old classification SUPERSEDED
→ new classification RESOLVED
→ only propositions with DEPENDS_ON edges become STALE/INVALIDATED
→ BL5 recomputes employment-tax/BHXH proposition
→ unrelated BL2 authority proposition remains current
```

### Failure oracle

- entire case reruns because of track-level dependency graph;
- unrelated propositions invalidated;
- tax result remains on old contractor classification.

---

## RF-05 — Evidence provenance separated from truth status

### Scenario

Founder says invoice was paid. A PDF receipt says `PAID`. Counterparty disputes receipt. No bank record is available.

### Expected state

```text
FACT F-01: payment occurred
status: DISPUTED / unresolved

EVIDENCE:
E-01 USER → supports F-01
E-02 DOCUMENT → supports F-01
E-03 COUNTERPARTY → contradicts F-01
```

### Failure oracle

- `DOCUMENTED` promoted to truth;
- source provenance stored as mutually exclusive fact status;
- counterparty dispute discarded because two sources support payment.

---

## RF-06 — Transition rule separates lifecycle from applicability

### Scenario

A current statute is effective today, but a transition provision preserves the previous regime for contracts entered before its effective date. Contract formed before the change; breach occurs today.

### Expected path

```text
owner identifies formation + breach temporal anchors
→ Authority Resolver returns current instrument + historical/transition authority set
→ lifecycle says current statute CURRENT_BINDING
→ owner evaluates applicability separately for formation/breach propositions
→ possibly different regimes for different propositions
```

### Failure oracle

- one global relevant date;
- current statute automatically applied to every proposition;
- transition rule ignored because current consolidated text was found.

---

## RF-07 — Authority freshness before irreversible action

### Scenario

A regulatory requirement was verified yesterday. Before company launches today, an authority-change signal indicates the implementing rule was suspended.

### Expected path

```text
launch action depends on regulatory proposition
→ prior authority freshness no longer satisfied
→ re-resolve authority
→ dependent proposition STALE until owner review
→ launch action cannot remain READY
```

### Failure oracle

- yesterday's cached authority remains sufficient;
- authority change invalidates whole case instead of exact dependent proposition;
- resolver decides applicability without BL7 owner.

---

## RF-08 — Feedback is not invalidation

### Scenario

BL3 resolves a transaction as legally valid. BL5 later finds the tax economics make the structure expensive but not unlawful.

### Expected path

```text
BL5
→ FEEDBACK to BL3/BL2
→ review trigger for possible restructuring
→ original legal-validity proposition remains current
→ user may choose to restructure or keep deal
```

### Failure oracle

- BL5 feedback automatically invalidates BL3 formation/validity;
- tax economics silently rewrite contract terms.

---

## RF-09 — Specialist returns to owner

### Scenario

BL8 needs preferential-origin analysis for imported goods and calls a technical specialist.

### Expected path

```text
BL8 owns origin/tariff proposition
→ invokes specialist under BL8
→ specialist returns candidate origin finding + authority + missing technical facts
→ BL8 accepts/conditions/rejects
→ only BL8 updates proposition
→ BL7 may later use result for domestic product issue if relevant
```

### Failure oracle

- BL1 calls specialist directly as top-level sibling;
- specialist writes final origin proposition without BL8 review;
- specialist writes final business answer/readiness.

---

## RF-10 — Composition conflict and action-specific readiness

### Scenario

BL2 and BL3 support signing a regulated-service contract. BL7 concludes the service cannot commence until a license is obtained. A second owner output ambiguously suggests commencement may be allowed under an exception, but the exception owner has not resolved the conflict.

### Expected path

```text
ACTION A sign contract
→ prerequisites positively resolved
→ READY if authority freshness satisfied

ACTION B commence service
→ COMPOSITION_CONFLICT on regulatory permission
→ VERIFY_BEFORE_ACTION (or stricter)
→ conflict returned to accountable owners
```

### Failure oracle

- one global readiness;
- synthesizer chooses the exception because it appears business-friendly;
- `no known blocker` used as READY for commencement.

---

## Preflight pass rule

A fixture passes only if the runtime can demonstrate the expected path events and state transitions. Final prose alone is insufficient evidence of architecture correctness.