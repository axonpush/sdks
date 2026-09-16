"""Alert rules over metric thresholds. ``/v2/alerts``."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from axonpush._internal.api.api.alerts import (
    alerts_create as _create_op,
    alerts_delete as _remove_op,
    alerts_list as _list_op,
    alerts_update as _update_op,
)
from axonpush._internal.api.models import (
    AlertRuleDTO,
    CreateInputBody,
    DeleteOutputBody,
    ListOutputBody1,
    UpdateInputBody,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


def _unwrap(result: ListOutputBody1 | None) -> List[AlertRuleDTO] | None:
    if result is None:
        return None
    return list(result.data or [])


class Alerts:
    """Alert rules over metric thresholds."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> List[AlertRuleDTO] | None:
        """List them all (envelope unwrapped). ``GET /v2/alerts``"""
        return self._client._invoke(_list_op, _coerce=_unwrap)

    def create(self, body: CreateInputBody) -> AlertRuleDTO | None:
        """Create one. ``POST /v2/alerts``"""
        return self._client._invoke(_create_op, body=body)

    def delete(self, alert_rule_id: str) -> DeleteOutputBody | None:
        """Delete one. ``DELETE /v2/alerts/{alertRuleId}``"""
        return self._client._invoke(_remove_op, alert_rule_id=alert_rule_id)

    def update(self, alert_rule_id: str, body: UpdateInputBody) -> AlertRuleDTO | None:
        """Update one. ``PATCH /v2/alerts/{alertRuleId}``"""
        return self._client._invoke(_update_op, alert_rule_id=alert_rule_id, body=body)


class AsyncAlerts:
    """Async sibling of :class:`Alerts`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> List[AlertRuleDTO] | None:
        """See :meth:`Alerts.list`."""
        return await self._client._invoke(_list_op, _coerce=_unwrap)

    async def create(self, body: CreateInputBody) -> AlertRuleDTO | None:
        """See :meth:`Alerts.create`."""
        return await self._client._invoke(_create_op, body=body)

    async def delete(self, alert_rule_id: str) -> DeleteOutputBody | None:
        """See :meth:`Alerts.delete`."""
        return await self._client._invoke(_remove_op, alert_rule_id=alert_rule_id)

    async def update(self, alert_rule_id: str, body: UpdateInputBody) -> AlertRuleDTO | None:
        """See :meth:`Alerts.update`."""
        return await self._client._invoke(_update_op, alert_rule_id=alert_rule_id, body=body)
