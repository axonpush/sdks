"""Govern policies resource — request-mutation policies. ``/govern-policies``."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from axonpush._internal.api.api.govern_policies import (
    govern_policies_create as _create_op,
    govern_policies_delete as _delete_op,
    govern_policies_list as _list_op,
    govern_policies_update as _update_op,
)
from axonpush._internal.api.models import (
    GovernPolicyBody,
    GovernPolicyView,
    ListOutputBody1,
    OkOutputBody,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


def _unwrap(result: ListOutputBody1 | None) -> List[GovernPolicyView] | None:
    if result is None:
        return None
    return list(result.policies or [])


class GovernPolicies:
    """Synchronous govern-policy CRUD."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> List[GovernPolicyView] | None:
        """List govern policies (envelope unwrapped). ``GET /govern-policies``"""
        return self._client._invoke(_list_op, _coerce=_unwrap)

    def create(self, body: GovernPolicyBody) -> GovernPolicyView | None:
        """Create a govern policy. ``POST /govern-policies``"""
        return self._client._invoke(_create_op, body=body)

    def update(self, policy_id: str, body: GovernPolicyBody) -> GovernPolicyView | None:
        """Update a govern policy. ``PATCH /govern-policies/{policyId}``"""
        return self._client._invoke(_update_op, policy_id=policy_id, body=body)

    def delete(self, policy_id: str) -> OkOutputBody | None:
        """Delete a govern policy. ``DELETE /govern-policies/{policyId}``"""
        return self._client._invoke(_delete_op, policy_id=policy_id)


class AsyncGovernPolicies:
    """Async sibling of :class:`GovernPolicies`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> List[GovernPolicyView] | None:
        """See :meth:`GovernPolicies.list`."""
        return await self._client._invoke(_list_op, _coerce=_unwrap)

    async def create(self, body: GovernPolicyBody) -> GovernPolicyView | None:
        """See :meth:`GovernPolicies.create`."""
        return await self._client._invoke(_create_op, body=body)

    async def update(self, policy_id: str, body: GovernPolicyBody) -> GovernPolicyView | None:
        """See :meth:`GovernPolicies.update`."""
        return await self._client._invoke(_update_op, policy_id=policy_id, body=body)

    async def delete(self, policy_id: str) -> OkOutputBody | None:
        """See :meth:`GovernPolicies.delete`."""
        return await self._client._invoke(_delete_op, policy_id=policy_id)
