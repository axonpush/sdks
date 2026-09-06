"""Artifacts a CI run leaves behind: JSON, JUnit XML and a GitHub summary.

Byte-comparable with the TypeScript and .NET CLIs' artifacts.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from xml.sax.saxutils import escape

TESTSUITE_NAME = "axonpush.evaluation"


@dataclass
class ItemResult:
    """One dataset example, as the local evaluator answered it."""

    item_id: str
    status: str
    output: object | None = None
    error: str | None = None
    latency_ms: float | None = None
    total_tokens: int | None = None
    cost_usd: float | None = None
    trace_id: str | None = None


@dataclass
class GateVerdict:
    passed: bool
    reasons: list[str] = field(default_factory=list)
    metrics: dict[str, object] = field(default_factory=dict)
    gate_run_id: str | None = None


@dataclass
class GitLineage:
    git_commit: str | None = None
    git_branch: str | None = None
    git_dirty: bool | None = None


@dataclass
class RunResult:
    experiment_id: str
    dataset_id: str
    dataset_revision: str
    started_at: str = ""
    completed_at: str = ""
    results: list[ItemResult] = field(default_factory=list)
    gate: GateVerdict | None = None
    cancelled: bool = False
    lineage: GitLineage = field(default_factory=GitLineage)


def _camel(name: str) -> str:
    head, *rest = name.split("_")
    return head + "".join(part.title() for part in rest)


def _camel_keys(value: object) -> object:
    if isinstance(value, dict):
        return {_camel(str(key)): _camel_keys(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_camel_keys(item) for item in value]
    return value


def to_json_report(run: RunResult) -> str:
    payload = {
        "experimentId": run.experiment_id,
        "datasetId": run.dataset_id,
        "datasetRevision": run.dataset_revision,
        "startedAt": run.started_at,
        "completedAt": run.completed_at,
        "cancelled": run.cancelled,
        "lineage": _camel_keys(
            {key: value for key, value in asdict(run.lineage).items() if value is not None}
        ),
        "results": [_camel_keys(asdict(item)) for item in run.results],
        "gate": _camel_keys(asdict(run.gate)) if run.gate else None,
    }
    return json.dumps(payload, indent=2, default=str) + "\n"


def _xml(value: str) -> str:
    return escape(value, {'"': "&quot;", "'": "&apos;"})


def to_junit_xml(run: RunResult) -> str:
    blocked = bool(run.gate and not run.gate.passed)
    failures = sum(1 for item in run.results if item.status != "passed") + int(blocked)
    skipped = sum(1 for item in run.results if item.status == "cancelled")
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<testsuite name="{TESTSUITE_NAME}" tests="{len(run.results) + int(blocked)}" '
        f'failures="{failures}" skipped="{skipped}" timestamp="{_xml(run.started_at)}">',
    ]
    for item in run.results:
        attrs = (
            f'classname="{TESTSUITE_NAME}" name="{_xml(item.item_id)}" '
            f'time="{(item.latency_ms or 0) / 1000:.3f}"'
        )
        if item.status == "passed":
            lines.append(f"  <testcase {attrs}/>")
            continue
        kind = "skipped" if item.status == "cancelled" else "failure"
        lines.append(
            f'  <testcase {attrs}><{kind} message="{_xml(item.error or item.status)}"/></testcase>'
        )
    if run.gate and not run.gate.passed:
        lines.append(
            f'  <testcase classname="{TESTSUITE_NAME}" name="release gate" time="0.000">'
            f'<failure message="gate failed">{_xml("; ".join(run.gate.reasons))}</failure>'
            "</testcase>"
        )
    lines.append("</testsuite>")
    return "\n".join(lines) + "\n"


def _status_line(run: RunResult, failed: int) -> str:
    if run.cancelled:
        return "Cancelled"
    if run.gate:
        return "Passed" if run.gate.passed else "Failed"
    return "Completed with failures" if failed else "Passed"


def to_github_summary(run: RunResult) -> str:
    passed = sum(1 for item in run.results if item.status == "passed")
    failed = sum(1 for item in run.results if item.status == "failed")
    commit = run.lineage.git_commit
    lines = [
        "## AxonPush evaluation",
        "",
        f"**{_status_line(run, failed)}** · {passed}/{len(run.results)} item(s) passed"
        + (f" · {failed} failed" if failed else ""),
        "",
        "| Experiment | Dataset revision | Commit |",
        "| --- | --- | --- |",
        f"| `{run.experiment_id}` | `{run.dataset_id}@{run.dataset_revision}` | "
        + (f"`{commit[:12]}`" if commit else "—")
        + " |",
    ]
    if run.gate:
        lines += ["", "### Release gate", ""]
        lines.append("Gate passed." if run.gate.passed else "Gate failed.")
        if run.gate.reasons:
            lines += [""] + [f"- {reason}" for reason in run.gate.reasons]
    unsuccessful = [item for item in run.results if item.status != "passed"]
    if unsuccessful:
        lines += ["", "### Failed items", ""]
        lines += [f"- `{item.item_id}`: {item.error or item.status}" for item in unsuccessful]
    return "\n".join(lines) + "\n"


def write_artifact(path: str | None, contents: str) -> None:
    """Write an artifact, creating the directory. A missing path is a no-op."""
    if not path:
        return
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(contents, encoding="utf-8")
