"""Loguru sink using its native stdlib logging.Handler adapter.

Use ``logger.add(sink, serialize=True)``. The serialized record preserves the
original body, timestamp and thread even when Loguru uses an enqueue worker.
"""

from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING, Any, Dict, Literal, Optional

try:
    import loguru  # noqa: F401
except ImportError:
    raise ImportError(
        "Loguru integration requires the 'loguru' extra. Install it with: pip install axonpush[loguru]"
    ) from None

from axonpush.integrations.logging_handler import AxonPushLoggingHandler
from axonpush.integrations._otel_payload import severity_from_text
from axonpush.integrations._publisher import (
    DEFAULT_QUEUE_SIZE,
    DEFAULT_SHUTDOWN_TIMEOUT_S,
    flush_after_invocation,
)

if TYPE_CHECKING:
    from axonpush.client import AsyncAxonPush, AxonPush

__all__ = ["create_axonpush_loguru_sink", "flush_after_invocation"]
_internal_logger = logging.getLogger("axonpush")


class _AxonPushLoguruSink(AxonPushLoggingHandler):
    """Native handler sink; publishing, capture and lifecycle use the stdlib integration."""

    _framework = "loguru"

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        # Historically this integration sets environment on the resource only.
        self._environment = None

    @staticmethod
    def _severity(record: logging.LogRecord) -> tuple[int, str]:
        return severity_from_text(record.levelname)

    def _record_attributes(self, record: logging.LogRecord) -> Dict[str, Any]:
        attributes = super()._record_attributes(record)
        attributes["code.filename"] = record.filename
        extra = attributes.pop("extra", None)
        if isinstance(extra, dict):
            attributes.update(extra)
        return attributes

    @staticmethod
    def _serialized_record(message: str) -> Dict[str, Any] | None:
        try:
            envelope = json.loads(message)
        except (ValueError, TypeError):
            return None
        if not isinstance(envelope, dict) or not isinstance(envelope.get("text"), str):
            return None
        raw = envelope.get("record")
        if not isinstance(raw, dict) or not isinstance(raw.get("message"), str):
            return None
        if not all(
            isinstance(raw.get(key), dict)
            for key in ("time", "level", "file", "thread", "process", "extra")
        ):
            return None
        if not isinstance(raw["time"].get("timestamp"), (int, float)) or not isinstance(
            raw["level"].get("name"), str
        ):
            return None
        return raw

    def emit(self, record: logging.LogRecord) -> None:
        try:
            serialized = self._serialized_record(record.getMessage())
            if serialized is None:
                _internal_logger.warning(
                    "AxonPush loguru sink requires logger.add(sink, serialize=True)"
                )
                return
            # The library owns LogRecord/exception conversion. Restore the
            # unformatted body and origin fields lost by its enqueue adapter.
            record = logging.makeLogRecord(record.__dict__.copy())
            record.msg, record.args = serialized["message"], ()
            record.created = serialized["time"]["timestamp"]
            record.threadName = serialized["thread"].get("name", record.threadName)
            record.process = serialized["process"].get("id", record.process)
            super().emit(record)
        except Exception:
            self.handleError(record)

    def handleError(self, record: logging.LogRecord) -> None:
        _internal_logger.warning("AxonPush loguru sink failed", exc_info=True)

    def __call__(self, message: Any) -> None:
        """Compatibility for direct invocation with a serialized record."""
        try:
            serialized = self._serialized_record(str(message))
            if serialized is None:
                _internal_logger.warning("AxonPush loguru sink expected a serialized record")
                return
            level = serialized.get("level", {})
            file = serialized.get("file", {})
            record = logging.makeLogRecord(
                {
                    "name": serialized.get("name", "loguru"),
                    "msg": str(message),
                    "args": (),
                    "levelname": level.get("name", "INFO"),
                    "levelno": level.get("no", logging.INFO),
                    "pathname": file.get("path", ""),
                    "filename": file.get("name", ""),
                    "funcName": serialized.get("function"),
                    "lineno": serialized.get("line", 0),
                    "module": serialized.get("module"),
                    "extra": serialized.get("extra", {}),
                }
            )
            exception = serialized.get("exception")
            if isinstance(exception, dict):
                record.__dict__["extra"] = {
                    **record.__dict__["extra"],
                    "exception.type": exception.get("type"),
                    "exception.message": exception.get("value"),
                }
            self.handle(record)
        except Exception:
            _internal_logger.warning("AxonPush loguru sink failed", exc_info=True)


def create_axonpush_loguru_sink(
    *,
    client: "AxonPush | AsyncAxonPush",
    channel_id: int | str,
    source: str = "app",
    service_name: Optional[str] = None,
    service_version: Optional[str] = None,
    environment: Optional[str] = None,
    agent_id: Optional[str] = None,
    mode: Optional[Literal["background", "sync"]] = None,
    queue_size: int = DEFAULT_QUEUE_SIZE,
    shutdown_timeout: float = DEFAULT_SHUTDOWN_TIMEOUT_S,
) -> _AxonPushLoguruSink:
    """Build a Loguru sink that forwards each record to AxonPush.

    Use ``logger.add(sink, serialize=True)`` as before. Serialization preserves
    the original body and enqueue origin; formatted traceback text is never
    captured as the message. ``logger.remove()`` closes the handler and drains
    its publisher. The supplied client remains caller-owned.
    """
    return _AxonPushLoguruSink(
        client=client,
        channel_id=channel_id,
        source=source,
        service_name=service_name,
        service_version=service_version,
        environment=environment,
        agent_id=agent_id,
        mode=mode,
        queue_size=queue_size,
        shutdown_timeout=shutdown_timeout,
    )
