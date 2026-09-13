# Architecture Vertical Slices v0.1

These scenarios test routing, ownership, handoff, invalidation, and synthesis. They intentionally avoid testing detailed substantive Vietnamese law at this stage.

## VS-01 — Domestic related-party contract with later breach

### Scenario

A founder owns a Vietnamese company and is also its director. The company wants to sign a large service agreement with another company owned by the founder's spouse. The founder says: `I own my company, so I can sign it.` After signing, the supplier delivers late and the founder wants to terminate immediately and claim a contractual penalty.

### Expected route

```text
BL1
→ identify corporate authority + related-party approval + contract + breach/remedy issues

BL2
→ distinguish ownership, director role, legal representation/authority, and transaction approval/conflict

BL3
→ only after/subject to BL2 state, establish contract terms, delivery obligation, actual delay, penalty/termination clauses

BL4
→ classify breach/excuse/materiality and remedy availability

SYNTHESIS
→ separate whether the company was properly bound/approved from whether late delivery supports termination/penalty
```

### Required invariants

- ownership must not become signing authority;
- signature/representation must not become related-party approval;
- delay must remain `deviation` until BL4 classifies breach/remedy;
- penalty and termination availability must not be inferred only from the existence of clauses;
- if BL2 approval remains unresolved, BL3/BL4 conclusions dependent on binding transaction state remain conditional.

### Blocking failures

- BL1 answers authority itself;
- BL3 ignores unresolved BL2 approval;
- BL4 is activated before an obligation/performance state exists;
- final answer concatenates `BL2 yes / BL4 no` without reconciling what each controls.

---

## VS-02 — Cross-border SaaS purchase with personal data

### Scenario

A Vietnamese SaaS company plans to buy cloud/software services from a foreign provider. The service will process Vietnamese customer personal data. The contract states that the Vietnamese customer bears all Vietnamese taxes and selects foreign governing law. Payment will be made abroad in foreign currency.

### Expected route

```text
BL1
→ identify cross-border contract + data/regulatory + tax + payment/FX issues

BL8
→ classify cross-border service/payment; resolve governing-law/treaty/FX overlay where material

BL3
→ reconstruct service agreement, tax clause, data terms, obligations, governing-law clause

BL7
→ independently test data/privacy/regulatory obligations; contract consent/terms do not establish compliance

BL5
→ resolve statutory tax/withholding/document consequences; tax clause only allocates economic burden

SYNTHESIS
→ state whether the transaction is ready, which contractual/regulatory/tax/payment conditions remain, and what should be verified before signing/payment
```

### Required invariants

- foreign transaction must not be routed to customs merely because it is cross-border;
- foreign governing law must not erase mandatory Vietnamese regulatory analysis;
- tax clause must not rewrite statutory tax roles;
- contract data permission must not become privacy compliance;
- BL5 must consume transaction classification rather than invent a new contract category;
- BL7 and BL5 may return conditions/blockers to BL3 without silently rewriting contract state.

### Blocking failures

- customs/HS path activated for a pure service transaction;
- BL3 treats data clause as proof of regulatory compliance;
- BL5 uses fixed foreign-contractor rates from memory;
- BL8 decides the whole case because a foreign party exists;
- final answer omits a material regulatory/tax condition discovered downstream.

---

## VS-03 — Reclassification invalidates downstream state

### Scenario

A Vietnamese company engages a person under a document titled `Service Agreement`. BL3 initially treats it as a service transaction from the provided document. Later facts show fixed working hours, direct manager supervision, ongoing monthly pay, and integration into the company's normal operations. The company now wants to terminate the relationship and asks about tax consequences.

### Expected route

```text
BL1
→ employment-classification issue becomes material

BL6
→ classify actual relationship

if classification changes:
RECLASSIFICATION_EVENT
→ invalidate affected BL3 service classification
→ invalidate dependent BL5 tax treatment
→ activate appropriate BL6 termination pathway
→ BL5 recomputes tax/social-insurance consequences from updated classification
→ BL4 only if dispute/remedy posture is material
```

### Required invariants

- document title remains documented evidence, not controlling legal classification;
- reclassification must be explicit;
- downstream tax conclusions must be invalidated/recomputed;
- BL5 cannot independently classify the worker;
- original service state must not survive silently into synthesis.

### Blocking failures

- old BL3 service classification remains active after BL6 changes it;
- only final wording changes while dependencies remain stale;
- freelancer/service tax treatment persists after employment reclassification.

---

## VS-04 — Border clearance does not equal market permission

### Scenario

A Vietnamese company imports a regulated physical product from an FTA partner. Customs documentation is accepted and the shipment clears the border. The business then asks whether it may immediately advertise and sell the product in Vietnam.

### Expected route

```text
BL1
→ separate trade/customs from domestic product/market regulation

BL8
→ trade policy, HS/origin/tariff/customs state

BL7
→ domestic product registration/approval/label/advertising/market-conduct requirements

BL5
→ import/tax consequences only when needed

SYNTHESIS
→ customs success is one condition, not proof of domestic market permission
```

### Required invariants

- HS classification ≠ origin ≠ FTA tariff entitlement;
- customs clearance ≠ domestic product approval;
- permission to sell ≠ permission to make every advertising claim;
- product specialist depth is activated only if concrete sector facts require it.

### Blocking failure

`Cleared customs → READY to sell` without BL7 analysis.

---

## Preflight pass rule

Architecture preflight passes these vertical slices only if routing, ownership, state preservation, reclassification, and synthesis are correct **before** scoring substantive legal correctness.
