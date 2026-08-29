"""Runs each dataset example through a local evaluator command.

The protocol matches the TypeScript runner exactly, so the same evaluator
script works from either CLI: one JSON object in on stdin, one JSON object out
on stdout.

    in   {"type": "axonpush.evaluation.input", "experimentId": "...",
          "item": {"id": "...", "input": ...}}
    out  {"output": <any>, "traceId"?: "...", "totalTokens"?: 12,
          "costUsd"?: 0.01, "error"?: "..."}
"""

from __future__ import annotations

import json
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from .reports import ItemResult

DEFAULT_CONCURRENCY = 4
DEFAULT_TIMEOUT_SECONDS = 30.0

_NO_OUTPUT = "Evaluator command did not emit a JSON object with an output field"


def run_item(
    command: str,
    experiment_id: str,
    item: dict[str, Any],
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
) -> ItemResult:
    """Run one example. Any failure becomes a failed result, never an exception."""
    item_id = str(item.get("itemId") or item.get("id") or "")
    payload = json.dumps(
        {
            "type": "axonpush.evaluation.input",
            "experimentId": experiment_id,
            "item": {"id": item_id, "input": item.get("input")},
        }
    )
    started = time.monotonic()
    try:
        completed = subprocess.run(  # noqa: S602 - the command is the user's own evaluator
            command,
            shell=True,
            input=payload,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return ItemResult(
            item_id=item_id,
            status="failed",
            error=f"Evaluator command timed out after {timeout_seconds:g}s",
            latency_ms=round((time.monotonic() - started) * 1000, 3),
        )

    latency_ms = round((time.monotonic() - started) * 1000, 3)
    if completed.returncode != 0:
        return ItemResult(
            item_id=item_id,
            status="failed",
            error=(completed.stderr or "").strip()
            or f"Evaluator command exited with code {completed.returncode}",
            latency_ms=latency_ms,
        )

    try:
        parsed = json.loads(completed.stdout.strip().splitlines()[-1])
    except (ValueError, IndexError):
        return ItemResult(item_id=item_id, status="failed", error=_NO_OUTPUT, latency_ms=latency_ms)

    if not isinstance(parsed, dict) or "output" not in parsed:
        return ItemResult(item_id=item_id, status="failed", error=_NO_OUTPUT, latency_ms=latency_ms)

    error = parsed.get("error")
    return ItemResult(
        item_id=item_id,
        status="failed" if error else "passed",
        output=parsed.get("output"),
        error=str(error) if error else None,
        latency_ms=latency_ms,
        total_tokens=parsed.get("totalTokens"),
        cost_usd=parsed.get("costUsd"),
        trace_id=parsed.get("traceId"),
    )


def run_items(
    command: str,
    experiment_id: str,
    items: list[dict[str, Any]],
    concurrency: int = DEFAULT_CONCURRENCY,
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
) -> list[ItemResult]:
    """Run every example, preserving dataset order in the results."""
    if not items:
        return []
    workers = max(1, min(concurrency, len(items)))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(
            pool.map(
                lambda item: run_item(command, experiment_id, item, timeout_seconds),
                items,
            )
        )
