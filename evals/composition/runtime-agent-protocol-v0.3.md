# Cold-Start Runtime Proof Protocol v0.3

**Frozen candidate:** `75135e67223c488bdecb9b2f753186bd2bab4601`

**Oracle:** `rf-oracles-v0.3.json`

The goal is to prove observable load/skip/order and state-transition behavior for RF-01 through RF-10. Final prose is not sufficient evidence.

## 1. Fresh runtime requirement

Run each fixture in a fresh agent session/process.

Prefer an empty temporary working directory rather than the repository root so the agent does not receive the whole repo through IDE/workspace indexing or preloaded context.

The repository may remain available at a separate path only so the walker/checker can execute Git commands against it.

Do not provide the agent with prior fixture traces or the expected final answer.

## 2. Candidate binding

The semantic/runtime candidate is exactly:

```text
75135e67223c488bdecb9b2f753186bd2bab4601
```

Do not evaluate `main` implicitly. The walker serves file content with:

```text
git show <candidate_sha>:<path>
```

and records a SHA-256 digest for every observed `READ`.

## 3. File-access rule

During the fixture run, the agent must not use direct repository file reads (`cat`, `Get-Content`, IDE file APIs, ordinary filesystem open) for skill/knowledge/reference/schema content.

It must request candidate content through:

```text
python <repo>/scripts/runtime_walker.py read --trace <trace.jsonl> --path <repo-relative-path>
```

This is the path-proof mechanism.

The checker can prove walker-mediated reads; it cannot prove the absence of hidden/preloaded context. Therefore use a fresh process + empty workdir and disable workspace preload/indexing where the chosen runtime permits it.

## 4. Trace initialization

Example (PowerShell; adjust paths):

```powershell
$Repo = "C:\path\to\vietnam-business-law-practitioner"
$RunDir = "$env:TEMP\vblp-rf01"
New-Item -ItemType Directory -Force $RunDir | Out-Null
$Trace = "$RunDir\trace.jsonl"

python "$Repo\scripts\runtime_walker.py" init `
  --repo-root $Repo `
  --fixture RF-01 `
  --candidate-sha 75135e67223c488bdecb9b2f753186bd2bab4601 `
  --trace $Trace `
  --run-id RF01-COLD-001 `
  --runner codex-local `
  --force
```

Use a different fresh run directory/run ID for every fixture.

## 5. Runtime event rule

The agent/runtime should emit externally observable semantic events through:

```text
python <repo>/scripts/runtime_walker.py emit --trace <trace.jsonl> --json '<event-object>'
```

Examples:

```json
{"event":"ROUTE_HYPOTHESIS","track":"BL3","status":"ROUTE_CONFIRMED"}
{"event":"ACTIVATE","track":"BL3"}
{"event":"LATE_ROUTE_SIGNAL","track":"BL7","reason":"consumer/data facts became material"}
{"event":"AUTHORITY_CALL","owner":"BL6","proposition_id":"P-BL6-01","temporal_anchor":"ACTION_DATE"}
{"event":"SPECIALIST_CALL","owner":"BL8","specialist":"preferential-origin"}
{"event":"INVALIDATE","proposition_id":"P-BL5-TAX","basis":"DEPENDS_ON"}
{"event":"ACTION_READINESS","action_id":"TERMINATE","state":"VERIFY_BEFORE_ACTION"}
{"event":"RUN_CONVERGED"}
```

Do not emit chain-of-thought. Emit only architecture/state events necessary to prove the contract.

## 6. Materiality rule

When a route/load/skip is debatable, the agent should emit:

```json
{
  "event":"MATERIALITY_DECISION",
  "subject":"...",
  "material":true,
  "reason_category":"ACTION_READINESS"
}
```

Allowed reason categories correspond to the canonical materiality gate:

- `ROUTE_OWNER`
- `CLASSIFICATION`
- `PROPOSITION_RESULT`
- `DEPENDENCY`
- `AUTHORITY_VERSION`
- `OPTION_SET`
- `PROCEDURE_EVIDENCE_DEADLINE`
- `ACTION_READINESS`

## 7. Convergence rule

The agent may emit `RUN_CONVERGED` only after the stop condition in `schemas/runtime-composition.md` is satisfied for the requested action(s).

Convergence does not mean `READY`; a run may converge to `VERIFY_BEFORE_ACTION`, `LEGAL_REVIEW_REQUIRED`, or `DO_NOT_PROCEED`.

## 8. Checker

After each fixture:

```powershell
python "$Repo\scripts\check_runtime_trace.py" `
  --repo-root $Repo `
  --oracle "$Repo\evals\composition\rf-oracles-v0.3.json" `
  --trace $Trace `
  --fixture RF-01
```

Exit code `0` means the observable trace satisfies the frozen oracle. Exit code `1` means FAIL.

## 9. What counts as evidence

Strong evidence:

- candidate SHA bound in every event;
- candidate file content served by `git show`;
- observed file `READ` order + SHA-256;
- forbidden file reads absent;
- route/late-route/owner events in required order;
- Authority Resolver call occurs before owner conclusion where required;
- exact invalidation targets;
- owner-bound specialist return path;
- per-action readiness;
- `RUN_CONVERGED` after closure.

Not sufficient by itself:

- final answer looks correct;
- agent says it skipped a file without observable access isolation;
- self-reported prose describing what it "would" have loaded;
- running all fixtures in one context after the architecture is already loaded.

## 10. Freeze gate

Do RF-01 through RF-10 first.

Phase 4 does not freeze on a simple pass count alone. Review traces for evidence leakage, unexpected reads, missing material routes, and checker/oracle weaknesses.

If all ten pass in fresh runs, perform held-out/perturbed CT cases before the independent freeze review.

Repair only concrete observed failures. Do not expand legal theory or add specialist modules during this gate.