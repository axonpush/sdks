"""The local evaluation lifecycle, which CI depends on being the same in both SDKs."""

from __future__ import annotations

import json
import sys
import threading
from typing import Any

from axonpush.eval.reports import GateVerdict, ItemResult
from axonpush.eval.runner import LocalRunnerOptions, run_local_evaluation


class FakeApi:
    """Records what the runner asked of the API, in order."""

    def __init__(
        self,
        items: list[dict[str, Any]] | None = None,
        statuses: list[str] | None = None,
    ) -> None:
        self.items = (
            items
            if items is not None
            else [
                {"id": "second", "input": {"name": "Lin"}},
                {"id": "first", "input": {"name": "Ada"}},
            ]
        )
        self.statuses = statuses or ["running"]
        self.submitted: list[list[ItemResult]] = []
        self.started = 0
        self.cancelled = 0

    def start_experiment(self, experiment_id: str) -> None:
        self.started += 1

    def get_experiment_status(self, experiment_id: str) -> str:
        return self.statuses.pop(0) if len(self.statuses) > 1 else self.statuses[0]

    def fetch_dataset_revision_items(self, dataset_id: str, revision: str) -> list[dict[str, Any]]:
        return self.items

    def submit_results(self, experiment_id: str, results: list[ItemResult]) -> None:
        self.submitted.append(results)

    def cancel_experiment(self, experiment_id: str) -> None:
        self.cancelled += 1

    def gate_experiment(self, *args: Any, **kwargs: Any) -> GateVerdict:
        return GateVerdict(passed=True)


def _echo_command() -> str:
    script = (
        "import json,sys;"
        "payload=json.load(sys.stdin);"
        'print(json.dumps({"output": payload["item"]["input"]["name"].upper()}))'
    )
    return f"{json.dumps(sys.executable)} -c {json.dumps(script)}"


def _options(**overrides: Any) -> LocalRunnerOptions:
    defaults: dict[str, Any] = {
        "dataset_id": "ds_1",
        "dataset_revision": "3",
        "experiment_id": "exp_1",
        "command": _echo_command(),
        "concurrency": 2,
    }
    defaults.update(overrides)
    return LocalRunnerOptions(**defaults)


def test_starts_the_experiment_and_submits_each_result_independently() -> None:
    api = FakeApi()

    run = run_local_evaluation(api, _options())

    assert api.started == 1
    assert len(api.submitted) == 2
    assert all(len(batch) == 1 for batch in api.submitted)
    assert [item.item_id for item in run.results] == ["first", "second"]
    assert {item.output for item in run.results} == {"ADA", "LIN"}
    assert run.cancelled is False
    assert api.cancelled == 0


def test_records_when_the_run_started_and_finished() -> None:
    run = run_local_evaluation(FakeApi(), _options())

    assert run.started_at.endswith("Z")
    assert run.completed_at >= run.started_at


def test_waits_for_the_experiment_to_be_running_before_evaluating() -> None:
    api = FakeApi(statuses=["queued", "queued", "running"])

    run = run_local_evaluation(api, _options())

    assert len(run.results) == 2
    assert api.statuses == ["running"]


def test_cancellation_stops_the_run_and_cancels_the_experiment() -> None:
    api = FakeApi()
    cancel = threading.Event()
    cancel.set()

    run = run_local_evaluation(api, _options(), cancel)

    assert run.cancelled is True
    assert api.cancelled == 1
    assert api.submitted == []


def test_a_submission_failure_is_raised_rather_than_reported_as_cancelled() -> None:
    api = FakeApi()

    def explode(experiment_id: str, results: list[ItemResult]) -> None:
        raise RuntimeError("submission refused")

    api.submit_results = explode  # type: ignore[method-assign]

    try:
        run_local_evaluation(api, _options())
    except RuntimeError as error:
        assert str(error) == "submission refused"
    else:  # pragma: no cover - the runner must not swallow this
        raise AssertionError("expected the submission failure to surface")
    assert api.cancelled == 0
