"""Task identity follows async flows without sharing state between requests."""
from contextvars import ContextVar

current_task: ContextVar[tuple[str, str | None] | None] = ContextVar("axonpush_task", default=None)


def task_metadata() -> dict[str, str]:
    task = current_task.get()
    if task is None:
        return {}
    result = {"axonpush.task_id": task[0]}
    if task[1]:
        result["axonpush.parent_task_id"] = task[1]
    return result
