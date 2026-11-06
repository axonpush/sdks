"""Verify source locations survive the actual adapter's wire payload."""

import logging
import sys
import traceback

import pytest

from axonpush.integrations._exceptions import (
    MAX_EXCEPTION_MESSAGE_CHARS,
    MAX_EXCEPTION_STACK_CHARS,
    exc_info_attributes,
    exception_attributes,
)
from axonpush.integrations.logging_handler import AxonPushLoggingHandler


def failed_operation():
    private_local = "local-value-must-not-be-captured"
    assert private_local
    raise ValueError("diagnostic failure")


def test_logging_exception_sends_traceback_source_location(fake_sync_client):
    handler = AxonPushLoggingHandler(client=fake_sync_client, channel_id="test", mode="sync")
    try:
        failed_operation()
    except ValueError:
        exc_info = sys.exc_info()
        line = traceback.extract_tb(exc_info[2])[-1].lineno
        record = logging.LogRecord(
            "test", logging.ERROR, __file__, 1, "operation failed", (), exc_info
        )
        handler.handle(record)
    finally:
        handler.close()
    payload = fake_sync_client.events.calls[0]["payload"]
    assert payload["body"] == "operation failed"
    attrs = payload["attributes"]
    assert attrs["exception.type"] == "ValueError"
    assert attrs["exception.message"] == "diagnostic failure"
    assert f"line {line}, in failed_operation" in attrs["exception.stacktrace"]
    assert __file__ in attrs["exception.stacktrace"]
    assert "local-value-must-not-be-captured" not in attrs["exception.stacktrace"]


def test_exception_chain_keeps_cause_locations_without_inventing_a_stack():
    assert "exception.stacktrace" not in exception_attributes(ValueError("not raised"))
    try:
        try:
            failed_operation()
        except ValueError as cause:
            raise RuntimeError("wrapper") from cause
    except RuntimeError as error:
        attrs = exception_attributes(error)
    assert attrs["exception.type"] == "RuntimeError"
    assert "ValueError: diagnostic failure" in attrs["exception.stacktrace"]
    assert "RuntimeError: wrapper" in attrs["exception.stacktrace"]
    assert "in failed_operation" in attrs["exception.stacktrace"]


def test_structlog_serializes_exc_info_and_preserves_downstream_record(fake_sync_client):
    pytest.importorskip("structlog")
    from axonpush.integrations.structlog import axonpush_structlog_processor

    processor = axonpush_structlog_processor(
        client=fake_sync_client, channel_id="test", mode="sync"
    )
    try:
        failed_operation()
    except ValueError:
        record = {"event": "operation failed", "exc_info": sys.exc_info()}
        assert processor(None, "error", record) is record
        assert record["exc_info"][2] is not None
    finally:
        processor.close()
    attrs = fake_sync_client.events.calls[0]["payload"]["attributes"]
    assert "exc_info" not in attrs
    assert "in failed_operation" in attrs["exception.stacktrace"]


def test_preformatted_exception_text_is_not_dropped(fake_sync_client):
    handler = AxonPushLoggingHandler(client=fake_sync_client, channel_id="test", mode="sync")
    record = logging.LogRecord("test", logging.ERROR, __file__, 1, "operation failed", (), None)
    record.exc_text = (
        'Traceback (most recent call last):\n  File "app.py", line 42, in run\nValueError: invalid'
    )
    handler.handle(record)
    handler.close()
    assert (
        fake_sync_client.events.calls[0]["payload"]["attributes"]["exception.stacktrace"]
        == record.exc_text
    )


def test_framework_callback_keeps_the_actual_failure_traceback(fake_sync_client):
    pytest.importorskip("langchain_core")
    from uuid import uuid4
    from axonpush.integrations.langchain import AxonPushCallbackHandler

    handler = AxonPushCallbackHandler(client=fake_sync_client, channel_id="test", mode="sync")
    try:
        failed_operation()
    except ValueError as error:
        handler.on_chain_error(error, run_id=uuid4())
    attrs = fake_sync_client.events.calls[0]["payload"]["attributes"]
    assert attrs["exception.type"] == "ValueError"
    assert "in failed_operation" in attrs["exception.stacktrace"]


def test_explicit_none_traceback_does_not_revive_the_exception_traceback():
    try:
        failed_operation()
    except ValueError as error:
        assert "exception.stacktrace" in exception_attributes(error)
        assert "exception.stacktrace" not in exception_attributes(error, None)
        assert "exception.stacktrace" not in exc_info_attributes((type(error), error, None))


def test_explicit_none_preserves_stdlib_cause_semantics():
    try:
        try:
            failed_operation()
        except ValueError as cause:
            raise RuntimeError("wrapper") from cause
    except RuntimeError as error:
        expected = "".join(traceback.format_exception(type(error), error, None))
        actual = exception_attributes(error, None)["exception.stacktrace"]
    assert actual == expected
    assert "in failed_operation" in actual


def test_exception_messages_and_preformatted_stacks_are_bounded(fake_sync_client):
    try:
        raise ValueError("x" * (2 * 1024 * 1024))
    except ValueError as error:
        attrs = exception_attributes(error)
    assert len(attrs["exception.message"]) <= MAX_EXCEPTION_MESSAGE_CHARS
    assert len(attrs["exception.stacktrace"]) <= MAX_EXCEPTION_STACK_CHARS
    assert "truncated" in attrs["exception.stacktrace"]
    assert (
        "test_exception_messages_and_preformatted_stacks_are_bounded"
        in attrs["exception.stacktrace"]
    )

    record = logging.LogRecord("test", logging.ERROR, __file__, 1, "original body", (), None)
    record.exc_text = "x" * (2 * 1024 * 1024) + "\nValueError: fixture"
    handler = AxonPushLoggingHandler(client=fake_sync_client, channel_id="test", mode="sync")
    handler.handle(record)
    handler.close()
    payload = fake_sync_client.events.calls[0]["payload"]
    assert payload["body"] == "original body"
    assert len(payload["attributes"]["exception.stacktrace"]) <= MAX_EXCEPTION_STACK_CHARS
    assert len(record.exc_text) > MAX_EXCEPTION_STACK_CHARS


def test_structlog_bounds_duplicate_formatted_stack_without_mutating_record(fake_sync_client):
    pytest.importorskip("structlog")
    from axonpush.integrations.structlog import axonpush_structlog_processor

    formatted = "x" * (2 * 1024 * 1024) + "\nValueError: fixture"
    record = {"event": "original body", "exception": formatted}
    processor = axonpush_structlog_processor(
        client=fake_sync_client, channel_id="test", mode="sync"
    )
    try:
        assert processor(None, "error", record) is record
    finally:
        processor.close()
    payload = fake_sync_client.events.calls[0]["payload"]
    assert payload["body"] == "original body"
    assert len(payload["attributes"]["exception"]) <= MAX_EXCEPTION_STACK_CHARS
    assert len(payload["attributes"]["exception.stacktrace"]) <= MAX_EXCEPTION_STACK_CHARS
    assert record["exception"] == formatted
