"""Traces resource — list (``GET /traces``) and get (``GET /traces/{traceId}``)."""

from __future__ import annotations

from typing import TYPE_CHECKING

from axonpush._internal.api.api.traces import (
    traces_get as _get_op,
    traces_list as _list_op,
)
from axonpush._internal.api.models import GetTraceOutputBody, ListTracesOutputBody

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class Traces:
    """List and fetch traces."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> ListTracesOutputBody | None:
        """List trace summaries (newest first). ``GET /traces``.

        Args:
            since: ISO 8601 datetime, inclusive lower bound.
            until: ISO 8601 datetime, exclusive upper bound.
            limit: Page size.
            offset: Row offset for pagination.
        """
        kwargs = {
            k: v
            for k, v in {
                "since": since,
                "until": until,
                "limit": limit,
                "offset": offset,
            }.items()
            if v is not None
        }
        return self._client._invoke(_list_op, **kwargs)

    def get(self, trace_id: str) -> GetTraceOutputBody | None:
        """Fetch a single trace with its events. ``GET /traces/{traceId}``."""
        return self._client._invoke(_get_op, trace_id=trace_id)


class AsyncTraces:
    """Async sibling of :class:`Traces`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(
        self,
        *,
        since: str | None = None,
        until: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> ListTracesOutputBody | None:
        """See :meth:`Traces.list`."""
        kwargs = {
            k: v
            for k, v in {
                "since": since,
                "until": until,
                "limit": limit,
                "offset": offset,
            }.items()
            if v is not None
        }
        return await self._client._invoke(_list_op, **kwargs)

    async def get(self, trace_id: str) -> GetTraceOutputBody | None:
        """See :meth:`Traces.get`."""
        return await self._client._invoke(_get_op, trace_id=trace_id)
