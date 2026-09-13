#!/usr/bin/env python3
"""Observable file-access/event walker for architecture runtime preflight.

The walker does not run an LLM. A local agent/runtime uses this CLI to read
frozen candidate files and append observable semantic events to a JSONL trace.
File reads come from `git show <candidate_sha>:<path>`, so the trace is bound to
exact candidate content rather than a mutable working tree.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def run_git(repo_root: Path, *args: str, text: bool = False) -> bytes | str:
    proc = subprocess.run(
        ["git", "-C", str(repo_root), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(proc.stderr.decode("utf-8", errors="replace").strip() or "git command failed")
    if text:
        return proc.stdout.decode("utf-8").strip()
    return proc.stdout


def meta_path(trace: Path) -> Path:
    return trace.with_suffix(trace.suffix + ".meta.json")


def load_meta(trace: Path) -> dict[str, Any]:
    mp = meta_path(trace)
    if not mp.exists():
        raise SystemExit(f"trace is not initialized: {trace}")
    return json.loads(mp.read_text(encoding="utf-8"))


def save_meta(trace: Path, meta: dict[str, Any]) -> None:
    mp = meta_path(trace)
    mp.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_event(trace: Path, meta: dict[str, Any], payload: dict[str, Any]) -> dict[str, Any]:
    meta["seq"] = int(meta.get("seq", 0)) + 1
    event = {
        "run_id": meta["run_id"],
        "seq": meta["seq"],
        "ts": utc_now(),
        "candidate_sha": meta["candidate_sha"],
        "fixture_id": meta["fixture_id"],
        **payload,
    }
    if not event.get("event"):
        raise SystemExit("event payload must contain non-empty 'event'")
    with trace.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
    save_meta(trace, meta)
    return event


def safe_repo_path(value: str) -> str:
    p = Path(value)
    if p.is_absolute() or ".." in p.parts:
        raise SystemExit("path must be repository-relative and may not contain '..'")
    return p.as_posix()


def cmd_init(args: argparse.Namespace) -> None:
    repo = Path(args.repo_root).resolve()
    trace = Path(args.trace).resolve()
    trace.parent.mkdir(parents=True, exist_ok=True)
    if trace.exists() and not args.force:
        raise SystemExit(f"trace already exists: {trace}; use --force to replace")

    run_git(repo, "cat-file", "-e", f"{args.candidate_sha}^{{commit}}")
    trace.write_text("", encoding="utf-8")
    mp = meta_path(trace)
    if mp.exists():
        mp.unlink()

    meta = {
        "run_id": args.run_id,
        "fixture_id": args.fixture,
        "candidate_sha": args.candidate_sha,
        "repo_root": str(repo),
        "seq": 0,
    }
    save_meta(trace, meta)
    event = append_event(
        trace,
        meta,
        {
            "event": "RUN_START",
            "runner": args.runner,
            "working_head": run_git(repo, "rev-parse", "HEAD", text=True),
        },
    )
    print(json.dumps(event, ensure_ascii=False))


def cmd_read(args: argparse.Namespace) -> None:
    trace = Path(args.trace).resolve()
    meta = load_meta(trace)
    repo = Path(meta["repo_root"])
    rel = safe_repo_path(args.path)
    content = run_git(repo, "show", f"{meta['candidate_sha']}:{rel}")
    assert isinstance(content, bytes)
    digest = hashlib.sha256(content).hexdigest()
    append_event(
        trace,
        meta,
        {
            "event": "READ",
            "path": rel,
            "content_sha256": digest,
            "bytes": len(content),
        },
    )
    sys.stdout.buffer.write(content)


def cmd_emit(args: argparse.Namespace) -> None:
    trace = Path(args.trace).resolve()
    meta = load_meta(trace)
    try:
        payload = json.loads(args.json)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid --json payload: {exc}") from exc
    if not isinstance(payload, dict):
        raise SystemExit("--json payload must be an object")
    for reserved in ("run_id", "seq", "ts", "candidate_sha", "fixture_id"):
        if reserved in payload:
            raise SystemExit(f"reserved field may not be supplied: {reserved}")
    event = append_event(trace, meta, payload)
    print(json.dumps(event, ensure_ascii=False))


def cmd_status(args: argparse.Namespace) -> None:
    trace = Path(args.trace).resolve()
    meta = load_meta(trace)
    print(json.dumps(meta, indent=2, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="initialize a frozen candidate trace")
    p.add_argument("--repo-root", default=".")
    p.add_argument("--fixture", required=True)
    p.add_argument("--candidate-sha", required=True)
    p.add_argument("--trace", required=True)
    p.add_argument("--run-id", required=True)
    p.add_argument("--runner", default="local-agent")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("read", help="read one candidate file and log the actual access")
    p.add_argument("--trace", required=True)
    p.add_argument("--path", required=True)
    p.set_defaults(func=cmd_read)

    p = sub.add_parser("emit", help="append one semantic runtime event")
    p.add_argument("--trace", required=True)
    p.add_argument("--json", required=True)
    p.set_defaults(func=cmd_emit)

    p = sub.add_parser("status", help="show trace metadata")
    p.add_argument("--trace", required=True)
    p.set_defaults(func=cmd_status)

    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
