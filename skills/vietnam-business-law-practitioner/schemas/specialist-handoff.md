# Specialist Handoff — Semantic Contract

A handoff transfers resolved state, unresolved state, and ownership context. It is not permission for the receiving track to reinterpret upstream decisions silently.

## Required handoff elements

A useful handoff should identify:

- activating issue;
- sending track;
- receiving owner/specialist;
- resolved facts/classifications;
- unresolved material conditions;
- authorities already resolved and reusable;
- exact decision requested from the receiver;
- downstream decisions waiting on the result.

## Example — BL2 to BL3

```text
ACTIVATING ISSUE:
Can the company enter the proposed distribution agreement?

FROM:
BL2

TO:
BL3

ENTITY:
Company A — confirmed

SIGNATORY:
Director B

REPRESENTATION:
confirmed

AUTHORITY_SCOPE:
likely within scope

CORPORATE_APPROVAL:
unresolved

RELATED_PARTY:
yes

OPEN_CONDITION:
member/board approval may be required

DECISION REQUESTED:
Determine what contractual relationship and obligations the proposed agreement creates.

CONDITION:
Final binding/enforceability position remains conditional on BL2 approval resolution.
```

## Return-to-owner rule

If the receiver discovers evidence that changes an upstream-owned classification or decision:

1. do not silently update it;
2. emit a signal to the owner;
3. identify the evidence;
4. identify dependent decisions that may be affected;
5. resume only after the shared state is updated.

Examples:

- BL3 discovers a power of attorney → signal BL2;
- BL5 sees payroll-style facts relevant to employee classification → signal BL6;
- BL7 discovers a foreign-platform fact that affects investment/cross-border status → signal BL8;
- BL8 discovers mandatory domestic product regulation → signal BL7.

## Specialist-depth handoff

A JIT specialist is a temporary depth provider, not a new global owner.

Example:

```text
OWNER:
BL8

SPECIALIST:
preferential-origin

QUESTION:
Does product X qualify for preferential origin under the relevant FTA for the planned import date?

INPUTS:
- candidate HS classification
- production/process facts
- country inputs
- shipment facts
- relevant FTA

OUTPUT EXPECTED:
- origin classification/candidates
- authority used
- unresolved technical facts
- eligibility conclusion/status

RETURN TO:
BL8
```

The specialist must not synthesize the whole business answer.
