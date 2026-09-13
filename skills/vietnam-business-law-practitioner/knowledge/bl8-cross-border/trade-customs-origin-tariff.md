# BL8 — Trade / Customs / HS / Origin / Tariff

## Owns

Determining goods-trade and border/customs propositions for actual or planned movement of goods across borders, including trade-policy route, customs role, HS classification, origin, customs valuation, **customs duty/tariff**, FTA/preferential treatment, and customs-state questions.

This unit owns **trade/customs/HS/origin/tariff/customs-duty propositions**. It does not decide domestic market/product permission, private contract obligations, BL5 non-customs tax treatment, or treat a product name/Incoterm as sufficient technical classification.

## Does not own

- domestic product/service market permission, product safety/sector approval, consumer/advertising conduct — BL7;
- contract formation/content, Incoterm or import-cost allocation as private-law terms — BL3;
- private breach/remedies/dispute procedure — BL4;
- VAT/CIT/PIT/withholding/excise or other non-customs-duty statutory tax treatment — BL5;
- corporate/importer entity authority — BL2;
- foreign-investment market access or investment-treaty propositions — `foreign-investment-market-access.md`;
- private-law governing-law/conflict/CISG/recognition-enforcement treaty propositions — `governing-law-treaty-enforcement.md`;
- FX/payment propositions — `fx-cross-border-payment.md`.

## Activate when

Use when a material decision depends on:

- actual/planned physical cross-border movement of goods;
- customs/import/export roles or responsibilities;
- tariff/trade-policy classification;
- HS classification;
- non-preferential/preferential origin;
- FTA/trade-agreement applicability to origin/preferential tariff;
- preferential tariff entitlement;
- customs valuation;
- customs duty/tariff or another border/customs charge intrinsically part of the trade/customs classification;
- customs declaration/clearance/status or another border process;
- whether a specialist is needed for HS/origin/customs technical depth.

Skip when the foreign element is only a service, software/data, financing, investment, payment, or contract issue with no material goods movement/customs proposition.

## Required state

Where material, consume:

- actual product/goods description, composition, function, form, specifications and use;
- shipment/movement facts and countries/locations;
- seller/buyer/importer/exporter/consignee and contractual logistics facts from BL3;
- Incoterm/shipping allocation as BL3 content, not statutory customs responsibility;
- origin/manufacturing/process/input facts;
- invoice/value/freight/insurance and other valuation inputs where material;
- permits/market-placement state from BL7 where relevant but separate;
- relevant FTA/trade-agreement and preference facts where material;
- relevant temporal anchors such as export/import/declaration/entry date;
- current/historical trade/customs authority.

Do not infer product technical facts from a marketing name if classification requires more detail.

## Core distinctions

### Foreign element ≠ goods trade

A foreign party or cross-border payment does not establish an import/export proposition.

Activate this unit only when actual/planned goods movement or another border/customs proposition is material.

### Treaty ownership follows proposition

FTA/trade-agreement propositions stay here when they affect preferential origin, tariff entitlement, trade treatment or another goods-trade proposition.

```text
investment treaty / market-access schedule
→ foreign-investment-market-access

private-law conflict / CISG / recognition treaty
→ governing-law-treaty-enforcement

FTA / preferential-origin / tariff treaty
→ trade-customs-origin-tariff
```

Do not route a treaty question by the noun `treaty`.

### Product name ≠ HS classification

A commercial name, SKU, invoice description or user shorthand may be insufficient for HS classification.

Use actual technical characteristics and request/retain unresolved facts where required. Do not guess an HS code from product name alone.

### HS classification ≠ origin

HS classification and origin are separate propositions.

```text
HS code resolved
≠ preferential origin resolved
```

Origin may depend on production/process/material facts and the relevant regime.

### Shipment country ≠ origin

Goods shipping from an FTA country do not automatically originate there for preferential purposes.

```text
shipped from FTA country
≠ qualifying origin
```

### FTA/trade agreement exists ≠ preferential tariff entitlement

Preferential treatment may depend on product classification, origin criteria, direct transport/shipment conditions, evidence/documentation, timing, and current regime conditions.

Do not infer `FTA = zero duty`.

### Incoterm ≠ statutory customs responsibility

BL3 owns Incoterm/private cost/risk allocation. BL8 owns statutory customs/trade responsibilities and border propositions.

Do not infer:

```text
DDP
→ seller legally becomes every statutory importer/tax/customs actor
```

without current authority and actual facts.

### Customs clearance ≠ domestic market permission

BL8 may resolve border/customs clearance. BL7 separately owns whether the product may be placed on/sold/advertised in the domestic market.

```text
CUSTOMS_CLEARED
≠ DOMESTICALLY_PERMITTED_TO_SELL
```

### Classification ≠ valuation ≠ customs duty/tariff ≠ BL5 tax ≠ final landed economics

Keep distinct:

- HS classification;
- origin;
- customs valuation;
- tariff/preference;
- customs duty proposition;
- another border/customs charge only where intrinsically part of the customs/trade classification;
- BL5 VAT/CIT/PIT/withholding/excise or other non-customs-duty statutory tax consequences;
- private cost allocation from BL3.

Do not let BL5 and BL8 independently own or calculate the same import fiscal item.

### Specialist finding ≠ committed BL8 proposition

HS/origin/customs specialists return candidate technical findings. BL8 must accept, condition, reject, or request more facts before promotion.

## Decision procedure

1. **State the trade/customs proposition.** Example: `What HS/origin/tariff/customs state governs Product P imported on date D?`
2. **Confirm actual goods-trade mode.** Do not activate the goods chain merely because the counterparty/payment is foreign.
3. **Consume private logistics/transaction facts.** BL3 terms/Incoterm/document stack are inputs, not statutory conclusions.
4. **Classify the treaty/source job if relevant.** FTA/trade-agreement origin/tariff stays here; investment/private-law treaty propositions route to their sibling owner.
5. **Resolve product facts before technical classification.** Identify composition/function/form/use/specification facts needed for HS or other classification.
6. **Resolve the smallest necessary chain.** Trade-policy → HS → origin → valuation/tariff/customs duty → customs process only as material; do not force every stage for every question.
7. **Invoke specialist depth where technical classification requires it.** Specialist remains owner-bound to BL8.
8. **Resolve current/historical authority.** Bind to import/export/declaration/entry temporal anchor.
9. **Separate customs fiscal result from BL5 tax consequence.** BL8 owns customs duty/tariff and intrinsically customs/trade charges; BL5 owns other statutory tax consequences.
10. **Separate border result from domestic market permission.** Late-route/consume BL7 where product approval/safety/label/sale permission is material.
11. **Commit BL8 trade state with explicit `bl8_role` / `substantive_owner`.** Supported, conditional, verify, blocked, disputed, or unresolved.
12. **Hand tax/payment/contract consequences outward.** BL5, FX unit, BL3 as appropriate without rewriting their state.

## Trade-state patterns

```text
P-BL8-HS-01
bl8_role: OWNER / OVERLAY
substantive_owner: BL2 / BL3 / BL4 / BL5 / BL6 / BL7 / null
product: <...>
material_product_facts: [...]
candidate_classification: <...>
specialist_dependency: <if used>
temporal_anchor: <...>
status: RESOLVED / CONDITIONAL / VERIFY / DISPUTED / UNRESOLVED
```

```text
P-BL8-ORIGIN-01
bl8_role: OWNER / OVERLAY
substantive_owner: BL2 / BL3 / BL4 / BL5 / BL6 / BL7 / null
hs_dependency: P-BL8-HS-...
production_facts: [...]
origin_regime_or_trade_agreement: <...>
origin_state: <...>
evidence_state: <...>
status: RESOLVED / CONDITIONAL / VERIFY / DISPUTED / UNRESOLVED
```

```text
P-BL8-CUSTOMS-01
bl8_role: OWNER / OVERLAY
substantive_owner: BL2 / BL3 / BL4 / BL5 / BL6 / BL7 / null
movement: IMPORT / EXPORT / TRANSIT / OTHER
customs_actor_state: <...>
hs_dependency: <...>
origin_dependency: <if material>
valuation_state: <if material>
tariff_preference_state: <if material>
customs_duty_state: <if material>
clearance_state: <...>
status: SUPPORTED / CONDITIONAL / VERIFY / BLOCKED / DISPUTED / UNRESOLVED
```

Trade/customs propositions will normally use `bl8_role: OWNER` with `substantive_owner: null`. Use `OVERLAY` only where the committed BL8 result explicitly conditions another owner's proposition/action; that owner remains substantive owner.

These are reasoning states, not hardcoded customs declarations.

## Evidence requirements

Potential evidence includes:

- technical specifications, composition, drawings/photos where relevant;
- manufacturer/process/material information;
- invoices, packing lists, transport/shipping records;
- contracts/Incoterms from BL3;
- country-of-origin/production evidence;
- certificates/declarations of origin where relevant;
- customs declarations/official rulings/clearance records;
- valuation inputs and payment/logistics evidence;
- official tariff/customs/trade authority;
- BL7 domestic product approval/label/safety state where separately material.

Do not treat invoice/product names as complete technical evidence where classification requires additional facts.

## Live authority triggers

Use Authority Resolver where current/historical law materially determines:

- HS nomenclature/classification rules;
- import/export prohibitions/restrictions and trade-policy treatment;
- origin rules and preferential-origin criteria;
- FTA/trade-agreement scope, schedules/status and preferential tariff conditions;
- customs valuation rules;
- customs duty/tariff and intrinsically border/customs charges;
- declaration/clearance procedures and customs actor obligations;
- documentary/evidence requirements;
- historical tariff/origin/customs rules at the entry/export date.

Do not hardcode HS codes, duty rates, tariff schedules, origin criteria, valuation adjustments, documentary forms, filing steps, agency names, or article numbers.

## Specialist JIT rule

Any active BL8 trade proposition may invoke owner-bound technical depth when material.

```text
BL8 trade proposition
→ materiality gate
→ SPECIALIST_CALL owner=BL8
→ candidate HS/origin/customs finding
→ BL8 accept / condition / reject
→ BL8 commits proposition
```

The specialist must not emit final action readiness or promote its finding directly into shared state.

## Cross-track handoffs

### From BL3

Consume transaction/shipping/Incoterm/private allocation facts. BL3 remains owner of contractual risk/cost/obligation allocation.

### To BL7

If the goods are cleared or expected to clear but domestic product/service permission, safety, labeling, advertising or sale conditions are material, late-route BL7. Do not infer domestic permission from customs status.

### To BL5

Provide committed customs/trade classifications, customs valuation and separately owned customs-duty/tariff state where material. BL5 owns VAT/CIT/PIT/withholding/excise and other non-customs-duty statutory tax consequences.

If the same fiscal item appears to be owned in both tracks, create/repair the proposition boundary before calculation; do not let both tracks compute it independently.

### To FX unit

If cross-border payment mechanics/classification are separately material, hand the committed goods-transaction mode to `fx-cross-border-payment.md`; trade state does not itself resolve FX payment legality.

### To investment / governing-law units

Route treaty questions by proposition: investment/market-access treaty commitments to the investment unit; private-law/CISG/recognition-enforcement treaty questions to the governing-law unit. FTA/trade-agreement origin/tariff questions remain here.

### To BL2

If customs actor/representation depends on entity/authority state, consume BL2 rather than inferring legal authority from shipping role/title.

## Failure modes

- foreign party/payment treated as import/export;
- treaty keyword routed automatically to governing-law unit despite FTA/origin/tariff proposition;
- HS guessed from product name;
- shipment country treated as preferential origin;
- FTA existence treated as zero duty;
- HS and origin collapsed;
- DDP/Incoterm treated as complete statutory customs allocation;
- BL5 and BL8 independently owning/calculating the same import fiscal item;
- customs clearance treated as permission to sell domestically;
- technical specialist finding bypassing BL8 owner review;
- `bl8_role` / `substantive_owner` omitted where overlay status is material;
- hardcoded tariff/HS/origin rules used as current law;
- full trade chain loaded when only one technical proposition is material.

## Escalation

Increase verification for ambiguous/multi-function products, controlled/restricted goods, preferential origin, complex manufacturing, related-party valuation, unusual routing/transshipment, high-duty exposure, binding-classification needs, material customs disputes, or any irreversible shipment where a wrong classification/origin/customs assumption could block entry or materially change economics.