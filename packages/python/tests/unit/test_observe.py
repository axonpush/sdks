"""observe / observe_many / identify / group through the real generated clients."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from typing import Any

import httpx
import pytest
import respx

from axonpush import AsyncAxonPush, AxonPush
from axonpush._tracing import TraceContext, _clear_current_trace, set_current_trace
from axonpush.exceptions import APIConnectionError, ValidationError

BASE = "http://observe.example.test"
WS = "ws_support"


def client(**overrides: Any) -> AxonPush:
    opts: dict[str, Any] = dict(
        base_url=BASE,
        api_key="ak_synthetic",
        tenant_id="synthetic-org",
        environment="dev",
        max_retries=0,
    )
    opts.update(overrides)
    return AxonPush(**opts)


def report_for(request: httpx.Request, **extra: Any) -> httpx.Response:
    body = json.loads(request.content)
    return httpx.Response(
        200,
        json={
            "receipts": [
                {
                    "sourceEventId": o["source_event_id"],
                    "status": "stored",
                    "receivedAt": "2026-10-03T00:00:01Z",
                    "projectedAt": None,
                }
                for o in body["observations"]
            ],
            "dropped": [],
            "dropCount": 0,
            **extra,
        },
    )


def sent(route: respx.Route, call: int = 0) -> list[dict[str, Any]]:
    return json.loads(route.calls[call].request.content)["observations"]


def test_observe_builds_core_envelope_with_defaults() -> None:
    with respx.mock(base_url=BASE) as router, client() as sdk:
        route = router.post(f"/workspaces/{WS}/observations").mock(
            side_effect=lambda r: report_for(r, dropped=["plan_tier"], dropCount=1)
        )
        report = sdk.observe(
            WS,
            "ticket.escalated",
            refs={"ticket": "t_42", "agent": "a_7"},
            attributes={"priority": "high", "plan_tier": "pro"},
        )
    obs = sent(route)[0]
    assert obs["schema_version"] == 1
    assert obs["event"] == "ticket.escalated"
    assert obs["refs"] == {"ticket": "t_42", "agent": "a_7"}
    assert obs["attributes"] == {"priority": "high", "plan_tier": "pro"}
    assert obs["environment"] == "dev"
    assert re.fullmatch(r"[0-9a-f-]{36}", obs["source_event_id"])
    assert datetime.fromisoformat(obs["occurred_at"]).tzinfo is not None
    assert "trace_id" not in obs
    assert report is not None
    assert report.dropped == ["plan_tier"]
    assert report.drop_count == 1


def test_observe_keeps_caller_identity_time_and_trace() -> None:
    with respx.mock(base_url=BASE) as router, client() as sdk:
        route = router.post(f"/workspaces/{WS}/observations").mock(side_effect=report_for)
        sdk.observe(
            WS,
            "ticket.resolved",
            source_event_id="evt-1",
            occurred_at=datetime(2026, 10, 1, 10, tzinfo=timezone.utc),
            trace_id="abc",
            span_id="def",
            environment="prod",
        )
    obs = sent(route)[0]
    assert obs["source_event_id"] == "evt-1"
    assert datetime.fromisoformat(obs["occurred_at"]) == datetime(
        2026, 10, 1, 10, tzinfo=timezone.utc
    )
    assert obs["trace_id"] == "abc"
    assert obs["span_id"] == "def"
    assert obs["environment"] == "prod"


def test_observe_attaches_bound_trace() -> None:
    trace_id = "0123456789abcdef0123456789abcdef"
    token = set_current_trace(TraceContext(trace_id=trace_id))
    try:
        with respx.mock(base_url=BASE) as router, client() as sdk:
            route = router.post(f"/workspaces/{WS}/observations").mock(side_effect=report_for)
            sdk.observe(WS, "ticket.opened")
    finally:
        _clear_current_trace(token)
    assert sent(route)[0]["trace_id"] == trace_id


def test_observe_redacts_secret_keys() -> None:
    with respx.mock(base_url=BASE) as router, client() as sdk:
        route = router.post(f"/workspaces/{WS}/observations").mock(side_effect=report_for)
        sdk.observe(WS, "ticket.opened", attributes={"api_key": "sk-123"})
    assert sent(route)[0]["attributes"] == {"api_key": "[REDACTED]"}


def test_observe_many_batches_by_100_and_merges() -> None:
    with respx.mock(base_url=BASE) as router, client() as sdk:
        route = router.post(f"/workspaces/{WS}/observations").mock(
            side_effect=lambda r: report_for(r, dropped=["x"], dropCount=2)
        )
        report = sdk.observe_many(
            WS, [{"event": "ticket.opened", "source_event_id": f"e{i}"} for i in range(150)]
        )
    assert [len(sent(route, i)) for i in range(2)] == [100, 50]
    assert report is not None
    assert len(report.receipts or []) == 150
    assert report.dropped == ["x"]
    assert report.drop_count == 4


def test_observe_fails_open_on_network_error() -> None:
    with respx.mock(base_url=BASE) as router, client() as sdk:
        router.post(f"/workspaces/{WS}/observations").mock(side_effect=httpx.ConnectError("down"))
        assert sdk.observe(WS, "ticket.opened") is None


def test_observe_raises_when_fail_open_disabled() -> None:
    with respx.mock(base_url=BASE) as router, client(fail_open=False) as sdk:
        router.post(f"/workspaces/{WS}/observations").mock(side_effect=httpx.ConnectError("down"))
        with pytest.raises(APIConnectionError):
            sdk.observe(WS, "ticket.opened")


def profile(entity: str, id: str, traits: dict[str, Any]) -> httpx.Response:
    return httpx.Response(
        200,
        json={
            "profile": {
                "entity": entity,
                "id": id,
                "traits": traits,
                "updatedAt": "2026-10-03T00:00:00Z",
            },
            "dropped": ["unknown_key"],
        },
    )


def test_identify_posts_traits_including_null_deletes() -> None:
    with respx.mock(base_url=BASE) as router, client() as sdk:
        route = router.post(f"/workspaces/{WS}/identify").mock(
            return_value=profile("agent", "a_7", {"display_name": "Triage bot"})
        )
        result = sdk.identify(
            WS, "agent", "a_7", {"display_name": "Triage bot", "team": None, "unknown_key": 1}
        )
    assert json.loads(route.calls[0].request.content) == {
        "entity": "agent",
        "id": "a_7",
        "traits": {"display_name": "Triage bot", "team": None, "unknown_key": 1},
    }
    assert result is not None
    assert result.profile.traits.to_dict() == {"display_name": "Triage bot"}
    assert result.dropped == ["unknown_key"]


def test_group_is_identify() -> None:
    with respx.mock(base_url=BASE) as router, client() as sdk:
        route = router.post(f"/workspaces/{WS}/identify").mock(
            return_value=profile("company", "c_1", {"name": "Acme"})
        )
        result = sdk.group(WS, "company", "c_1", {"name": "Acme"})
    assert json.loads(route.calls[0].request.content) == {
        "entity": "company",
        "id": "c_1",
        "traits": {"name": "Acme"},
    }
    assert result is not None and result.profile.entity == "company"


def test_identify_fails_open_and_surfaces_validation() -> None:
    with respx.mock(base_url=BASE) as router, client() as sdk:
        route = router.post(f"/workspaces/{WS}/identify")
        route.mock(side_effect=httpx.ConnectError("down"))
        assert sdk.identify(WS, "agent", "a", {}) is None
        route.mock(return_value=httpx.Response(422, json={"title": "Unprocessable", "status": 422}))
        with pytest.raises(ValidationError):
            sdk.identify(WS, "nope", "a", {})


@pytest.mark.asyncio
async def test_async_observe_identify_and_group() -> None:
    with respx.mock(base_url=BASE) as router:
        obs_route = router.post(f"/workspaces/{WS}/observations").mock(side_effect=report_for)
        id_route = router.post(f"/workspaces/{WS}/identify").mock(
            return_value=profile("company", "c_1", {"name": "Acme"})
        )
        async with AsyncAxonPush(
            base_url=BASE, api_key="ak_synthetic", tenant_id="synthetic-org", max_retries=0
        ) as sdk:
            report = await sdk.observe(WS, "ticket.opened", refs={"ticket": "t_1"})
            await sdk.identify(WS, "agent", "a_1", {"display_name": "Bot"})
            await sdk.group(WS, "company", "c_1", {"name": "Acme"})
    assert report is not None and len(report.receipts or []) == 1
    assert sent(obs_route)[0]["refs"] == {"ticket": "t_1"}
    assert "environment" not in sent(obs_route)[0]
    assert [json.loads(c.request.content)["entity"] for c in id_route.calls] == [
        "agent",
        "company",
    ]
