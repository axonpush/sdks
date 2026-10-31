"""Unit tests for the Loguru sink."""

from __future__ import annotations

from typing import Iterator

import pytest

pytest.importorskip("loguru")

from loguru import logger as loguru_logger  # noqa: E402

from axonpush.integrations.loguru import create_axonpush_loguru_sink  # noqa: E402

from .conftest import FakeSyncClient  # noqa: E402


@pytest.fixture(autouse=True)
def _reset_loguru() -> Iterator[None]:
    loguru_logger.remove()
    yield
    loguru_logger.remove()


class TestLoguruSink:
    def test_emits_app_log_event(self, fake_sync_client: FakeSyncClient) -> None:
        sink = create_axonpush_loguru_sink(
            client=fake_sync_client,
            channel_id="ch_x",
            service_name="myapp",
            mode="sync",
        )
        loguru_logger.add(sink, serialize=True)
        loguru_logger.error("connection refused")
        assert len(fake_sync_client.events.calls) == 1
        call = fake_sync_client.events.calls[0]
        assert call["channel_id"] == "ch_x"
        assert call["event_type"].value == "app.log"
        assert call["payload"]["body"] == "connection refused"
        assert call["payload"]["severityText"] == "ERROR"
        assert call["metadata"]["framework"] == "loguru"

    def test_extra_kwargs_become_attributes(self, fake_sync_client: FakeSyncClient) -> None:
        sink = create_axonpush_loguru_sink(client=fake_sync_client, channel_id="ch_x", mode="sync")
        loguru_logger.add(sink, serialize=True)
        loguru_logger.bind(user_id=42).info("hi")
        attrs = fake_sync_client.events.calls[0]["payload"]["attributes"]
        assert attrs.get("user_id") == 42

    def test_agent_log_source(self, fake_sync_client: FakeSyncClient) -> None:
        sink = create_axonpush_loguru_sink(
            client=fake_sync_client,
            channel_id="ch_x",
            source="agent",
            mode="sync",
        )
        loguru_logger.add(sink, serialize=True)
        loguru_logger.info("a")
        assert fake_sync_client.events.calls[0]["event_type"].value == "agent.log"

    def test_invalid_source_rejected(self, fake_sync_client: FakeSyncClient) -> None:
        with pytest.raises(ValueError, match="source must be"):
            create_axonpush_loguru_sink(
                client=fake_sync_client,
                channel_id="ch_x",
                source="bogus",
                mode="sync",
            )

    def test_invalid_mode_rejected(self, fake_sync_client: FakeSyncClient) -> None:
        with pytest.raises(ValueError, match="mode must be"):
            create_axonpush_loguru_sink(
                client=fake_sync_client,
                channel_id="ch_x",
                mode="bogus",  # type: ignore[arg-type]
            )

    def test_int_channel_id_emits_deprecation(self, fake_sync_client: FakeSyncClient) -> None:
        with pytest.warns(DeprecationWarning):
            sink = create_axonpush_loguru_sink(client=fake_sync_client, channel_id=42, mode="sync")
        loguru_logger.add(sink, serialize=True)
        loguru_logger.info("x")
        assert fake_sync_client.events.calls[0]["channel_id"] == "42"

    def test_publish_exception_swallowed(self, fake_sync_client: FakeSyncClient) -> None:
        fake_sync_client.events.exception = RuntimeError("nope")
        sink = create_axonpush_loguru_sink(client=fake_sync_client, channel_id="ch_x", mode="sync")
        loguru_logger.add(sink, serialize=True)
        loguru_logger.error("survives")

    def test_reentrancy_guard_drops_records(self, fake_sync_client: FakeSyncClient) -> None:
        from axonpush.integrations import _publisher as p

        sink = create_axonpush_loguru_sink(client=fake_sync_client, channel_id="ch_x", mode="sync")
        loguru_logger.add(sink, serialize=True)
        token = p._in_publisher_path.set(True)
        try:
            loguru_logger.info("inside")
        finally:
            p._in_publisher_path.reset(token)
        assert fake_sync_client.events.calls == []


def test_native_handler_preserves_message_context_and_custom_severity(fake_sync_client):
    sink = create_axonpush_loguru_sink(
        client=fake_sync_client, channel_id="ch_x", environment="staging", mode="sync"
    )
    handler_id = loguru_logger.add(sink, format="{message}", serialize=True, level=0)
    with loguru_logger.contextualize(request_id="request-1"):
        loguru_logger.bind(user_id=42, msg="attribute-not-body").trace("native body")
    try:
        loguru_logger.level("AXON_NOTICE_TEST")
    except ValueError:
        loguru_logger.level("AXON_NOTICE_TEST", no=35)
    loguru_logger.log("AXON_NOTICE_TEST", "custom body")
    loguru_logger.remove(handler_id)
    first, custom = fake_sync_client.events.calls
    assert first["payload"]["body"] == "native body"
    assert first["payload"]["severityNumber"] == 1
    assert first["payload"]["attributes"]["user_id"] == 42
    assert first["payload"]["attributes"]["request_id"] == "request-1"
    assert first["payload"]["attributes"]["msg"] == "attribute-not-body"
    assert first["payload"]["resource"]["deployment.environment"] == "staging"
    assert "environment" not in first  # Preserve the integration's resource-only environment.
    assert custom["payload"]["severityNumber"] == 9  # Unknown names retain the INFO fallback.
    assert first["metadata"] == {"framework": "loguru"}


def test_loguru_remove_drains_publisher_and_keeps_client_owned_by_caller(fake_sync_client):
    sink = create_axonpush_loguru_sink(client=fake_sync_client, channel_id="ch_x")
    publisher = sink._publisher
    assert publisher is not None
    handler_id = loguru_logger.add(sink, serialize=True)
    for index in range(12):
        loguru_logger.info("record {}", index)
    loguru_logger.remove(handler_id)
    assert len(fake_sync_client.events.calls) == 12
    assert sink._publisher is None
    sink.close()  # Handler lifecycle remains idempotent.


def test_loguru_native_adapter_preserves_exception_traceback(fake_sync_client, monkeypatch):
    sink = create_axonpush_loguru_sink(client=fake_sync_client, channel_id="ch_x", mode="sync")
    records = []
    original = sink.handle

    def capture(record):
        records.append(record)
        return original(record)

    monkeypatch.setattr(sink, "handle", capture)
    handler_id = loguru_logger.add(sink, format="{message}", serialize=True)
    try:
        raise ValueError("synthetic failure")
    except ValueError:
        loguru_logger.exception("operation failed")
    loguru_logger.remove(handler_id)
    assert records[0].exc_info[2] is not None
    assert fake_sync_client.events.calls[0]["payload"]["body"] == "operation failed"
    attrs = fake_sync_client.events.calls[0]["payload"]["attributes"]
    assert attrs["exception.type"] == "ValueError"
    assert attrs["exception.message"] == "synthetic failure"


def test_enqueue_keeps_origin_time_thread_and_json_body(fake_sync_client):
    import json
    import threading
    import time

    sink = create_axonpush_loguru_sink(client=fake_sync_client, channel_id="ch_x", mode="sync")
    handler_id = loguru_logger.add(sink, serialize=True, enqueue=True)
    body = json.dumps({"record": {"message": "ordinary JSON, not an envelope"}})
    before = time.time_ns()
    loguru_logger.info(body)
    after = time.time_ns()
    loguru_logger.remove(handler_id)
    payload = fake_sync_client.events.calls[0]["payload"]
    assert payload["body"] == body
    assert payload["attributes"]["thread.name"] == threading.current_thread().name
    # Loguru represents timestamps as floats; allow microsecond rounding.
    assert before - 1000 <= int(payload["timeUnixNano"]) <= after + 1000


@pytest.mark.parametrize(
    "message", ["not-json", '{"record":null}', '{"text":"x","record":{"message":"x","time":null}}']
)
def test_malformed_direct_input_cannot_escape_sink(fake_sync_client, message):
    sink = create_axonpush_loguru_sink(client=fake_sync_client, channel_id="ch_x", mode="sync")
    sink(message)
    assert fake_sync_client.events.calls == []
    sink.close()


def test_plain_native_messages_are_rejected_instead_of_capturing_diagnostic_text(fake_sync_client):
    sink = create_axonpush_loguru_sink(client=fake_sync_client, channel_id="ch_x", mode="sync")
    handler_id = loguru_logger.add(sink, format="{message}", serialize=False)
    loguru_logger.info('{"record":{"message":"user content"}}')
    loguru_logger.remove(handler_id)
    assert fake_sync_client.events.calls == []
