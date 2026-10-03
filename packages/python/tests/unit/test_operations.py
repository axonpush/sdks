"""Business contract conformance through the real generated HTTP clients."""

from __future__ import annotations

import json
from pathlib import Path

import httpx
import pytest
import respx

from axonpush import AsyncAxonPush, AxonPush, Observation
from axonpush._internal.api.models import WorkspaceIngestInputBody
from axonpush.exceptions import AuthenticationError

ROOT = Path(__file__).resolve().parents[4]
FIXTURE = json.loads((ROOT / "contract/fixtures/activity-observation.json").read_text())
BASE = "http://operations.example.test"
RECEIPT = {
    "sourceEventId": FIXTURE["source_event_id"],
    "status": "stored",
    "receivedAt": "2026-10-03T00:00:01Z",
    "projectedAt": None,
}


def client() -> AxonPush:
    return AxonPush(
        base_url=BASE,
        api_key="ak_synthetic",
        tenant_id="synthetic-org",
        environment="dev",
        max_retries=0,
    )


def test_retry_preserves_identity_occurrence_and_projection_receipts() -> None:
    body = WorkspaceIngestInputBody(
        environment="dev", observations=[Observation.from_dict(FIXTURE)]
    )
    with respx.mock(base_url=BASE) as router, client() as sdk:
        accepted = router.post("/workspaces/synthetic-workspace/observations").mock(
            return_value=httpx.Response(200, json={"receipts": [RECEIPT]})
        )
        receipt = router.get(
            "/workspaces/synthetic-workspace/observations/" + FIXTURE["source_event_id"]
        ).mock(
            side_effect=[
                httpx.Response(200, json=RECEIPT),
                httpx.Response(
                    200,
                    json={**RECEIPT, "status": "projected", "projectedAt": "2026-10-03T00:00:02Z"},
                ),
            ]
        )
        first = sdk.observations.accept("synthetic-workspace", body)
        sdk.observations.accept("synthetic-workspace", body)
        assert first.receipts[0].status == "stored"
        assert first.receipts[0].projected_at is None
        assert accepted.calls[0].request.content == accepted.calls[1].request.content
        sent = json.loads(accepted.calls[0].request.content)["observations"][0]
        assert sent["source_event_id"] == FIXTURE["source_event_id"]
        assert sent["occurred_at"] == "2026-10-03T00:00:00+00:00"
        assert sent["actor"]["related_agent_ids"] == FIXTURE["actor"]["related_agent_ids"]
        assert sent["client"]["confidence"] == "self_reported"
        assert sent["client"]["conflict"] is True
        assert sent["client"]["evidence"] == FIXTURE["client"]["evidence"]
        assert sent["correlation"] == FIXTURE["correlation"]
        assert accepted.calls[0].request.headers["x-axonpush-environment"] == "dev"
        assert (
            sdk.observations.receipt(
                "synthetic-workspace", FIXTURE["source_event_id"], {"environment": "dev"}
            ).status
            == "stored"
        )
        projected = sdk.observations.receipt(
            "synthetic-workspace", FIXTURE["source_event_id"], {"environment": "dev"}
        )
        assert projected.status == "projected" and projected.projected_at is not None
        assert receipt.calls[0].request.url.params["environment"] == "dev"


def test_authoring_auth_failure_is_visible_with_fail_open_enabled() -> None:
    with respx.mock(base_url=BASE) as router, client() as sdk:
        router.post("/workspaces/synthetic-workspace/activate").mock(
            return_value=httpx.Response(401, json={"title": "Unauthorized", "status": 401})
        )
        from axonpush._internal.api.models import ActivateInputBody

        with pytest.raises(AuthenticationError):
            sdk.workspaces.activate(
                "synthetic-workspace", ActivateInputBody(revision="r1", generation=1)
            )


@pytest.mark.asyncio
async def test_async_exact_lookup_keeps_pagination_and_scope() -> None:
    with respx.mock(base_url=BASE) as router:
        route = router.get("/workspaces/synthetic-workspace/activity").mock(
            return_value=httpx.Response(200, json={"entities": [], "nextCursor": "next-agent"})
        )
        async with AsyncAxonPush(
            base_url=BASE, api_key="ak_synthetic", tenant_id="synthetic-org", max_retries=0
        ) as sdk:
            result = await sdk.activity.entities(
                "synthetic-workspace",
                {
                    "agent_id": "synthetic-candidate-1",
                    "environment": "dev",
                    "limit": 2,
                    "cursor": "previous-agent",
                },
            )
        assert result.next_cursor == "next-agent"
        assert route.calls[0].request.url.params["agentId"] == "synthetic-candidate-1"
        assert route.calls[0].request.url.params["limit"] == "2"
        assert route.calls[0].request.url.params["cursor"] == "previous-agent"


def test_facade_types_match_generated_operation_contracts() -> None:
    """Anonymous schemas can be renumbered when another resource is added."""
    import ast
    import importlib
    import types
    from typing import Any, Union, get_args, get_origin, get_type_hints

    from axonpush._internal.api.models import ErrorModel

    def variants(hint: Any) -> set[Any]:
        if get_origin(hint) in (types.UnionType, Union):
            return set(get_args(hint))
        return {hint}

    resources = ROOT / "packages/python/src/axonpush/resources"
    for path in sorted(resources.glob("*.py")):
        if path.name.startswith("_"):
            continue
        module = importlib.import_module("axonpush.resources." + path.stem)
        for cls in ast.parse(path.read_text()).body:
            if not isinstance(cls, ast.ClassDef):
                continue
            for method in cls.body:
                if not isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    continue
                for call in ast.walk(method):
                    if not (
                        isinstance(call, ast.Call)
                        and isinstance(call.func, ast.Attribute)
                        and call.func.attr == "_invoke"
                    ):
                        continue
                    op = getattr(module, call.args[0].id)
                    facade = get_type_hints(getattr(getattr(module, cls.name), method.name))
                    generated = get_type_hints(op._get_kwargs)
                    if "body" in facade:
                        assert facade["body"] == generated["body"], (path.name, method.name)
                    if not any(k.arg == "_coerce" for k in call.keywords):
                        actual = variants(facade["return"]) - {type(None)}
                        expected = variants(get_type_hints(op._parse_response)["return"]) - {
                            ErrorModel
                        }
                        if Any not in actual:
                            assert actual == expected, (path.name, method.name)


def test_lifecycle_alert_uses_alert_body_and_scope() -> None:
    from axonpush.exceptions import NotFoundError
    from axonpush.resources.alerts import CreateAlertRuleInput

    payload = {
        "name": "Synthetic open lifecycle incidents",
        "metric": "lifecycle_open",
        "operator": "gte",
        "threshold": 1,
        "destinationType": "email",
        "destination": "synthetic@example.test",
        "appId": "synthetic-app",
        "environmentId": "synthetic-dev",
        "service": "pipeline",
    }
    with respx.mock(base_url=BASE) as router, client() as sdk:
        route = router.post("/v2/alerts").mock(
            return_value=httpx.Response(404, json={"title": "Not Found", "status": 404})
        )
        with pytest.raises(NotFoundError):
            sdk.alerts.create(CreateAlertRuleInput.from_dict(payload))
        assert json.loads(route.calls[0].request.content) == payload
