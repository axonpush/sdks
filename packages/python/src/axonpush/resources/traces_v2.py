"""Trace search with facets, spans and attribute keys."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from axonpush._internal.api.api.traces_v2 import (
    trace_v2_controller_attribute_keys as _attribute_keys_op,
    trace_v2_controller_detail as _detail_op,
    trace_v2_controller_events as _events_op,
    trace_v2_controller_facets as _facets_op,
    trace_v2_controller_list as _list_op,
    trace_v2_controller_spans as _spans_op,
    trace_v2_controller_stats as _stats_op,
)
from axonpush._internal.api.models import (
    TraceAttributeKeysV2ResponseDto,
    TraceDetailV2ResponseDto,
    TraceEventsV2ResponseDto,
    TraceFacetsV2ResponseDto,
    TraceListV2ResponseDto,
    TraceSpanSearchV2ResponseDto,
    TraceV2ControllerStatsResponse200,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class TracesV2:
    """Trace search with facets, spans and attribute keys."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self, params: Mapping[str, Any] | None = None) -> TraceListV2ResponseDto | None:
        """List them all. `GET /v2/traces`"""
        return self._client._invoke(_list_op, **dict(params or {}))

    def stats(
        self, *, app_id: str | None = None, environment: str | None = None
    ) -> TraceV2ControllerStatsResponse200 | None:
        """Aggregated dashboard stats. `GET /v2/traces/stats`"""
        return self._client._invoke(_stats_op, app_id=app_id, environment=environment)

    def attribute_keys(
        self, params: Mapping[str, Any] | None = None
    ) -> TraceAttributeKeysV2ResponseDto | None:
        """Attribute keys. `GET /v2/traces/attribute-keys`"""
        return self._client._invoke(_attribute_keys_op, **dict(params or {}))

    def facets(self, params: Mapping[str, Any] | None = None) -> TraceFacetsV2ResponseDto | None:
        """Facets. `GET /v2/traces/facets`"""
        return self._client._invoke(_facets_op, **dict(params or {}))

    def detail(self, trace_id: str) -> TraceDetailV2ResponseDto | None:
        """Detail. `GET /v2/traces/{traceId}`"""
        return self._client._invoke(_detail_op, trace_id=trace_id)

    def events(self, trace_id: str) -> TraceEventsV2ResponseDto | None:
        """Events. `GET /v2/traces/{traceId}/events`"""
        return self._client._invoke(_events_op, trace_id=trace_id)

    def spans(
        self, trace_id: str, limit: str | None = None, q: str | None = None
    ) -> TraceSpanSearchV2ResponseDto | None:
        """Spans. `GET /v2/traces/{traceId}/spans`"""
        return self._client._invoke(_spans_op, trace_id=trace_id, limit=limit, q=q)


class AsyncTracesV2:
    """Async sibling of :class:`TracesV2`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self, params: Mapping[str, Any] | None = None) -> TraceListV2ResponseDto | None:
        """See :meth:`TracesV2.list`."""
        return await self._client._invoke(_list_op, **dict(params or {}))

    async def stats(
        self, *, app_id: str | None = None, environment: str | None = None
    ) -> TraceV2ControllerStatsResponse200 | None:
        """See :meth:`TracesV2.stats`."""
        return await self._client._invoke(_stats_op, app_id=app_id, environment=environment)

    async def attribute_keys(
        self, params: Mapping[str, Any] | None = None
    ) -> TraceAttributeKeysV2ResponseDto | None:
        """See :meth:`TracesV2.attribute_keys`."""
        return await self._client._invoke(_attribute_keys_op, **dict(params or {}))

    async def facets(
        self, params: Mapping[str, Any] | None = None
    ) -> TraceFacetsV2ResponseDto | None:
        """See :meth:`TracesV2.facets`."""
        return await self._client._invoke(_facets_op, **dict(params or {}))

    async def detail(self, trace_id: str) -> TraceDetailV2ResponseDto | None:
        """See :meth:`TracesV2.detail`."""
        return await self._client._invoke(_detail_op, trace_id=trace_id)

    async def events(self, trace_id: str) -> TraceEventsV2ResponseDto | None:
        """See :meth:`TracesV2.events`."""
        return await self._client._invoke(_events_op, trace_id=trace_id)

    async def spans(
        self, trace_id: str, limit: str | None = None, q: str | None = None
    ) -> TraceSpanSearchV2ResponseDto | None:
        """See :meth:`TracesV2.spans`."""
        return await self._client._invoke(_spans_op, trace_id=trace_id, limit=limit, q=q)
