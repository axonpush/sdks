"""Aggregate timeseries and breakdowns. ``/analytics``."""

from __future__ import annotations

from typing import TYPE_CHECKING

from axonpush._internal.api.api.analytics import (
    analytics_breakdown as _breakdown_op,
    analytics_timeseries as _timeseries_op,
)
from axonpush._internal.api.models import (
    AnalyticsBreakdownDimension,
    AnalyticsTimeseriesBucket,
    BreakdownOutputBody,
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
