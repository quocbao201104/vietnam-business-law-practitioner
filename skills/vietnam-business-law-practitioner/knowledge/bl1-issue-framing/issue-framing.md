# BL1 — Issue Framing

## Owns

Turning a business situation into a bounded map of material legal questions, candidate actions, missing facts, and proposition owners.

This unit owns the **question map**. It does not decide the substantive BL2–BL8 answers.

## Does not own

- corporate authority or ownership conclusions — BL2;
- transaction formation/content — BL3;
- breach/remedy conclusions — BL4;
- tax consequences — BL5;
- employment classification — BL6;
- regulatory permission/compliance — BL7;
- governing-law/treaty/foreign-investment/trade conclusions — BL8.

## Activate when

Use when the user presents a business situation rather than a narrowly framed legal proposition, when several legal domains may interact, or when the requested action is unclear.

Skip or compress when the user already asks a narrow, correctly scoped proposition whose owner is clear.

## Required state

Capture only facts capable of changing route, owner, classification, proposition result, authority version, available options, procedure/evidence/deadline, or action readiness.

At minimum, identify where material:

- business objective;
- candidate action(s);
- actors and asserted roles;
- relationship between actors;
- object/activity/transaction;
- geography/foreign element;
- event sequence and temporal anchors;
- available documents/evidence;
- disputed or unknown facts;
- desired outcome and timing.

## Core distinctions

### User story ≠ legal issue map

Users normally describe events, labels, goals, or frustrations. Convert those into legal propositions before searching for law.

### Label ≠ classification

Labels such as `freelancer`, `agent`, `partner`, `deposit`, `force majeure`, `consumer`, or `investment` are evidence about how the situation is described, not final legal classifications.

### Fact ≠ evidence source

`The invoice was paid` is a factual proposition. A receipt, bank record, user statement, or counterparty statement is evidence concerning that proposition.

### Business objective ≠ legal pathway

`I want to remove this employee`, `I want out of this contract`, or `I want to pay less tax` are objectives. They do not establish a lawful pathway, remedy, or classification.

### One matter ≠ one legal question

A single business action may require several owned propositions. Do not collapse them into one global yes/no issue.

## Decision procedure

1. **State the business objective.** What is the user actually trying to do: sign, launch, hire, terminate, collect, defend, restructure, invest, import, pay, exit, or preserve an option?
2. **Split candidate actions.** Separate actions whose legal prerequisites may differ. Example: `sign agreement` and `start regulated activity` are different actions.
3. **Reconstruct actors and relationships.** Preserve asserted roles without promoting them into legal status.
4. **Build the material timeline.** Record only dates/events capable of changing legal regime, authority version, procedure, or readiness.
5. **Extract factual propositions.** Separate established, disputed, and unknown propositions from source/evidence provenance.
6. **Convert the story into legal questions.** Phrase questions in decision terms, not statute names.
7. **Assign candidate owners.** Use `../INDEX.md` for detailed routing.
8. **Mark route uncertainty.** Use `ROUTE_CONFIRMED`, `ROUTE_PLAUSIBLE`, `ROUTE_UNRESOLVED`, or `ROUTE_REJECTED`.
9. **Identify missing information by materiality.** Ask only when the missing fact can change the legal result or requested action readiness and cannot safely be handled conditionally.
10. **Hand off without solving downstream propositions.** Preserve the issue map, facts, temporal anchors, evidence, and unresolved conditions.

## Materiality gate

A fact, issue, route, or proposition is material when changing it can change at least one of:

- route or accountable owner;
- legal classification;
- proposition result/status;
- proposition dependency;
- authority version or lifecycle relevant to the proposition;
- available option set;
- required procedure/evidence/deadline;
- action readiness.

If none can change, do not expand the case merely because the fact is legally interesting.

## Question design patterns

Prefer questions such as:

- `Who can bind the company for this transaction?` → BL2
- `What agreement/obligation actually exists?` → BL3
- `Does this deviation support termination, damages, or another remedy?` → BL4
- `Who bears the statutory tax/withholding consequence?` → BL5
- `Is this relationship legally employment or independent service?` → BL6
- `May this activity/product/conduct lawfully occur in the market?` → BL7
- `Does a foreign element change governing law, market access, payment, or trade treatment?` → BL8

Avoid framing like `Which article applies?` before the underlying legal proposition is known.

## Live authority triggers

Issue framing itself usually does not require deep live-law research. Call authority resolution at BL1 only when a meta-level proposition materially affects routing, for example:

- whether a regime exists or was replaced for the relevant period;
- whether an instrument is effective or only future-effective;
- whether a temporal transition may require historical routing;
- whether a mandatory special regime is plausibly triggered and must be handed to its owner.

Finding a source does not make BL1 the owner of the substantive proposition.

## Evidence requirements

Preserve:

- which facts come from user assertion;
- which facts are represented in documents;
- which facts are independently verified;
- which propositions are disputed or unknown;
- which missing facts are blocking versus safely conditional.

Do not convert document language into external truth.

## Cross-track handoffs

A BL1 handoff should contain:

- objective and candidate action(s);
- material facts/evidence status;
- temporal anchors;
- issue/proposition question;
- candidate owner;
- route state;
- unresolved conditions;
- reason the owner was activated.

Do not attach an unearned substantive conclusion to the handoff.

## Failure modes

- keyword-to-track or keyword-to-statute routing;
- treating the user's legal label as resolved classification;
- asking a universal intake questionnaire regardless of materiality;
- collapsing several actions into one readiness state;
- routing by nouns instead of decision questions;
- searching law before the legal proposition is framed;
- treating a document statement as established fact;
- letting BL1 answer a proposition owned by BL2–BL8;
- refusing to late-route when downstream facts change the issue map.

## Escalation

Escalate framing depth when the situation contains major irreversible actions, urgent deadlines, regulator/enforcement activity, material ownership changes, serious dispute exposure, or facts that plausibly create criminal exposure.

Escalation changes the verification burden; it does not replace issue framing.