# BL8 — Governing Law / Private-law Treaty / CISG / Recognition-Enforcement Overlay

## Owns

Determining cross-border conflict-of-laws, governing-law, **private-law treaty/CISG**, and cross-border recognition/enforcement-regime overlay propositions that materially affect another owner’s substantive contract/dispute analysis.

This unit owns **governing-law/conflict, CISG/private-law treaty applicability, and recognition/enforcement-regime overlay propositions**. It does not own ordinary contract formation/content, the contractual existence/content of a dispute-resolution clause, domestic dispute procedure/remedies, investment/market-access treaty propositions, FTA/trade-agreement origin/tariff propositions, or the final substantive contract proposition merely because a foreign element exists.

## Does not own

- private contract formation/content/obligations and contractual existence/content/validity/effect of dispute-resolution clauses — BL3;
- breach/remedies, invocation, filing mechanics, service, claim deadlines and procedural execution under the resolved/conditioned regime/forum — BL4;
- corporate state — BL2;
- tax treatment — BL5;
- domestic regulatory permission — BL7;
- investment/market-access treaty commitments, schedules or investor-treatment propositions — `foreign-investment-market-access.md`;
- FTA/trade-agreement origin/tariff propositions — `trade-customs-origin-tariff.md`;
- FX/payment propositions — `fx-cross-border-payment.md`.

## Activate when

Use when a material decision depends on:

- which law/regime governs a cross-border contract or specific private-law proposition;
- whether a choice-of-law clause is material to governing-law analysis;
- whether CISG or another private-law/conflict instrument applies, is excluded, displaced, or conditioned;
- whether mandatory/overriding rules or public-policy limits affect the resolved governing-law position;
- whether treaty/applicability/recognition conditions create a viable cross-border recognition/enforcement pathway for an award/judgment or another dispute result;
- whether the same private-law dispute/contract proposition spans multiple legal regimes or temporal anchors.

Do not activate merely because the word `treaty` appears. Route investment/market-access treaty questions to `foreign-investment-market-access.md` and FTA/trade-agreement origin/tariff questions to `trade-customs-origin-tariff.md`.

Skip when the foreign element cannot change the governing regime, CISG/private-law treaty applicability, or recognition/enforcement regime for the requested action.

## Required state

Where material, consume:

- parties/entities and relevant places from BL2/BL3;
- transaction/contract type and performance geography from BL3;
- contractual choice-of-law and dispute-resolution clause content from BL3 where already resolved;
- dispute posture/forum/procedural state from BL4 where already resolved;
- relevant nationality/place-of-business/performance/enforcement facts;
- contract formation/performance/breach/award/judgment/enforcement temporal anchors where material;
- current/historical conflict, CISG/private-law treaty and recognition/enforcement authority.

Do not reconstruct the contract or dispute clause merely to resolve the cross-border overlay.

## Core distinctions

### Treaty ownership follows proposition, not noun

```text
investment / market-access treaty commitment
→ foreign-investment-market-access

private-law governing regime / CISG / conflict treaty
or recognition-enforcement treaty overlay
→ governing-law-treaty-enforcement

FTA / trade-agreement origin or tariff entitlement
→ trade-customs-origin-tariff
```

A generic `TREATY_APPLIES` proposition is too coarse when the treaty affects different legal jobs. Create proposition-specific state.

### Foreign party ≠ foreign governing law

A foreign counterparty does not itself determine governing law.

Do not infer:

```text
Vietnam party involved
→ Vietnamese law automatically governs
```

or:

```text
foreign seller involved
→ foreign law automatically governs
```

Resolve the actual conflict/governing-law proposition.

### Governing law ≠ contract content

BL3 owns what the parties agreed and what the contract/terms say. BL8 owns what governing-law/conflict consequence follows where a foreign element makes that proposition material.

A governing-law clause is BL3 contractual content; its conflict-law effect is BL8.

### CISG/private-law treaty applicability ≠ contract formation itself

BL8 determines whether the relevant private-law international instrument/regime is applicable or excluded/conditioned. BL3 then resolves formation/content/obligations under the resolved regime.

Do not let BL8 become the contract owner merely because CISG/private-law treaty analysis is required.

### Governing law ≠ dispute clause ≠ procedural execution ≠ recognition/enforcement regime

Keep four propositions distinct:

```text
contractual dispute-clause content/effect as a term
→ BL3

governing-law / CISG / private-law treaty /
recognition-enforcement regime overlay
→ BL8

invocation / filing / service / procedural sequence /
deadlines / interim-remedial posture
→ BL4
```

No owner should silently duplicate another’s proposition.

### Arbitration seat/forum label ≠ all law questions resolved

A seat/forum/arbitration label may affect several propositions but does not automatically determine governing law for every issue, substantive contract law, or recognition/enforcement result.

### Treaty exists ≠ treaty applies to this proposition

Treaty membership/existence is authority/fact context, not case applicability by itself. BL8 must resolve the exact private-law/recognition proposition against parties, transaction, scope, exclusions, declarations/reservations, temporal anchor, and other material conditions.

### Recognition/enforcement regime ≠ procedural execution

BL8 owns:

- cross-border recognition/enforcement regime;
- treaty/applicability/recognition conditions;
- whether a viable cross-border recognition/enforcement pathway exists.

BL4 owns:

- where/how to file;
- service;
- procedural sequence;
- deadlines;
- interim/remedial posture;
- procedural execution of the pathway.

```text
Does the foreign-award recognition regime apply?
→ BL8

Where/how/when do we file the recognition request?
→ BL4
```

BL8 may condition BL4 procedure but must not execute it.

## Employment overlay inputs

For an employment-specific term, consume its content and any choice-of-law term
from BL6 rather than requiring BL3 to own it. Resolve the cross-border regime
proposition here with `bl8_role: OVERLAY` and `substantive_owner: BL6`; return it
to BL6 for employment merits. Route dispute procedure to BL4 only when material.
A foreign element alone does not activate investment, FX or customs units.

## Decision procedure

1. **State the cross-border regime proposition.** Example: `Which law/regime governs Contract C for formation/performance issue P?`
2. **Classify the treaty/regime job before routing.** Private-law/CISG/conflict or recognition-enforcement remains here; investment treaty goes to the investment unit; FTA/trade treaty goes to the trade unit.
3. **Consume substantive term and dispute state.** Commercial terms/choice-of-law content come from BL3; employment-specific term content comes from BL6. Consume BL4 dispute posture only if relevant.
4. **Map connecting facts.** Parties/place of business, performance, transaction type, chosen law, forum/seat/enforcement location, and other material contacts.
5. **Separate proposition types.** Governing law, CISG/private-law treaty applicability, dispute-clause content, recognition/enforcement regime, and procedural execution must remain distinct.
6. **Resolve current/historical conflict/treaty authority.** Bind the result to proposition-specific temporal anchor(s).
7. **Resolve CISG/private-law treaty scope and exclusions where material.** Do not infer applicability from party nationality or treaty existence alone.
8. **For foreign awards/judgments, resolve only the recognition/enforcement regime and viability conditions.** Do not perform BL4 filing/service/deadline analysis.
9. **Commit BL8 regime state with explicit `bl8_role` and `substantive_owner`.** Resolved, conditioned, disputed, verify, or unresolved.
10. **Return substantive/procedural reasoning to the correct owner.** BL3 reasons about contract formation/content/obligations under the resolved regime; BL4 handles procedural execution/remedies.

## Regime-state pattern

```text
P-BL8-LAW-01
bl8_role: OWNER / OVERLAY
substantive_owner: BL2 / BL3 / BL4 / BL5 / BL6 / BL7 / null
cross_border_mode: CONTRACT / DISPUTE / RECOGNITION_ENFORCEMENT / OTHER
bl3_dependencies: [...]
bl4_dependencies: [...]
bl6_dependencies: <employment term/merits IDs when material>
choice_of_law_state: <if material>
connecting_facts: [...]
candidate_regimes: [...]
private_law_treaty_or_cisg_state: <if material>
recognition_enforcement_regime: <if material>
recognition_conditions: [...]
temporal_anchors: [...]
status: RESOLVED / CONDITIONAL / VERIFY / DISPUTED / UNRESOLVED
```

Typical contract/CISG results that condition BL3 use:

```text
bl8_role: OVERLAY
substantive_owner: BL3
```

Typical recognition/enforcement-regime results that condition procedural execution use:

```text
bl8_role: OVERLAY
substantive_owner: BL4
```

The marker never authorizes BL8 to resolve BL3 obligations or BL4 procedure.

These are reasoning states, not fixed jurisdictional labels.

## Evidence requirements

Potential evidence includes:

- executed contract/order/terms and clause versions from BL3;
- parties’ places of business and relevant transaction geography;
- performance/delivery/service locations;
- forum/seat/enforcement-location facts;
- private-law treaty/CISG membership/status and reservations/declarations where material;
- award/judgment facts and recognition-location facts;
- official texts and current/historical conflict/recognition rules;
- procedural documents from BL4 where recognition/enforcement is material.

Do not treat a contract heading, address, invoice currency, or party nationality as dispositive governing-law evidence by itself.

## Live authority triggers

Use Authority Resolver where current/historical law materially determines:

- conflict-of-laws rules and choice-of-law effect;
- mandatory/overriding-law interaction;
- CISG/private-law treaty membership, scope, exclusions, declarations/reservations, amendment/status;
- cross-border recognition/enforcement treaty/regime and recognition conditions;
- historical rules at formation, performance, dispute, award/judgment, or enforcement date.

Do not hardcode treaty-party status, declarations/reservations, recognition conditions, procedural forms, article numbers, or current conflict rules as stable knowledge.

## Cross-track handoffs

### From / to BL3

BL3 supplies contractual terms, including choice-of-law/dispute clause content. BL8 returns the resolved/conditioned governing regime/CISG/private-law treaty overlay. BL3 then applies that regime to its owned contract propositions.

Do not infer that a BL8 governing-law result automatically resolves formation, validity, interpretation, obligation or performance.

### From / to BL4

BL4 supplies dispute posture/forum facts where material. BL8 supplies the cross-border recognition/enforcement regime and treaty/applicability conditions. BL4 owns filing, service, deadlines, remedies and procedural execution under the resolved/conditioned pathway.

If an enforcement issue reveals a new governing-law/treaty question, BL4 may signal BL8; BL8 does not independently seize BL4 procedure ownership.

### To investment unit

If a treaty question concerns investor treatment, market access, entry/control or investment commitments/schedules, route to `foreign-investment-market-access.md` rather than resolving it here.

### To trade unit

If a treaty question concerns FTA/trade-agreement origin or tariff entitlement, route to `trade-customs-origin-tariff.md`.

### To BL7

If a mandatory domestic public-law rule/permission is separately material, late-route BL7. Governing-law choice does not waive mandatory regulatory analysis.

## Failure modes

- treaty noun treated as automatic route to this unit;
- investment-treaty or FTA proposition absorbed into private-law treaty reasoning;
- Vietnamese law applied automatically because one party is Vietnamese;
- foreign law assumed automatically because one party is foreign;
- governing-law clause content and conflict-law effect collapsed into one owner;
- treaty existence treated as automatic applicability;
- international sale treated as automatic CISG or automatic Vietnamese commercial law;
- seat/forum treated as resolving every governing-law issue;
- BL8 recognition/enforcement analysis swallowing BL4 filing/service/deadline/procedure;
- `bl8_role` / `substantive_owner` omitted where overlay status is material;
- recognition/enforcement overlay used to reopen substantive merits without an owner signal;
- current treaty/conflict/recognition rules recalled from memory without live verification.

## Escalation

Increase verification for multi-country performance, non-standard choice-of-law clauses, mixed goods/services, treaty exclusions/reservations, mandatory-law conflicts, complex arbitration/forum structures, parallel proceedings, foreign awards/judgments, or any irreversible contract/dispute action where the governing regime materially changes substantive rights or enforceability.