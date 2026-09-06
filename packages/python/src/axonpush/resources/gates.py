"""Release-gate policies and the history of gate decisions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from axonpush._internal.api.api.gate_policies import (
    gate_policy_controller_get as _gate_policy_get_op,
    gate_policy_controller_list as _gate_policy_list_op,
    gate_policy_controller_remove as _gate_policy_remove_op,
    gate_policy_controller_save as _gate_policy_save_op,
)
from axonpush._internal.api.api.gate_runs import (
    gate_run_controller_list as _gate_run_list_op,
)
from axonpush._internal.api.models import (
    GatePolicyDeleteDto,
    GatePolicyDto,
    GatePolicyListDto,
    GateRunListDto,
    SaveGatePolicyDto,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class Gates:
    """Release-gate policies and the history of gate decisions."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list_policies(self) -> GatePolicyListDto | None:
        """List policies. `GET /v2/gate-policies`"""
        return self._client._invoke(_gate_policy_list_op)

    def save_policy(self, body: SaveGatePolicyDto) -> GatePolicyDto | None:
        """Save policy. `POST /v2/gate-policies`"""
        return self._client._invoke(_gate_policy_save_op, body=body)

    def delete_policy(self, scope_type: str, scope_id: str) -> GatePolicyDeleteDto | None:
        """Delete policy. `DELETE /v2/gate-policies/{scopeType}/{scopeId}`"""
        return self._client._invoke(
            _gate_policy_remove_op, scope_type=scope_type, scope_id=scope_id
        )

    def get_policy(self, scope_type: str, scope_id: str) -> GatePolicyDto | None:
        """Get policy. `GET /v2/gate-policies/{scopeType}/{scopeId}`"""
        return self._client._invoke(_gate_policy_get_op, scope_type=scope_type, scope_id=scope_id)

    def list_runs(
        self, cursor: str | None = None, experiment_id: str | None = None, limit: str | None = None
    ) -> GateRunListDto | None:
        """List runs. `GET /v2/gate-runs`"""
        return self._client._invoke(
            _gate_run_list_op, cursor=cursor, experiment_id=experiment_id, limit=limit
        )


class AsyncGates:
    """Async sibling of :class:`Gates`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list_policies(self) -> GatePolicyListDto | None:
        """See :meth:`Gates.list_policies`."""
        return await self._client._invoke(_gate_policy_list_op)

    async def save_policy(self, body: SaveGatePolicyDto) -> GatePolicyDto | None:
        """See :meth:`Gates.save_policy`."""
        return await self._client._invoke(_gate_policy_save_op, body=body)

    async def delete_policy(self, scope_type: str, scope_id: str) -> GatePolicyDeleteDto | None:
        """See :meth:`Gates.delete_policy`."""
        return await self._client._invoke(
            _gate_policy_remove_op, scope_type=scope_type, scope_id=scope_id
        )

    async def get_policy(self, scope_type: str, scope_id: str) -> GatePolicyDto | None:
        """See :meth:`Gates.get_policy`."""
        return await self._client._invoke(
            _gate_policy_get_op, scope_type=scope_type, scope_id=scope_id
        )

    async def list_runs(
        self, cursor: str | None = None, experiment_id: str | None = None, limit: str | None = None
    ) -> GateRunListDto | None:
        """See :meth:`Gates.list_runs`."""
        return await self._client._invoke(
            _gate_run_list_op, cursor=cursor, experiment_id=experiment_id, limit=limit
        )
