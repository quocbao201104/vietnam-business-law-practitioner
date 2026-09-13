# BL2 — Ownership / Corporate Control / State Change

## Owns

Determining the company's **corporate ownership, voting/control, and corporate-state transition** for business-law decisions.

This unit owns the internal corporate facts and legal propositions about who owns what, who can exercise corporate rights, and what corporate state exists before/after a transaction.

It does not own foreign-investor classification, market-access consequences, treaty/investment-law control tests, or regulatory approval for foreign investment; those belong to BL8.

## Does not own

- contract terms/closing obligations — BL3;
- tax consequences of transfers/distributions/restructuring — BL5;
- employment consequences — BL6;
- sector/public-law licensing — BL7;
- foreign-investment status, market access, investment procedures, or cross-border control tests — BL8.

## Activate when

Use when the decision depends on:

- who legally owns equity/member interests/shares or comparable corporate rights;
- whether a transfer/subscription/contribution has actually changed ownership state;
- voting rights or corporate control;
- beneficial/economic interest versus completed legal ownership;
- capitalization/member/shareholder state;
- dilution, issuance, transfer, redemption, conversion, restructuring, merger-like or other corporate-state change;
- whether corporate records match the claimed ownership/control state.

## Required state

Where material, capture:

- entity/corporate form;
- current and historical owners/members/shareholders;
- legal/economic interest claimed by each actor;
- voting/control rights;
- transfer/subscription/contribution instruments;
- payment/contribution evidence;
- approvals/conditions precedent;
- closing/completion evidence;
- corporate registers/certificates/registry evidence where relevant;
- charter/governance rights affecting control;
- relevant dates;
- foreign ownership facts that may trigger BL8.

## Core distinctions

### Economic contribution ≠ completed legal ownership

Paying money, funding a company, financing a founder, signing a subscription/transfer document, or agreeing an economic split does not automatically prove that the legal ownership state changed.

Resolve the steps/evidence required for the particular corporate state transition.

### Contract right ≠ current ownership state

A party may have a contractual right to receive shares/interests later while not yet holding the completed legal ownership position today.

BL3 owns the contract right; BL2 owns the resulting corporate ownership state once the relevant conditions/steps are resolved.

### Ownership percentage ≠ complete control analysis

Corporate control may depend on more than headline percentage. Voting rights, veto/reserved matters, appointment rights, class rights, governance agreements, dispersed ownership, or other legal rights can matter.

Do not use a universal percentage threshold as a stable control rule.

### Corporate control ≠ foreign-investment control test

BL2 may determine:

- cap table;
- voting rights;
- internal control rights;
- corporate appointment/governance rights.

BL8 determines whether those facts satisfy a **foreign-investment-specific** control/status/market-access test.

### Beneficial/economic interest ≠ registered/legal title

Preserve the distinction where it changes a legal proposition. Do not collapse nominee, beneficial, contractual, economic, voting, and registered interests into one field called `owner`.

### Planned transfer ≠ completed state change

Keep clear states such as:

```text
proposed
signed/committed
conditions pending
closing/completion pending
corporate records pending
completed/resolved
contested
```

Use only the distinctions needed for the decision; do not invent bureaucracy when the state is already clear.

## Decision procedure

1. **State the ownership/control proposition.** Example: `Does Buyer B currently own 40%?`, `Who can exercise voting rights today?`, `Did the transfer change corporate state?`
2. **Resolve the starting corporate state.** Consume entity records/evidence from `entity-actor-state.md`.
3. **Separate legal title, economic interest, voting rights, and contractual claims where material.**
4. **Map the state-change mechanism.** Transfer, issuance/subscription, contribution, conversion, redemption, restructuring, inheritance/succession, or another mechanism as applicable.
5. **Identify conditions and required corporate steps.** Coordinate internal approvals with `approval-conflict-governance.md` and transaction terms with BL3.
6. **Verify completion evidence.** Do not infer ownership change solely from signed documents or payment.
7. **Resolve control separately from ownership percentage.** Identify legally relevant voting/governance rights without importing a foreign-investment test.
8. **Bind state to time.** Determine ownership/control at the date relevant to signing, approval, tax, investment, dispute, or other downstream proposition.
9. **Commit the corporate-state proposition.** Supported, conditional, disputed, unresolved, or superseded.
10. **Hand foreign-element facts to BL8 when triggered.** BL8 determines foreign-investor/control/market-access consequences.

## Corporate-state proposition design

Prefer propositions such as:

- `P-BL2-OWN-01: Actor A held legal ownership of interest X at date D.`
- `P-BL2-OWN-02: Buyer B had a contractual acquisition right but ownership transfer was not yet completed.`
- `P-BL2-CTRL-01: Actor A could exercise voting right V under the resolved corporate state.`
- `P-BL2-STATE-01: Issuance/transfer changed the cap table from state S1 to S2.`

Avoid propositions like:

- `A controls the company because A owns 51%` without resolving the actual corporate/control question;
- `foreign investor controls the company` inside BL2 when a foreign-investment legal test is required.

## Evidence requirements

Potential evidence includes:

- corporate/member/shareholder registers;
- ownership certificates or equivalent records where relevant;
- charter/governance documents;
- subscription/transfer/contribution agreements;
- closing certificates/confirmations;
- payment/contribution evidence;
- resolutions/approvals;
- amended corporate records;
- regulatory/registry records where their legal effect is material;
- side agreements governing voting, veto, appointment, or transfer rights.

No single document is universally conclusive. Evidence sufficiency depends on the ownership/control proposition and relevant date.

## Live authority triggers

Live authority is normally required when the result depends on:

- current rules for creation/transfer/completion of corporate ownership;
- statutory rights attached to corporate interests;
- current registration/recording effect;
- capital contribution/subscription timing or consequences;
- corporate forms and ownership mechanisms;
- merger/restructuring/state-transition rules;
- historical rules at the relevant transaction date.

Do not hardcode current ownership thresholds, filing procedures, forms, deadlines, or foreign-investment percentages.

## Cross-track handoffs

### From BL3

BL3 may establish that parties agreed a transfer/subscription or closing condition. BL2 determines whether/when the corporate ownership state actually changed.

### To BL3

Return current corporate ownership/control state and unresolved completion conditions when they affect transaction rights/obligations.

### To BL5

Provide the resolved ownership/state-change proposition and transaction facts. BL5 determines tax consequences.

### To BL7

Provide ownership/control state only if a sector/public-law permission depends on it. BL7 owns the regulatory proposition.

### To BL8

Provide:

- cap table;
- legal ownership state;
- voting/control rights;
- transaction/state change;
- relevant dates;
- unresolved corporate conditions.

BL8 then determines foreign-investor status, foreign-investment control tests, market access, and investment procedure.

## Feedback and invalidation

A later ownership correction or completed state change may invalidate exact downstream propositions linked through `DEPENDS_ON`.

Examples:

- BL8 foreign-investment proposition depending on outdated cap table;
- BL5 tax proposition depending on transfer completion date;
- governance approval proposition depending on voting rights at a meeting date.

Do not invalidate unrelated BL2/BL3/BL5/BL8 state merely because ownership changed somewhere in the case.

## Failure modes

- payment treated as completed ownership transfer;
- signed share/interest agreement treated as current legal title without checking completion;
- contractual acquisition right treated as already-owned equity;
- beneficial/economic interest collapsed into registered/legal title;
- ownership percentage used as a universal control rule;
- BL2 deciding foreign-investment control/market-access consequences;
- current cap table projected backward to an earlier approval/transaction date;
- tax or transaction owner independently reconstructing corporate ownership instead of consuming BL2 state.

## Escalation

Increase verification for disputed cap tables, founder/investor disputes, major dilution or control changes, incomplete closings, undocumented side arrangements, nominee/beneficial ownership complexity, cross-border acquisitions, or transactions where downstream authority/tax/regulatory conclusions depend on the exact ownership state.