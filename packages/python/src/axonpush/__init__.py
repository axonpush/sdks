"""AxonPush — observability and event infrastructure for AI agent systems.

Top-level package. Public API is re-exported here; internal helpers live
under ``axonpush._internal`` and are not part of the supported surface.
"""

from axonpush._version import __version__

# from _exports_a.txt
from axonpush.client import AxonPush, AsyncAxonPush
from axonpush.exceptions import (
    AxonPushError,
    APIConnectionError,
    AuthenticationError,
    ForbiddenError,
    NotFoundError,
    RateLimitError,
    RetryableError,
    ServerError,
    ValidationError,
)
from axonpush._tracing import TraceContext, current_trace, get_or_create_trace
from axonpush._config import Settings

# from _exports_b.txt
from axonpush.models import (
    App,
    Channel,
    Environment,
    Event,
    EventBody,
    EventDetails,
    EventType,
    Organization,
    TraceSummary,
    UserOrg,
    WebhookDelivery,
    WebhookEndpoint,
)
from axonpush.resources.alerts import Alerts, AsyncAlerts
from axonpush.resources.analytics import Analytics, AsyncAnalytics
from axonpush.resources.apps import Apps, AsyncApps
from axonpush.resources.capabilities import AsyncCapabilities, Capabilities
from axonpush.resources.channels import AsyncChannels, Channels
from axonpush.resources.environments import AsyncEnvironments, Environments
from axonpush.resources.events import AsyncEvents, Events
from axonpush.resources.moderation import AsyncModeration, Moderation
from axonpush.resources.organizations import AsyncOrganizations, Organizations
from axonpush.resources.traces import AsyncTraces, Traces
from axonpush.resources.traces_v2 import AsyncTracesV2, TracesV2
from axonpush.resources.webhooks import AsyncWebhooks, Webhooks

# from _exports_d.txt
from axonpush.integrations.sentry import install_sentry

# OTel-native telemetry. Guarded so the base SDK imports without the
# ``[otel]`` extra installed; the names are only exported when it is.
try:
    from axonpush.telemetry import (
        TelemetryHandle,
        configure_telemetry,
        genai_span,
        record_genai_content,
        record_genai_response,
    )

    _HAS_TELEMETRY = True
except ImportError:
    _HAS_TELEMETRY = False

__all__ = [
    "APIConnectionError",
    "Alerts",
    "Analytics",
    "App",
    "Apps",
    "AsyncAlerts",
    "AsyncAnalytics",
    "AsyncApps",
    "AsyncAxonPush",
    "AsyncCapabilities",
    "AsyncChannels",
    "AsyncEnvironments",
    "AsyncEvents",
    "AsyncModeration",
    "AsyncOrganizations",
    "AsyncTraces",
    "AsyncTracesV2",
    "AsyncWebhooks",
    "AuthenticationError",
    "AxonPush",
    "AxonPushError",
    "Capabilities",
    "Channel",
    "Channels",
    "Environment",
    "Environments",
    "Event",
    "EventBody",
    "EventDetails",
    "EventType",
    "Events",
    "ForbiddenError",
    "Moderation",
    "NotFoundError",
    "Organization",
    "Organizations",
    "RateLimitError",
    "RetryableError",
    "ServerError",
    "Settings",
    "TraceContext",
    "TraceSummary",
    "Traces",
    "TracesV2",
    "UserOrg",
    "ValidationError",
    "WebhookDelivery",
    "WebhookEndpoint",
    "Webhooks",
    "__version__",
    "current_trace",
    "get_or_create_trace",
    "install_sentry",
]

if _HAS_TELEMETRY:
    __all__ += [
        "TelemetryHandle",
        "configure_telemetry",
        "genai_span",
        "record_genai_content",
        "record_genai_response",
    ]
