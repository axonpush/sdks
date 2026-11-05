"""CrewAI integration for AxonPush.

Provides a step-callback bag (:class:`AxonPushCrewCallbacks`) that you
attach to a Crew's task / agent ``step_callback``. CrewAI's hook surface
between 0.50 and 0.90 has stayed largely stable: a single callable that
receives a step output object exposing ``agent``, ``tool``, ``tool_input``,
``result``, ``thought``. We code against attribute access only, so any
0.50+ release that exposes those names works.

Tested against ``crewai>=0.50.0,<2.0`` (Python >=3.11).

Install::

    pip install axonpush[crewai]
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from contextlib import AbstractContextManager
from threading import RLock
from typing import TYPE_CHECKING, Any, Dict, Literal, Optional

from axonpush._evidence_context import task_metadata
from axonpush._tracing import get_or_create_trace
from axonpush.integrations._publisher import (
    BackgroundPublisher,
    DEFAULT_QUEUE_SIZE,
    DEFAULT_SHUTDOWN_TIMEOUT_S,
)
from axonpush.integrations._utils import coerce_channel_id
from axonpush.models import EventType
from axonpush.integrations._task_lifecycle import (
    DeclaredTaskGoal,
    FrameworkTaskLifecycle,
    TaskBoundary,
    declared_task,
)

if TYPE_CHECKING:
    from axonpush.client import AxonPush

logger = logging.getLogger("axonpush")


class AxonPushCrewCallbacks:
    """A bundle of step / task / crew callbacks for CrewAI."""

    def __init__(
        self,
        client: "AxonPush",
        channel_id: int | str,
        *,
        agent_id: str = "crewai",
        trace_id: Optional[str] = None,
        mode: Optional[Literal["background", "sync"]] = None,
        queue_size: int = DEFAULT_QUEUE_SIZE,
        shutdown_timeout: float = DEFAULT_SHUTDOWN_TIMEOUT_S,
    ) -> None:
        self._client = client
        self._channel_id = coerce_channel_id(channel_id)
        self._agent_id = agent_id
        self._trace = get_or_create_trace(trace_id)
        self._task_listeners: list[Callable[[], None]] = []

        resolved_mode = mode or "background"
        if resolved_mode == "background":
            self._publisher: Optional[BackgroundPublisher] = BackgroundPublisher(
                client,
                queue_size=queue_size,
                shutdown_timeout=shutdown_timeout,
            )
        else:
            self._publisher = None

    def task(self, goal: str) -> AbstractContextManager[str]:
        """Wrap a complete kickoff when using older CrewAI callback APIs."""
        return declared_task(goal, self._emit_task_boundary)

    def _emit_task_boundary(self, boundary: TaskBoundary) -> None:
        kind, payload, metadata = boundary
        self._publish(kind, EventType.CUSTOM, payload, extra_metadata=metadata)

    def listen_for_tasks(
        self, task_goal: DeclaredTaskGoal, *, crew: Any = None
    ) -> Callable[[], None]:
        """Opt in to native kickoff start/completion/failure events.

        Keep the returned stop function and call it before closing this handler.
        Requires CrewAI's event_id / started_event_id correlation; older events
        without those identifiers are left undeclared rather than guessed.
        An optional crew limits this listener to that object.
        """
        try:
            from crewai.events import (
                crewai_event_bus,
                CrewKickoffStartedEvent,
                CrewKickoffCompletedEvent,
                CrewKickoffFailedEvent,
            )
        except ImportError:
            raise ImportError(
                "Native task events require CrewAI with kickoff lifecycle events; use callbacks.task(goal) on older versions"
            ) from None
        lifecycle = FrameworkTaskLifecycle(task_goal, "crewai")
        stopped = False
        event_lock = RLock()
        pending: dict[str, str] = {}
        try:
            from crewai.events.event_bus import is_replaying
        except ImportError:

            def is_replaying() -> bool:
                return False

        def selected(source: Any, event: Any) -> bool:
            return (
                not stopped
                and not is_replaying()
                and (crew is None or source is crew or getattr(event, "crew", None) is crew)
            )

        def started(source: Any, event: Any) -> None:
            if not selected(source, event):
                return
            run_id = getattr(event, "event_id", None)
            if not isinstance(run_id, str) or not run_id:
                return
            with event_lock:
                boundary = lifecycle.start(
                    run_id,
                    None,
                    name=getattr(event, "crew_name", None),
                    input=getattr(event, "inputs", None),
                )
                if boundary:
                    self._emit_task_boundary(boundary)
                    outcome = pending.pop(run_id, None)
                    if outcome:
                        completed = lifecycle.finish(run_id, outcome)
                        if completed:
                            self._emit_task_boundary(completed)

        def ended(source: Any, event: Any) -> None:
            if not selected(source, event):
                return
            run_id = getattr(event, "started_event_id", None)
            if not isinstance(run_id, str) or not run_id:
                return
            with event_lock:
                outcome = "failed" if isinstance(event, CrewKickoffFailedEvent) else "succeeded"
                boundary = lifecycle.finish(run_id, outcome)
                if boundary:
                    self._emit_task_boundary(boundary)
                elif len(pending) < 10_000:
                    pending[run_id] = outcome

        listeners = [
            (CrewKickoffStartedEvent, started),
            (CrewKickoffCompletedEvent, ended),
            (CrewKickoffFailedEvent, ended),
        ]
        for event_type, callback in listeners:
            crewai_event_bus.on(event_type)(callback)

        def stop() -> None:
            nonlocal stopped
            if stopped:
                return
            stopped = True
            with event_lock:
                lifecycle.clear()
                pending.clear()
            for event_type, callback in listeners:
                crewai_event_bus.off(event_type, callback)
            self._task_listeners.remove(stop)

        self._task_listeners.append(stop)
        return stop

    def on_crew_start(self) -> None:
        self._publish("crew.start", EventType.AGENT_START, {"framework": "crewai"})

    def on_step(self, step_output: Any) -> None:
        agent_name = str(getattr(step_output, "agent", self._agent_id))
        tool = getattr(step_output, "tool", None)

        if tool:
            tool_name = str(tool)
            self._publish(
                f"tool.{tool_name}.start",
                EventType.AGENT_TOOL_CALL_START,
                {
                    "tool_name": tool_name,
                    "tool_input": str(getattr(step_output, "tool_input", ""))[:500],
                },
                agent_id=agent_name,
            )
            result = getattr(step_output, "result", None)
            if result is not None:
                self._publish(
                    f"tool.{tool_name}.end",
                    EventType.AGENT_TOOL_CALL_END,
                    {"tool_name": tool_name, "result_preview": str(result)[:500]},
                    agent_id=agent_name,
                )
        else:
            self._publish(
                "agent.step",
                EventType.AGENT_MESSAGE,
                {"thought": str(getattr(step_output, "thought", ""))[:500]},
                agent_id=agent_name,
            )

    def on_task_complete(self, task_output: Any) -> None:
        self._publish(
            "task.complete",
            EventType.AGENT_END,
            {
                "task_description": str(getattr(task_output, "description", ""))[:200],
                "output_preview": str(task_output)[:500],
            },
        )

    def on_crew_end(self, result: Any = None) -> None:
        self._publish(
            "crew.end",
            EventType.AGENT_END,
            {"result_preview": str(result)[:500] if result else None},
        )

    def _publish(
        self,
        identifier: str,
        event_type: EventType,
        payload: Dict[str, Any],
        *,
        agent_id: Optional[str] = None,
        extra_metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        try:
            publish_kwargs: Dict[str, Any] = {
                "identifier": identifier,
                "payload": payload,
                "channel_id": self._channel_id,
                "agent_id": agent_id or self._agent_id,
                "trace_id": self._trace.trace_id,
                "span_id": self._trace.next_span_id(),
                "event_type": event_type,
                "metadata": {"framework": "crewai", **task_metadata(), **(extra_metadata or {})},
            }
            if self._publisher is not None:
                self._publisher.submit(publish_kwargs)
                return
            self._client.events.publish(**publish_kwargs)
        except Exception:
            logger.warning(
                "AxonPush: failed to emit event %r, suppressing.",
                identifier,
                exc_info=True,
            )

    def flush(self, timeout: Optional[float] = None) -> None:
        if self._publisher is not None:
            self._publisher.flush(timeout)

    def close(self) -> None:
        for stop in list(self._task_listeners):
            stop()
        if self._publisher is not None:
            self._publisher.close()
            self._publisher = None
