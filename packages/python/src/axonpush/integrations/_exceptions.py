"""Standard exception attributes shared by framework and logging adapters."""

from __future__ import annotations

import sys
import traceback
from types import TracebackType
from typing import Any, Optional


def exception_attributes(
    error: BaseException, tb: Optional[TracebackType] = None
) -> dict[str, Any]:
    attributes: dict[str, Any] = {
        "exception.type": type(error).__name__,
        "exception.message": str(error),
    }
    captured = tb if tb is not None else error.__traceback__
    if captured is not None or error.__cause__ is not None or error.__context__ is not None:
        # Preserve chained exceptions and source locations without capturing
        # locals or retaining traceback objects in the publisher queue.
        attributes["exception.stacktrace"] = "".join(
            traceback.format_exception(type(error), error, captured)
        )
    return attributes


def exc_info_attributes(value: Any) -> dict[str, Any]:
    if value is True:
        value = sys.exc_info()
    if isinstance(value, BaseException):
        return exception_attributes(value)
    if isinstance(value, tuple) and len(value) == 3 and isinstance(value[1], BaseException):
        return exception_attributes(value[1], value[2])
    return {}
