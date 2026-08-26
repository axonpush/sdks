"""Aggregate timeseries, breakdowns and A/B comparisons."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from axonpush._internal.api.api.analytics_v2 import (
    analytics_controller_breakdown as _breakdown_op,
    analytics_controller_compare as _compare_op,
    analytics_controller_timeseries as _timeseries_op,
)
from axonpush._internal.api.models import (
    AnalyticsBreakdownResponseDto,
    AnalyticsCompareResponseDto,
    AnalyticsTimeseriesResponseDto,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class Analytics:
    """Aggregate timeseries, breakdowns and A/B comparisons."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def breakdown(
        self, params: Mapping[str, Any] | None = None
    ) -> AnalyticsBreakdownResponseDto | None:
        """Breakdown. `GET /v2/analytics/breakdown`"""
        return self._client._invoke(_breakdown_op, **dict(params or {}))

    def compare(
        self, params: Mapping[str, Any] | None = None
    ) -> AnalyticsCompareResponseDto | None:
        """Compare. `GET /v2/analytics/compare`"""
        return self._client._invoke(_compare_op, **dict(params or {}))

    def timeseries(
        self, params: Mapping[str, Any] | None = None
    ) -> AnalyticsTimeseriesResponseDto | None:
        """Timeseries. `GET /v2/analytics/timeseries`"""
        return self._client._invoke(_timeseries_op, **dict(params or {}))


class AsyncAnalytics:
    """Async sibling of :class:`Analytics`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def breakdown(
        self, params: Mapping[str, Any] | None = None
    ) -> AnalyticsBreakdownResponseDto | None:
        """See :meth:`Analytics.breakdown`."""
        return await self._client._invoke(_breakdown_op, **dict(params or {}))

    async def compare(
        self, params: Mapping[str, Any] | None = None
    ) -> AnalyticsCompareResponseDto | None:
        """See :meth:`Analytics.compare`."""
        return await self._client._invoke(_compare_op, **dict(params or {}))

    async def timeseries(
        self, params: Mapping[str, Any] | None = None
    ) -> AnalyticsTimeseriesResponseDto | None:
        """See :meth:`Analytics.timeseries`."""
        return await self._client._invoke(_timeseries_op, **dict(params or {}))
