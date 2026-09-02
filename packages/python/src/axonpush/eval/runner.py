"""Runs each dataset example through a local evaluator command.

The protocol matches the TypeScript runner exactly, so the same evaluator
script works from either CLI: one JSON object in on stdin, one JSON object out
on stdout.

    in   {"type": "axonpush.evaluation.input", "experimentId": "...",
          "item": {"id": "...", "input": ...}, "configuration": {...}}
    out  {"output": <any>, "traceId"?: "...", "totalTokens"?: 12,
          "costUsd"?: 0.01, "error"?: "..."}

The lifecycle matches too: start the experiment, wait for it to be running,
submit each result as it lands, and cancel the experiment on interrupt rather
than leaving it running forever.
"""

from __future__ import annotations

import json
import subprocess
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any

from .git import capture_git_lineage
from .reports import GitLineage, ItemResult, RunResult

if TYPE_CHECKING:
    from .api import EvaluationApi

DEFAULT_CONCURRENCY = 4
DEFAULT_TIMEOUT_SECONDS = 30.0
DEFAULT_STARTUP_TIMEOUT_SECONDS = 30.0
STARTUP_POLL_INTERVAL_SECONDS = 0.25
TERMINATE_GRACE_SECONDS = 1.0

_NO_OUTPUT = "Evaluator command did not emit a JSON object with an output field"
_TERMINAL_STATUSES = ("failed", "cancelled", "completed")


class CancelledError(Exception):
    """The run was interrupted; the local decision is authoritative."""


@dataclass
class LocalRunnerOptions:
    dataset_id: str
    dataset_revision: str
    experiment_id: str
    command: str
    concurrency: int = DEFAULT_CONCURRENCY
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS
    startup_timeout_seconds: float = DEFAULT_STARTUP_TIMEOUT_SECONDS
    configuration: dict[str, Any] | None = field(default=None)


def _as_text(value: object) -> str | None:
    return str(value) if isinstance(value, str) and value else None


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _read_output(stdout: str) -> dict[str, Any]:
    """The last JSON line carrying an `output` field wins; diagnostics may precede it."""
    for line in reversed([line.strip() for line in stdout.splitlines() if line.strip()]):
        try:
            parsed = json.loads(line)
        except ValueError:
            continue
        if isinstance(parsed, dict) and "output" in parsed:
            return parsed
    raise ValueError(_NO_OUTPUT)


def run_item(
    command: str,
    experiment_id: str,
    item: dict[str, Any],
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
    configuration: dict[str, Any] | None = None,
    cancel: threading.Event | None = None,
) -> ItemResult:
    """Run one example. Any failure becomes a failed result, never an exception."""
    item_id = str(item.get("itemId") or item.get("id") or "")
    payload = json.dumps(
        {
            "type": "axonpush.evaluation.input",
            "experimentId": experiment_id,
            "item": {"id": item_id, "input": item.get("input")},
            **({"configuration": configuration} if configuration else {}),
        }
    )
    if cancel is not None and cancel.is_set():
        return ItemResult(item_id=item_id, status="cancelled", error="Evaluation was cancelled")

    started = time.monotonic()
    # The command is the customer's own evaluator, run on the customer's host.
    process = subprocess.Popen(  # noqa: S602
        command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    watchdog = _cancel_watchdog(process, cancel)
    try:
        stdout, stderr = process.communicate(payload, timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        _terminate(process)
        return ItemResult(
            item_id=item_id,
            status="failed",
            error=f"Evaluator timed out after {timeout_seconds:g}s",
            latency_ms=round((time.monotonic() - started) * 1000, 3),
        )
    finally:
        if watchdog is not None:
            watchdog.set()

    latency_ms = round((time.monotonic() - started) * 1000, 3)
    if cancel is not None and cancel.is_set():
        return ItemResult(
            item_id=item_id,
            status="cancelled",
            error="Evaluation was cancelled",
            latency_ms=latency_ms,
        )
    if process.returncode != 0:
        return ItemResult(
            item_id=item_id,
            status="failed",
            error=(stderr or "").strip() or f"Evaluator exited with code {process.returncode}",
            latency_ms=latency_ms,
        )

    try:
        parsed = _read_output(stdout)
    except ValueError as error:
        return ItemResult(item_id=item_id, status="failed", error=str(error), latency_ms=latency_ms)

    reported = parsed.get("error")
    return ItemResult(
        item_id=item_id,
        status="failed" if reported else "passed",
        output=parsed.get("output"),
        error=str(reported) if reported else None,
        latency_ms=latency_ms,
        total_tokens=parsed.get("totalTokens"),
        cost_usd=parsed.get("costUsd"),
        trace_id=parsed.get("traceId"),
    )


def _terminate(process: subprocess.Popen[str]) -> None:
    process.terminate()
    try:
        process.wait(timeout=TERMINATE_GRACE_SECONDS)
    except subprocess.TimeoutExpired:
        process.kill()


def _cancel_watchdog(
    process: subprocess.Popen[str], cancel: threading.Event | None
) -> threading.Event | None:
    """Kill the evaluator when the run is cancelled, rather than waiting it out."""
    if cancel is None:
        return None
    done = threading.Event()

    def watch() -> None:
        while not done.wait(0.1):
            if cancel.is_set():
                _terminate(process)
                return

    threading.Thread(target=watch, daemon=True).start()
    return done


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


def _wait_for_running(
    api: EvaluationApi,
    experiment_id: str,
    timeout_seconds: float,
    cancel: threading.Event,
) -> None:
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() <= deadline:
        if cancel.is_set():
            raise CancelledError
        status = api.get_experiment_status(experiment_id)
        if status == "running":
            return
        if status in _TERMINAL_STATUSES:
            raise RuntimeError(
                f"Experiment {experiment_id} entered {status} before local execution started"
            )
        if cancel.wait(STARTUP_POLL_INTERVAL_SECONDS):
            raise CancelledError
    raise RuntimeError(
        f"Experiment {experiment_id} did not reach running within {timeout_seconds:g}s"
    )


def run_local_evaluation(
    api: EvaluationApi,
    options: LocalRunnerOptions,
    cancel: threading.Event | None = None,
) -> RunResult:
    """Execute an immutable dataset revision locally and submit each result as it lands.

    The evaluator runs on the caller's host; no customer code is uploaded.
    """
    if not options.dataset_id or not options.experiment_id or not options.command.strip():
        raise ValueError("dataset_id, experiment_id and command are required")

    cancel = cancel or threading.Event()
    started_at = _now()
    captured = capture_git_lineage()
    lineage = GitLineage(
        git_commit=_as_text(captured.get("gitCommit")),
        git_branch=_as_text(captured.get("gitBranch")),
        git_dirty=bool(captured["gitDirty"]) if "gitDirty" in captured else None,
    )
    results: list[ItemResult] = []
    lock = threading.Lock()
    submission_error: list[BaseException] = []

    items: list[dict[str, Any]] = []
    try:
        api.start_experiment(options.experiment_id)
        _wait_for_running(api, options.experiment_id, options.startup_timeout_seconds, cancel)
        items = api.fetch_dataset_revision_items(options.dataset_id, options.dataset_revision)
    except CancelledError:
        cancel.set()

    def evaluate(item: dict[str, Any]) -> None:
        if cancel.is_set():
            return
        result = run_item(
            options.command,
            options.experiment_id,
            item,
            options.timeout_seconds,
            options.configuration,
            cancel,
        )
        with lock:
            results.append(result)
        if result.status == "cancelled":
            cancel.set()
            return
        try:
            api.submit_results(options.experiment_id, [result])
        except BaseException as error:  # noqa: BLE001 - recorded and re-raised below
            if not cancel.is_set():
                submission_error.append(error)
            cancel.set()

    if items:
        workers = max(1, min(options.concurrency, len(items)))
        with ThreadPoolExecutor(max_workers=workers) as pool:
            list(pool.map(evaluate, items))

    cancelled = cancel.is_set() and not submission_error
    if cancelled:
        try:
            api.cancel_experiment(options.experiment_id)
        except Exception:  # noqa: BLE001 - local cancellation stays authoritative
            pass
    if submission_error:
        raise submission_error[0]

    return RunResult(
        experiment_id=options.experiment_id,
        dataset_id=options.dataset_id,
        dataset_revision=options.dataset_revision,
        started_at=started_at,
        completed_at=_now(),
        cancelled=cancelled,
        lineage=lineage,
        results=sorted(results, key=lambda item: item.item_id),
    )
