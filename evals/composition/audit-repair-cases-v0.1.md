# Audit repair cases v0.1

These are semantic review scenarios for the uncommitted repairs following the
2026-09-13 audit. They are not candidate-bound cold-start oracles and have no
runtime PASS status. Historical CT/RF/BL JIT oracles retain their original binding.

## AR-01 — Employment dispute and mutual exit

Input: BL6 relationship, terms and separation merits are committed. The employee
contests the separation. Parties propose an agreed end date and final employment
payments. No separate commercial transaction is disputed.

Expected: BL4 consumes BL6 merits for claim/remedy/procedure. BL6 separation owns
the agreed employment end-state/content/effect; BL4 consumes its committed or
conditioned update for remaining claims and procedural consequences. No invented
BL3 obligation/performance prerequisite. A still-open BL4 claim-liability issue
is separate from re-deciding the BL6 ground.

Perturbation: settlement also changes an unrelated commercial loan. Split the
loan terms to BL3; do not transfer all employment terms with them. If only an
ongoing pay term changes, BL6 engagement/terms owns that proposition.

## AR-02 — Cross-border employment term

Input: a committed BL6 employment-specific term is affected by a material
cross-border governing-law question; there is no goods, investment or FX issue.

Expected: BL8 governing-law unit consumes BL6 term content, records `OVERLAY` and
`substantive_owner: BL6`, and returns regime findings to BL6 for merits. Skip
investment/FX/trade units. Do not assign the employment term to BL3 or BL8.

Perturbation: remove the foreign/regime issue. Do not retain BL8 merely because
the employee's name or employer brand sounds foreign.

## AR-03 — Reliable upstream result versus reopened result

Input: employment classification is committed and reliable. Only a pay change is
requested; no new classification evidence, authority change or scope change.

Expected: BL6 engagement/terms consumes classification without reading its
sibling classification unit again. Dependence alone is not a reload trigger.

Perturbation: new material work facts contradict the committed classification.
Read the classification unit, use owner review and preserve conditional dependent
reasoning. Do not infer that selective loading forbids necessary re-review.

Apply equivalent controls to BL3 committed terms, BL4 committed deadlines and
BL8 committed governing-law state.

## AR-04 — Contribution-only question

Input: BL6 employee/employer and remuneration facts are committed. User asks about
compulsory social-insurance coverage, contribution base, period and evidence.

Expected: BL5 characterization resolves scheme coverage/contributor roles;
base/method/rate/timing resolves scheme-specific computation and periods;
documentation resolves registration/declaration/payroll/payment evidence. Each
material legal requirement uses current/historical authority and owner
applicability. No invented rates, coverage or legal conclusions in this fixture.

Skip incentives unless separate preferential relief/economics becomes material.
Do not equate tax base with contribution base, payroll deductions with remittance,
or employee classification with automatic coverage of every scheme.

Perturbations: coverage already committed and only base is asked (skip coverage
unit); only payment evidence is asked (documentation only); tax question added
(separate tax propositions); cheaper contributions desired (no reclassification).

## Checker regression scope

`scripts/test_runtime_trace.py` exercises synthetic state-validator behavior:
stale/invalidated blockers, refreshed/unrelated controls, correct/wrong/reconciled
owner writes, rejected foreign proposals, assignment laundering, and separate
authority/conflict metadata. Its PASS is software-test evidence, not an LLM run.

Relevant existing suites: BL3–BL8 narrow JIT selectivity; BL4 settlement;
BL6 reclassification; BL8 overlay; CT/RF ownership, invalidation, conflict and
readiness; freshness expiry/re-resolution. Rerun on an appropriately frozen
integrated candidate before claiming current runtime coverage.
