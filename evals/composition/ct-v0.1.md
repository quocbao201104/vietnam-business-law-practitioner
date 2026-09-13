# Composition Adversarial Suite v0.1

Architecture failure is about state/ownership/composition, not stylistic disagreement.

| ID | Scenario | Expected invariant | Blocking failure |
|---|---|---|---|
| CT-01 | Founder says `I own the company, so I can sign` | BL2 separates ownership from authority | Owner status treated as signing authority |
| CT-02 | CEO signs large related-party deal without visible board/member approval | BL2 separates representation from transaction approval; BL3 remains conditional | Signature treated as sufficient approval |
| CT-03 | Employee signs PO without visible POA; company receives goods and pays repeatedly | BL2 tests ratification/course of conduct | Contract automatically declared non-binding |
| CT-04 | Supplier delivers 10 days late | BL3 records deviation; BL4 tests breach/excuse/remedy | Delay automatically triggers penalty/termination |
| CT-05 | Contract says `customer bears all Vietnam taxes` | BL3 records allocation; BL5 resolves statutory duty | Clause treated as rewriting tax law |
| CT-06 | User calls worker freelancer; worker has fixed schedule and manager supervision | BL6 owns classification; BL5 waits | Freelancer tax applied directly from label |
| CT-07 | Employee underperforms; founder wants disciplinary dismissal | BL6 separates performance from misconduct | Poor performance treated as disciplinary offence |
| CT-08 | Employer wants access to employee messages to prove misconduct | BL6 evidence need; BL7 privacy/regulatory check | Evidence need treated as unlimited monitoring right |
| CT-09 | B2C SaaS terms say customer consents to any data use | BL3 recognizes term; BL7 independently tests regulation | Contract consent treated as privacy compliance |
| CT-10 | Distributor agrees not to sell competitors | BL3 contractual state; BL7 competition trigger | Agreement treated as automatically lawful |
| CT-11 | Singapore buyer acquires 40% of Vietnamese company | BL2 corporate mechanics; BL8 foreign-investment overlay | Corporate validity treated as sufficient |
| CT-12 | Vietnamese buyer purchases goods from foreign seller | BL8 tests governing-law/CISG layer before BL3 when material | Vietnamese commercial law applied automatically |
| CT-13 | Goods ship from an FTA country | BL8 separates shipment, origin, HS, tariff entitlement | `FTA country = 0% duty` |
| CT-14 | User gives only product name and asks for HS code | BL8 requires specialist classification/material product facts | Model guesses one HS code |
| CT-15 | Contract uses DDP Vietnam | BL3 commercial allocation; BL8 statutory border roles | DDP treated as transferring every legal duty |
| CT-16 | Law enacted now takes effect next year | BL1 state = FUTURE_EFFECTIVE | Future law applied as current |
| CT-17 | Implementing regulation is later suspended/replaced | Shared authority state invalidates dependent decisions | Cached old rule continues silently |
| CT-18 | Parties settle debt with acknowledgement + new schedule | BL4 settlement → BL3 new transaction state; deadlines reconsidered | Old contract state remains unchanged |
| CT-19 | New evidence shows service contractor is actually employee | Explicit BL6 reclassification + downstream invalidation | State changes silently |
| CT-20 | Imported product clears customs but lacks domestic product approval | BL8 border success; BL7 market blocker | Customs clearance treated as permission to sell |

## Blocking architecture failures

- silent fact promotion;
- silent classification change;
- decision ownership violation;
- stale/future authority used as current;
- mandatory regulatory layer bypassed;
- downstream reasoning based on invalidated state;
- unsupported action-readiness.

A legally reasonable alternative interpretation is not automatically a failure if uncertainty, authority status, and ownership are preserved.
