"""Spend policies resource — budget and rate controls. ``/spend-policies``."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from axonpush._internal.api.api.spend_policies import (
    spend_policies_create as _create_op,
    spend_policies_delete as _delete_op,
    spend_policies_list as _list_op,
    spend_policies_update as _update_op,
)
from axonpush._internal.api.models import (
    ListOutputBody,
    OkOutputBody,
    Policy,
    PolicyBody,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


def _unwrap(result: ListOutputBody | None) -> List[Policy] | None:
    if result is None:
        return None
    return list(result.policies or [])


class SpendPolicies:
    """Synchronous spend-policy CRUD."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> List[Policy] | None:
        """List spend policies (envelope unwrapped). ``GET /spend-policies``"""
        return self._client._invoke(_list_op, _coerce=_unwrap)

    def create(self, body: PolicyBody) -> Policy | None:
        """Create a spend policy. ``POST /spend-policies``"""
        return self._client._invoke(_create_op, body=body)

    def update(self, policy_id: str, body: PolicyBody) -> Policy | None:
        """Update a spend policy. ``PATCH /spend-policies/{policyId}``"""
        return self._client._invoke(_update_op, policy_id=policy_id, body=body)

    def delete(self, policy_id: str) -> OkOutputBody | None:
        """Delete a spend policy. ``DELETE /spend-policies/{policyId}``"""
        return self._client._invoke(_delete_op, policy_id=policy_id)


class AsyncSpendPolicies:
    """Async sibling of :class:`SpendPolicies`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> List[Policy] | None:
        """See :meth:`SpendPolicies.list`."""
        return await self._client._invoke(_list_op, _coerce=_unwrap)

    async def create(self, body: PolicyBody) -> Policy | None:
        """See :meth:`SpendPolicies.create`."""
        return await self._client._invoke(_create_op, body=body)

    async def update(self, policy_id: str, body: PolicyBody) -> Policy | None:
        """See :meth:`SpendPolicies.update`."""
        return await self._client._invoke(_update_op, policy_id=policy_id, body=body)

    async def delete(self, policy_id: str) -> OkOutputBody | None:
        """See :meth:`SpendPolicies.delete`."""
        return await self._client._invoke(_delete_op, policy_id=policy_id)
