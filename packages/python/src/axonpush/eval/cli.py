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
import signal
import sys
import threading
from typing import Any

from axonpush.client import AxonPush
from axonpush.exceptions import AxonPushError

from .api import EvaluationApiError, HttpEvaluationApi
from .git import capture_git_lineage
from .reports import (
    RunResult,
    to_github_summary,
    to_json_report,
    to_junit_xml,
    write_artifact,
)
from .runner import (
    DEFAULT_CONCURRENCY,
    DEFAULT_STARTUP_TIMEOUT_SECONDS,
    DEFAULT_TIMEOUT_SECONDS,
    LocalRunnerOptions,
    run_local_evaluation,
)
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
    run.add_argument("--revision", required=True, help="Dataset revision")
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
    run.add_argument(
        "--startup-timeout",
        type=float,
        default=DEFAULT_STARTUP_TIMEOUT_SECONDS,
        help="Seconds to wait for the experiment to enter running",
    )
    run.add_argument(
        "--configuration",
        help="Target configuration as JSON; sent to the evaluator and a new experiment",
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
        option.flag: getattr(args, option.flag.replace("-", "_")) for option in THRESHOLD_OPTIONS
    }


def _evaluator_versions(entries: list[str]) -> list[dict[str, Any]]:
    versions: list[dict[str, Any]] = []
    for entry in entries:
        head, separator, tail = entry.rpartition("@")
        if not separator or not head or not tail:
            raise ValueError("--evaluator must have the form <id>@<version>")
        versions.append({"evaluatorId": head, "version": tail})
    return versions


def _configuration(raw: str | None) -> dict[str, Any] | None:
    if not raw:
        return None
    try:
        parsed = json.loads(raw)
    except ValueError as error:
        raise ValueError(f"--configuration must be JSON: {error}") from error
    if not isinstance(parsed, dict):
        raise ValueError("--configuration must be a JSON object")
    return parsed


def _install_cancellation() -> threading.Event:
    cancel = threading.Event()

    def handle(_signal: int, _frame: object) -> None:
        cancel.set()

    for name in ("SIGINT", "SIGTERM"):
        handler = getattr(signal, name, None)
        if handler is not None:
            signal.signal(handler, handle)
    return cancel


def _create_experiment(api: HttpEvaluationApi, args: argparse.Namespace) -> str:
    if not args.target:
        raise ValueError("--target is required when --experiment is not given")
    configuration = _configuration(args.configuration)
    return api.create_experiment(
        {
            "name": args.name or f"local-{args.dataset}-r{args.revision}",
            "datasetId": args.dataset,
            "datasetRevision": args.revision,
            "targetId": args.target,
            "evaluatorVersions": _evaluator_versions(args.evaluator),
            **({"baselineExperimentId": args.baseline} if args.baseline else {}),
            **({"configuration": configuration} if configuration else {}),
            **capture_git_lineage(),
        }
    )


def _write_artifacts(args: argparse.Namespace, run: RunResult) -> None:
    write_artifact(args.json_path, to_json_report(run))
    write_artifact(args.junit_path, to_junit_xml(run))
    write_artifact(
        args.github_summary_path or os.environ.get("GITHUB_STEP_SUMMARY"),
        to_github_summary(run),
    )
    sys.stdout.write(to_json_report(run))


def run_command(args: argparse.Namespace) -> int:
    # fail_open is the right default for tracing inside an application — an
    # observability call must never take the app down. It is the wrong default
    # here: a gate that silently passes because the API was unreachable is
    # worse than no gate.
    cancel = _install_cancellation()

    with AxonPush(fail_open=False) as client:
        api = HttpEvaluationApi(client)
        experiment_id = args.experiment or _create_experiment(api, args)

        run = run_local_evaluation(
            api,
            LocalRunnerOptions(
                dataset_id=args.dataset,
                dataset_revision=str(args.revision),
                experiment_id=experiment_id,
                command=args.command,
                concurrency=args.concurrency,
                timeout_seconds=args.timeout,
                startup_timeout_seconds=args.startup_timeout,
                configuration=_configuration(args.configuration),
            ),
            cancel,
        )

        if not args.no_gate and not run.cancelled:
            run.gate = api.gate_experiment(
                experiment_id,
                to_wire_thresholds(_threshold_values(args)),
                {
                    "source": "cli",
                    "gitCommit": run.lineage.git_commit,
                    "gitBranch": run.lineage.git_branch,
                },
            )

    _write_artifacts(args, run)

    if run.cancelled:
        return EXIT_CANCELLED
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
    except (EvaluationApiError, AxonPushError) as error:
        sys.stderr.write(f"axonpush-eval: {error}\n")
        return EXIT_REMOTE_FAILURE
    except ValueError as error:
        sys.stderr.write(f"axonpush-eval: {error}\n")
        parser.print_usage(sys.stderr)
        return EXIT_USAGE


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
