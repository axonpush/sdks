"""Caller discovery never turns an absent or failed response into permission."""

from unittest.mock import AsyncMock, Mock

import pytest

from axonpush._internal.api.models import OperationCapabilities
from axonpush.resources.capabilities import AsyncCapabilities, Capabilities, operation_availability


def snapshot():
    return OperationCapabilities.from_dict(
        {
            "registryRevision": "test",
            "operations": [
                {"operationId": "alerts.list", "availability": "allowed"},
                {"operationId": "alerts.create", "availability": "denied"},
                {"operationId": "events.get", "availability": "conditional"},
            ],
        }
    )


def test_availability_is_explicit_and_missing_is_unknown():
    assert operation_availability(snapshot(), "alerts.list") == "allowed"
    assert operation_availability(snapshot(), "alerts.create") == "denied"
    assert operation_availability(snapshot(), "events.get") == "conditional"
    assert operation_availability(snapshot(), "missing") == "unknown"
    assert operation_availability(None, "alerts.list") == "unknown"


def test_sync_operations_do_not_cache_previous_permissions():
    client = Mock()
    client._invoke.side_effect = [snapshot(), None]
    resource = Capabilities(client)
    assert operation_availability(resource.operations(), "alerts.list") == "allowed"
    assert operation_availability(resource.operations(), "alerts.list") == "unknown"
    assert client._invoke.call_count == 2
    operation = client._invoke.call_args.args[0]
    assert operation._get_kwargs()["url"] == "/capabilities/operations"


@pytest.mark.asyncio
async def test_async_operations_do_not_cache_previous_permissions():
    client = Mock()
    client._invoke = AsyncMock(side_effect=[snapshot(), None])
    resource = AsyncCapabilities(client)
    assert operation_availability(await resource.operations(), "alerts.list") == "allowed"
    assert operation_availability(await resource.operations(), "alerts.list") == "unknown"
    assert client._invoke.await_count == 2
