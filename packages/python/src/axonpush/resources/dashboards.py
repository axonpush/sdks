"""Dashboards resource — CRUD over saved analytics dashboards. ``/dashboards``."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from axonpush._internal.api.api.dashboards import (
    dashboards_create as _create_op,
    dashboards_delete as _delete_op,
    dashboards_get as _get_op,
    dashboards_list as _list_op,
    dashboards_update as _update_op,
)
from axonpush._internal.api.models import (
    DashboardBody,
    DashboardView,
    ListOutputBody2,
    OkOutputBody,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


def _unwrap(result: ListOutputBody2 | None) -> List[DashboardView] | None:
    if result is None:
        return None
    return list(result.dashboards or [])


class Dashboards:
    """Synchronous dashboard CRUD."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> List[DashboardView] | None:
        """List saved dashboards (envelope unwrapped). ``GET /dashboards``"""
        return self._client._invoke(_list_op, _coerce=_unwrap)

    def get(self, dashboard_id: str) -> DashboardView | None:
        """Fetch a dashboard by id. ``GET /dashboards/{dashboardId}``"""
        return self._client._invoke(_get_op, dashboard_id=dashboard_id)

    def create(self, body: DashboardBody) -> DashboardView | None:
        """Create a dashboard. ``POST /dashboards``"""
        return self._client._invoke(_create_op, body=body)

    def update(self, dashboard_id: str, body: DashboardBody) -> DashboardView | None:
        """Replace a dashboard. ``PUT /dashboards/{dashboardId}``"""
        return self._client._invoke(_update_op, dashboard_id=dashboard_id, body=body)

    def delete(self, dashboard_id: str) -> OkOutputBody | None:
        """Delete a dashboard. ``DELETE /dashboards/{dashboardId}``"""
        return self._client._invoke(_delete_op, dashboard_id=dashboard_id)


class AsyncDashboards:
    """Async sibling of :class:`Dashboards`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> List[DashboardView] | None:
        """See :meth:`Dashboards.list`."""
        return await self._client._invoke(_list_op, _coerce=_unwrap)

    async def get(self, dashboard_id: str) -> DashboardView | None:
        """See :meth:`Dashboards.get`."""
        return await self._client._invoke(_get_op, dashboard_id=dashboard_id)

    async def create(self, body: DashboardBody) -> DashboardView | None:
        """See :meth:`Dashboards.create`."""
        return await self._client._invoke(_create_op, body=body)

    async def update(self, dashboard_id: str, body: DashboardBody) -> DashboardView | None:
        """See :meth:`Dashboards.update`."""
        return await self._client._invoke(_update_op, dashboard_id=dashboard_id, body=body)

    async def delete(self, dashboard_id: str) -> OkOutputBody | None:
        """See :meth:`Dashboards.delete`."""
        return await self._client._invoke(_delete_op, dashboard_id=dashboard_id)
