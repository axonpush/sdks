"""Capabilities resource — server feature flags, scopes and license. ``/capabilities``."""

from __future__ import annotations

from typing import TYPE_CHECKING

from axonpush._internal.api.api.capabilities import capabilities_get as _get_op
from axonpush._internal.api.models import CapabilitiesOutputBody

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


class Capabilities:
    """Server-advertised capabilities for the calling key."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def get(self) -> CapabilitiesOutputBody | None:
        """Fetch capabilities (version, feature flags, scopes, license). ``GET /capabilities``"""
        return self._client._invoke(_get_op)


class AsyncCapabilities:
    """Async sibling of :class:`Capabilities`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def get(self) -> CapabilitiesOutputBody | None:
        """See :meth:`Capabilities.get`."""
        return await self._client._invoke(_get_op)
