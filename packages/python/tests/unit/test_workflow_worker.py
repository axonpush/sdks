from __future__ import annotations

from typing import Any

import httpx

from axonpush.workflow_worker import WorkflowWorker


ACTION = {
    "id": "act_1",
    "case_key": "case_1",
    "case_id": "booking_1",
    "handler": "calendar",
    "mode": "execute",
    "revision": 3,
}


def worker_for(
    handler: httpx.MockTransport, events: list[dict[str, Any]] | None = None
) -> WorkflowWorker:
    return WorkflowWorker(
        "https://api.example.test",
        "workspace",
        "development",
        "secret",
        "calendar",
        client=httpx.Client(transport=handler),
        on_event=events.append if events is not None else None,
    )


def test_tick_settles_claim_once() -> None:
    requests: list[dict[str, Any]] = []

    def respond(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/worker/claim"):
            return httpx.Response(200, json={"action": ACTION})
        requests.append(__import__("json").loads(request.content))
        return httpx.Response(200, json={})

    worker = worker_for(httpx.MockTransport(respond))
    executed: list[str] = []
    assert worker.tick(lambda action: executed.append(action["id"]) or {"ok": True}, lambda _: {})
    assert executed == ["act_1"]
    assert requests == [{"result": "executed", "output": {"ok": True}, "revision": 3}]
    worker.close()


def test_uncertain_execution_is_ambiguous() -> None:
    receipts: list[dict[str, Any]] = []

    def respond(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/worker/claim"):
            return httpx.Response(200, json={"action": ACTION})
        receipts.append(__import__("json").loads(request.content))
        return httpx.Response(200, json={})

    def uncertain(_: dict[str, Any]) -> dict[str, Any]:
        raise RuntimeError("connection disappeared after commit")

    worker = worker_for(httpx.MockTransport(respond))
    assert worker.tick(uncertain, lambda _: {})
    assert receipts == [{"result": "ambiguous", "revision": 3}]
    worker.close()


def test_stale_receipt_is_a_lost_lease() -> None:
    events: list[dict[str, Any]] = []

    def respond(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/worker/claim"):
            return httpx.Response(200, json={"action": ACTION})
        return httpx.Response(409, json={"detail": "stale lease"})

    worker = worker_for(httpx.MockTransport(respond), events)
    assert worker.tick(lambda _: {}, lambda _: {})
    assert any(event["type"] == "lease_lost" for event in events)
    worker.close()
