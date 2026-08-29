"""``axonpush-eval`` — replay a dataset against a candidate and gate the release.

Exit codes match the TypeScript CLI, because CI configuration is written
against the number, not the language:

    0    passed
    1    the gate blocked the release
    2    invalid usage
    3    the API could not be reached or refused the call
    4    one or more examples failed to evaluate
    130  cancelled
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any

from axonpush._internal.api.models import (
    CreateExperimentDto,
    ExperimentGateDto,
    SubmitLocalExperimentResultsDto,
)
from axonpush.client import AxonPush
from axonpush.exceptions import AxonPushError

from .git import capture_git_lineage
from .reports import (
    GateVerdict,
    RunResult,
    to_github_summary,
    to_json_report,
    to_junit_xml,
    write_artifact,
)
from .runner import DEFAULT_CONCURRENCY, DEFAULT_TIMEOUT_SECONDS, run_items
from .thresholds import THRESHOLD_OPTIONS, to_wire_thresholds

EXIT_SUCCESS = 0
EXIT_GATE_FAILED = 1
EXIT_USAGE = 2
EXIT_REMOTE_FAILURE = 3
EXIT_EVALUATION_FAILURE = 4
EXIT_CANCELLED = 130


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="axonpush-eval",
        description=(
            "Replay a dataset revision against a local evaluator command and "
            "apply the release gate."
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run", help="Run a dataset revision and gate the result")
    run.add_argument("--dataset", required=True, help="Dataset id")
    run.add_argument("--revision", required=True, type=int, help="Dataset revision")
    run.add_argument("--command", required=True, help="Evaluator command; JSON in, JSON out")
    run.add_argument("--experiment", help="Existing experiment id to submit into")
    run.add_argument("--target", help="Evaluation target id, when creating an experiment")
    run.add_argument("--name", help="Name for a newly created experiment")
    run.add_argument(
        "--evaluator",
        action="append",
        default=[],
        metavar="ID@VERSION",
        help="Evaluator version for a new experiment; repeatable",
    )
    run.add_argument("--baseline", help="Baseline experiment id, for delta thresholds")
    run.add_argument("--concurrency", type=int, default=DEFAULT_CONCURRENCY)
    run.add_argument(
        "--timeout",
        type=float,
        default=DEFAULT_TIMEOUT_SECONDS,
        help="Per-example evaluator timeout in seconds",
    )
    run.add_argument("--no-gate", action="store_true", help="Do not invoke the release gate")
    run.add_argument("--json", dest="json_path", help="Write a JSON artifact")
    run.add_argument("--junit", dest="junit_path", help="Write a JUnit XML artifact")
    run.add_argument(
        "--github-summary",
        dest="github_summary_path",
        help="Write GitHub Actions markdown (defaults to $GITHUB_STEP_SUMMARY)",
    )
    for option in THRESHOLD_OPTIONS:
        run.add_argument(f"--{option.flag}", type=float, default=None, help=option.help)
    return parser


def _threshold_values(args: argparse.Namespace) -> dict[str, float | None]:
    return {
        option.flag: getattr(args, option.flag.replace("-", "_"))
        for option in THRESHOLD_OPTIONS
    }


def _evaluator_versions(entries: list[str]) -> list[dict[str, Any]]:
    versions: list[dict[str, Any]] = []
    for entry in entries:
        head, separator, tail = entry.rpartition("@")
        if not separator or not head or not tail:
            raise ValueError("--evaluator must have the form <id>@<version>")
        versions.append({"evaluatorId": head, "version": int(tail)})
    return versions


def _unwrap(value: Any, field: str) -> Any:
    """Read a field off a generated model or a plain dict, whichever came back."""
    if value is None:
        return None
    if isinstance(value, dict):
        return value.get(field)
    return getattr(value, field, None)


def run_command(args: argparse.Namespace) -> int:
    # fail_open is the right default for tracing inside an application — an
    # observability call must never take the app down. It is the wrong default
    # here: a gate that silently passes because the API was unreachable is
    # worse than no gate.
    client = AxonPush(fail_open=False)

    with client:
        experiment_id = args.experiment
        if not experiment_id:
            if not args.target:
                raise ValueError("--target is required when --experiment is not given")
            created = client.experiments.create(
                CreateExperimentDto.from_dict({
                    "name": args.name or f"local-{args.dataset}-r{args.revision}",
                    "datasetId": args.dataset,
                    "datasetRevision": args.revision,
                    "targetId": args.target,
                    "evaluatorVersions": _evaluator_versions(args.evaluator),
                    **({"baselineExperimentId": args.baseline} if args.baseline else {}),
                    **capture_git_lineage(),
                })
            )
            experiment_id = _unwrap(created, "experiment_id") or _unwrap(created, "experimentId")
            if not experiment_id:
                raise AxonPushError("The API did not return an experiment id")

        items_response = client.datasets.items(args.dataset, str(args.revision))
        items = _unwrap(items_response, "data") or []
        normalised = [item if isinstance(item, dict) else item.to_dict() for item in items]

        results = run_items(
            args.command,
            experiment_id,
            normalised,
            concurrency=args.concurrency,
            timeout_seconds=args.timeout,
        )

        client.experiments.submit_results(
            experiment_id,
            SubmitLocalExperimentResultsDto.from_dict({
                "results": [
                    {
                        "itemId": item.item_id,
                        "output": item.output,
                        **({"error": item.error} if item.error else {}),
                        **({"latencyMs": item.latency_ms} if item.latency_ms is not None else {}),
                        **(
                            {"totalTokens": item.total_tokens}
                            if item.total_tokens is not None
                            else {}
                        ),
                        **({"costUsd": item.cost_usd} if item.cost_usd is not None else {}),
                        **({"traceId": item.trace_id} if item.trace_id else {}),
                    }
                    for item in results
                ]
            }),
        )

        run = RunResult(
            experiment_id=experiment_id,
            dataset_id=args.dataset,
            dataset_revision=args.revision,
            results=results,
        )

        if not args.no_gate:
            verdict = client.experiments.gate(
                experiment_id,
                ExperimentGateDto.from_dict(to_wire_thresholds(_threshold_values(args))),
            )
            run.gate = GateVerdict(
                passed=bool(_unwrap(verdict, "passed")),
                reasons=list(_unwrap(verdict, "reasons") or []),
                metrics=dict(_unwrap(verdict, "metrics") or {}),
            )

    write_artifact(args.json_path, to_json_report(run))
    write_artifact(args.junit_path, to_junit_xml(run))
    write_artifact(
        args.github_summary_path or os.environ.get("GITHUB_STEP_SUMMARY"),
        to_github_summary(run),
    )
    sys.stdout.write(to_json_report(run))

    if run.gate and not run.gate.passed:
        return EXIT_GATE_FAILED
    if any(item.status != "passed" for item in run.results):
        return EXIT_EVALUATION_FAILURE
    return EXIT_SUCCESS


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as exit_error:  # argparse already printed the problem
        return EXIT_USAGE if exit_error.code else EXIT_SUCCESS

    try:
        return run_command(args)
    except KeyboardInterrupt:
        sys.stderr.write("axonpush-eval: cancelled\n")
        return EXIT_CANCELLED
    except AxonPushError as error:
        sys.stderr.write(f"axonpush-eval: {error}\n")
        return EXIT_REMOTE_FAILURE
    except (ValueError, TypeError, json.JSONDecodeError) as error:
        sys.stderr.write(f"axonpush-eval: {error}\n")
        return EXIT_USAGE


if __name__ == "__main__":  # pragma: no cover - module entry point
    raise SystemExit(main())
