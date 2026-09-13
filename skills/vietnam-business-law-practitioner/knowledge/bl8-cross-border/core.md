# BL8 — Investment / Cross-border / Trade

BL8 resolves only the **material cross-border propositions** created by foreign investment, governing-law/treaty questions, cross-border payment/FX rules, and goods trade/customs. A foreign element may activate BL8, but it does not transfer ownership of the whole matter into BL8.

This `core.md` is a **JIT router**, not a foreign-law/customs encyclopedia. Load only the capability unit needed for the material proposition.

## Owns when acting as proposition owner

BL8 owns propositions about:

- foreign-investor status, foreign-investment market access, and foreign-investment control/entry/change tests;
- governing-law/conflict-of-laws, treaty/CISG applicability, and international-enforcement overlay;
- FX/cross-border payment and capital-flow classification;
- goods trade/customs, HS, origin, valuation/tariff and preferential-treatment propositions;
- BL8-owned specialist activation/integration for technical trade/origin/customs depth.

## Overlay role

BL8 may also operate only as a **cross-border overlay** while another track remains substantive owner.

Examples:

- BL2 owns corporate identity, cap table, voting/control and approvals; BL8 owns the foreign-investment consequence of that committed state.
- BL3 owns contract formation/content/obligations and the contractual content/effect of a dispute-resolution clause; BL8 owns governing-law/treaty/CISG or international-enforcement overlay.
- BL4 owns dispute posture, invocation, filing mechanics, deadlines and remedies under the resolved/conditioned regime/forum; BL8 owns only the cross-border treaty/enforcement overlay.
- BL5 owns tax consequences; BL8 may supply the foreign payment/investment/trade classification that BL5 consumes.
- BL7 owns domestic product/service market permission and conduct; BL8 owns border/trade or foreign-investment propositions.

The handoff/state should make clear whether BL8 is acting as **accountable proposition owner** or **overlay provider**.

## Does not own

- corporate mechanics, cap table, voting/control or corporate approvals — BL2;
- ordinary private contract formation/content/obligations — BL3;
- private breach/remedies/claim-preservation timing/procedure — BL4;
- tax treatment — BL5;
- employment merits — BL6;
- domestic product/service market permission, privacy/data or market conduct — BL7.

## Core distinctions

- foreign element ≠ import/export;
- foreign element ≠ BL8 owns the whole case;
- corporate control (BL2) ≠ foreign-investment control test (BL8);
- corporate validity ≠ foreign-investment compliance;
- foreign ownership percentage ≠ complete market-access analysis;
- governing law ≠ dispute-clause content ≠ dispute procedure ≠ international enforcement;
- treaty exists ≠ treaty applies to the proposition;
- international sale ≠ automatic CISG or automatic Vietnamese commercial law;
- foreign invoice/payment ≠ one fixed FX/capital-flow category;
- cross-border payment ≠ goods trade/customs;
- product name ≠ HS classification;
- HS classification ≠ origin ≠ preferential tariff entitlement;
- shipment country ≠ preferential origin;
- FTA exists ≠ zero tariff;
- Incoterm/private allocation ≠ statutory customs responsibility;
- customs clearance ≠ domestic market permission;
- specialist finding ≠ committed BL8 proposition.

## JIT capability routing

### Foreign investment / market access

Load `foreign-investment-market-access.md` when the question depends on:

- foreign-investor status;
- foreign-investment market-access conditions/restrictions;
- acquisition/subscription/project/investment-entry trigger;
- foreign-investment ownership/control tests;
- changes in investor/ownership/control/activity that may alter foreign-investment state.

This unit consumes BL2 corporate state; it must not reconstruct cap table/control merely because the investment test depends on them.

### Governing law / treaty / CISG / international enforcement

Load `governing-law-treaty-enforcement.md` when the question depends on:

- governing law/conflict-of-laws;
- treaty/CISG applicability/exclusion;
- mandatory-law interaction in a cross-border contract;
- cross-border recognition/international-enforcement overlay.

BL3 remains owner of contract/clause content. BL4 remains owner of invocation/procedure/deadlines/remedies.

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
- tariff/preference or customs valuation;
- owner-bound HS/origin/customs specialist depth.

Do not load this unit for a foreign service/software/investment/payment case with no material goods movement.

Do not load all four units by default.

## Sibling JIT rule

BL8 sibling units are **not a mandatory pipeline**.

A committed BL8 proposition may be consumed directly from shared state without loading its owning sibling when reliable and not material to reopen.

Load the sibling only when the proposition is unresolved, disputed, stale, contradictory, or material to the current action.

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
→ conflict / governing law / treaty / CISG overlay
```

The BL8 result returns to BL3 for substantive contract reasoning. BL8 does not become the contract owner.

### BL4 procedure ≠ BL8 international overlay

BL4 owns invocation, filing, limitation/deadline, procedure and remedies. BL8 owns only governing-law/treaty/international-enforcement overlay where a foreign element materially changes it.

Do not independently resolve the same forum/procedure proposition in both tracks.

### BL8 flow classification ≠ BL5 tax treatment

```text
BL8
→ foreign payment / investment / trade flow classification

BL5
→ tax / withholding / tax-document consequence
```

Tax economics never justify changing a BL8 factual/legal flow classification.

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
BL8: governing-law / treaty / CISG / international-enforcement overlay
BL4: invocation / procedure / deadlines / remedies
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
- BL8 flow classification becomes material to tax → activate/hand to BL5.

BL8 must not repair another owner’s state silently.

## Live authority behavior

Stable BL8 knowledge defines ownership, distinctions, JIT routing and evidence needs. Use Authority Resolver whenever current/historical law materially determines:

- foreign-investor/market-access/control tests;
- governing-law/conflict/treaty/CISG rules/status;
- international recognition/enforcement overlay;
- FX/cross-border payment/capital-flow conditions;
- trade/customs/HS/origin/tariff/valuation rules;
- temporal transition at closing, contract, payment, border entry, award/judgment or enforcement date.

Do not hardcode foreign-ownership thresholds, restricted-sector lists, treaty membership/reservations, account/payment rules, HS codes, tariff rates, origin criteria, customs forms/procedures, or article numbers.

Before a material irreversible cross-border action, re-resolve stale authority when a changed rule could affect permission, classification, option set, procedure/evidence, or action readiness.

## Handoff rules

- BL2 ↔ BL8: BL2 owns corporate mechanics; BL8 owns foreign-investment consequences from committed corporate facts.
- BL3 ↔ BL8: BL3 owns contract/clause/obligations; BL8 owns governing-law/treaty/CISG and relevant cross-border overlays.
- BL4 ↔ BL8: BL4 owns dispute procedure/remedies/deadlines; BL8 owns international treaty/enforcement overlay.
- BL8 → BL5: committed foreign payment/investment/trade classification; BL5 owns tax consequences.
- BL8 ↔ BL7: BL8 owns border/trade/foreign-investment propositions; BL7 owns domestic product/service market permission and conduct.
- BL8 specialist → BL8: candidate depth only; BL8 owner integration required before shared-state promotion.

## Failure modes

- foreign element treated as BL8 ownership of the whole matter;
- foreign party treated as import/export;
- BL2 corporate control reused as foreign-investment control without separate test;
- foreign ownership percentage used as complete market-access answer;
- Vietnamese law applied automatically because a Vietnamese party exists;
- treaty/FTA existence treated as automatic applicability/benefit;
- BL4 and BL8 independently resolving the same forum/procedure proposition;
- foreign invoice automatically classified as one payment mode;
- tax result used to back-solve BL8 flow classification;
- HS guessed from product name;
- shipment country treated as preferential origin;
- DDP/Incoterm treated as complete statutory customs allocation;
- customs clearance treated as domestic market permission;
- specialist finding bypassing BL8 owner review;
- current cross-border thresholds/rates/lists/treaty status recalled from memory;
- all four BL8 units loaded for a narrow foreign-element question.

## Escalation

Increase verification for high-value/irreversible acquisitions, restricted sectors, treaty-dependent contracts, complex governing-law/arbitration structures, capital/loan/remittance flows, ambiguous goods classification/origin, preferential tariff claims, controlled goods, international enforcement, or any case where a wrong cross-border classification could block closing/payment/shipment or materially alter another owner’s conclusion.