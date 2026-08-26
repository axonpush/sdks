"""Semantic clustering over traces: clusters, flow and coverage."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, List

from axonpush._internal.api.api.trace_intelligence import (
    trace_intelligence_controller_add_to_dataset as _add_to_dataset_op,
    trace_intelligence_controller_coverage as _coverage_op,
    trace_intelligence_controller_create_backfill as _create_backfill_op,
    trace_intelligence_controller_flow as _flow_op,
    trace_intelligence_controller_get_backfill as _get_backfill_op,
    trace_intelligence_controller_get_cluster as _get_cluster_op,
    trace_intelligence_controller_get_settings as _get_settings_op,
    trace_intelligence_controller_get_signals as _get_signals_op,
    trace_intelligence_controller_list_backfills as _list_backfills_op,
    trace_intelligence_controller_list_clusters as _list_clusters_op,
    trace_intelligence_controller_test_provider as _test_provider_op,
    trace_intelligence_controller_update_settings as _update_settings_op,
)
from axonpush._internal.api.models import (
    AddTraceClusterToDatasetDto,
    CreateTraceIntelligenceBackfillDto,
    TestTraceIntelligenceProviderDto,
    TraceClusterDatasetActionResponseDto,
    TraceIntelligenceBackfillResponseDto,
    TraceIntelligenceClusterListResponseDto,
    TraceIntelligenceClusterResponseDto,
    TraceIntelligenceCoverageResponseDto,
    TraceIntelligenceFlowResponseDto,
    TraceIntelligenceProviderTestResponseDto,
    TraceIntelligenceSettingsResponseDto,
    TraceIntelligenceSignalsResponseDto,
    UpdateTraceIntelligenceSettingsDto,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class TraceIntelligence:
    """Semantic clustering over traces: clusters, flow and coverage."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list_backfills(self) -> List[TraceIntelligenceBackfillResponseDto] | None:
        """List backfills. `GET /v2/trace-intelligence/backfills`"""
        return self._client._invoke(_list_backfills_op)

    def create_backfill(
        self, body: CreateTraceIntelligenceBackfillDto
    ) -> TraceIntelligenceBackfillResponseDto | None:
        """Create backfill. `POST /v2/trace-intelligence/backfills`"""
        return self._client._invoke(_create_backfill_op, body=body)

    def get_backfill(self, job_id: str) -> TraceIntelligenceBackfillResponseDto | None:
        """Get backfill. `GET /v2/trace-intelligence/backfills/{jobId}`"""
        return self._client._invoke(_get_backfill_op, job_id=job_id)

    def list_clusters(
        self, params: Mapping[str, Any] | None = None
    ) -> TraceIntelligenceClusterListResponseDto | None:
        """List clusters. `GET /v2/trace-intelligence/clusters`"""
        return self._client._invoke(_list_clusters_op, **dict(params or {}))

    def get_cluster(self, cluster_id: str) -> TraceIntelligenceClusterResponseDto | None:
        """Get cluster. `GET /v2/trace-intelligence/clusters/{clusterId}`"""
        return self._client._invoke(_get_cluster_op, cluster_id=cluster_id)

    def add_to_dataset(
        self, cluster_id: str, body: AddTraceClusterToDatasetDto
    ) -> TraceClusterDatasetActionResponseDto | None:
        """Add to dataset. `POST /v2/trace-intelligence/clusters/{clusterId}/actions/add-to-dataset`"""
        return self._client._invoke(_add_to_dataset_op, cluster_id=cluster_id, body=body)

    def coverage(
        self, params: Mapping[str, Any] | None = None
    ) -> TraceIntelligenceCoverageResponseDto | None:
        """Coverage. `GET /v2/trace-intelligence/coverage`"""
        return self._client._invoke(_coverage_op, **dict(params or {}))

    def flow(
        self, params: Mapping[str, Any] | None = None
    ) -> TraceIntelligenceFlowResponseDto | None:
        """Flow. `GET /v2/trace-intelligence/flow`"""
        return self._client._invoke(_flow_op, **dict(params or {}))

    def get_settings(self) -> TraceIntelligenceSettingsResponseDto | None:
        """Get settings. `GET /v2/trace-intelligence/settings`"""
        return self._client._invoke(_get_settings_op)

    def update_settings(
        self, body: UpdateTraceIntelligenceSettingsDto
    ) -> TraceIntelligenceSettingsResponseDto | None:
        """Update settings. `PUT /v2/trace-intelligence/settings`"""
        return self._client._invoke(_update_settings_op, body=body)

    def test_provider(
        self, body: TestTraceIntelligenceProviderDto
    ) -> TraceIntelligenceProviderTestResponseDto | None:
        """Test provider. `POST /v2/trace-intelligence/settings/provider/test`"""
        return self._client._invoke(_test_provider_op, body=body)

    def get_signals(self, trace_id: str) -> TraceIntelligenceSignalsResponseDto | None:
        """Get signals. `GET /v2/trace-intelligence/traces/{traceId}/signals`"""
        return self._client._invoke(_get_signals_op, trace_id=trace_id)


class AsyncTraceIntelligence:
    """Async sibling of :class:`TraceIntelligence`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list_backfills(self) -> List[TraceIntelligenceBackfillResponseDto] | None:
        """See :meth:`TraceIntelligence.list_backfills`."""
        return await self._client._invoke(_list_backfills_op)

    async def create_backfill(
        self, body: CreateTraceIntelligenceBackfillDto
    ) -> TraceIntelligenceBackfillResponseDto | None:
        """See :meth:`TraceIntelligence.create_backfill`."""
        return await self._client._invoke(_create_backfill_op, body=body)

    async def get_backfill(self, job_id: str) -> TraceIntelligenceBackfillResponseDto | None:
        """See :meth:`TraceIntelligence.get_backfill`."""
        return await self._client._invoke(_get_backfill_op, job_id=job_id)

    async def list_clusters(
        self, params: Mapping[str, Any] | None = None
    ) -> TraceIntelligenceClusterListResponseDto | None:
        """See :meth:`TraceIntelligence.list_clusters`."""
        return await self._client._invoke(_list_clusters_op, **dict(params or {}))

    async def get_cluster(self, cluster_id: str) -> TraceIntelligenceClusterResponseDto | None:
        """See :meth:`TraceIntelligence.get_cluster`."""
        return await self._client._invoke(_get_cluster_op, cluster_id=cluster_id)

    async def add_to_dataset(
        self, cluster_id: str, body: AddTraceClusterToDatasetDto
    ) -> TraceClusterDatasetActionResponseDto | None:
        """See :meth:`TraceIntelligence.add_to_dataset`."""
        return await self._client._invoke(_add_to_dataset_op, cluster_id=cluster_id, body=body)

    async def coverage(
        self, params: Mapping[str, Any] | None = None
    ) -> TraceIntelligenceCoverageResponseDto | None:
        """See :meth:`TraceIntelligence.coverage`."""
        return await self._client._invoke(_coverage_op, **dict(params or {}))

    async def flow(
        self, params: Mapping[str, Any] | None = None
    ) -> TraceIntelligenceFlowResponseDto | None:
        """See :meth:`TraceIntelligence.flow`."""
        return await self._client._invoke(_flow_op, **dict(params or {}))

    async def get_settings(self) -> TraceIntelligenceSettingsResponseDto | None:
        """See :meth:`TraceIntelligence.get_settings`."""
        return await self._client._invoke(_get_settings_op)

    async def update_settings(
        self, body: UpdateTraceIntelligenceSettingsDto
    ) -> TraceIntelligenceSettingsResponseDto | None:
        """See :meth:`TraceIntelligence.update_settings`."""
        return await self._client._invoke(_update_settings_op, body=body)

    async def test_provider(
        self, body: TestTraceIntelligenceProviderDto
    ) -> TraceIntelligenceProviderTestResponseDto | None:
        """See :meth:`TraceIntelligence.test_provider`."""
        return await self._client._invoke(_test_provider_op, body=body)

    async def get_signals(self, trace_id: str) -> TraceIntelligenceSignalsResponseDto | None:
        """See :meth:`TraceIntelligence.get_signals`."""
        return await self._client._invoke(_get_signals_op, trace_id=trace_id)
