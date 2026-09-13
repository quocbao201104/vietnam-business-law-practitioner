# BL8 — Governing Law / Treaty / CISG / International Enforcement Overlay

## Owns

Determining cross-border conflict-of-laws, governing-law, treaty/CISG, and international-enforcement overlay propositions that materially affect another owner’s substantive contract/dispute analysis.

This unit owns **governing-law/conflict, treaty/CISG applicability, and international-enforcement overlay propositions**. It does not own ordinary contract formation/content, the contractual existence/content of a dispute-resolution clause, domestic dispute procedure/remedies, or the final substantive contract proposition merely because a foreign element exists.

## Does not own

- private contract formation/content/obligations and contractual existence/content/validity/effect of dispute-resolution clauses — BL3;
- breach/remedies, invocation, filing mechanics, claim deadlines and procedure under the resolved/conditioned regime/forum — BL4;
- corporate state — BL2;
- tax treatment — BL5;
- domestic regulatory permission — BL7;
- foreign-investment, FX/payment, or trade/customs propositions owned by other BL8 units.

## Activate when

Use when a material decision depends on:

- which law/regime governs a cross-border contract or specific proposition;
- whether a choice-of-law clause is material to governing-law analysis;
- whether treaty/CISG or another international instrument applies, is excluded, displaced, or conditioned;
- whether mandatory/overriding rules or public-policy limits affect the resolved governing-law position;
- international recognition/enforcement overlay for an award/judgment or another cross-border dispute result;
- whether the same dispute/contract proposition spans multiple legal regimes or temporal anchors.

Skip when the foreign element cannot change the governing regime, treaty applicability, or international-enforcement posture for the requested action.

## Required state

Where material, consume:

- parties/entities and relevant places from BL2/BL3;
- transaction/contract type and performance geography from BL3;
- contractual choice-of-law and dispute-resolution clause content from BL3 where already resolved;
- dispute posture/forum/procedural state from BL4 where already resolved;
- relevant nationality/place-of-business/performance/enforcement facts;
- contract formation/performance/breach/enforcement temporal anchors where material;
- current/historical conflict, treaty/CISG and enforcement authority.

Do not reconstruct the contract or dispute clause merely to resolve the cross-border overlay.

## Core distinctions

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

### Treaty/CISG applicability ≠ contract formation itself

BL8 determines whether an international instrument/regime is applicable or excluded/conditioned. BL3 then resolves formation/content/obligations under the resolved regime.

Do not let BL8 become the contract owner merely because CISG/treaty analysis is required.

### Governing law ≠ dispute clause ≠ procedure ≠ international enforcement

Keep four propositions distinct:

```text
contractual dispute-clause content/effect as a term
→ BL3

governing-law/treaty/international-enforcement overlay
→ BL8

invocation/forum procedure/deadlines/remedies
→ BL4
```

No owner should silently duplicate another’s proposition.

### Arbitration seat/forum label ≠ all law questions resolved

A seat/forum/arbitration label may affect several propositions but does not automatically determine governing law for every issue, substantive contract law, or international-enforcement result.

### Treaty exists ≠ treaty applies to this proposition

Treaty membership/existence is authority/fact context, not case applicability by itself. The accountable BL8 proposition owner must resolve applicability against the parties, transaction, scope, exclusions, declarations/reservations, temporal anchor, and other material conditions.

### International enforcement overlay ≠ domestic merits re-litigation

BL8 owns the cross-border recognition/enforcement overlay where material. BL4 continues to own domestic dispute/remedy/procedure propositions under the resolved regime/forum. BL8 does not reopen contract/breach merits without an explicit owner-triggered dependency.

## Decision procedure

1. **State the cross-border regime proposition.** Example: `Which law/regime governs Contract C for formation/performance issue P?`
2. **Consume BL3/BL4 state.** Contract terms/choice-of-law/dispute clause from BL3; current dispute posture from BL4 if relevant.
3. **Map connecting facts.** Parties/place of business, performance, transaction type, chosen law, forum/seat/enforcement location, and other material contacts.
4. **Separate proposition types.** Governing law, treaty/CISG applicability, dispute clause content, procedure, and enforcement overlay must remain distinct.
5. **Resolve current/historical conflict/treaty authority.** Bind the result to the proposition-specific temporal anchor(s).
6. **Resolve treaty/CISG scope and exclusions where material.** Do not infer applicability from party nationality or treaty existence alone.
7. **Commit BL8 regime state.** Resolved, conditioned, disputed, verify, or unresolved.
8. **Return substantive reasoning to the correct owner.** BL3 reasons about contract formation/content/obligations under the resolved regime; BL4 handles invocation/procedure/remedies.
9. **For international enforcement, resolve only the overlay.** Preserve existing BL3/BL4 owned merits/procedure state unless a new material contradiction/route signal arises.

## Regime-state pattern

```text
P-BL8-LAW-01
cross_border_mode: CONTRACT / DISPUTE / ENFORCEMENT / OTHER
bl3_dependencies: [...]
bl4_dependencies: [...]
choice_of_law_state: <if material>
connecting_facts: [...]
candidate_regimes: [...]
treaty_cisg_state: <if material>
enforcement_overlay: <if material>
temporal_anchors: [...]
status: RESOLVED / CONDITIONAL / VERIFY / DISPUTED / UNRESOLVED
```

These are reasoning states, not fixed jurisdictional labels.

## Evidence requirements

Potential evidence includes:

- executed contract/order/terms and clause versions from BL3;
- parties’ places of business and relevant transaction geography;
- performance/delivery/service locations;
- forum/seat/enforcement-location facts;
- treaty membership/status and reservations/declarations where material;
- official texts and current/historical conflict/enforcement rules;
- award/judgment/procedural documents where international enforcement is material.

Do not treat a contract heading, address, invoice currency, or party nationality as dispositive governing-law evidence by itself.

## Live authority triggers

Use Authority Resolver where current/historical law materially determines:

- conflict-of-laws rules and choice-of-law effect;
- mandatory/overriding-law interaction;
- treaty/CISG membership, scope, exclusions, declarations/reservations, amendment/status;
- international recognition/enforcement framework;
- historical rules at formation, performance, dispute, award/judgment, or enforcement date.

Do not hardcode treaty-party status, declarations/reservations, enforcement conditions, procedural forms, article numbers, or current conflict rules as stable knowledge.

## Cross-track handoffs

### From / to BL3

BL3 supplies contractual terms, including choice-of-law/dispute clause content. BL8 returns the resolved/conditioned governing regime/treaty overlay. BL3 then applies that regime to its owned contract propositions.

Do not infer that a BL8 governing-law result automatically resolves formation, validity, interpretation, obligation or performance.

### From / to BL4

BL4 supplies dispute posture/forum facts where material. BL8 supplies cross-border treaty/international-enforcement overlay. BL4 owns invocation, filing, deadlines, remedies and procedure under the resolved/conditioned forum/regime.

If an enforcement issue reveals a new governing-law/treaty question, BL4 may signal BL8; BL8 does not independently seize BL4 procedure ownership.

### To BL7

If a mandatory domestic public-law rule/permission is separately material, late-route BL7. Governing-law choice does not waive mandatory regulatory analysis.

## Failure modes

- Vietnamese law applied automatically because one party is Vietnamese;
- foreign law assumed automatically because one party is foreign;
- governing-law clause content and conflict-law effect collapsed into one owner;
- treaty existence treated as automatic applicability;
- international sale treated as automatic CISG or automatic Vietnamese commercial law;
- seat/forum treated as resolving every governing-law issue;
- BL8 and BL4 independently resolving the same procedure/forum proposition;
- international enforcement overlay used to reopen substantive merits without an owner signal;
- current treaty/conflict/enforcement rules recalled from memory without live verification.

## Escalation

Increase verification for multi-country performance, non-standard choice-of-law clauses, mixed goods/services, treaty exclusions/reservations, mandatory-law conflicts, complex arbitration/forum structures, parallel proceedings, foreign awards/judgments, or any irreversible contract/dispute action where the governing regime materially changes substantive rights or enforceability.