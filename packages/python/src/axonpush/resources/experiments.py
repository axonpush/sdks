"""Evaluation runs, their results and the release gate."""

from __future__ import annotations

from typing import TYPE_CHECKING

from axonpush._internal.api.api.experiments import (
    experiment_controller_cancel as _cancel_op,
    experiment_controller_compare as _compare_op,
    experiment_controller_create as _create_op,
    experiment_controller_gate as _gate_op,
    experiment_controller_get as _get_op,
    experiment_controller_list as _list_op,
    experiment_controller_remove as _remove_op,
    experiment_controller_results as _results_op,
    experiment_controller_run as _run_op,
    experiment_controller_submit_results as _submit_results_op,
)
from axonpush._internal.api.models import (
    CreateExperimentDto,
    ExperimentComparisonDto,
    ExperimentDeleteDto,
    ExperimentDto,
    ExperimentGateDto,
    ExperimentGateResultDto,
    ExperimentListDto,
    ExperimentResultListDto,
    SubmitLocalExperimentResultsDto,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class Experiments:
    """Evaluation runs, their results and the release gate."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> ExperimentListDto | None:
        """List them all. `GET /v2/experiments`"""
        return self._client._invoke(_list_op)

    def create(self, body: CreateExperimentDto) -> ExperimentDto | None:
        """Create one. `POST /v2/experiments`"""
        return self._client._invoke(_create_op, body=body)

    def delete(self, experiment_id: str) -> ExperimentDeleteDto | None:
        """Delete one. `DELETE /v2/experiments/{experimentId}`"""
        return self._client._invoke(_remove_op, experiment_id=experiment_id)

    def get(self, experiment_id: str) -> ExperimentDto | None:
        """Fetch one by id. `GET /v2/experiments/{experimentId}`"""
        return self._client._invoke(_get_op, experiment_id=experiment_id)

    def cancel(self, experiment_id: str) -> ExperimentDto | None:
        """Cancel. `POST /v2/experiments/{experimentId}/cancel`"""
        return self._client._invoke(_cancel_op, experiment_id=experiment_id)

    def compare(
        self, experiment_id: str, baseline_experiment_id: str | None = None
    ) -> ExperimentComparisonDto | None:
        """Compare. `GET /v2/experiments/{experimentId}/compare`"""
        return self._client._invoke(
            _compare_op, experiment_id=experiment_id, baseline_experiment_id=baseline_experiment_id
        )

    def gate(self, experiment_id: str, body: ExperimentGateDto) -> ExperimentGateResultDto | None:
        """Gate. `POST /v2/experiments/{experimentId}/gate`"""
        return self._client._invoke(_gate_op, experiment_id=experiment_id, body=body)

    def results(self, experiment_id: str) -> ExperimentResultListDto | None:
        """Results. `GET /v2/experiments/{experimentId}/results`"""
        return self._client._invoke(_results_op, experiment_id=experiment_id)

    def submit_results(
        self, experiment_id: str, body: SubmitLocalExperimentResultsDto
    ) -> ExperimentDto | None:
        """Submit results. `POST /v2/experiments/{experimentId}/results`"""
        return self._client._invoke(_submit_results_op, experiment_id=experiment_id, body=body)

    def run(self, experiment_id: str) -> ExperimentDto | None:
        """Run. `POST /v2/experiments/{experimentId}/run`"""
        return self._client._invoke(_run_op, experiment_id=experiment_id)


class AsyncExperiments:
    """Async sibling of :class:`Experiments`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> ExperimentListDto | None:
        """See :meth:`Experiments.list`."""
        return await self._client._invoke(_list_op)

    async def create(self, body: CreateExperimentDto) -> ExperimentDto | None:
        """See :meth:`Experiments.create`."""
        return await self._client._invoke(_create_op, body=body)

    async def delete(self, experiment_id: str) -> ExperimentDeleteDto | None:
        """See :meth:`Experiments.delete`."""
        return await self._client._invoke(_remove_op, experiment_id=experiment_id)

    async def get(self, experiment_id: str) -> ExperimentDto | None:
        """See :meth:`Experiments.get`."""
        return await self._client._invoke(_get_op, experiment_id=experiment_id)

    async def cancel(self, experiment_id: str) -> ExperimentDto | None:
        """See :meth:`Experiments.cancel`."""
        return await self._client._invoke(_cancel_op, experiment_id=experiment_id)

    async def compare(
        self, experiment_id: str, baseline_experiment_id: str | None = None
    ) -> ExperimentComparisonDto | None:
        """See :meth:`Experiments.compare`."""
        return await self._client._invoke(
            _compare_op, experiment_id=experiment_id, baseline_experiment_id=baseline_experiment_id
        )

    async def gate(
        self, experiment_id: str, body: ExperimentGateDto
    ) -> ExperimentGateResultDto | None:
        """See :meth:`Experiments.gate`."""
        return await self._client._invoke(_gate_op, experiment_id=experiment_id, body=body)

    async def results(self, experiment_id: str) -> ExperimentResultListDto | None:
        """See :meth:`Experiments.results`."""
        return await self._client._invoke(_results_op, experiment_id=experiment_id)

    async def submit_results(
        self, experiment_id: str, body: SubmitLocalExperimentResultsDto
    ) -> ExperimentDto | None:
        """See :meth:`Experiments.submit_results`."""
        return await self._client._invoke(
            _submit_results_op, experiment_id=experiment_id, body=body
        )

    async def run(self, experiment_id: str) -> ExperimentDto | None:
        """See :meth:`Experiments.run`."""
        return await self._client._invoke(_run_op, experiment_id=experiment_id)
