# BL3 — Document Stack / Terms / Interpretation

## Owns

Reconstructing the transaction's governing document stack, identifying what terms are part of the transaction, and resolving the content/relationship of contractual terms within BL3 ownership.

This unit owns **what the agreement says and which transaction documents/terms govern**, including the contract-law formation/incorporation/validity/effect of a dispute-resolution clause as a contractual term.

It does not own signatory authority, statutory tax liability, regulatory permission, cross-border governing-law/treaty applicability, or dispute invocation/procedure.

## Does not own

- entity/signing authority or corporate approval — BL2;
- breach/remedy/dispute invocation/procedure/deadlines — BL4;
- statutory tax consequences — BL5;
- public-law permission/mandatory compliance — BL7;
- governing-law/treaty/CISG/international-enforcement overlay — BL8.

## Activate when

Use when the decision depends on:

- which document/version governs;
- whether a quotation, PO, order form, annex, schedule, policy, standard term, email, platform term, or later writing is incorporated;
- precedence among several documents;
- negotiated versus standard terms;
- interpretation of a material clause;
- whether a dispute-resolution clause exists, what it says, or whether it was contractually formed/incorporated/effective;
- whether different language/version copies conflict;
- whether external references/linked terms were actually part of the transaction.

Skip or compress when the relevant term is undisputed and the document stack cannot change the requested action.

## Required state

Where material, capture:

- committed/conditioned formation/effectiveness proposition from shared state when formation matters;
- full candidate document list and versions;
- chronology;
- signatures/acceptance/incorporation evidence;
- precedence clauses;
- negotiated changes/redlines;
- annexes/schedules/specifications;
- standard/platform terms and version/date;
- referenced external documents;
- relevant communications/conduct;
- language versions;
- temporal anchor and applicable contract regime where material.

Do not load `formation-transaction-state.md` merely because this unit consumes a formation proposition. Load it only when formation/effectiveness is unresolved, disputed, stale, contradictory, or material to reopen.

## Core distinctions

### Signed document ≠ complete contract position

A main agreement may be only one layer in the transaction.

Potential layers include:

- master agreement;
- order form / PO / quotation;
- annex / schedule / statement of work;
- product/service specifications;
- accepted standard terms;
- incorporated policy;
- later amendment;
- settlement/change agreement;
- communications or conduct that may affect interpretation/state.

Do not assume all layers apply; resolve incorporation and precedence.

### Document existence ≠ incorporation

A term available on a website, in a standard PDF, or attached to an email is not automatically part of the agreement.

Ask whether it was incorporated under the applicable regime and transaction facts.

### Standard term ≠ negotiated term

Preserve whether a clause was individually negotiated, standard-form, externally referenced, or later modified when that distinction can change interpretation/effect.

### Precedence clause ≠ universal answer

A precedence clause may resolve some conflicts but not every inconsistency, incorporation issue, later amendment, mandatory-law constraint, or ambiguity.

### Term content ≠ statutory consequence

BL3 determines what parties agreed. BL5/BL7/BL8 determine statutory consequences within their ownership.

Examples:

- `buyer bears all taxes` ≠ statutory taxpayer resolved;
- `seller is fully compliant` ≠ regulatory compliance proved;
- `DDP`/trade term ≠ statutory customs responsibility automatically transferred;
- `Vietnam law` clause ≠ BL8 governing-law proposition resolved in every cross-border case.

### Dispute-resolution clause: contractual effect ≠ procedure/enforcement

BL3 owns:

- whether a dispute-resolution clause exists;
- the clause text/content;
- its document location/version;
- whether the clause was contractually formed/incorporated;
- its contract-law validity/effect as a contractual term;
- contractual preconditions/steps expressed in the clause.

BL4 owns:

- invocation of the resolved clause/forum;
- dispute posture;
- procedural consequences;
- deadlines and remedy procedure.

BL8 owns cross-border governing-law/treaty/international-enforcement overlay.

Do not infer:

```text
arbitration clause exists
→ arbitration procedure available / properly invoked
```

or:

```text
cross-border dispute
→ BL3 decides treaty/enforcement consequence
```

## Decision procedure

1. **State the term proposition.** Example: `What payment deadline did the parties agree?` or `Was this arbitration clause incorporated/effective as a contractual term?`
2. **Inventory candidate documents.** Do not start interpretation from the first PDF found.
3. **Bind each document to chronology/version.** Identify draft, executed, superseded, later, referenced, or uncertain state.
4. **Resolve incorporation.** Determine which documents/standard terms became part of the transaction under the applicable regime/facts.
5. **Resolve precedence/conflicts.** Apply explicit precedence or later-agreement rules only within their supported scope.
6. **Separate negotiated/standard/external terms where material.** Preserve special interpretation/control issues for live authority if needed.
7. **Interpret the material term.** Use text, transaction structure, defined terms, related clauses, annexes, chronology, and legally relevant context without inventing business intent.
8. **For dispute clauses, resolve only BL3 contractual propositions.** Hand invocation/procedure/deadlines to BL4 and cross-border overlay to BL8.
9. **Commit the term proposition.** Supported, conditional, disputed, ambiguous, unresolved, or superseded.
10. **Hand obligations onward only when needed.** Load `obligations-conditions-performance.md` only if obligation/due/performance state is material; otherwise leave the committed term proposition in shared state for later consumption.

## Document-stack pattern

A useful representation is:

```text
D-01 Master agreement       status: EXECUTED
D-02 Order form             status: INCORPORATED
D-03 Website terms v3       status: INCORPORATION_DISPUTED
D-04 Amendment 1            status: LATER_EFFECTIVE
D-05 Email draft            status: NON_GOVERNING_DRAFT
```

Then create term propositions with source links:

```text
P-BL3-TERM-01
statement: payment due 30 days after accepted invoice
source: D-01 §X + D-04 §Y
status: SUPPORTED
```

Do not treat these labels as statutory categories; they are reasoning state.

## Evidence requirements

Potential evidence includes:

- executed agreements;
- annexes/schedules/SOWs/order forms;
- redlines/version history;
- emails/chats transmitting or accepting terms;
- platform clickwrap/acceptance logs;
- standard terms and archived versions;
- translated/bilingual copies;
- later amendments/waivers/settlements;
- business records showing which specification/version parties performed against.

Do not infer acceptance/integration merely because a document exists in one party's files.

## Live authority triggers

Resolve live authority where the result depends on:

- incorporation/control of standard terms;
- electronic records/acceptance;
- required form for particular contractual terms;
- contract-law validity/effect of a dispute-resolution clause;
- interpretation rules that materially change outcome;
- special statutory treatment of standard terms/consumer-facing terms;
- historical contract rules at the relevant date.

Do not hardcode article numbers, mandatory clauses, or category-specific formalities as stable knowledge.

## Cross-track handoffs

### From BL2

Consume authority/approval propositions where they affect whether a document binds the entity. Do not reconstruct corporate authority from signatures or titles.

### To BL4

Provide resolved obligation/term and dispute-clause contractual propositions. BL4 decides breach/remedy/invocation/procedure under the appropriate regime.

### To BL5

Provide the commercial tax/cost allocation term only. BL5 decides statutory tax treatment.

### To BL7

If a term purports to authorize regulated conduct, collect consent, allocate compliance, or make consumer/data/product claims, hand the public-law proposition to BL7.

### To BL8

Provide exact governing-law/dispute/trade/payment clause content. BL8 decides cross-border conflict/treaty/FX/trade/international-enforcement overlay where material.

## Failure modes

- main PDF treated as complete contract;
- every attachment/website term treated as incorporated;
- precedence clause used to bypass incorporation or later-change analysis;
- formation unit loaded despite reliable committed formation state;
- current website terms projected backward to historical contract;
- standard terms and negotiated terms treated identically when legally material;
- tax/compliance/customs allocation clause treated as statutory conclusion;
- dispute-clause contractual validity/effect collapsed into invocation/procedure/enforcement conclusion;
- ambiguous term resolved by invented commercial intent;
- BL3 interpreting a document without resolving which version governs.
