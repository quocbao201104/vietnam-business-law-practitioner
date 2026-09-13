# BL1 — Regime Routing

## Owns

Identifying candidate legal regime layers and routing the propositions they create to accountable BL owners.

BL1 owns the **candidate regime map and route hypothesis**. It does not decide that a candidate substantive regime actually governs a BL2–BL8 proposition.

## Does not own

- final governing-law/conflict/treaty/CISG applicability — BL8 where cross-border;
- corporate/entity conclusions — BL2;
- formation/content/performance — BL3;
- breach/remedy — BL4;
- tax regime consequences — BL5;
- employment classification — BL6;
- regulatory permission or market conduct — BL7.

## Activate when

Use when:

- several bodies of law may interact;
- a special/mandatory regime may displace or supplement a general one;
- the user assumes one statute controls the whole matter;
- a foreign element may change the governing regime;
- public-law permission may constrain a private-law transaction;
- procedure/forum is being collapsed into substantive law;
- a downstream owner needs a route hypothesis rather than a statute dump.

## Required state

- issue/question map from BL1 framing;
- accountable proposition candidates;
- actor/status/activity/object facts;
- geography and foreign elements;
- temporal anchors;
- transaction/relationship type candidates;
- regulatory/sector signals;
- user action(s).

## Core distinctions

### Regime stack ≠ one statute

A legal position may require several coordinated layers, for example:

```text
mandatory / sector-specific law
+ transaction/relationship law
+ general fallback rules
+ implementing instruments
+ party agreement where legally permitted
+ procedure/forum rules where relevant
```

Do not assume every layer applies. The purpose of the stack is to identify candidate questions and owners.

### General rule ≠ special rule

When a narrower regime plausibly controls a proposition, route it for owner resolution rather than defaulting to the general regime.

### Private agreement ≠ public permission

A validly agreed term may still be constrained by mandatory regulation. Route contract content to BL3 and public-law permission/compliance to BL7.

### Substantive law ≠ procedure/forum

The law governing contractual rights is not automatically the law governing forum, arbitration procedure, limitation, recognition, or enforcement.

### Corporate validity ≠ foreign-investment compliance

BL2 may resolve corporate mechanics while BL8 separately resolves foreign-investment/market-access propositions.

### Domestic transaction logic ≠ cross-border regime

A foreign party, foreign performance, foreign payment, foreign law clause, or goods movement may activate BL8. It does not automatically mean customs/import-export analysis.

## Candidate regime mapping procedure

1. **Start from owned propositions, not statute names.** Identify what must be decided.
2. **Detect mandatory/public-law layers.** Ask whether sector, licensing, consumer, competition, data, product, employment, tax, or other mandatory rules can constrain the action.
3. **Detect relationship/transaction layers.** Identify candidate corporate, contract, employment, tax, regulatory, or cross-border owners.
4. **Detect foreign elements immediately.** Do not wait until the end of the analysis to notice a foreign party, governing-law clause, payment route, investment status, or goods movement.
5. **Separate substantive and procedural questions.** Route clause content to BL3, cross-border governing/treaty overlay to BL8, and dispute posture/procedure/remedies to BL4 after the regime/forum proposition is resolved.
6. **Mark temporal uncertainty.** If regime selection may change by event date or transition rule, activate temporal applicability.
7. **Create route hypotheses.** Use route states rather than silently treating the first plausible regime as settled.
8. **Hand off candidate regimes to proposition owners.** Owners resolve applicability using live authority where material.
9. **Allow late activation.** If downstream facts reveal a missed mandatory or cross-border layer, emit `LATE_ROUTE_SIGNAL` and update the route map explicitly.

## Route-state semantics

### `ROUTE_CONFIRMED`

The known facts make the track materially necessary to resolve a proposition or requested action.

### `ROUTE_PLAUSIBLE`

The track may be material, but a fact/classification needed to confirm activation is still unresolved.

### `ROUTE_UNRESOLVED`

The runtime cannot yet determine whether the track is material because a blocking framing fact is missing or contradictory.

### `ROUTE_REJECTED`

The current facts establish that the candidate track is not material to the requested action.

A rejected route may be reopened only by new material evidence or an authority change that affects the route basis. Reopening must be explicit.

## Common routing patterns

### Corporate + contract

```text
Who may bind the company? → BL2
What transaction exists? → BL3
```

Do not let signature alone answer both.

### Contract + regulation

```text
What did parties agree? → BL3
Is the conduct permitted? → BL7
```

Agreement does not prove legality.

### Employment + tax

```text
What is the relationship? → BL6
What tax/BHXH consequences follow? → BL5
```

BL5 must not classify the worker itself.

### Cross-border contract

```text
Foreign/treaty/governing-law proposition → BL8
Contract formation/content under resolved regime → BL3
Dispute/remedy under resolved regime/forum → BL4
```

### Import then domestic sale

```text
Border/trade/customs proposition → BL8
Domestic product/market permission → BL7
Tax consequences where material → BL5
```

Customs success does not prove permission to market.

## Live authority triggers

Live authority is needed when route confirmation depends materially on whether:

- a special regime currently exists or applied at the relevant time;
- an activity/product/actor falls within a current mandatory perimeter;
- a foreign/treaty regime may apply;
- a current or historical instrument changes which owner/proposition must be resolved;
- transition/repeal/suspension changes the candidate regime stack.

BL1 may discover the authority signal, but the accountable owner decides substantive case applicability.

## Cross-track handoffs

A regime-routing handoff should include:

- proposition/question;
- candidate owner;
- route state;
- candidate regime/overlay reason;
- material facts supporting activation;
- temporal anchor(s);
- unresolved activation fact(s);
- whether live authority is required.

## Failure modes

- one-law collapse;
- statute-first routing;
- assuming the most general law controls because it is familiar;
- treating `B2B`, `foreign`, `investment`, `consumer`, or similar labels as sufficient legal classification;
- forgetting mandatory public-law overlays because a contract exists;
- treating foreign element as automatically customs/import-export;
- letting BL1 decide CISG/governing-law applicability;
- collapsing governing law, forum, arbitral procedure, and enforcement;
- keeping a rejected route closed after new material evidence;
- activating every plausible track defensively instead of applying materiality.

## Escalation

Increase verification depth when competing regimes can produce materially different validity, permission, ownership, remedy, tax, or enforcement outcomes.

Do not solve regime ambiguity by loading every track or citing every possibly relevant statute.