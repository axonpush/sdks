"""Artifacts a CI run leaves behind: JSON, JUnit XML and a GitHub summary."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr


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


@dataclass
class RunResult:
    experiment_id: str
    dataset_id: str
    dataset_revision: int
    results: list[ItemResult] = field(default_factory=list)
    gate: GateVerdict | None = None
    cancelled: bool = False


def to_json_report(run: RunResult) -> str:
    payload = {
        "experimentId": run.experiment_id,
        "datasetId": run.dataset_id,
        "datasetRevision": run.dataset_revision,
        "cancelled": run.cancelled,
        "results": [asdict(item) for item in run.results],
        "gate": asdict(run.gate) if run.gate else None,
    }
    return json.dumps(payload, indent=2, default=str) + "\n"


def to_junit_xml(run: RunResult) -> str:
    failures = sum(1 for item in run.results if item.status != "passed")
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<testsuite name="axonpush-eval" tests="{len(run.results)}" failures="{failures}">',
    ]
    for item in run.results:
        name = quoteattr(item.item_id)
        if item.status == "passed":
            lines.append(f"  <testcase name={name} />")
            continue
        message = quoteattr(item.error or "evaluation failed")
        lines.append(f"  <testcase name={name}>")
        lines.append(f"    <failure message={message} />")
        lines.append("  </testcase>")
    if run.gate and not run.gate.passed:
        reasons = escape("; ".join(run.gate.reasons))
        lines.append('  <testcase name="release gate">')
        lines.append(f'    <failure message="gate failed">{reasons}</failure>')
        lines.append("  </testcase>")
    lines.append("</testsuite>")
    return "\n".join(lines) + "\n"


def to_github_summary(run: RunResult) -> str:
    passed = sum(1 for item in run.results if item.status == "passed")
    lines = ["## axonpush release gate", ""]
    if run.gate is None:
        lines.append("Gate not evaluated.")
    elif run.gate.passed:
        lines.append("**Passed.** Nothing regressed against the thresholds.")
    else:
        lines.append("**Blocked.** The following thresholds were not met:")
        lines.append("")
        lines.extend(f"- {reason}" for reason in run.gate.reasons)
    lines += ["", f"{passed} of {len(run.results)} examples passed.", ""]
    return "\n".join(lines)


def write_artifact(path: str | None, contents: str) -> None:
    """Write an artifact, creating the directory. A missing path is a no-op."""
    if not path:
        return
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(contents, encoding="utf-8")
