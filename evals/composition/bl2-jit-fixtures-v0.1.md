# BL2 JIT Path Fixtures v0.1

**Frozen semantic candidate:** `6dec6a6172f99a44353f1f29561ed3015202b6fc`

These fixtures test BL2 **internal JIT routing and ownership boundaries**, not Vietnamese substantive-law correctness.

A plausible final answer fails if the runtime loads the wrong BL2 unit, reconstructs another unit's owned state, bypasses BL3 for disputed contractual content, or lets BL2 decide a BL8 foreign-investment proposition.

---

## BL2-JIT-01 — Founder-owner asks whether they can sign

### Scenario

A founder says: `I own the company. Can I sign this agreement for it?`

The company identity and founder role must be distinguished before representation/signing authority is resolved. No fact makes related-party governance or ownership-state reconstruction material.

### Expected read path

```text
SKILL.md
→ knowledge/INDEX.md
→ bl2-corporate/core.md
→ bl2-corporate/entity-actor-state.md
→ bl2-corporate/authority-representation.md
```

### Expected skips

```text
bl2-corporate/approval-conflict-governance.md
bl2-corporate/ownership-control-state-change.md
```

### Required semantic path

```text
ACTIVATE BL2
→ entity/actor proposition
→ authority/representation proposition
→ no inference owner = company
→ no inference ownership = authority
```

### Failure oracle

- founder ownership is treated as signing authority;
- governance or ownership unit is loaded without material trigger;
- BL3 is asked to decide representation authority.

---

## BL2-JIT-02 — Authorized CEO in a related-party transaction

### Scenario

The CEO's representation authority is already material and can be resolved. The proposed transaction is with a related party, so internal approval/conflict governance must also be resolved. The ownership/voting state for the approval date is already committed and not disputed.

### Expected read path

```text
SKILL.md
→ knowledge/INDEX.md
→ bl2-corporate/core.md
→ bl2-corporate/authority-representation.md
→ bl2-corporate/approval-conflict-governance.md
```

### Expected skip

```text
bl2-corporate/ownership-control-state-change.md
```

when committed ownership/voting state is already available and cannot change the approval result.

### Required semantic path

```text
authority proposition
≠ governance approval proposition

resolved voting state
→ consumed by governance
→ governance does not reconstruct cap table/control
```

### Failure oracle

- signature authority is treated as approval;
- related-party signal is treated as automatic invalidity;
- ownership unit is loaded despite no unresolved ownership/voting proposition;
- governance reconstructs cap table/control state itself.

### Perturbation — voting state at meeting date is unresolved

Change only one fact: the voting entitlement/cap table at the approval meeting date is disputed or unresolved.

Expected path becomes:

```text
approval-conflict-governance
→ ownership/control dependency detected
→ ownership-control-state-change.md
→ committed voting/ownership proposition returned
→ governance resumes and applies approval rule
```

Governance must not finalize the approval proposition before the ownership/voting dependency is resolved or explicitly left unresolved in readiness.

---

## BL2-JIT-03 — Investor signed and paid; asks whether they own 40% now

### Scenario

An investor signed an acquisition/subscription document and paid money. They ask whether they currently own 40% of the company.

The main proposition is completed corporate ownership state, not signing authority.

### Expected read path

```text
SKILL.md
→ knowledge/INDEX.md
→ bl2-corporate/core.md
→ bl2-corporate/ownership-control-state-change.md
```

### Conditional activation

BL3 activates **only if** a contractual formation/content/closing-condition proposition must be resolved before BL2 can determine whether the corporate state changed.

### Expected skip

```text
bl2-corporate/authority-representation.md
```

unless signer authority becomes independently material.

### Required semantic path

```text
signed/payment
≠ completed ownership

contract right — BL3 if material
corporate ownership state — BL2 ownership unit
```

### Failure oracle

- payment or signed document is promoted directly into ownership;
- authority unit loads merely because a document was signed;
- BL2 reconstructs disputed contract content instead of consuming BL3 when contractual meaning is material.

---

## BL2-JIT-04 — Foreign buyer acquires a stake

### Scenario

A foreign buyer acquires or proposes to acquire a stake in a Vietnamese company. Corporate entity, cap-table, voting/control rights, and state-change facts are material. The question also asks whether the acquisition creates foreign-investment control/market-access consequences.

### Expected path

```text
BL2
→ entity-actor-state as needed
→ ownership-control-state-change
→ committed corporate ownership/control facts
→ activate BL8
→ BL8 owns foreign-investor/control/market-access proposition
```

### Forbidden conclusion

BL2 must not emit a substantive conclusion such as:

```text
foreign investor controls the company under the applicable investment-law test
```

It may emit only the corporate facts/state that BL8 consumes.

### Failure oracle

- entity unit reconstructs cap table/control instead of ownership unit;
- BL2 applies a foreign-investment control threshold/test;
- BL8 is skipped despite the foreign-investment proposition being material;
- BL8 reconstructs corporate ownership instead of consuming BL2 state.

---

## Pass rule

A BL2 JIT fixture passes only when both are preserved:

1. **knowledge selectivity** — required BL2 units are read and non-material units remain unread where the fixture forbids them;
2. **ownership path** — entity, authority, governance, ownership, BL3 contractual content, and BL8 foreign-investment propositions remain with their accountable owners.

Final prose alone is not evidence.