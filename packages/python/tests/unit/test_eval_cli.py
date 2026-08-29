"""The gate is the product claim; these tests hold it to the contract."""

from __future__ import annotations

import json
import sys

import pytest

from axonpush.eval.cli import EXIT_USAGE, build_parser
from axonpush.eval.reports import GateVerdict, ItemResult, RunResult, to_junit_xml
from axonpush.eval.runner import run_item
from axonpush.eval.thresholds import THRESHOLD_OPTIONS, to_wire_thresholds

# The seven names the gate endpoint accepts. The server validates with
# forbidNonWhitelisted, so anything else is a 400 rather than an ignored field.
ACCEPTED_WIRE_NAMES = {
    "minScore",
    "maxFailureRate",
    "maxLatencyMs",
    "maxCostUsd",
    "minScoreDelta",
    "maxLatencyIncreasePercent",
    "maxCostIncreasePercent",
}


def test_every_threshold_maps_onto_a_name_the_api_accepts() -> None:
    assert {option.wire for option in THRESHOLD_OPTIONS} == ACCEPTED_WIRE_NAMES


def test_unset_thresholds_are_omitted_rather_than_sent_as_zero() -> None:
    assert to_wire_thresholds({option.flag: None for option in THRESHOLD_OPTIONS}) == {}


def test_a_deliberate_zero_survives() -> None:
    assert to_wire_thresholds({"minimum-score": 0.0}) == {"minScore": 0.0}


def test_tolerated_regression_becomes_a_minimum_delta() -> None:
    assert to_wire_thresholds({"max-score-regression": 0.02}) == {"minScoreDelta": -0.02}
    assert to_wire_thresholds({"max-score-regression": -0.02}) == {"minScoreDelta": -0.02}


def test_ratios_become_percentages() -> None:
    assert to_wire_thresholds({"max-cost-increase-ratio": 0.1}) == {"maxCostIncreasePercent": 10}
    assert to_wire_thresholds({"max-latency-increase-ratio": 0.25}) == {
        "maxLatencyIncreasePercent": 25
    }


def test_parser_exposes_every_threshold_flag() -> None:
    args = build_parser().parse_args(
        [
            "run",
            "--dataset",
            "ds_1",
            "--revision",
            "3",
            "--command",
            "true",
            "--minimum-score",
            "0.8",
            "--max-cost-increase-ratio",
            "0.1",
        ]
    )
    assert args.minimum_score == 0.8
    assert args.max_cost_increase_ratio == 0.1
    assert args.max_failure_rate is None


def test_usage_errors_exit_two() -> None:
    from axonpush.eval.cli import main

    assert main(["run", "--dataset", "ds_1"]) == EXIT_USAGE


def test_runner_reads_one_json_object_per_example() -> None:
    script = (
        "import json,sys;"
        "payload=json.load(sys.stdin);"
        'print(json.dumps({"output": payload["item"]["input"]["name"].upper(),'
        ' "totalTokens": 3}))'
    )
    command = f"{json.dumps(sys.executable)} -c {json.dumps(script)}"

    result = run_item(command, "exp_1", {"itemId": "first", "input": {"name": "Ada"}})

    assert result.status == "passed"
    assert result.output == "ADA"
    assert result.total_tokens == 3


def test_runner_turns_a_broken_evaluator_into_a_failed_example() -> None:
    script = "print('not json')"
    command = f"{json.dumps(sys.executable)} -c {json.dumps(script)}"

    result = run_item(command, "exp_1", {"itemId": "first", "input": {}})

    assert result.status == "failed"
    assert result.error is not None


@pytest.mark.parametrize("passed", [True, False])
def test_junit_reports_the_gate_as_its_own_case(passed: bool) -> None:
    run = RunResult(
        experiment_id="exp_1",
        dataset_id="ds_1",
        dataset_revision=3,
        results=[ItemResult(item_id="first", status="passed")],
        gate=GateVerdict(passed=passed, reasons=[] if passed else ["score 0.9 is below 0.95"]),
    )

    xml = to_junit_xml(run)

    assert ("release gate" in xml) is not passed
    if not passed:
        assert "score 0.9 is below 0.95" in xml
