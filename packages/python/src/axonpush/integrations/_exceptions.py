"""Standard exception attributes shared by framework and logging adapters."""

from __future__ import annotations

import sys
import traceback
from types import TracebackType
from typing import Any

MAX_EXCEPTION_STACK_CHARS = 32 * 1024
MAX_EXCEPTION_MESSAGE_CHARS = 4096
_MAX_EXCEPTION_TYPE_CHARS = 256
_MAX_EXCEPTION_FRAMES = 64
_TRUNCATED = "…[truncated]"
_STACK_TRUNCATED = "[axonpush diagnostics truncated]\n"


class _UseExceptionTraceback:
    pass


_USE_EXCEPTION_TRACEBACK = _UseExceptionTraceback()


def _bounded_text(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - len(_TRUNCATED)] + _TRUNCATED


def bounded_stack(value: str) -> str:
    """Keep the latest Python failure, with an explicit earlier-content marker."""
    if len(value) <= MAX_EXCEPTION_STACK_CHARS:
        return value
    return _STACK_TRUNCATED + value[-(MAX_EXCEPTION_STACK_CHARS - len(_STACK_TRUNCATED)) :]


def bound_exception_attributes(attributes: dict[str, Any]) -> dict[str, Any]:
    """Bound standard diagnostics on an adapter-owned dictionary, not its input."""
    for key, limit in (
        ("exception.type", _MAX_EXCEPTION_TYPE_CHARS),
        ("exception.message", MAX_EXCEPTION_MESSAGE_CHARS),
    ):
        value = attributes.get(key)
        if isinstance(value, str):
            attributes[key] = _bounded_text(value, limit)
    stack = attributes.get("exception.stacktrace")
    if isinstance(stack, str):
        attributes["exception.stacktrace"] = bounded_stack(stack)
    return attributes


def _formatted_stack(error: BaseException, tb: TracebackType | None) -> str:
    # Stream stdlib formatting instead of joining an unbounded formatted list.
    # Negative limit retains the crashing frames, and capture_locals stays off.
    formatted = traceback.TracebackException(
        type(error),
        error,
        tb,
        limit=-_MAX_EXCEPTION_FRAMES,
        lookup_lines=False,
        capture_locals=False,
        compact=True,
    )
    tail = ""
    total = 0
    for part in formatted.format(chain=True):
        total += len(part)
        # A single huge exception message/source excerpt must not evict every
        # useful file:line frame from the bounded tail.
        part = _bounded_text(part, MAX_EXCEPTION_MESSAGE_CHARS + _MAX_EXCEPTION_TYPE_CHARS + 512)
        if len(part) >= MAX_EXCEPTION_STACK_CHARS:
            tail = part[-MAX_EXCEPTION_STACK_CHARS:]
        else:
            tail = (tail + part)[-MAX_EXCEPTION_STACK_CHARS:]
    if total > MAX_EXCEPTION_STACK_CHARS:
        return _STACK_TRUNCATED + tail[-(MAX_EXCEPTION_STACK_CHARS - len(_STACK_TRUNCATED)) :]
    return tail


def exception_attributes(
    error: BaseException,
    tb: TracebackType | None | _UseExceptionTraceback = _USE_EXCEPTION_TRACEBACK,
) -> dict[str, Any]:
    attributes: dict[str, Any] = {
        "exception.type": _bounded_text(type(error).__name__, _MAX_EXCEPTION_TYPE_CHARS),
    }
    try:
        attributes["exception.message"] = _bounded_text(str(error), MAX_EXCEPTION_MESSAGE_CHARS)
    except Exception:
        pass  # A custom exception formatter must not break the caller's logger.
    try:
        captured = error.__traceback__ if isinstance(tb, _UseExceptionTraceback) else tb
        if captured is not None or error.__cause__ is not None or error.__context__ is not None:
            # Only strings enter the queue, never the exception/traceback/locals.
            attributes["exception.stacktrace"] = _formatted_stack(error, captured)
    except Exception:
        pass
    return attributes


def exc_info_attributes(value: Any) -> dict[str, Any]:
    if value is True:
        value = sys.exc_info()
    if isinstance(value, BaseException):
        return exception_attributes(value)
    if isinstance(value, tuple) and len(value) == 3 and isinstance(value[1], BaseException):
        return exception_attributes(value[1], value[2])
    return {}


def exception_payload(error: BaseException) -> dict[str, Any]:
    """Keep legacy framework fields and standard attributes within one budget."""
    attributes = exception_attributes(error)
    return {
        "error": attributes.get("exception.message", ""),
        "error_type": attributes.get("exception.type", ""),
        "attributes": attributes,
    }
