"""The evaluation surface the runner depends on.

Kept as a protocol with one HTTP implementation, mirroring the TypeScript
``EvaluationApi``: the runner can then be tested without a transport, and the
two languages stay describable by the same interface.
"""

from __future__ import annotations

import sys

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Protocol

from axonpush._internal.api.models import (
    CreateExperimentDto,
    ExperimentGateDto,
    SubmitLocalExperimentResultsDto,
)
from axonpush.exceptions import AxonPushError

if TYPE_CHECKING:
    from axonpush.client import AxonPush

    from .reports import GateVerdict, ItemResult

GATE_PROVENANCE_FIELDS = ("source", "gitCommit", "gitBranch", "release")

_warned = False


def _warn_once(message: str) -> None:
    global _warned
    if _warned:
        return
    _warned = True
    print(f"axonpush: {message}", file=sys.stderr)


class EvaluationApiError(AxonPushError):
    """The API answered with a shape the runner cannot use."""


def unwrap(value: Any, field: str) -> Any:
    """Read a field off a generated model or a plain dict, whichever came back."""
    if value is None:
        return None
    if isinstance(value, dict):
        return value.get(field)
    return getattr(value, field, None)


def as_mapping(value: Any) -> dict[str, Any]:
    """Generated models are attrs classes, not mappings; `dict()` on one raises."""
    if value is None:
        return {}
    if isinstance(value, dict):
        return dict(value)
    to_dict = getattr(value, "to_dict", None)
    return dict(to_dict()) if callable(to_dict) else {}


def to_wire_provenance(provenance: Mapping[str, Any] | None) -> dict[str, str]:
    """The gate endpoint validates with ``forbidNonWhitelisted``.

    Only the four fields it declares may be sent. ``gitDirty`` belongs to the
    experiment, not the decision, and would be rejected here.
    """
    if not provenance:
        return {}
    return {
        key: str(provenance[key])
        for key in GATE_PROVENANCE_FIELDS
        if provenance.get(key) is not None
    }


def _result_payload(item: ItemResult) -> dict[str, Any]:
    payload: dict[str, Any] = {"itemId": item.item_id, "output": item.output}
    optional = {
        "error": item.error,
        "latencyMs": item.latency_ms,
        "totalTokens": item.total_tokens,
        "costUsd": item.cost_usd,
        "traceId": item.trace_id,
    }
    payload.update({key: value for key, value in optional.items() if value is not None})
    return payload


class EvaluationApi(Protocol):
    """What ``run_local_evaluation`` needs. See :class:`HttpEvaluationApi`."""

    def fetch_dataset_revision_items(
        self, dataset_id: str, revision: str
    ) -> list[dict[str, Any]]: ...

    def submit_results(self, experiment_id: str, results: list[ItemResult]) -> None: ...

    def start_experiment(self, experiment_id: str) -> None: ...

    def get_experiment_status(self, experiment_id: str) -> str: ...

    def cancel_experiment(self, experiment_id: str) -> None: ...

    def gate_experiment(
        self,
        experiment_id: str,
        thresholds: Mapping[str, float] | None = None,
        provenance: Mapping[str, Any] | None = None,
    ) -> GateVerdict: ...


class HttpEvaluationApi:
    """Drives the evaluation endpoints through the ordinary resource layer."""

    def __init__(self, client: AxonPush) -> None:
        self._client = client

    def create_experiment(self, options: Mapping[str, Any]) -> str:
        created = self._client.experiments.create(CreateExperimentDto.from_dict(dict(options)))
        experiment_id = unwrap(created, "experiment_id") or unwrap(created, "experimentId")
        if not experiment_id:
            raise EvaluationApiError("The API did not return an experiment id")
        return str(experiment_id)

    def fetch_dataset_revision_items(self, dataset_id: str, revision: str) -> list[dict[str, Any]]:
        response = self._client.datasets.items(dataset_id, revision)
        items = unwrap(response, "data")
        if items is None:
            raise EvaluationApiError("Dataset revision items response was invalid")
        return [item if isinstance(item, dict) else item.to_dict() for item in items]

    def submit_results(self, experiment_id: str, results: list[ItemResult]) -> None:
        self._client.experiments.submit_results(
            experiment_id,
            SubmitLocalExperimentResultsDto.from_dict(
                {"results": [_result_payload(item) for item in results]}
            ),
        )

    def start_experiment(self, experiment_id: str) -> None:
        self._client.experiments.run(experiment_id)

    def get_experiment_status(self, experiment_id: str) -> str:
        status = unwrap(self._client.experiments.get(experiment_id), "status")
        if not isinstance(status, str):
            raise EvaluationApiError("Experiment status response was invalid")
        return status

    def cancel_experiment(self, experiment_id: str) -> None:
        self._client.experiments.cancel(experiment_id)

    def gate_experiment(
        self,
        experiment_id: str,
        thresholds: Mapping[str, float] | None = None,
        provenance: Mapping[str, Any] | None = None,
    ) -> GateVerdict:
        from .reports import GateVerdict

        wire_thresholds = dict(thresholds or {})
        wire_provenance = to_wire_provenance(provenance)

        def send(body: dict[str, Any]) -> Any:
            return self._client.experiments.gate(experiment_id, ExperimentGateDto.from_dict(body))

        try:
            verdict = send({**wire_thresholds, **wire_provenance})
        except AxonPushError as error:
            # forbidNonWhitelisted: a server older than these fields rejects the whole call.
            if error.status_code != 400 or not wire_provenance:
                raise
            _warn_once(
                f"This axonpush server does not accept {', '.join(wire_provenance)} on the "
                "gate. The decision will be recorded without them; upgrade the server to "
                "attribute it to a commit."
            )
            verdict = send(wire_thresholds)

        passed = unwrap(verdict, "passed")
        if not isinstance(passed, bool):
            raise EvaluationApiError("Gate response was invalid")
        return GateVerdict(
            passed=passed,
            reasons=list(unwrap(verdict, "reasons") or []),
            metrics=as_mapping(unwrap(verdict, "metrics")),
            gate_run_id=unwrap(verdict, "gate_run_id") or unwrap(verdict, "gateRunId"),
        )
