"""Public model aliases over the auto-generated ``_internal.api.models`` layer.

Importers should use these names rather than reaching into the private
``_internal`` package directly. The aliases here are stable across the
public API; field changes still flow through codegen.

``EventType`` is defined locally: the Go contract accepts a free-form
``eventType`` string and no longer ships an enum, but the framework
integrations and user code still lean on these canonical constants.
"""

from __future__ import annotations

from enum import Enum

from axonpush._internal.api.models import (
    AppDTO as App,
    ChannelDTO as Channel,
    DeliveryDTO as WebhookDelivery,
    EndpointDTO as WebhookEndpoint,
    EnvironmentDTO as Environment,
    EventBody,
    EventDTO as EventDetails,
    EventOutputBody as Event,
    OrganizationDTO as Organization,
    TraceSummaryDTO as TraceSummary,
    UserOrgDTO as UserOrg,
)


class EventType(str, Enum):
    """Canonical event-type strings emitted by the SDK integrations.

    The backend accepts any string for ``eventType`` (defaulting to
    ``custom``); this enum captures the values the bundled framework
    integrations produce. Being a ``str`` subclass, members compare and
    serialize as their raw value (e.g. ``"agent.start"``).
    """

    AGENT_START = "agent.start"
    AGENT_END = "agent.end"
    AGENT_ERROR = "agent.error"
    AGENT_MESSAGE = "agent.message"
    AGENT_HANDOFF = "agent.handoff"
    AGENT_LLM_TOKEN = "agent.llm.token"
    AGENT_TOOL_CALL_START = "agent.tool_call.start"
    AGENT_TOOL_CALL_END = "agent.tool_call.end"
    AGENT_LOG = "agent.log"
    APP_LOG = "app.log"
    APP_SPAN = "app.span"

    def __str__(self) -> str:
        return self.value


__all__ = [
    "App",
    "Channel",
    "Environment",
    "Event",
    "EventBody",
    "EventDetails",
    "EventType",
    "Organization",
    "TraceSummary",
    "UserOrg",
    "WebhookDelivery",
    "WebhookEndpoint",
]
