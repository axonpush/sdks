"""Validates that the integration handlers correctly schedule async publishes
when given an AsyncAxonPush client. The unit tests cover the
``loop.create_task(result)`` branch with respx mocks, but never validate
that the scheduled coroutine actually completes against a real backend.
"""

from __future__ import annotations

import asyncio
import logging
import uuid

import pytest

from axonpush import AsyncAxonPush, EventType
from axonpush.integrations.logging_handler import AxonPushLoggingHandler

pytestmark = pytest.mark.e2e


async def test_logging_handler_with_async_client_round_trip(backend):
    async with AsyncAxonPush(
        api_key=backend.api_key,
        tenant_id=backend.tenant_id,
        base_url=backend.base_url,
    ) as client:
        ch = await client.channels.create(backend.app_id, f"async-int-{uuid.uuid4().hex[:8]}")
        try:
            logger_name = f"e2e.async.{ch.channel_id}"
            logger = logging.getLogger(logger_name)
            logger.handlers.clear()
            logger.setLevel(logging.DEBUG)
            logger.propagate = False
            logger.addHandler(AxonPushLoggingHandler(client=client, channel_id=ch.channel_id))
            try:
                logger.error("async round trip")
                # Poll for up to 2s — gives the create_task'd coroutine
                # time to complete its publish.
                events = []
                for _ in range(20):
                    await asyncio.sleep(0.1)
                    result = await client.events.search(channel_id=ch.channel_id, limit=50)
                    events = result.events if result else []
                    if any((e.payload or {}).get("body") == "async round trip" for e in events):
                        break
                else:
                    pytest.fail(
                        f"async log never reached the backend within 2s; "
                        f"saw events: {[e.payload for e in events]}"
                    )
                matches = [e for e in events if (e.payload or {}).get("body") == "async round trip"]
                assert matches[0].event_type == EventType.APP_LOG
                assert matches[0].payload["severityText"] == "ERROR"
            finally:
                logger.handlers.clear()
        finally:
            try:
                await client.channels.delete(backend.app_id, ch.channel_id)
            except Exception:
                pass
