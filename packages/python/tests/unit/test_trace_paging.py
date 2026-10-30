from unittest.mock import AsyncMock, Mock

import pytest

from axonpush.resources.traces import AsyncTraces, Traces


def test_trace_get_forwards_page_options_without_prefetch():
    client = Mock()
    client._invoke.return_value = None
    Traces(client).get("trace", limit=100, cursor="cursor")
    client._invoke.assert_called_once()
    assert client._invoke.call_args.kwargs == {
        "trace_id": "trace",
        "limit": 100,
        "cursor": "cursor",
    }


@pytest.mark.asyncio
async def test_async_trace_get_forwards_page_options_without_prefetch():
    client = Mock()
    client._invoke = AsyncMock(return_value=None)
    await AsyncTraces(client).get("trace", limit=100, cursor="cursor")
    client._invoke.assert_awaited_once()
    assert client._invoke.call_args.kwargs == {
        "trace_id": "trace",
        "limit": 100,
        "cursor": "cursor",
    }
