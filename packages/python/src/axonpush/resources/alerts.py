"""Alert rules over metric thresholds."""

from __future__ import annotations

from typing import TYPE_CHECKING

from axonpush._internal.api.api.alerts import (
    alert_controller_create as _create_op,
    alert_controller_list as _list_op,
    alert_controller_remove as _remove_op,
    alert_controller_update as _update_op,
)
from axonpush._internal.api.models import (
    AlertDeleteDto,
    AlertRuleDto,
    AlertRuleListDto,
    CreateAlertRuleDto,
    UpdateAlertRuleDto,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class Alerts:
    """Alert rules over metric thresholds."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> AlertRuleListDto | None:
        """List them all. `GET /v2/alerts`"""
        return self._client._invoke(_list_op)

    def create(self, body: CreateAlertRuleDto) -> AlertRuleDto | None:
        """Create one. `POST /v2/alerts`"""
        return self._client._invoke(_create_op, body=body)

    def delete(self, alert_rule_id: str) -> AlertDeleteDto | None:
        """Delete one. `DELETE /v2/alerts/{alertRuleId}`"""
        return self._client._invoke(_remove_op, alert_rule_id=alert_rule_id)

    def update(self, alert_rule_id: str, body: UpdateAlertRuleDto) -> AlertRuleDto | None:
        """Update one. `PATCH /v2/alerts/{alertRuleId}`"""
        return self._client._invoke(_update_op, alert_rule_id=alert_rule_id, body=body)


class AsyncAlerts:
    """Async sibling of :class:`Alerts`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> AlertRuleListDto | None:
        """See :meth:`Alerts.list`."""
        return await self._client._invoke(_list_op)

    async def create(self, body: CreateAlertRuleDto) -> AlertRuleDto | None:
        """See :meth:`Alerts.create`."""
        return await self._client._invoke(_create_op, body=body)

    async def delete(self, alert_rule_id: str) -> AlertDeleteDto | None:
        """See :meth:`Alerts.delete`."""
        return await self._client._invoke(_remove_op, alert_rule_id=alert_rule_id)

    async def update(self, alert_rule_id: str, body: UpdateAlertRuleDto) -> AlertRuleDto | None:
        """See :meth:`Alerts.update`."""
        return await self._client._invoke(_update_op, alert_rule_id=alert_rule_id, body=body)
