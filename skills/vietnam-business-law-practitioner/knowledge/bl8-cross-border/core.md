# BL8 — Investment / Cross-border / Trade

BL8 resolves only the **material cross-border propositions** created by foreign investment, governing-law/private-law treaty questions, cross-border payment/FX rules, and goods trade/customs. A foreign element may activate BL8, but it does not transfer ownership of the whole matter into BL8.

This `core.md` is a **JIT router**, not a foreign-law/customs encyclopedia. Load only the capability unit needed for the material proposition.

## Owns when acting as proposition owner

BL8 owns propositions about:

- foreign-investor status, foreign-investment market access, foreign-investment control/entry/change tests, and investment/market-access treaty commitments relevant to those propositions;
- governing-law/conflict-of-laws, CISG/private-law treaty applicability, and cross-border recognition/enforcement-regime overlay;
- FX/cross-border payment and capital-flow classification;
- goods trade/customs, HS, origin, customs valuation, customs duty/tariff and preferential-treatment propositions, including FTA/trade-agreement propositions relevant to origin/tariff entitlement;
- BL8-owned specialist activation/integration for technical trade/origin/customs depth.

## Overlay role

BL8 may also operate only as a **cross-border overlay** while another track remains substantive owner.

Examples:

- BL2 owns corporate identity, cap table, voting/control and approvals; BL8 owns the foreign-investment consequence of that committed state.
- BL3 owns contract formation/content/obligations and the contractual content/effect of a dispute-resolution clause; BL8 owns governing-law/CISG/private-law treaty overlay.
- BL4 owns dispute posture, invocation, filing mechanics, deadlines and remedies; BL8 owns only the cross-border recognition/enforcement regime and treaty overlay.
- BL5 owns tax consequences; BL8 may supply the foreign payment/investment/trade classification or customs-duty proposition that BL5 consumes where relevant.
- BL7 owns domestic product/service market permission and conduct; BL8 owns border/trade or foreign-investment propositions.

Every committed BL8 proposition must make the dual role operationally explicit:

```text
bl8_role: OWNER | OVERLAY
substantive_owner: BL2 | BL3 | BL4 | BL5 | BL6 | BL7 | null
```

Use `OWNER` when BL8 is the accountable owner of the proposition itself. Use `OVERLAY` when the BL8 proposition conditions another track's substantive proposition/action while that track remains the substantive owner. This marker does not transfer ownership and does not create a new primitive.

For a governing-law overlay on an employment-specific term, BL6 supplies term
content and retains employment merits. BL8 records `OVERLAY` with
`substantive_owner: BL6` and returns the resolved/conditioned regime to BL6.

## Does not own

- corporate mechanics, cap table, voting/control or corporate approvals — BL2;
- ordinary private contract formation/content/obligations — BL3;
- private breach/remedies/claim-preservation timing/procedural execution — BL4;
- VAT/CIT/PIT/withholding/excise or other non-customs-duty statutory tax treatment — BL5;
- employment merits — BL6;
- domestic product/service market permission, privacy/data or market conduct — BL7.

## Core distinctions

- foreign element ≠ import/export;
- foreign element ≠ BL8 owns the whole case;
- corporate control (BL2) ≠ foreign-investment control test (BL8);
- corporate validity ≠ foreign-investment compliance;
- foreign ownership percentage ≠ complete market-access analysis;
- treaty exists ≠ governing-law unit owns the treaty question;
- investment treaty proposition ≠ private-law treaty/CISG proposition ≠ FTA/trade proposition;
- governing law ≠ dispute-clause content ≠ dispute procedure ≠ cross-border recognition/enforcement regime;
- international sale ≠ automatic CISG or automatic Vietnamese commercial law;
- foreign invoice/payment ≠ one fixed FX/capital-flow category;
- cross-border payment ≠ goods trade/customs;
- product name ≠ HS classification;
- HS classification ≠ origin ≠ preferential tariff entitlement;
- shipment country ≠ preferential origin;
- FTA exists ≠ zero tariff;
- Incoterm/private allocation ≠ statutory customs responsibility;
- customs duty/tariff proposition ≠ BL5 non-customs tax proposition;
- customs clearance ≠ domestic market permission;
- specialist finding ≠ committed BL8 proposition.

## JIT capability routing

### Foreign investment / market access

Load `foreign-investment-market-access.md` when the question depends on:

- foreign-investor status;
- foreign-investment market-access conditions/restrictions;
- acquisition/subscription/project/investment-entry trigger;
- foreign-investment ownership/control tests;
- investment/market-access treaty commitments, schedules or investor treatment relevant to entry/control;
- changes in investor/ownership/control/activity that may alter foreign-investment state.

This unit consumes BL2 corporate state; it must not reconstruct cap table/control merely because the investment test depends on them.

### Governing law / private-law treaty / CISG / recognition-enforcement regime

Load `governing-law-treaty-enforcement.md` when the question depends on:

- governing law/conflict-of-laws;
- CISG/private-law treaty applicability/exclusion;
- mandatory-law interaction in a cross-border contract;
- treaty/applicability/recognition conditions for a foreign award/judgment or other cross-border enforcement result.

Do **not** route a treaty question here merely because the word `treaty` appears. Investment/market-access treaty propositions stay with the investment unit; FTA/trade-agreement origin/tariff propositions stay with the trade unit.

BL3 remains owner of contract/clause content. BL4 remains owner of invocation, filing, service, procedural sequence, deadlines, interim/remedial posture and other procedural execution.

### FX / cross-border payment

Load `fx-cross-border-payment.md` when the question depends on:

- legal classification of a cross-border payment/capital flow;
- current/capital/loan/investment/service/goods/distribution payment mode;
- FX/account/channel/registration/reporting conditions;
- a BL8 payment classification needed by BL5.

Do not activate customs merely because payment is foreign.

### Trade / customs / HS / origin / tariff

Load `trade-customs-origin-tariff.md` when actual/planned goods movement or another border/customs proposition is material, including:

- import/export/customs role/state;
- HS classification;
- origin/preferential origin;
- FTA/trade-agreement applicability for preferential origin/tariff;
- customs valuation, customs duty/tariff or preference;
- owner-bound HS/origin/customs specialist depth.

Do not load this unit for a foreign service/software/investment/payment case with no material goods movement.

Do not load all four units by default.

## Sibling JIT rule

BL8 sibling units are **not a mandatory pipeline**.

A committed BL8 proposition may be consumed directly from shared state without loading its owning sibling when reliable and not material to reopen.

Load the sibling only when the proposition is unresolved, disputed, stale, contradictory, or material to reopen.

Examples:

```text
BL2 corporate ownership/control already committed;
user asks only whether foreign acquisition triggers market-access/control condition
→ foreign-investment-market-access
```

```text
Governing regime already committed;
user asks only what BL3 obligation follows under that regime
→ BL3 consumes BL8 state
→ do not reload BL8
```

```text
Cross-border flow already committed as service payment;
BL5 asks only for tax consequence
→ BL5 consumes BL8 state
→ do not reload FX unit
```

```text
HS already committed;
question is only preferential origin
→ trade-customs-origin-tariff
→ consume committed HS proposition
→ do not recompute HS unless material
```

Do not force:

```text
foreign investment
→ governing law/treaty
→ FX/payment
→ trade/customs
```

for every foreign-element question.

## Internal ownership rules

### Foreign element is a materiality signal, not a super-owner rule

First identify the exact proposition changed by the foreign element.

```text
foreign fact
→ what proposition can change?
→ assign accountable owner
→ activate BL8 only for BL8-owned/overlay proposition
```

Do not route an entire case to BL8 merely because one party, shareholder, payment, asset or performance location is foreign.

### Owner vs overlay must be state-visible

A BL8 proposition or handoff is invalidly underspecified when it omits whether BL8 is `OWNER` or `OVERLAY` where that distinction is material.

```text
BL8-owned cross-border proposition
→ bl8_role = OWNER
→ substantive_owner = null

BL8 cross-border proposition conditioning another track
→ bl8_role = OVERLAY
→ substantive_owner = <that track>
```

`OVERLAY` never authorizes BL8 to resolve the substantive owner's proposition.

### Treaty ownership follows the proposition, not the noun

```text
investment / market-access treaty commitment or investor treatment
→ foreign-investment-market-access

private-law governing regime / CISG / conflict treaty
or recognition-enforcement treaty overlay
→ governing-law-treaty-enforcement

FTA / trade-agreement origin or tariff entitlement
→ trade-customs-origin-tariff
```

When a treaty can affect more than one proposition, create separate propositions with separate owners/dependencies rather than one generic `TREATY_APPLIES` state.

### BL2 corporate state ≠ BL8 investment state

```text
BL2
→ entity / cap table / ownership / voting / corporate control / approval

BL8 investment unit
→ foreign-investor / market-access / foreign-investment control consequence
```

BL8 consumes committed BL2 propositions rather than reconstructing them.

### BL3 contract state ≠ BL8 governing regime

```text
BL3
→ contract / clause content / obligations

BL8 governing-law unit
→ conflict / governing law / CISG/private-law treaty overlay
```

The BL8 result returns to BL3 for substantive contract reasoning. BL8 does not become the contract owner.

### BL4 procedural execution ≠ BL8 recognition/enforcement regime

BL8 owns the cross-border recognition/enforcement **regime**: treaty/applicability/recognition conditions and whether a viable cross-border recognition/enforcement pathway exists.

BL4 owns procedural execution of that pathway: where/how to file, service, procedural sequence, deadlines, interim/remedial posture and other claim/dispute procedure.

```text
Does the foreign-award recognition regime apply?
→ BL8

Where/how/when do we file the recognition request?
→ BL4
```

BL8 may condition BL4 procedure but must not execute it.

### BL8 flow classification ≠ BL5 tax treatment

```text
BL8
→ foreign payment / investment / trade flow classification

BL5
→ VAT / CIT / PIT / withholding / excise / other non-customs-duty tax consequence
```

Tax economics never justify changing a BL8 factual/legal flow classification.

### Customs fiscal boundary is explicit

BL8 trade/customs owns:

- customs classification;
- customs valuation;
- tariff rate/preferential tariff;
- customs duty proposition;
- another border/customs charge only when intrinsically part of the customs/trade classification.

BL5 owns VAT/CIT/PIT/withholding/excise and other statutory tax consequences unless the architecture explicitly assigns the exact customs-duty proposition to BL8.

Do not let BL5 and BL8 independently calculate/own the same import fiscal proposition.

### BL8 border status ≠ BL7 domestic permission

```text
BL8
→ import/export/customs/trade state

BL7
→ domestic market placement / product-service permission / conduct
```

Customs clearance never proves permission to sell/operate domestically.

### Governing law / treaty / procedure remain separate propositions

For cross-border contracts/disputes:

```text
BL3: clause contractual content/effect as a term
BL8: governing-law / CISG/private-law treaty / recognition-enforcement regime overlay
BL4: invocation / procedural execution / deadlines / remedies
```

Each owner consumes the others' committed propositions where needed rather than duplicating them.

### Trade chain is JIT, not mandatory

Within `trade-customs-origin-tariff.md`, activate only the technical step needed.

```text
trade-policy → HS → origin → valuation/tariff → customs
```

is a possible dependency chain, not a required full sequence for every goods question.

A committed HS proposition may be consumed by origin/tariff reasoning without recomputing HS unless stale/disputed/material.

## Specialist JIT rule

A specialist is never a top-level BL8 sibling and never owns the final BL8 proposition.

Any active BL8 capability owning the material proposition may invoke technical depth after the canonical materiality gate.

Typical trade specialists include HS classification, preferential origin, valuation/customs technical questions.

Use:

```text
material BL8 proposition
→ owning BL8 capability
→ materiality gate
→ SPECIALIST_CALL owner=BL8
→ candidate technical finding / authority / unresolved facts / uncertainty
→ owning BL8 capability accepts / conditions / rejects
→ BL8 commits owned proposition
```

Do not guess HS/origin because specialist depth is inconvenient. Do not let a specialist promote its finding directly into shared legal state.

## Change / late-route behavior

A BL8 result may reveal another owner is material:

- foreign acquisition facts reveal domestic sector permission → late-route BL7;
- trade/customs resolution reveals domestic product approval is required → late-route BL7;
- payment evidence contradicts BL3 transaction purpose → `CONTRADICTION_SIGNAL` to BL3;
- investment evidence contradicts BL2 cap-table/control state → `CONTRADICTION_SIGNAL` to BL2;
- BL8 flow classification becomes material to tax → activate/hand to BL5;
- recognition/enforcement regime becomes actionable → hand procedural execution to BL4.

BL8 must not repair another owner’s state silently.

## Live authority behavior

Stable BL8 knowledge defines ownership, distinctions, JIT routing and evidence needs. Use Authority Resolver whenever current/historical law materially determines:

- foreign-investor/market-access/control tests and investment-treaty/market-access commitments;
- governing-law/conflict/CISG/private-law treaty rules/status;
- international recognition/enforcement regime and treaty conditions;
- FX/cross-border payment/capital-flow conditions;
- trade/customs/HS/origin/FTA/tariff/valuation/customs-duty rules;
- temporal transition at closing, contract, payment, border entry, award/judgment or enforcement date.

Do not hardcode foreign-ownership thresholds, restricted-sector lists, treaty membership/reservations, account/payment rules, HS codes, tariff rates, origin criteria, customs forms/procedures, or article numbers.

Before a material irreversible cross-border action, re-resolve stale authority when a changed rule could affect permission, classification, option set, procedure/evidence, or action readiness.

## Handoff rules

- BL2 ↔ BL8: BL2 owns corporate mechanics; BL8 owns foreign-investment consequences from committed corporate facts.
- BL3 ↔ BL8: BL3 owns contract/clause/obligations; BL8 owns governing-law/CISG/private-law treaty and relevant cross-border overlays.
- BL4 ↔ BL8: BL8 owns the cross-border recognition/enforcement regime; BL4 owns filing/service/procedural execution/remedies/deadlines.
- BL8 → BL5: committed foreign payment/investment/trade classification and any separately owned customs-duty state; BL5 owns non-customs-duty tax consequences.
- BL8 ↔ BL7: BL8 owns border/trade/foreign-investment propositions; BL7 owns domestic product/service market permission and conduct.
- BL8 specialist → BL8: candidate depth only; BL8 owner integration required before shared-state promotion.

## Failure modes

- foreign element treated as BL8 ownership of the whole matter;
- foreign party treated as import/export;
- treaty keyword routed automatically to governing-law unit;
- BL8 overlay state missing `bl8_role` / `substantive_owner` and silently absorbing another owner's proposition;
- BL2 corporate control reused as foreign-investment control without separate test;
- foreign ownership percentage used as complete market-access answer;
- Vietnamese law applied automatically because a Vietnamese party exists;
- treaty/FTA existence treated as automatic applicability/benefit;
- BL8 international-enforcement analysis swallowing BL4 filing/service/deadline/procedure;
- foreign invoice automatically classified as one payment mode;
- tax result used to back-solve BL8 flow classification;
- BL5 and BL8 independently owning/calculating the same import fiscal item;
- HS guessed from product name;
- shipment country treated as preferential origin;
- DDP/Incoterm treated as complete statutory customs allocation;
- customs clearance treated as domestic market permission;
- specialist finding bypassing BL8 owner review;
- current cross-border thresholds/rates/lists/treaty status recalled from memory;
- all four BL8 units loaded for a narrow foreign-element question.

## Escalation

Increase verification for high-value/irreversible acquisitions, restricted sectors, treaty-dependent contracts, complex governing-law/arbitration structures, capital/loan/remittance flows, ambiguous goods classification/origin, preferential tariff claims, controlled goods, international enforcement, or any case where a wrong cross-border classification could block closing/payment/shipment or materially alter another owner’s conclusion.