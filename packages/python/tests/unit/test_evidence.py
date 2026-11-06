import asyncio
from unittest.mock import MagicMock

import pytest

from axonpush._evidence_context import current_task, task_metadata
from axonpush.integrations._publisher import BackgroundPublisher, AsyncBackgroundPublisher
from axonpush.evidence import AsyncEvidenceRecorder, EvidenceRecorder
from axonpush.resources.events import Events


def test_background_task_identity_is_snapshotted_before_thread_handoff():
    client = MagicMock()
    client._redact_telemetry = None
    client.events = Events(client)
    publisher = BackgroundPublisher(client)
    token = current_task.set(("first", "parent"))
    publisher.submit({"identifier": "first", "payload": {}, "channel_id": "channel"})
    current_task.reset(token)
    publisher.submit({"identifier": "outside", "payload": {}, "channel_id": "channel"})
    publisher.close()
    bodies = [call.kwargs["body"] for call in client._invoke.call_args_list]
    first = next(body for body in bodies if body.identifier == "first")
    outside = next(body for body in bodies if body.identifier == "outside")
    assert first.metadata.additional_properties["axonpush.task_id"] == "first"
    assert first.metadata.additional_properties["axonpush.parent_task_id"] == "parent"
    assert not hasattr(outside.metadata, "additional_properties")


@pytest.mark.asyncio
async def test_async_worker_does_not_leak_its_creator_task():
    seen = []

    class Publisher:
        async def publish(self, **params):
            seen.append((params, task_metadata()))

    client = MagicMock()
    client.events = Publisher()
    publisher = AsyncBackgroundPublisher(client)
    token = current_task.set(("first", None))
    publisher.submit({"identifier": "first", "payload": {}, "channel_id": "channel"})
    current_task.reset(token)
    publisher.submit({"identifier": "outside", "payload": {}, "channel_id": "channel"})
    await publisher.close()
    assert seen[0][0]["metadata"]["axonpush.task_id"] == "first"
    assert "metadata" not in seen[1][0]
    assert all(context == {} for _, context in seen)


def test_task_propagation_and_nested_context():
    client = MagicMock()
    client._redact_telemetry = None
    events = Events(client)
    recorder = EvidenceRecorder(events, "channel", "agent")
    with recorder.task("Review a case") as parent:
        with recorder.task("Check a reference") as child:
            events.publish("ordinary", {}, "channel")
            body = client._invoke.call_args.kwargs["body"]
            assert body.metadata.additional_properties["axonpush.task_id"] == child
            assert body.metadata.additional_properties["axonpush.parent_task_id"] == parent
        assert task_metadata()["axonpush.task_id"] == parent
    assert task_metadata() == {}


def test_failure_preserves_application_exception():
    events = MagicMock()
    recorder = EvidenceRecorder(events, "channel", "agent")
    failure = RuntimeError("private text")
    with pytest.raises(RuntimeError) as caught:
        with recorder.task("Review a case"):
            raise failure
    assert caught.value is failure
    assert events.publish.call_args.kwargs["payload"] == {"outcome": "failed"}
    assert task_metadata() == {}


@pytest.mark.asyncio
async def test_async_tasks_are_isolated():
    calls = []

    class Publisher:
        async def publish(self, **kwargs):
            calls.append((kwargs, task_metadata()))

    recorder = AsyncEvidenceRecorder(Publisher(), "channel", "agent")

    async def run(index):
        async with recorder.task(f"Case {index}") as task_id:
            await asyncio.sleep(0)
            await recorder.denied(str(index), "tool", "shadow")
            return task_id

    ids = await asyncio.gather(run(1), run(2))
    assert len(set(ids)) == 2
    assert {
        context["axonpush.task_id"]
        for call, context in calls
        if call["identifier"] == "policy.denied"
    } == set(ids)
    assert task_metadata() == {}
