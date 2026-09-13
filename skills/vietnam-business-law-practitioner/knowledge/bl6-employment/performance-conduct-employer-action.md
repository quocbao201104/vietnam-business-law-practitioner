# BL6 — Performance / Conduct / Employer Action

## Owns

Classifying an ongoing employment issue as performance, misconduct/conduct, capability, attendance, policy/process, or another employer-management problem, and determining the lawful employer-side action pathway supported by the committed facts.

This unit owns **ongoing management/action pathway propositions**. It does not create a legal ground merely because the employer wants a particular outcome, and it does not own restructuring/redundancy or negotiated/separation state unless routed to the separation unit.

## Does not own

- employee/contractor/employer classification — `relationship-classification.md`;
- employment terms/current work state — `engagement-terms-work-state.md`;
- organizational restructuring/separation/post-employment protection — `restructuring-separation-protection.md`;
- corporate authority of the employer-side actor — BL2;
- dispute remedies/procedure — BL4;
- tax/contribution consequences — BL5;
- privacy/data/monitoring and regulatory compliance — BL7.

## Activate when

Use when the employer needs to decide what lawful management action follows from:

- poor or disputed performance;
- alleged misconduct/policy breach;
- attendance/absence issues;
- capability/fitness/qualification concerns;
- failure to follow instruction or process;
- repeated operational problems;
- warning/improvement/disciplinary questions;
- proposed suspension or other interim management measure;
- evidence gathered to support a management action.

Skip when the issue is purely hiring/terms/current state, organizational restructuring, mutual separation, post-employment protection, tax, privacy, or dispute procedure.

## Required state

Where material, consume:

- committed relationship/employer state;
- committed employment terms/current work state;
- exact duty/standard/policy/instruction allegedly involved;
- factual event/performance record;
- chronology;
- prior feedback/warnings/improvement steps where relevant;
- policy versions and communication evidence;
- investigation/evidence provenance;
- protected/high-risk state where legally material;
- BL2 authority/approval state for the employer-side actor where material;
- BL7 monitoring/privacy state where evidence collection depends on it;
- relevant temporal anchors and current/historical employment authority.

Do not treat desired outcome as evidence of the underlying issue category.

## Core distinctions

### Performance problem ≠ misconduct

Failure to meet output, quality, capability, skill, or target expectations is not automatically disciplinary misconduct.

Misconduct generally requires its own factual/legal proposition concerning conduct, rule/duty, attribution, evidence, and applicable process.

Do not route:

```text
poor result
→ misconduct
```

without support.

### Misconduct ≠ immediate dismissal

Even where misconduct is supported, the employer action may depend on severity, applicable rules, procedure, prior state, evidence, timing, protected conditions, and current authority.

Do not jump from allegation to sanction.

### Desired outcome ≠ legal ground

`We need this person gone`, `we want to terminate quickly`, `we need an example`, or another managerial preference cannot create performance, misconduct, restructuring, or other legal ground.

Use:

```text
facts
→ issue classification
→ lawful pathway
→ available action
```

not:

```text
desired outcome
→ invent pathway
```

### Performance target ≠ legally usable standard by default

A KPI, target, score, manager opinion, ranking, or internal metric may be relevant evidence, but the legal significance depends on the employment terms, policies, communication, measurement quality, and applicable law.

Do not equate `below target` with a legally sufficient performance ground.

### Policy breach ≠ proven misconduct

First establish:

- what rule/duty applied;
- whether the worker knew/should legally be bound by it where material;
- what happened;
- evidence and attribution;
- whether the rule/process itself is legally usable.

A policy label is not the conclusion.

### Investigation evidence ≠ privacy compliance

Evidence may be useful for BL6 merits while its collection/processing raises BL7 privacy, monitoring, surveillance, data-retention, or sector-regulatory issues.

BL6 must not legalize the evidence-collection method merely because the evidence is relevant.

### Management measure ≠ final separation

Warning, coaching, improvement plan, reassignment, suspension, investigation, or discipline may be separate from termination/separation.

If the employer is considering organizational change, redundancy, negotiated exit, or final separation, route the relevant proposition to `restructuring-separation-protection.md` rather than forcing it through misconduct/performance.

## Decision procedure

1. **State the exact employer-action question.** Example: `What lawful pathway, if any, is supported by Employee E's documented performance issue?`
2. **Consume relationship and work state.** Do not reconstruct classification or material employment terms unless contradictory evidence requires review.
3. **Classify the issue category from facts.** Performance, conduct/misconduct, attendance, capability, instruction/process, mixed/uncertain, or not established.
4. **Bind the standard/duty.** Identify the employment term, policy, lawful instruction, performance criterion, or statutory duty relied upon.
5. **Build evidence chronology.** Separate allegation, contemporaneous evidence, worker response, manager interpretation, and later documentation.
6. **Check collection/process overlays.** Route monitoring/privacy evidence issues to BL7; authority/approval issues to BL2.
7. **Resolve current lawful pathway.** Identify available management steps/process under live authority; do not guess procedure from generic HR practice.
8. **Check protected/high-risk conditions.** Where material, identify conditions that can change or block the proposed action.
9. **Commit action-path state.** Supported, conditional, evidence-insufficient, process-required, blocked, disputed, or unresolved.
10. **Route separation if reached.** If the supported path may culminate in termination/separation, pass the committed issue/action state to `restructuring-separation-protection.md`; do not silently terminate inside this unit.

## Issue/action pattern

```text
P-BL6-ACT-01
relationship_dependency: P-BL6-REL-...
work_state_dependency: P-BL6-STATE-...
issue_type: PERFORMANCE / CONDUCT / ATTENDANCE / CAPABILITY / MIXED / UNRESOLVED
standard_or_duty: <source>
factual_status: SUPPORTED / DISPUTED / NOT_ESTABLISHED
process_state: <required / in-progress / completed / unresolved>
action_path: <coaching / warning / investigation / discipline / other>
status: SUPPORTED / CONDITIONAL / VERIFY / BLOCKED / UNRESOLVED
```

These are reasoning states, not statutory sanction categories.

## Evidence requirements

Potential evidence includes:

- committed employment terms/policies;
- performance records and objective work output;
- instructions and acknowledgements;
- attendance/absence records;
- incident reports;
- contemporaneous communications;
- investigation records and worker response;
- prior feedback/warnings/improvement steps;
- comparator/context evidence where legally material;
- monitoring/system evidence with separate BL7 legality state where needed;
- authority/approval evidence for the proposed employer action.

Do not manufacture documentation after the event and treat it as contemporaneous fact.

## Live authority triggers

Use Authority Resolver where current/historical law materially determines:

- lawful performance-management or disciplinary pathways;
- required procedure/process/evidence;
- sanction/action prerequisites;
- suspension/interim measure rules;
- protected/high-risk conditions affecting employer action;
- historical rules at the relevant conduct/action date.

Do not hardcode sanction lists, process steps, meeting deadlines, warning counts, notice periods, or article numbers.

## Cross-track handoffs

### From engagement/terms

Consume committed role/duty/policy/current-state propositions. If evidence materially contradicts those terms, signal the owning unit rather than rewriting them here.

### To separation/restructuring

Provide the committed performance/conduct/action-path proposition when a lawful separation question actually arises. The separation unit must not invent a misconduct/performance ground independently.

### To BL7

Route monitoring, surveillance, device, biometric, employee-data, investigation-data, or other public-law/privacy questions to BL7.

### To BL2

Consume corporate authority/approval where a manager/body's power to impose a material action is legally relevant.

### To BL4

When the issue becomes an active claim/dispute, BL6 keeps employment merits/pathway ownership; BL4 owns dispute posture, remedies, deadlines, and procedure.

### To BL5

Send only committed employment/action facts that create tax/contribution consequences; BL5 does not decide the employer-action pathway.

## Failure modes

- poor performance relabeled misconduct for convenience;
- misconduct allegation treated as proven;
- supported misconduct treated as automatic dismissal right;
- employer's desired termination outcome used to invent legal ground;
- KPI/manager rating treated as dispositive legal standard;
- policy label treated as proof of misconduct;
- surveillance evidence used without BL7 check where material;
- protected/high-risk conditions ignored;
- restructuring disguised as performance or misconduct;
- termination executed inside this unit without separation-path analysis;
- current HR procedure recalled from memory as current law.

## Escalation

Increase verification for dismissal-sensitive conduct, disputed investigations, retaliation/discrimination-type risk signals, protected leave/status, surveillance-derived evidence, senior/executive workers, repeated performance processes, or any employer action whose mistake could create irreversible employment consequences.