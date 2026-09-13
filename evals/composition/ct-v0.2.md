# Composition Adversarial Suite v0.2

**Canonical suite.** Supersedes `ct-v0.1.md` for Phase 4 architecture evaluation.

A case passes only if both the final outcome and the expected execution path are preserved. A plausible answer produced through the wrong route/owner/authority/invalidation path is an architecture failure.

## Path oracle dimensions

Where material, record:

- initial route hypothesis;
- activated owners;
- intentionally skipped tracks;
- late-route activation;
- proposition owner;
- authority call + temporal anchor(s) + freshness;
- specialist invocation + return owner;
- contradiction/reclassification transition;
- typed dependency/invalidation;
- composition conflict handling;
- per-action readiness.

| ID | Scenario | Expected architecture path | Blocking failure |
|---|---|---|---|
| CT-01 | Founder says `I own the company, so I can sign` | BL1 route BL2; BL2 separates ownership from authority | Owner status treated as signing authority |
| CT-02 | CEO signs large related-party deal without visible board/member approval | BL2 owns representation + approval propositions; BL3 transaction proposition depends on required approval where material | Signature treated as sufficient approval |
| CT-03 | Employee signs PO without visible POA; company receives goods and pays repeatedly | BL2 tests authority/ratification from evidence; BL3 consumes committed BL2 proposition | Contract automatically declared non-binding from missing POA |
| CT-04 | Supplier delivers 10 days late | BL3 owns obligation/performance; late-route/activate BL4; BL4 owns breach/excuse/remedy | Delay directly becomes penalty/termination |
| CT-05 | Contract says `customer bears all Vietnam taxes` | BL3 owns allocation clause; BL5 owns statutory taxpayer/withholder consequence | Clause treated as rewriting tax law |
| CT-06 | User calls worker freelancer; fixed schedule + manager supervision | BL6 owns classification; BL5 waits or conditions tax proposition | Freelancer tax applied directly from label |
| CT-07 | Employee underperforms; founder wants disciplinary dismissal | BL6 distinguishes performance vs misconduct pathway | Poor performance treated as disciplinary offence |
| CT-08 | Employer wants employee-message access to prove misconduct | BL6 evidence need; late-route BL7 privacy/regulatory proposition | Evidence need treated as unlimited monitoring right |
| CT-09 | B2C SaaS terms say customer consents to any data use | BL3 records clause; BL7 independently owns regulatory permission | Contract consent treated as privacy compliance |
| CT-10 | Distributor agrees not to sell competitors | BL3 contractual proposition; BL7 competition trigger | Agreement treated as automatically lawful |
| CT-11 | Singapore buyer acquires 40% of Vietnamese company | BL2 corporate share/control proposition; BL8 foreign-investment/market-access proposition | Corporate validity treated as sufficient foreign-investment compliance |
| CT-12 | Vietnamese buyer purchases goods from foreign seller | BL1 route hypothesis → BL8 governing-law/CISG proposition → BL3 contract reasoning | Vietnamese commercial law applied automatically |
| CT-13 | Goods ship from an FTA country | BL8 separates shipment, origin, HS, tariff entitlement; specialists owner-bound if used | `FTA country = 0% duty` |
| CT-14 | User gives only product name and asks for HS code | BL8 invokes HS specialist under BL8; missing product facts remain unresolved | Model guesses HS directly or specialist bypasses owner |
| CT-15 | Contract uses DDP Vietnam | BL3 owns Incoterm allocation; BL8 owns statutory border/customs roles | DDP treated as transferring every statutory duty |
| CT-16 | Law enacted now takes effect next year | Authority result lifecycle `FUTURE_EFFECTIVE`; current action cannot use as current rule | Future law applied as current |
| CT-17 | Implementing regulation later suspended/replaced | authority freshness/change signal → re-resolution → exact `DEPENDS_ON` propositions stale | Cached old rule remains current/READY silently |
| CT-18 | Parties settle debt with acknowledgement + new schedule | BL4 settlement event → signal/feedback BL3 → BL3 commits changed transaction state; affected deadlines/remedies recompute | Old contract state remains unchanged or feedback auto-invalidates unrelated propositions |
| CT-19 | New evidence suggests service contractor may actually be employee | `CLASSIFICATION_SIGNAL` → BL6 `RECLASSIFICATION_REVIEW`; dependent actions verify; only after commit invalidate exact dependents | Immediate silent employee reclassification or old state used unchanged |
| CT-20 | Imported product clears customs but lacks domestic approval | BL8 customs proposition supported; late-route BL7; sell/advertise actions separately gated | Customs clearance treated as permission to sell |
| CT-21 | Company may sign regulated-service contract today but may not perform until license | BL2/BL3 support sign action; BL7 blocks commence action; readiness per action | One global `READY` or one global `DO_NOT_PROCEED` |
| CT-22 | User says debt paid; receipt says paid; creditor disputes; no bank evidence | Fact proposition keeps evidence provenance separate; epistemic status remains disputed/unresolved | `DOCUMENTED` treated as established truth |
| CT-23 | Strong evidence suggests contractor may be employee but evidence incomplete | BL6 reclassification review; prior committed state remains but dependent terminate/pay actions become `VERIFY_BEFORE_ACTION` | Silent promotion to employee or ignoring competing candidate |
| CT-24 | Statute current today but transition rule preserves old regime for old contracts | Resolver returns lifecycle + transition authority; proposition owner decides case applicability against formation anchor | `CURRENT_BINDING` automatically treated as applicable |
| CT-25 | Authority verified yesterday; regulator suspends today before irreversible action | freshness/change trigger → re-resolve before readiness | Yesterday's cache keeps action READY |
| CT-26 | BL5 finds tax filing inconsistent with BL2 ownership state | BL5 emits `CONTRADICTION_SIGNAL` with evidence → BL2 review; BL5 does not reconstruct ownership | BL5 silently rewrites cap table/control |
| CT-27 | Cross-border contract has Singapore arbitration clause and Vietnam enforcement issue | BL3 owns clause content; BL8 governing-law/treaty/international-enforcement overlay; BL4 dispute procedure/remedies after resolved regime | BL4 and BL8 independently resolve same forum proposition |
| CT-28 | BL5 finds tax economics make current structure unattractive | `FEEDBACK` to BL2/BL3 creates review trigger only | Tax feedback automatically invalidates legally valid structure |
| CT-29 | Two valid owner propositions create incompatible action conditions | create `COMPOSITION_CONFLICT`; return to owners; action not READY | Synthesizer chooses whichever conclusion appears reasonable |

## Blocking architecture failures

- silent fact promotion;
- provenance/truth-status collapse;
- silent route repair;
- closed-world BL1 routing;
- proposition ownership violation;
- specialist bypass of owner;
- silent classification change;
- candidate reclassification treated as committed;
- track-level feedback treated as executable invalidation;
- stale/future authority used as current;
- lifecycle treated as case applicability;
- wrong/single temporal anchor when multiple anchors matter;
- mandatory regulatory layer bypassed;
- downstream reasoning based on stale/invalidated state;
- global readiness for actions with different prerequisites;
- `READY` without positive prerequisite closure;
- synthesizer creating or choosing substantive legal conclusions;
- stale state delta overwriting a newer owner state.

## Pass rule

A legally reasonable alternative interpretation is not automatically a failure if ownership, evidence status, authority lifecycle/applicability, dependencies, route state, and affected action readiness remain explicit.

The suite passes only when frozen cases preserve the expected **activation path, proposition ownership, authority dependencies, state transitions, invalidation semantics, specialist return path, and final per-action decision under adversarial perturbation**.