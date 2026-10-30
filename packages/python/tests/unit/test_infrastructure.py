import asyncio
import threading
from types import SimpleNamespace

import pytest
from pydantic import ValidationError
from axonpush._config import Settings
from axonpush.exceptions import _parse_retry_after, APIConnectionError
from axonpush._internal.transport import call_with_retries_async
from axonpush.integrations._publisher import BackgroundPublisher


def test_settings_bounds():
    for value in (-1, -2):
        with pytest.raises(ValidationError):
            Settings(max_retries=value)
    for value in (0, float("inf"), float("nan")):
        with pytest.raises(ValidationError):
            Settings(timeout=value)


def test_retry_after_http_date_and_nonfinite():
    assert _parse_retry_after("Wed, 21 Oct 2099 07:28:00 GMT") > 0
    assert _parse_retry_after("inf") is None
    assert _parse_retry_after("nan") is None
    assert _parse_retry_after("-1") is None


@pytest.mark.asyncio
async def test_total_deadline_and_caller_cancellation():
    async def pending(**kwargs):
        await asyncio.sleep(60)

    operation = SimpleNamespace(asyncio_detailed=pending)
    with pytest.raises(APIConnectionError, match="timed out"):
        await call_with_retries_async(operation, max_retries=3, timeout=0.01)
    task = asyncio.create_task(call_with_retries_async(operation, max_retries=3))
    await asyncio.sleep(0)
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task


def test_full_queue_shutdown_eventually_stops_worker():
    started, release = threading.Event(), threading.Event()

    def publish(**kwargs):
        started.set()
        release.wait(2)

    publisher = BackgroundPublisher(
        SimpleNamespace(events=SimpleNamespace(publish=publish)), queue_size=1
    )
    try:
        publisher.submit({"identifier": "first"})
        assert started.wait(1)
        publisher.submit({"identifier": "second"})
        worker = publisher._thread
        publisher.close(timeout=0)
        assert publisher._thread is worker
        assert publisher.dropped == 1
        release.set()
        worker.join(1)
        assert not worker.is_alive()
    finally:
        release.set()
        publisher.close(timeout=0.1)


def test_non_idempotent_creation_is_not_retried():
    import httpx
    from axonpush._internal.transport import call_with_retries_sync, _inject_request_headers
    from axonpush.exceptions import APIConnectionError

    calls = []

    def operation(**kwargs):
        calls.append(1)
        _inject_request_headers(
            httpx.Request("POST", "https://example.invalid/apps", json={"name": "synthetic"})
        )
        raise APIConnectionError("synthetic lost response")

    with pytest.raises(APIConnectionError):
        call_with_retries_sync(SimpleNamespace(sync_detailed=operation), max_retries=3)
    assert len(calls) == 1
