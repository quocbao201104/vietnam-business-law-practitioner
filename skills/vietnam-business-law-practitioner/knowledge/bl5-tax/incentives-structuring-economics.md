# BL5 — Incentives / Structuring / Economic Feedback

## Owns

Determining whether a preferential tax benefit/incentive/treatment is actually available for the resolved business state, and translating supported tax consequences into bounded structuring/economic feedback for the owning business/legal tracks.

This unit owns **preferential incentive/exemption/holiday entitlement propositions and tax-economic feedback** after the underlying taxable scope/business state is sufficiently resolved. It does not redesign or reclassify the underlying transaction, corporate structure, employment relationship, foreign-investment pathway, or product strategy.

## Does not own

- corporate ownership/governance/structure — BL2;
- transaction formation/terms/obligations — BL3;
- breach/remedy — BL4;
- taxable-scope/non-taxable characterization integral to whether an event falls within a tax regime — `characterization-events-roles.md`;
- employment classification/pathway — BL6;
- regulatory permission — BL7;
- investment/FX/trade/customs structure — BL8;
- bookkeeping/accounting/financial-modeling decisions.

## Activate when

Use when the decision depends on:

- whether a claimed preferential tax incentive/exemption/holiday/preference is actually available after taxable scope is established;
- whether qualifying conditions for that preferential benefit remain satisfied;
- whether two otherwise lawful structures have materially different supported tax consequences;
- whether tax cost/timing/document burden makes an upstream option unattractive;
- whether a planned restructuring needs tax consequences fed back to BL2/BL3/BL6/BL8;
- whether tax optimization language should be reframed into compliant tax-aware structuring.

Skip when the user only needs taxable-scope characterization, rate, or documentation analysis and no structural/business decision changes.

## Required state

Where material, consume:

- committed BL5 characterization/role proposition;
- committed base/rate/timing proposition;
- committed documentary eligibility state;
- upstream business options from BL2/BL3/BL6/BL8;
- current/historical incentive authority;
- factual eligibility conditions;
- relevant action date/planned transaction date;
- estimated supported tax consequence for each option;
- uncertainty/freshness state.

Do not independently redesign or reclassify upstream business/legal state merely to obtain a tax benefit.

## Core distinctions

### Taxable-scope exclusion ≠ preferential exemption/incentive

`characterization-events-roles.md` owns whether a resolved business event falls inside/outside taxable scope where an exclusion is integral to defining the regime itself.

This unit owns a claimed preferential benefit, exemption, holiday, or incentive after the relevant taxable regime/business state is otherwise sufficiently established and entitlement depends on qualifying conditions.

Do not let the word `exemption` create duplicate ownership. Ask whether the proposition is about **scope** or **preferential entitlement**.

### Incentive category match ≠ entitlement

A company/project/activity appearing to resemble an incentive category does not establish entitlement.

Resolve the exact legal conditions, relevant actor/activity/location/time/document state, and current authority.

### Incentive entitlement ≠ permanent entitlement

Conditions may be time-bound, event-bound, approval/document-bound, or lost after a change in facts/law.

Bind the proposition to the relevant period/action.

### Lower nominal tax ≠ better structure

Tax is only one constraint. A lower-tax option may increase regulatory, contractual, operational, financing, governance, employment, execution, or evidence risk.

BL5 may provide **FEEDBACK**; it does not silently overrule the owning track.

### Tax economics ≠ upstream invalidity

If a valid BL2/BL3/BL6/BL8 option is tax-expensive, the normal edge is:

```text
BL5 tax consequence
→ FEEDBACK
→ owning track may reconsider a prospective lawful option
```

not:

```text
unattractive tax result
→ invalidate/reclassify upstream legal state
```

Only explicit `DEPENDS_ON` propositions may be invalidated when an upstream fact changes.

### Tax feedback ≠ reclassification authority

Tax economics alone never justify changing a factual/legal classification.

BL5 feedback may cause an owner to:

- reconsider a **prospective lawful option**;
- restructure or re-negotiate future conduct where legally available;
- reopen a classification only when **new non-tax facts/evidence** make that classification genuinely reviewable under the owning track's rules.

Example:

```text
employee tax/contribution cost is high
≠ reason to classify worker as contractor
```

BL6 still owns the employment classification based on the relationship facts and applicable law.

### Tax-aware structuring ≠ evasion

Optimize only among lawful, supportable options. Do not invent transactions, labels, sham arrangements, circular flows, fake invoices, artificial employment/contractor statuses, or unsupported residency/ownership positions to manufacture a tax result.

### Tax result ≠ accounting/finance recommendation

BL5 may explain legal tax cash/timing consequences. It does not own bookkeeping treatment, financial reporting, valuation, financing, or full investment-return analysis.

## Contribution relief and economics

Routine scheme coverage exclusions belong to characterization. Load this unit
for contributions only when a separately claimed preferential relief requires
entitlement analysis, or a supported contribution cost changes a comparison of
lawful prospective options. Consume coverage, computation and evidence results;
verify relief conditions live and preserve the distinction from tax incentives.
Cost feedback never changes BL6 relationship/employer classification.

## Decision procedure

1. **State the decision being informed.** Example: `Does supported tax treatment materially change which lawful prospective option should be considered?`
2. **Consume the upstream options.** Do not create a new corporate/contract/employment/cross-border option from tax intuition alone.
3. **Resolve preferential incentive entitlement where claimed.** Verify all material legal/factual/documentary conditions with current authority. Return taxable-scope questions to `characterization-events-roles.md` when needed.
4. **Compute only supported tax consequences.** Use committed BL5 base/rate/timing/document state; preserve uncertainty.
5. **Compare tax consequences on like-for-like assumptions.** Do not use different hidden business assumptions to favor one option.
6. **Identify non-tax dependencies.** Mark BL2/BL3/BL6/BL7/BL8 consequences that remain for their owners.
7. **Emit bounded feedback.** State what tax fact changes the economics or merits review of the prospective option and why.
8. **Return to the owner.** The owning track may reconsider or restructure/re-negotiate future conduct where legally available. Reopen an existing classification only when new non-tax facts/evidence independently justify review. Tax economics alone never justify reclassification.
9. **Re-resolve before irreversible action.** Incentive/rate/threshold/freshness changes can invalidate the tax comparison without changing upstream legal facts.

## Feedback pattern

```text
P-BL5-ECON-01
upstream_option: OPTION-A
supported_tax_effect: <amount/range/timing/condition>
incentive_dependency: <if any>
document_dependency: <if any>
uncertainty: <...>
edge: FEEDBACK
recommended_owner_review: BL2 / BL3 / BL6 / BL8
```

For incentive entitlement:

```text
P-BL5-INC-01
incentive: <candidate preferential benefit>
eligibility_conditions: [...]
temporal_scope: <...>
documentary_dependency: P-BL5-DOC-...
status: ELIGIBLE / CONDITIONAL / NOT_ESTABLISHED / UNRESOLVED / NOT_APPLICABLE
```

These are reasoning states, not statutory labels.

## Evidence requirements

Potential evidence includes:

- committed corporate/transaction/employment/cross-border state;
- official incentive eligibility records/approvals where legally material;
- documents proving factual conditions;
- current authority for the incentive;
- supported base/rate/timing calculations;
- evidence of planned action date/location/activity;
- scenario assumptions explicitly stated by the user/owning track.

Do not infer eligibility from marketing materials, generic investment promotion pages, or the company’s own description when authoritative conditions are material.

## Live authority triggers

Use Authority Resolver where the result depends on:

- current preferential tax incentives/exemptions/holidays/preferences;
- eligibility conditions;
- effective periods/transitional rules;
- current rates/thresholds used in option comparison;
- clawback/loss-of-entitlement consequences;
- historical incentive rules for an existing project/transaction.

Taxable-scope exclusions integral to whether the event belongs in the regime remain with `characterization-events-roles.md`.

Do not hardcode incentive lists, tax holidays, preferential rates, thresholds, geographic lists, qualification periods, or application procedures as stable knowledge.

## Cross-track handoffs

### To BL2

Return tax feedback about prospective ownership/capital/restructuring options. BL2 owns the corporate state and whether/how to change it.

### To BL3

Return tax feedback about prospective pricing/payment/allocation/transaction structure. BL3 owns contract terms and transaction change.

### To BL6

Return tax/contribution consequences of the committed employment classification/pathway. BL6 owns employee/contractor and employment-law employer classification/action.

Tax economics alone must not be used as a reason to reclassify the worker. Reopen BL6 only when new non-tax facts/evidence independently make the relationship classification reviewable.

### To BL8

Return tax consequences of a cross-border/investment/payment/trade structure. BL8 owns the cross-border mode and investment/trade proposition.

### From characterization unit

Consume the committed taxable-scope/regime proposition. Return scope/exclusion questions to `characterization-events-roles.md`; do not duplicate them here.

### From documentation unit

Consume documentary eligibility/gaps. Do not declare an incentive available when its documentary prerequisite remains unresolved.

## Failure modes

- taxable-scope exclusion and preferential incentive exemption given duplicate owners;
- category resemblance treated as incentive entitlement;
- outdated incentive/rate used for current structuring;
- lowest nominal tax treated as automatically optimal;
- BL5 redesigning corporate/contract/employment/cross-border state without owner review;
- tax feedback emitted as automatic invalidation;
- tax economics used to justify employment, transaction, ownership, residency, or cross-border reclassification;
- tax optimization used to justify fake/sham labels or unsupported transactions;
- marketing/investment-promotion material treated as binding incentive authority;
- accounting/financial recommendation presented as tax-law conclusion;
- false precision in option comparison despite unresolved authority/documents.

## Escalation

Increase verification for restructurings, acquisitions, foreign investment, related-party arrangements, large capital expenditures, incentive-dependent investments, worker-model changes, cross-border payment structures, or any irreversible decision whose commercial case materially depends on current tax treatment.