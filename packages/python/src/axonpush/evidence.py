"""Passive evidence helpers over the normal events resource.

Goals/reasons obey content capture and erasure settings. SDK-reported decisions
do not authenticate their human actor and never enforce policy.
"""

from __future__ import annotations

from contextlib import asynccontextmanager, contextmanager
from collections.abc import AsyncIterator, Iterator
from typing import Any, Literal
from uuid import uuid4

from ._evidence_context import current_task

Decision = Literal["approved", "overrode", "stopped", "escalated"]


class EvidenceRecorder:
    def __init__(self, events: Any, channel_id: str, agent_id: str) -> None:
        self.events, self.channel_id, self.agent_id = events, channel_id, agent_id

    def _emit(self, kind: str, **payload: Any) -> Any:
        return self.events.publish(
            identifier=kind,
            payload=payload,
            channel_id=self.channel_id,
            agent_id=self.agent_id,
            event_type="custom",
            metadata={
                "axonpush.evidence.version": 1,
                "axonpush.evidence.kind": kind,
                "axonpush.evidence.origin": "sdk_reported",
            },
        )

    @contextmanager
    def task(self, goal: str) -> Iterator[str]:
        if not goal.strip():
            raise ValueError("A declared task requires a goal")
        parent = current_task.get()
        task_id = str(uuid4())
        token = current_task.set((task_id, parent[0] if parent else None))
        try:
            self._emit("agent.task.start", goal=goal)
            try:
                yield task_id
            except BaseException:
                try:
                    self._emit("agent.task.end", outcome="failed")
                except BaseException:
                    pass  # Preserve the application's exception.
                raise
            else:
                self._emit("agent.task.end", outcome="succeeded")
        finally:
            current_task.reset(token)

    def decision(
        self, decision: Decision, target_span_id: str, actor: str, reason: str | None = None
    ) -> Any:
        return self._emit(
            "oversight.decision",
            decision=decision,
            target_span_id=target_span_id,
            actor=actor,
            reason=reason,
        )

    def denied(
        self, rule: str, tool: str, mode: Literal["shadow", "enforce"], reason: str | None = None
    ) -> Any:
        return self._emit("policy.denied", rule=rule, tool=tool, mode=mode, reason=reason)

    def notice_shown(self, notice_id: str, audience: str, channel: str) -> Any:
        return self._emit("notice.shown", notice_id=notice_id, audience=audience, channel=channel)


class AsyncEvidenceRecorder(EvidenceRecorder):
    """Use with AsyncAxonPush.events; all publisher methods are awaitable."""

    @asynccontextmanager
    async def task(self, goal: str) -> AsyncIterator[str]:  # type: ignore[override]
        if not goal.strip():
            raise ValueError("A declared task requires a goal")
        parent = current_task.get()
        task_id = str(uuid4())
        token = current_task.set((task_id, parent[0] if parent else None))
        try:
            await self._emit("agent.task.start", goal=goal)
            try:
                yield task_id
            except BaseException:
                try:
                    await self._emit("agent.task.end", outcome="failed")
                except BaseException:
                    pass
                raise
            else:
                await self._emit("agent.task.end", outcome="succeeded")
        finally:
            current_task.reset(token)
