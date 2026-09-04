"""Public model aliases over the auto-generated ``_internal.api.models`` layer.

Importers should use these names rather than reaching into the private
``_internal`` package directly. The aliases here are stable across the
public API; field changes still flow through codegen.
"""

from __future__ import annotations

from axonpush._internal.api.models import (
    ApiKeyCreateResponseDto,
    ApiKeyResponseDto as ApiKey,
    AppResponseDto as App,
    ChannelResponseDto as Channel,
    CreateEventDto,
    EventType,
    EnvironmentResponseDto as Environment,
    EventIngestResponseDto as Event,
    EventListResponseDto,
    EventResponseDto as EventDetails,
    OrganizationCreateResponseDto,
    OrganizationResponseDto as Organization,
    WebhookDeliveryResponseDto as WebhookDelivery,
    WebhookDeliveryStatus as DeliveryStatus,
    WebhookEndpointCreateResponseDto,
    WebhookEndpointResponseDto as WebhookEndpoint,
)

__all__ = [
    "ApiKey",
    "ApiKeyCreateResponseDto",
    "App",
    "Channel",
    "CreateEventDto",
    "DeliveryStatus",
    "Environment",
    "Event",
    "EventDetails",
    "EventListResponseDto",
    "EventType",
    "Organization",
    "OrganizationCreateResponseDto",
    "WebhookDelivery",
    "WebhookEndpoint",
    "WebhookEndpointCreateResponseDto",
]
