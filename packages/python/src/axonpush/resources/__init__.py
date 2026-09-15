"""Resource classes wiring the public facade to the generated client.

Each resource maps to a slice of the Go/Huma contract and exposes a sync
class plus an ``Async`` prefixed sibling:
``events``, ``channels``, ``apps``, ``environments``, ``webhooks``,
``traces`` (alias ``traces_v2``), ``organizations``, ``alerts``,
``analytics``, ``moderation``, ``capabilities``.
"""

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

__all__ = [
    "Alerts",
    "Analytics",
    "Apps",
    "AsyncAlerts",
    "AsyncAnalytics",
    "AsyncApps",
    "AsyncCapabilities",
    "AsyncChannels",
    "AsyncEnvironments",
    "AsyncEvents",
    "AsyncModeration",
    "AsyncOrganizations",
    "AsyncTraces",
    "AsyncTracesV2",
    "AsyncWebhooks",
    "Capabilities",
    "Channels",
    "Environments",
    "Events",
    "Moderation",
    "Organizations",
    "Traces",
    "TracesV2",
    "Webhooks",
]
