"""The gate call against a server older than the provenance fields."""

from __future__ import annotations

from typing import Any

import pytest

from axonpush.eval import api as eval_api
from axonpush.eval.api import HttpEvaluationApi
from axonpush.exceptions import ValidationError


class FakeExperiments:
    """Rejects the first body the way `forbidNonWhitelisted` does."""

    def __init__(self, reject: int = 1) -> None:
        self.bodies: list[dict[str, Any]] = []
        self.reject = reject

    def gate(self, experiment_id: str, body: Any) -> dict[str, Any]:
        self.bodies.append(body.to_dict())
        if len(self.bodies) <= self.reject:
            raise ValidationError("property source should not exist", status_code=400)
        return {"passed": True, "reasons": [], "metrics": {}, "gateRunId": "run_1"}


class FakeClient:
    def __init__(self, experiments: FakeExperiments) -> None:
        self.experiments = experiments


@pytest.fixture(autouse=True)
def _reset_warning() -> None:
    eval_api._warned = False


def test_retries_without_provenance_when_the_server_rejects_it(
    capsys: pytest.CaptureFixture[str],
) -> None:
    experiments = FakeExperiments()
    api = HttpEvaluationApi(FakeClient(experiments))  # type: ignore[arg-type]

    verdict = api.gate_experiment(
        "exp_1",
        {"minScore": 0.8},
        {"source": "cli", "gitCommit": "abc1234"},
    )

    assert verdict.passed is True
    assert len(experiments.bodies) == 2
    assert experiments.bodies[0]["source"] == "cli"
    assert experiments.bodies[1] == {"minScore": 0.8}
    assert "does not accept source, gitCommit" in capsys.readouterr().err


def test_a_validation_error_with_no_provenance_to_blame_is_raised() -> None:
    experiments = FakeExperiments()
    api = HttpEvaluationApi(FakeClient(experiments))  # type: ignore[arg-type]

    with pytest.raises(ValidationError):
        api.gate_experiment("exp_1", {"minScore": 0.8})

    assert len(experiments.bodies) == 1


def test_the_warning_is_printed_once_per_process(capsys: pytest.CaptureFixture[str]) -> None:
    api = HttpEvaluationApi(FakeClient(FakeExperiments()))  # type: ignore[arg-type]
    provenance = {"source": "cli"}

    api.gate_experiment("exp_1", {"minScore": 0.8}, provenance)
    api.gate_experiment("exp_2", {"minScore": 0.8}, provenance)

    assert capsys.readouterr().err.count("does not accept") == 1
