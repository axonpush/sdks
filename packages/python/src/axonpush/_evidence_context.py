"""Task identity follows async flows without sharing state between requests."""

from contextvars import ContextVar
from typing import Any

current_task: ContextVar[tuple[str, str | None] | None] = ContextVar("axonpush_task", default=None)


def task_metadata() -> dict[str, str]:
    task = current_task.get()
    if task is None:
        return {}
    result = {"axonpush.task_id": task[0]}
    if task[1]:
        result["axonpush.parent_task_id"] = task[1]
    return result


def capture_task(params: dict[str, Any]) -> dict[str, Any]:
    """Snapshot identity before a thread, background task or Redis handoff."""
    metadata = task_metadata()
    if not metadata:
        return params
    return {**params, "metadata": {**metadata, **(params.get("metadata") or {})}}
