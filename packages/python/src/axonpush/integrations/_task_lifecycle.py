"""Opt-in root boundaries. Run names and successful child calls are never goals."""

from __future__ import annotations

from collections.abc import Callable, Iterator
from contextlib import contextmanager
from threading import RLock
from typing import Any
from uuid import uuid4

from axonpush._evidence_context import current_task

DeclaredTaskGoal = str | Callable[[dict[str, Any]], str | None]
TaskBoundary = tuple[str, dict[str, Any], dict[str, Any]]
_MAXIMUM_RUNS = 10_000


def _identity(task: tuple[str, str | None, str]) -> dict[str, Any]:
    return {
        "axonpush.task_id": task[0],
        **({"axonpush.parent_task_id": task[1]} if task[1] else {}),
    }


def _boundary(task: tuple[str, str | None, str], kind: str, **payload: Any) -> TaskBoundary:
    return (
        kind,
        payload,
        {
            **_identity(task),
            "axonpush.evidence.version": 1,
            "axonpush.evidence.kind": kind,
            "axonpush.evidence.origin": "sdk_reported",
        },
    )


class FrameworkTaskLifecycle:
    """Thread-safe, bounded callback mappings, removed when the root completes."""

    def __init__(self, goal: DeclaredTaskGoal | None, framework: str) -> None:
        self._goal, self._framework = goal, framework
        self._runs: dict[str, tuple[str, str | None, str]] = {}
        self._members: dict[str, set[str]] = {}
        self._completed: dict[str, None] = {}
        self._lock = RLock()

    def clear(self) -> None:
        with self._lock:
            self._runs.clear()
            self._members.clear()
            self._completed.clear()

    def start(self, run_id: str, parent_run_id: str | None, **context: Any) -> TaskBoundary | None:
        if self._goal is None:
            return None
        with self._lock:
            if parent_run_id:
                self.metadata(run_id, parent_run_id)
                return None
            if (
                run_id in self._runs
                or run_id in self._completed
                or len(self._runs) >= _MAXIMUM_RUNS
            ):
                return None
            try:
                goal = (
                    self._goal({**context, "framework": self._framework, "run_id": run_id})
                    if callable(self._goal)
                    else self._goal
                )
            except Exception:
                return None
            if not isinstance(goal, str) or not goal.strip() or len(goal) > 32_000:
                return None
            parent = current_task.get()
            task = (str(uuid4()), parent[0] if parent else None, run_id)
            self._runs[run_id] = task
            self._members[run_id] = {run_id}
            return _boundary(task, "agent.task.start", goal=goal)

    def metadata(self, run_id: str | None, parent_run_id: str | None = None) -> dict[str, Any]:
        with self._lock:
            task = self._runs.get(run_id) if run_id else None
            if task is None and parent_run_id:
                task = self._runs.get(parent_run_id)
                if task and run_id and len(self._runs) < _MAXIMUM_RUNS:
                    self._runs[run_id] = task
                    self._members[task[2]].add(run_id)
            return _identity(task) if task else {}

    def finish(self, run_id: str, outcome: str) -> TaskBoundary | None:
        with self._lock:
            task = self._runs.get(run_id)
            if task is None or task[2] != run_id:
                return None
            for key in self._members.pop(run_id):
                self._runs.pop(key, None)
            self._completed[run_id] = None
            if len(self._completed) > _MAXIMUM_RUNS:
                self._completed.pop(next(iter(self._completed)))
            return _boundary(task, "agent.task.end", outcome=outcome)


@contextmanager
def declared_task(goal: str, emit: Callable[[TaskBoundary], None]) -> Iterator[str]:
    """Wrap the complete runner call when its hooks lack a root failure callback."""
    if not isinstance(goal, str) or not goal.strip() or len(goal) > 32_000:
        raise ValueError("A declared task requires a nonempty goal up to 32000 characters")
    parent = current_task.get()
    task = (str(uuid4()), parent[0] if parent else None, "scope")
    token = current_task.set((task[0], task[1]))
    try:
        emit(_boundary(task, "agent.task.start", goal=goal))
        try:
            yield task[0]
        except BaseException:
            emit(_boundary(task, "agent.task.end", outcome="failed"))
            raise
        else:
            emit(_boundary(task, "agent.task.end", outcome="succeeded"))
    finally:
        current_task.reset(token)
