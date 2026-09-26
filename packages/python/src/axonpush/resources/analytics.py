"""Aggregate timeseries and breakdowns. ``/analytics``."""

from __future__ import annotations

from typing import TYPE_CHECKING

from axonpush._internal.api.api.analytics import (
    analytics_breakdown as _breakdown_op,
    analytics_diff as _diff_op,
    analytics_dimension_values as _dimension_values_op,
    analytics_dimensions as _dimensions_op,
    analytics_heatmap as _heatmap_op,
    analytics_ingestion_status as _ingestion_status_op,
    analytics_latency as _latency_op,
    analytics_overview as _overview_op,
    analytics_timeseries as _timeseries_op,
)
from axonpush._internal.api.models import (
    AnalyticsBreakdownDimension,
    AnalyticsHeatmapBucket,
    AnalyticsHeatmapScale,
    AnalyticsOverviewBucket,
    AnalyticsOverviewOutputBody,
    AnalyticsTimeseriesBucket,
    BreakdownOutputBody,
    DiffInputBody,
    DiffOutputBody,
    DimensionsOutputBody,
    DimensionValuesOutputBody,
    HeatmapOutputBody,
    IngestionStatusOutputBody,
    LatencyPercentilesDTO,
    TimeseriesOutputBody,
)
from axonpush._internal.api.types import UNSET

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class Analytics:
    """Aggregate timeseries and breakdowns."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def breakdown(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        dimension: AnalyticsBreakdownDimension | str | None = None,
        limit: int | None = None,
    ) -> BreakdownOutputBody | None:
        """Breakdown by dimension. ``GET /analytics/breakdown``"""
        return self._client._invoke(
            _breakdown_op,
            since=since if since is not None else UNSET,
            until=until if until is not None else UNSET,
            dimension=dimension if dimension is not None else UNSET,
            limit=limit if limit is not None else UNSET,
        )

    def timeseries(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        bucket: AnalyticsTimeseriesBucket | str | None = None,
    ) -> TimeseriesOutputBody | None:
        """Bucketed timeseries. ``GET /analytics/timeseries``"""
        return self._client._invoke(
            _timeseries_op,
            since=since if since is not None else UNSET,
            until=until if until is not None else UNSET,
            bucket=bucket if bucket is not None else UNSET,
        )

    def overview(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        bucket: AnalyticsOverviewBucket | str | None = None,
    ) -> AnalyticsOverviewOutputBody | None:
        """Aggregate overview KPIs. ``GET /analytics/overview``"""
        return self._client._invoke(
            _overview_op,
            since=since if since is not None else UNSET,
            until=until if until is not None else UNSET,
            bucket=bucket if bucket is not None else UNSET,
        )

    def heatmap(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        bucket: AnalyticsHeatmapBucket | str | None = None,
        scale: AnalyticsHeatmapScale | str | None = None,
        buckets: int | None = None,
    ) -> HeatmapOutputBody | None:
        """Activity heatmap. ``GET /analytics/heatmap``"""
        return self._client._invoke(
            _heatmap_op,
            since=since if since is not None else UNSET,
            until=until if until is not None else UNSET,
            bucket=bucket if bucket is not None else UNSET,
            scale=scale if scale is not None else UNSET,
            buckets=buckets if buckets is not None else UNSET,
        )

    def diff(self, body: DiffInputBody) -> DiffOutputBody | None:
        """Compare two cohorts. ``POST /analytics/diff``"""
        return self._client._invoke(_diff_op, body=body)

    def ingestion_status(
        self,
        *,
        environment: str | None = None,
    ) -> IngestionStatusOutputBody | None:
        """Ingestion freshness and volume. ``GET /analytics/ingestion-status``"""
        return self._client._invoke(
            _ingestion_status_op,
            environment=environment if environment is not None else UNSET,
        )

    def dimensions(
        self,
        *,
        environment: str | None = None,
        limit: int | None = None,
    ) -> DimensionsOutputBody | None:
        """Discover the custom dimensions this org emits. ``GET /analytics/dimensions``"""
        return self._client._invoke(
            _dimensions_op,
            environment=environment if environment is not None else UNSET,
            limit=limit if limit is not None else UNSET,
        )

    def dimension_values(
        self,
        *,
        key: str,
        environment: str | None = None,
        limit: int | None = None,
    ) -> DimensionValuesOutputBody | None:
        """Observed values for one custom dimension. ``GET /analytics/dimensions/values``"""
        return self._client._invoke(
            _dimension_values_op,
            key=key,
            environment=environment if environment is not None else UNSET,
            limit=limit if limit is not None else UNSET,
        )

    def latency(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        model: str | None = None,
        provider: str | None = None,
        source: str | None = None,
        service: str | None = None,
        operation: str | None = None,
        filter_tag_key: str | None = None,
        filter_tag_value: str | None = None,
    ) -> LatencyPercentilesDTO | None:
        """Latency percentiles over the window. ``GET /analytics/latency``"""
        return self._client._invoke(
            _latency_op,
            since=since if since is not None else UNSET,
            until=until if until is not None else UNSET,
            model=model if model is not None else UNSET,
            provider=provider if provider is not None else UNSET,
            source=source if source is not None else UNSET,
            service=service if service is not None else UNSET,
            operation=operation if operation is not None else UNSET,
            filter_tag_key=filter_tag_key if filter_tag_key is not None else UNSET,
            filter_tag_value=filter_tag_value if filter_tag_value is not None else UNSET,
        )


class AsyncAnalytics:
    """Async sibling of :class:`Analytics`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def breakdown(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        dimension: AnalyticsBreakdownDimension | str | None = None,
        limit: int | None = None,
    ) -> BreakdownOutputBody | None:
        """See :meth:`Analytics.breakdown`."""
        return await self._client._invoke(
            _breakdown_op,
            since=since if since is not None else UNSET,
            until=until if until is not None else UNSET,
            dimension=dimension if dimension is not None else UNSET,
            limit=limit if limit is not None else UNSET,
        )

    async def timeseries(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        bucket: AnalyticsTimeseriesBucket | str | None = None,
    ) -> TimeseriesOutputBody | None:
        """See :meth:`Analytics.timeseries`."""
        return await self._client._invoke(
            _timeseries_op,
            since=since if since is not None else UNSET,
            until=until if until is not None else UNSET,
            bucket=bucket if bucket is not None else UNSET,
        )

    async def overview(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        bucket: AnalyticsOverviewBucket | str | None = None,
    ) -> AnalyticsOverviewOutputBody | None:
        """See :meth:`Analytics.overview`."""
        return await self._client._invoke(
            _overview_op,
            since=since if since is not None else UNSET,
            until=until if until is not None else UNSET,
            bucket=bucket if bucket is not None else UNSET,
        )

    async def heatmap(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        bucket: AnalyticsHeatmapBucket | str | None = None,
        scale: AnalyticsHeatmapScale | str | None = None,
        buckets: int | None = None,
    ) -> HeatmapOutputBody | None:
        """See :meth:`Analytics.heatmap`."""
        return await self._client._invoke(
            _heatmap_op,
            since=since if since is not None else UNSET,
            until=until if until is not None else UNSET,
            bucket=bucket if bucket is not None else UNSET,
            scale=scale if scale is not None else UNSET,
            buckets=buckets if buckets is not None else UNSET,
        )

    async def diff(self, body: DiffInputBody) -> DiffOutputBody | None:
        """See :meth:`Analytics.diff`."""
        return await self._client._invoke(_diff_op, body=body)

    async def ingestion_status(
        self,
        *,
        environment: str | None = None,
    ) -> IngestionStatusOutputBody | None:
        """See :meth:`Analytics.ingestion_status`."""
        return await self._client._invoke(
            _ingestion_status_op,
            environment=environment if environment is not None else UNSET,
        )

    async def dimensions(
        self,
        *,
        environment: str | None = None,
        limit: int | None = None,
    ) -> DimensionsOutputBody | None:
        """See :meth:`Analytics.dimensions`."""
        return await self._client._invoke(
            _dimensions_op,
            environment=environment if environment is not None else UNSET,
            limit=limit if limit is not None else UNSET,
        )

    async def dimension_values(
        self,
        *,
        key: str,
        environment: str | None = None,
        limit: int | None = None,
    ) -> DimensionValuesOutputBody | None:
        """See :meth:`Analytics.dimension_values`."""
        return await self._client._invoke(
            _dimension_values_op,
            key=key,
            environment=environment if environment is not None else UNSET,
            limit=limit if limit is not None else UNSET,
        )

    async def latency(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        model: str | None = None,
        provider: str | None = None,
        source: str | None = None,
        service: str | None = None,
        operation: str | None = None,
        filter_tag_key: str | None = None,
        filter_tag_value: str | None = None,
    ) -> LatencyPercentilesDTO | None:
        """See :meth:`Analytics.latency`."""
        return await self._client._invoke(
            _latency_op,
            since=since if since is not None else UNSET,
            until=until if until is not None else UNSET,
            model=model if model is not None else UNSET,
            provider=provider if provider is not None else UNSET,
            source=source if source is not None else UNSET,
            service=service if service is not None else UNSET,
            operation=operation if operation is not None else UNSET,
            filter_tag_key=filter_tag_key if filter_tag_key is not None else UNSET,
            filter_tag_value=filter_tag_value if filter_tag_value is not None else UNSET,
        )
