import asyncio
from unittest.mock import Mock
import pytest
from axonpush import AxonPush, AsyncAxonPush
from axonpush.request_context import current_context, capture_event


def context(id):
    return dict(
        workspace_id="ws",
        environment="dev",
        subjects={"user": id, "company": "acme"},
        bindings={"accepted": {"attributes": {"userId": "user"}}},
    )


def test_nested_context_and_multiple_clients():
    a = AxonPush(api_key="test", tenant_id="org")
    b = AxonPush(api_key="test", tenant_id="org")
    with a.with_context(**context("alice")) as scope:
        with pytest.raises(RuntimeError):
            with a.with_context(**context("bob")):
                raise RuntimeError("stop")
        assert current_context(a)["subjects"]["user"] == "alice"
        assert current_context(b) is None
        captured = scope.capture()
        captured["subjects"]["user"] = "changed"
        assert current_context(a)["subjects"]["user"] == "alice"
    assert current_context(a) is None
    a.close()
    b.close()


@pytest.mark.asyncio
async def test_concurrent_async_requests():
    client = AsyncAxonPush(api_key="test", tenant_id="org")

    async def run(id):
        async with client.with_context(**context(id)):
            await asyncio.sleep(0)
            assert current_context(client)["subjects"]["user"] == id

    await asyncio.gather(run("alice"), run("bob"))
    assert current_context(client) is None
    await client.close()


def test_real_builders_observe_facts_and_capture():
    client = AxonPush(api_key="test", tenant_id="org")
    client._invoke = Mock(return_value=None)
    with client.with_context(**context("alice")) as scope:
        scope.observe("accepted", refs={"booking": "b1"})
        body = client._invoke.call_args.kwargs["body"].to_dict()
        assert body["observations"][0]["attributes"] == {"userId": "alice"}
        scope.facts("booking", dict(case_id="b1", facts=[], coverage=[]))
        assert client._invoke.call_args.kwargs["body"].to_dict()["input"]["subjects"] == {
            "user": "alice",
            "company": "acme",
        }
        with pytest.raises(ValueError):
            scope.facts(
                "booking", dict(case_id="b1", subjects={"user": "bob"}, facts=[], coverage=[])
            )
        captured = capture_event(
            client, {"identifier": "event", "payload": {}, "channel_id": "channel"}
        )
        with pytest.raises(ValueError):
            capture_event(client, {"metadata": {"user.id": "bob"}})
    assert captured["metadata"]["user.id"] == "alice"
    client.events.publish(**captured)
    assert (
        client._invoke.call_args.kwargs["body"].to_dict()["metadata"]["telemetry.subjects"][
            "company"
        ]
        == "acme"
    )
    client.close()
