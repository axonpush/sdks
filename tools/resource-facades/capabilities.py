"""Capabilities resource — server feature flags, scopes and license. ``/capabilities``."""

from __future__ import annotations
from typing import TYPE_CHECKING, Literal
from axonpush._internal.api.api.capabilities import capabilities_get as _get_op
from axonpush._internal.api.models import CapabilitiesOutputBody, OperationCapabilities
from axonpush._internal.api.api.capabilities import capabilities_operations as _operations_op

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


OperationAvailability = Literal["allowed", "denied", "conditional", "unknown"]


def operation_availability(snapshot: OperationCapabilities | None, operation_id: str) -> OperationAvailability:
    """Discovery is advisory; missing results never grant access."""
    if snapshot is None:
        return "unknown"
    for operation in snapshot.operations or []:
        if operation.operation_id != operation_id:
            continue
        if operation.availability == "allowed":
            return "allowed"
        if operation.availability == "denied":
            return "denied"
        if operation.availability == "conditional":
            return "conditional"
    return "unknown"


class Capabilities:
    """Deployment metadata and caller-specific operation discovery."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def get(self) -> CapabilitiesOutputBody | None:
        """Fetch capabilities (version, feature flags, scopes, license). ``GET /capabilities``"""
        return self._client._invoke(_get_op)

    def operations(self) -> OperationCapabilities | None:
        """Fetch current caller permissions without caching. None means unknown."""
        return self._client._invoke(_operations_op)
