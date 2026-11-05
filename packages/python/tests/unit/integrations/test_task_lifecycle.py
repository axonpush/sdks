"""Declared goals use actual root boundaries and preserve legacy defaults."""

from __future__ import annotations

import sys
from types import ModuleType, SimpleNamespace
from uuid import uuid4

import pytest

from axonpush._evidence_context import current_task
from axonpush.integrations._task_lifecycle import FrameworkTaskLifecycle
from axonpush.integrations.crewai import AxonPushCrewCallbacks
from .conftest import FakeAsyncClient, FakeSyncClient


def boundaries(calls):
    return [call for call in calls if call["identifier"].startswith("agent.task.")]


def test_blank_selector_does_not_invent_a_task():
    for goal in [" ", lambda _: None, lambda _: (_ for _ in ()).throw(ValueError("bad selector"))]:
        tasks = FrameworkTaskLifecycle(goal, "test")
        assert tasks.start("root", None, name="Not a declared goal") is None
        assert tasks.finish("root", "failed") is None


def test_sync_langchain_overlapping_roots_children_and_failure():
    pytest.importorskip("langchain_core")
    from axonpush.integrations.langchain import AxonPushCallbackHandler

    client = FakeSyncClient()
    handler = AxonPushCallbackHandler(
        client, "ch", mode="sync", task_goal=lambda context: context["input"].get("declared_goal")
    )
    a, b, child, tool = uuid4(), uuid4(), uuid4(), uuid4()
    handler.on_chain_start({}, {"declared_goal": "Declared A"}, run_id=a)
    handler.on_chain_start({}, {"declared_goal": "Declared B"}, run_id=b)
    handler.on_chain_start({}, {}, run_id=child, parent_run_id=a)
    handler.on_tool_start({"name": "search"}, "", run_id=tool, parent_run_id=child)
    handler.on_chain_error(ValueError("runner failed"), run_id=b)
    handler.on_chain_end({}, run_id=child, parent_run_id=a)
    handler.on_chain_end({}, run_id=a)
    handler.on_chain_end({}, run_id=a)
    evidence = boundaries(client.events.calls)
    assert len(evidence) == 4
    a_id, b_id = (
        evidence[0]["metadata"]["axonpush.task_id"],
        evidence[1]["metadata"]["axonpush.task_id"],
    )
    assert a_id != b_id
    assert (
        next(call for call in client.events.calls if call["identifier"] == "tool.search.start")[
            "metadata"
        ]["axonpush.task_id"]
        == a_id
    )
    assert [
        (call["metadata"]["axonpush.task_id"], call["payload"]["outcome"]) for call in evidence[2:]
    ] == [(b_id, "failed"), (a_id, "succeeded")]
    handler.on_tool_start({"name": "after"}, "", run_id=uuid4(), parent_run_id=a)
    assert "axonpush.task_id" not in client.events.calls[-1]["metadata"]


async def test_async_langchain_declared_goal_and_legacy_defaults():
    pytest.importorskip("langchain_core")
    from axonpush.integrations.langchain import AsyncAxonPushCallbackHandler

    client = FakeAsyncClient()
    handler = AsyncAxonPushCallbackHandler(client, "ch", task_goal="Answer the declared question")
    root = uuid4()
    await handler.on_chain_start({}, {}, run_id=root)
    await handler.on_chain_end({}, run_id=root)
    await handler.aflush(timeout=1)
    assert [call["payload"] for call in boundaries(client.events.calls)] == [
        {"goal": "Answer the declared question"},
        {"outcome": "succeeded"},
    ]
    await handler.aclose()
    legacy = FakeAsyncClient()
    handler = AsyncAxonPushCallbackHandler(legacy, "ch")
    await handler.on_chain_start({"name": "Unstated intent"}, {}, run_id=uuid4())
    await handler.aflush(timeout=1)
    assert len(legacy.events.calls) == 1 and not boundaries(legacy.events.calls)
    await handler.aclose()


async def test_openai_scope_keeps_handoffs_open_and_preserves_runner_error():
    pytest.importorskip("agents")
    from axonpush.integrations.openai_agents import AxonPushRunHooks

    client = FakeAsyncClient()
    hooks = AxonPushRunHooks(client, "ch")
    with pytest.raises(RuntimeError, match="runner failed"):
        async with hooks.task("Resolve the explicit request") as task_id:
            await hooks.on_handoff(
                SimpleNamespace(), SimpleNamespace(name="triage"), SimpleNamespace(name="expert")
            )
            await hooks.on_agent_end(SimpleNamespace(), SimpleNamespace(name="triage"), "handoff")
            assert current_task.get()[0] == task_id
            raise RuntimeError("runner failed")
    assert current_task.get() is None
    await hooks.flush(timeout=1)
    calls = client.events.calls
    assert [call["payload"] for call in boundaries(calls)] == [
        {"goal": "Resolve the explicit request"},
        {"outcome": "failed"},
    ]
    assert all(call["metadata"]["axonpush.task_id"] == task_id for call in calls)
    await hooks.close()


def test_crewai_scope_reports_failure_without_fabricating_success():
    client = FakeSyncClient()
    callbacks = AxonPushCrewCallbacks(client, "ch", mode="sync")
    with pytest.raises(ValueError, match="kickoff failed"):
        with callbacks.task("Declared crew objective"):
            callbacks.on_task_complete(SimpleNamespace(description="child finished"))
            assert len(boundaries(client.events.calls)) == 1
            raise ValueError("kickoff failed")
    assert boundaries(client.events.calls)[-1]["payload"] == {"outcome": "failed"}
    assert current_task.get() is None


def test_native_crewai_events_correlate_concurrent_executions_and_unregister(monkeypatch):
    class Started:
        pass

    class Completed:
        pass

    class Failed:
        pass

    class Bus:
        def __init__(self):
            self.handlers = {}

        def on(self, event_type):
            def register(callback):
                self.handlers.setdefault(event_type, []).append(callback)
                return callback

            return register

        def off(self, event_type, callback):
            self.handlers[event_type].remove(callback)

        def emit(self, kind, source, **fields):
            event = kind()
            for key, value in fields.items():
                setattr(event, key, value)
            for callback in list(self.handlers.get(kind, [])):
                callback(source, event)

    bus = Bus()
    package = ModuleType("crewai")
    package.__path__ = []
    events = ModuleType("crewai.events")
    (
        events.crewai_event_bus,
        events.CrewKickoffStartedEvent,
        events.CrewKickoffCompletedEvent,
        events.CrewKickoffFailedEvent,
    ) = bus, Started, Completed, Failed
    monkeypatch.setitem(sys.modules, "crewai", package)
    monkeypatch.setitem(sys.modules, "crewai.events", events)
    client = FakeSyncClient()
    callbacks = AxonPushCrewCallbacks(client, "ch", mode="sync")
    crew = object()
    stop = callbacks.listen_for_tasks(lambda context: context["input"]["goal"], crew=crew)
    bus.emit(Started, object(), event_id="ignored", inputs={"goal": "Wrong crew"})
    bus.emit(Started, crew, event_id="a", inputs={"goal": "Declared A"})
    bus.emit(Started, crew, event_id="b", inputs={"goal": "Declared B"})
    bus.emit(Completed, crew, started_event_id="b")
    bus.emit(Failed, crew, started_event_id="a")
    bus.emit(Completed, crew, started_event_id="a")
    bus.emit(Completed, crew)  # No correlation: never fabricate completion.
    evidence = boundaries(client.events.calls)
    assert len(evidence) == 4
    assert [call["payload"] for call in evidence] == [
        {"goal": "Declared A"},
        {"goal": "Declared B"},
        {"outcome": "succeeded"},
        {"outcome": "failed"},
    ]
    assert (
        evidence[0]["metadata"]["axonpush.task_id"] == evidence[3]["metadata"]["axonpush.task_id"]
    )
    assert (
        evidence[1]["metadata"]["axonpush.task_id"] == evidence[2]["metadata"]["axonpush.task_id"]
    )
    bus.emit(Completed, crew, started_event_id="late")
    bus.emit(Started, crew, event_id="late", inputs={"goal": "Reordered delivery"})
    assert [call["payload"] for call in boundaries(client.events.calls)[-2:]] == [
        {"goal": "Reordered delivery"},
        {"outcome": "succeeded"},
    ]
    count = len(client.events.calls)
    bus.emit(Started, crew, event_id="a", inputs={"goal": "Duplicate start"})
    assert len(client.events.calls) == count
    started_callback = bus.handlers[Started][0]

    class ClosingStart(Started):
        inputs = {"goal": "Must not emit after close"}

        @property
        def event_id(self):
            callbacks.close()
            return "closed-before-lock"

    started_callback(crew, ClosingStart())
    assert len(client.events.calls) == count
    stop()  # Idempotent unregister after close.
    assert not any(bus.handlers.values())
