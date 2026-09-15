"""Webhooks resource — manage endpoints and inspect deliveries."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from axonpush._internal.api.api.webhooks import (
    webhooks_create_endpoint as _create_op,
    webhooks_delete_endpoint as _delete_op,
    webhooks_list_deliveries as _deliveries_op,
    webhooks_list_endpoints as _list_op,
)
from axonpush._internal.api.models import (
    CreateEndpointInputBody,
    CreateEndpointOutputBody,
    ListDeliveriesOutputBody,
    ListEndpointsOutputBody,
    MessageOutputBody,
)
from axonpush._internal.api.types import UNSET
from axonpush.models import WebhookDelivery, WebhookEndpoint

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


def _unwrap_endpoints(result: ListEndpointsOutputBody | None) -> List[WebhookEndpoint] | None:
    if result is None:
        return None
    return list(result.data or [])


def _unwrap_deliveries(result: ListDeliveriesOutputBody | None) -> List[WebhookDelivery] | None:
    if result is None:
        return None
    return list(result.data or [])


def _build_create_dto(
    *,
    url: str,
    channel_id: str,
    event_types: list[str] | None,
    description: str | None,
) -> CreateEndpointInputBody:
    return CreateEndpointInputBody(
        url=url,
        channel_id=channel_id,
        event_types=event_types if event_types is not None else UNSET,
        description=description if description is not None else UNSET,
    )


class Webhooks:
    """Synchronous webhook endpoint + delivery operations."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def create_endpoint(
        self,
        *,
        url: str,
        channel_id: str,
        event_types: list[str] | None = None,
        description: str | None = None,
    ) -> CreateEndpointOutputBody | None:
        """Register a webhook endpoint on a channel.

        Args:
            url: Target URL the backend will POST to.
            channel_id: Source channel id.
            event_types: Optional event-type filter (empty / omitted = all).
            description: Free-form note.

        Returns:
            The created endpoint (response includes the raw secret once).
        """
        body = _build_create_dto(
            url=url,
            channel_id=channel_id,
            event_types=event_types,
            description=description,
        )
        return self._client._invoke(_create_op, body=body)

    def list_endpoints(self, channel_id: str) -> List[WebhookEndpoint] | None:
        """List endpoints attached to a channel (envelope unwrapped)."""
        return self._client._invoke(_list_op, channel_id=channel_id, _coerce=_unwrap_endpoints)

    def delete_endpoint(self, endpoint_id: str) -> MessageOutputBody | None:
        """Delete a webhook endpoint."""
        return self._client._invoke(_delete_op, endpoint_id=endpoint_id)

    def deliveries(self, endpoint_id: str) -> List[WebhookDelivery] | None:
        """List deliveries for a webhook endpoint (envelope unwrapped)."""
        return self._client._invoke(
            _deliveries_op, endpoint_id=endpoint_id, _coerce=_unwrap_deliveries
        )


class AsyncWebhooks:
    """Async sibling of :class:`Webhooks`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def create_endpoint(
        self,
        *,
        url: str,
        channel_id: str,
        event_types: list[str] | None = None,
        description: str | None = None,
    ) -> CreateEndpointOutputBody | None:
        """See :meth:`Webhooks.create_endpoint`."""
        body = _build_create_dto(
            url=url,
            channel_id=channel_id,
            event_types=event_types,
            description=description,
        )
        return await self._client._invoke(_create_op, body=body)

    async def list_endpoints(self, channel_id: str) -> List[WebhookEndpoint] | None:
        """See :meth:`Webhooks.list_endpoints`."""
        return await self._client._invoke(
            _list_op, channel_id=channel_id, _coerce=_unwrap_endpoints
        )

    async def delete_endpoint(self, endpoint_id: str) -> MessageOutputBody | None:
        """See :meth:`Webhooks.delete_endpoint`."""
        return await self._client._invoke(_delete_op, endpoint_id=endpoint_id)

    async def deliveries(self, endpoint_id: str) -> List[WebhookDelivery] | None:
        """See :meth:`Webhooks.deliveries`."""
        return await self._client._invoke(
            _deliveries_op, endpoint_id=endpoint_id, _coerce=_unwrap_deliveries
        )
