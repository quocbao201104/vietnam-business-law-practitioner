# Main skill review — 2026-09-13

## Assessment and evidence boundary

Reviewed revision: `18ae61152a3250b2d0627e1848492f78b3557c54`.

The skill has a coherent decision-oriented foundation, but its detailed routing
does not consistently implement that foundation across domains. The strongest
content is the separation of evidence from conclusions, legal authority from
applicability, and permission from private agreement. The most actionable
weaknesses are cross-track handoffs, selective loading, and incomplete mechanical
verification of the ownership/current-state invariants.

This review identifies four runtime-instruction findings and two checker findings.
It also records design concerns and unproven capabilities separately. None of
these findings establishes a measured failure rate for generated legal answers.

Evidence used:

- Static review of the kernel, routing index, eight BL cores, all six schemas,
  five authority references, and specialist entry point.
- Targeted review of the decision procedures and core distinctions across all
  32 capability units, with deeper input/output and handoff inspection for the
  findings below. This is not a line-by-line legal certification of every unit.
- Evaluation catalog, cold-start protocol, candidate bindings from all nine
  oracle JSON files, and targeted relevant fixture inspection.
- Six synthetic probes against the current checker's generic validators.

The probes are checker tests, not fabricated execution evidence. They do not
invoke an LLM, resolve Vietnamese law, run a frozen fixture, or establish Level 2
evidence. No legal rule, rate, deadline, treaty status, or portal availability was
independently verified against live sources during this review.

No runtime instruction, oracle, or production checker was changed. The existing
untracked root `AGENTS.md` was preserved.

## Findings

### F1 — P2: BL4's contract-only handoff path does not cover the employment work assigned to it

Evidence:

- [BL6 separation/protection](../../skills/vietnam-business-law-practitioner/knowledge/bl6-employment/restructuring-separation-protection.md),
  especially "Mutual exit", "Employment separation", and the decision procedure:
  BL6 owns employment separation, agreed status/terms, and continuing employment
  state; BL4 receives disputed claims, remedies, and procedure.
- [BL4 breach/liability](../../skills/vietnam-business-law-practitioner/knowledge/bl4-remedies-disputes/breach-excuse-liability.md),
  lines 5–7 and 144: the unit starts after BL3 establishes obligation/performance
  and directs the reader to consume BL3 state.
- [BL4 remedies](../../skills/vietnam-business-law-practitioner/knowledge/bl4-remedies-disputes/remedies-loss-mitigation.md),
  "Required state" and "Remedy-state pattern": inputs are BL4 liability and BL3
  contract propositions, with no explicit employment-merits handoff.
- [BL4 dispute/settlement](../../skills/vietnam-business-law-practitioner/knowledge/bl4-remedies-disputes/dispute-posture-procedure-settlement.md),
  "Settlement loop": agreed changes to obligations always return to BL3.

Reproduction by contract walkthrough: BL6 has committed an employment separation
position. A worker contests it and the parties propose a mutual exit changing
employment terms and payments. The outer routing assigns merits/state to BL6
and claims/procedure to BL4. Inside BL4, the stated liability inputs require BL3
and the settlement loop sends the changed obligations to BL3. The reader must
invent an exception or risk giving employment state two owners.

This is an incomplete/contradictory handoff specification, not proof that an LLM
necessarily takes the wrong path. Contractual inputs can be relevant; the defect
is making the commercial-contract route the only explicit route for work whose
substantive owner can be BL6.

Repair direction: let BL4 consume an explicitly identified substantive owner's
merits/state. Return settlement changes to that owner by proposition type. Keep
BL3 for ordinary commercial-contract changes and BL6 for employment-specific
changes. Add an employment claim and a disputed mutual-exit composition probe.

### F2 — P2: BL8's overlay representation omits BL6

Evidence:

- [BL8 core](../../skills/vietnam-business-law-practitioner/knowledge/bl8-cross-border/core.md),
  line 33, allows `substantive_owner: BL2 | BL3 | BL4 | BL5 | BL7 | null`.
- The same list appears in the
  [routing index](../../skills/vietnam-business-law-practitioner/knowledge/INDEX.md)
  and BL8 capability state patterns, including
  [governing-law/treaty](../../skills/vietnam-business-law-practitioner/knowledge/bl8-cross-border/governing-law-treaty-enforcement.md).
- [BL6 core](../../skills/vietnam-business-law-practitioner/knowledge/bl6-employment/core.md)
  explicitly consumes material BL8 cross-border propositions while retaining
  employment ownership.

Reproduction: an employment-specific term depends on a material cross-border
governing-law proposition. BL6 owns the employment term; BL8 supplies the regime
overlay. The documented overlay value set cannot name BL6. Using `null` loses
the substantive-owner link; substituting BL3 changes the owner.

Repair direction: make the representation and corresponding handoff examples
support BL6, then add a BL8-to-BL6 case. No ninth track is required. This is a
representation defect even before any particular foreign-law answer is tested.

### F3 — P2: Sibling loading confuses material dependence with a need to reopen

Evidence:

- [BL3 core](../../skills/vietnam-business-law-practitioner/knowledge/bl3-contracts/core.md),
  lines 47–55: a reliable committed sibling result may be consumed without a
  read, but a sibling is loaded when its proposition is "otherwise material to
  the current decision".
- The same broad clause appears in the BL4–BL8 cores; for example
  [BL6 core](../../skills/vietnam-business-law-practitioner/knowledge/bl6-employment/core.md),
  line 95, and [BL8 core](../../skills/vietnam-business-law-practitioner/knowledge/bl8-cross-border/core.md),
  line 129.
- The [index](../../skills/vietnam-business-law-practitioner/knowledge/INDEX.md)
  uses the narrower condition "material to reopen". The
  [BL6 JIT oracle](../../evals/composition/bl6-jit-oracles-v0.1.json), JIT-02,
  forbids reading relationship classification for a current-terms-only case.

Reproduction: employment classification is committed and reliable, and the user
asks about a pay change. Classification is material to the resulting employment
analysis, but there is no new reason to revisit it. The broad core clause permits
or prompts a read that the index, example, and oracle tell the runtime to skip.

Repair direction: consistently distinguish "the answer depends on this current
result" from "this result now needs review". Retain dependency links without
reloading the owning capability. Verify the change with the existing narrow JIT
cases and a perturbation that actually makes the upstream result stale.

### F4 — P2: Social-insurance ownership is assigned to BL5 without a matching capability route

Evidence:

- [Index](../../skills/vietnam-business-law-practitioner/knowledge/INDEX.md),
  line 181, assigns BHXH/contribution consequences to BL5.
- [BL6 core](../../skills/vietnam-business-law-practitioner/knowledge/bl6-employment/core.md)
  excludes those consequences and hands them to BL5.
- [BL5 core](../../skills/vietnam-business-law-practitioner/knowledge/bl5-tax/core.md),
  "Owns" and "JIT capability routing", describes tax characterization, taxable
  base/rate, invoice eligibility, and tax incentives.
- [BL5 characterization](../../skills/vietnam-business-law-practitioner/knowledge/bl5-tax/characterization-events-roles.md)
  mentions contribution handoffs, but its operational route and state pattern
  are tax-specific. The
  [computation unit](../../skills/vietnam-business-law-practitioner/knowledge/bl5-tax/base-method-rate-timing.md)
  activates after tax characterization and describes a taxable base and tax
  period, without an explicit contribution-coverage/base route.

Reproduction: BL6 has resolved employee/employer state and the user asks only
whether mandatory contributions apply, on what contribution base, and for which
period. BL5 is the assigned track, but the detailed map does not say which unit
owns coverage, contribution-specific roles, base, and documentation. The model
must extrapolate tax concepts or invent a capability mapping.

This is missing stable reasoning/routing for an already claimed scope, not a
request to store current contribution percentages. Repair it within the existing
BL5 units if practical, separating contribution coverage/base from tax treatment,
and add a contribution-only JIT case.

### F5 — P2: The checker accepts a stale/invalidated independent blocker

Evidence:

- [Conflict validator](../../scripts/check_runtime_trace.py), lines 347–357,
  updates `latest_prop_status` only on `PROPOSITION_STATUS`.
- Its independent-blocker check at line 578 reads that cached status; it does
  not consume later `STALE` or `INVALIDATE` events for the same proposition.
- [Runtime trace contract](../../skills/vietnam-business-law-practitioner/schemas/runtime-trace.md)
  defines those state-transition events. Terminal conflict readiness requires
  an independent **current** supported blocker.

Synthetic reproduction: record `P-BLOCK` as `SUPPORTED`, terminalize an unrelated
conflict, commit a delta making `P-BLOCK` stale/invalidated, emit the corresponding
state event, then derive `DO_NOT_PROCEED` solely from `P-BLOCK`. The generic
validators return no errors. Replacing that event with
`PROPOSITION_STATUS status=STALE` correctly produces an error.

Impact: mechanical acceptance depends on which valid event vocabulary expresses
the same state change. A checker result can overstate current-blocker support.
This does not show that a real legal run produced that answer.

Repair direction: replay effective proposition status across all relevant state
events and require explicit supported recomputation before a blocker can be
reused. Preserve controls for an unrelated invalidation and a refreshed blocker.

### F6 — P2: Generic delta validation checks owner presence, not owner authority

Evidence:

- [State-delta validator](../../scripts/check_runtime_trace.py), line 175,
  requires a non-empty owner string but does not join affected IDs to ownership.
- The generic validation dispatch does not reconstruct an `OWNER_ASSIGN` map.
- [Kernel ownership invariant](../../skills/vietnam-business-law-practitioner/SKILL.md)
  requires only the accountable owner to commit or replace its proposition.

Synthetic reproduction: assign `P-REL` to BL6, then apply a revision-correct BL5
delta to `P-REL`. All three generic validators return no errors, as they do for
the valid BL6 control.

Fixture-specific forbidden patterns catch some named examples, but do not prove
this invariant for arbitrary material IDs. A fresh ID or different event shape
can escape those particular patterns.

Repair direction: validate owner/object relationships for owned propositions,
including permitted initial assignment and owner-neutral/shared objects. Do not
infer ownership solely from ID spelling. Add negative cases for unauthorized
replacement and controls for legitimate authority/conflict metadata writes.

## Design concerns and remaining coverage questions

### D1 — Selective file loading still has a large instruction footprint

Measured using whitespace-delimited word counts, not model token estimates:

| File on an illustrative narrow BL5 live-law path | Words |
| --- | ---: |
| Kernel | 3,482 |
| Entire routing index | 2,934 |
| BL5 core | 1,227 |
| BL5 base/method/rate/timing | 977 |
| Legal work state | 2,039 |
| Authority resolver | 1,335 |
| Search strategy | 1,508 |
| Source status | 407 |
| Total | 13,909 |

The kernel is 571 lines. Even this path assumes a committed tax characterization
and excludes additional source references, output/trace contracts, retrieved law,
and user evidence. This measures instruction volume, not latency, cost, or legal
accuracy. An already-loaded session can reuse context.

The first routing read contains detailed instructions for every track before a
single core is selected, and each core repeats much of its route section. A
smaller top-level index and thinner always-on kernel are worth testing after
semantic repairs. Do not trim necessary authority safeguards merely to hit a
word target; compare read volume and behavior on the same cases.

### D2 — Reclassification review lacks explicit non-change completion semantics

The state/composition/trace contracts specify signal, review, and committed new
classification. They do not equally specify how a completed review rejects a
candidate while retaining the old classification, or finishes inconclusively
without falsely resolving either candidate. Convergence disallows pending review.

An owner update may be sufficient in this semantic system, so this review does
not claim a demonstrated infinite loop. Nevertheless, the exit and trace evidence
are underspecified. Test both outcomes, including a later genuine reopening,
before requiring a new event or global primitive.

### D3 — BL7 regulatory-enforcement handling needs a concrete coverage test

BL4 excludes regulator-facing enforcement and sends it to BL7. BL7's detailed
units center on perimeter, permission maintenance, market conduct, and data
operations. A business challenging a regulatory decision requires a clear owner
for response, challenge, and timing propositions. The reviewed routes do not make
that procedural boundary sufficiently explicit to certify coverage.

Treat this as a targeted scenario to evaluate, not proof that another permanent
unit is necessary. Preserve the distinction between public-law review and private
claim procedure.

## Coverage by section

| Section | Useful behavior retained | Review result |
| --- | --- | --- |
| Kernel/intake | Starts from requested action; asks only for blocking facts; preserves conditional answers | Clear purpose; footprint and review exits need work |
| BL1: four framing/routing/temporal/authority units | Does not promote downstream classification; avoids a universal authority gateway | No additional confirmed local defect in targeted review |
| BL2: four actor/authority/governance/ownership units | Separates entity, representative, approval, and completed ownership | Useful distinctions; needs operational JIT evidence |
| BL3: four formation/terms/performance/change units | Distinguishes assent, effectiveness, obligation due, performance, and remedy | F3; settlement handoff also implicated in F1 |
| BL4: four liability/remedy/preservation/procedure units | Distinguishes liability from recovery and deadlines from filing mechanics | F1; contract cases dominate the explicit inputs |
| BL5: four characterization/computation/documents/incentive units | Distinguishes statutory liability from allocation, invoice from entitlement, and feedback from reclassification | F4; contribution scope is not operationalized |
| BL6: four relationship/terms/action/separation units | Separates performance, misconduct, restructuring, and mutual exit; respects privacy ownership | F1/F2 interfaces, F3, and D2 |
| BL7: four perimeter/permission/conduct/data units | Separates permission from conduct, and useful evidence from lawful collection | D3; no claim of comprehensive sector coverage |
| BL8: four investment/regime/FX/trade units | Separates treaty jobs, payment from customs, origin from shipment, and border clearance from domestic permission | F2; other reviewed distinctions are useful |
| Authority and references | Identity/version/provision checks, official fallback, and proposition-specific applicability | Internally coherent in reviewed paths; live retrieval untested here |
| Shared state/composition/output | Stable IDs, revision-safe deltas, non-READY endpoints, explicit action links | F5/F6 limit verification; D2 remains open |
| Specialist | Candidate findings return to owner; no mandatory extra agent | A contract for depth, not evidence of specialist competence |
| Evals | Separates manual, cold-start, and independent evidence | Current runtime proof remains incomplete |

## Verification performed

1. Inventoried 54 runtime Markdown files, including 32 capability units.
2. Parsed all nine oracle JSON files and recorded their distinct historical
   candidate bindings. No frozen oracle was rebound to current HEAD.
3. Checked inline Markdown file references against containing directory, skill
   root, and repository root. Unresolved literal basenames were contextual
   references to files named elsewhere in the same section; they were not counted
   as confirmed missing-file bugs. This was not an exhaustive link/anchor check.
4. Ran the six synthetic generic-validator probes below. No cold-start fixture
   or full CLI/oracle trace pass is claimed.
5. Reviewed the new review/probe artifacts and checked final worktree status.

Reproduce from the repository root:

```text
python research/reviews/skill-audit-probes-2026-09-13.py --help
python research/reviews/skill-audit-probes-2026-09-13.py
```

Observed checker SHA-256:
`0ae88bbd0ad686bb5899b58ad88b4791a96c851034b44d4351e692d951c7f439`.

| Synthetic probe | Should generic checks reject? | Observed rejection |
| --- | --- | --- |
| Current supported independent blocker | No | No |
| Blocker changed by `PROPOSITION_STATUS status=STALE` | Yes | Yes |
| Blocker changed by `STALE` | Yes | No |
| Blocker changed by `INVALIDATE` | Yes | No |
| BL6 writes a BL6-owned proposition | No | No |
| BL5 writes a BL6-owned proposition | Yes | No |

The probe program's successful exit means it collected observations, not that
the skill or invariants passed. The script does not write a runtime trace or
alter an oracle. Its findings are limited to the generic validators called by
the production checker; fixture-specific rules may reject additional events.

## Follow-through sequence

1. Repair F1/F2/F4 using existing owners and proposition types; add targeted
   employment, cross-border employment, and contribution cases.
2. Repair F3 consistently across canonical routes and consumers.
3. Repair F5/F6 and exercise negative controls before relying on checker PASS.
4. Resolve D2 through explicit retained/inconclusive review scenarios; probe D3
   before deciding whether any structural extension is needed.
5. Measure and reduce D1 without weakening ownership or live-law requirements.
6. Review/freeze an appropriate integrated candidate and run isolated runtime
   cases, including live authority and answer-quality review. Historical oracle
   results cannot certify later semantics.

The [evaluation catalog](../../evals/composition/README.md) explicitly says all
eight BL JIT layers are **NOT YET PROVEN** and the broader runtime gate remains
open. This review does not change that status. The current session has already
read the architecture and cannot itself serve as a clean cold-start run.
