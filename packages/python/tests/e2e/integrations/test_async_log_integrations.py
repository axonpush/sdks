"""Validates that the integration handlers correctly schedule async publishes
when given an AsyncAxonPush client. The unit tests cover the
``loop.create_task(result)`` branch with respx mocks, but never validate
that the scheduled coroutine actually completes against a real backend.
"""

from __future__ import annotations

import logging
import uuid

import pytest

from axonpush import AsyncAxonPush, EventType
from axonpush.integrations.logging_handler import AxonPushLoggingHandler
from tests.e2e._evidence import read_events_async

pytestmark = pytest.mark.e2e


async def test_logging_handler_with_async_client_round_trip(backend):
    async with AsyncAxonPush(
        api_key=backend.api_key,
        tenant_id=backend.tenant_id,
        base_url=backend.base_url,
        environment=backend.environment,
        fail_open=False,
    ) as client:
        ch = await client.channels.create(backend.app_id, f"async-int-{uuid.uuid4().hex[:8]}")
        try:
            logger_name = f"e2e.async.{ch.channel_id}"
            logger = logging.getLogger(logger_name)
            logger.handlers.clear()
            logger.setLevel(logging.DEBUG)
            logger.propagate = False
            handler = AxonPushLoggingHandler(client=client, channel_id=ch.channel_id)
            logger.addHandler(handler)
            try:
                logger.error("async round trip")
                events = await read_events_async(client, ch.channel_id)
                matches = [e for e in events if (e.payload or {}).get("body") == "async round trip"]
                assert matches[0].event_type == EventType.APP_LOG
                assert matches[0].payload["severityText"] == "ERROR"
            finally:
                logger.removeHandler(handler)
                handler.close()
        finally:
            await client.channels.delete(backend.app_id, ch.channel_id)
