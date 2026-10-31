"""Run the core examples through the real SDK transport with synthetic HTTP.

This catches facade/model drift and verifies that example cleanup cannot delete
caller-owned resources. No credentials or network access are needed.
"""

import importlib.util
import json
import runpy
import sys
from pathlib import Path
from types import ModuleType

import httpx
import pytest
import respx

EXAMPLES = Path(__file__).resolve().parents[2] / "examples"


@pytest.mark.parametrize("filename", ["01_quickstart.py", "06_async_client.py"])
@pytest.mark.parametrize("reuse_channel", [False, True])
@pytest.mark.parametrize("fail_search", [False, True])
def test_runnable_examples_use_current_contract_and_own_cleanup(
    filename, reuse_channel, fail_search, monkeypatch
):
    config = ModuleType("config")
    config.BASE_URL = "https://example.invalid"
    config.ENVIRONMENT = None
    config.APP_ID = None
    config.CHANNEL_ID = "ch_existing" if reuse_channel else None
    config.require_credentials = lambda: None
    monkeypatch.setitem(sys.modules, "config", config)
    monkeypatch.setenv("AXONPUSH_API_KEY", "ak_example_test")
    monkeypatch.setenv("AXONPUSH_TENANT_ID", "org_example")
    spec = importlib.util.spec_from_file_location("resources", EXAMPLES / "resources.py")
    resources = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(resources)
    monkeypatch.setitem(sys.modules, "resources", resources)

    requests = []

    def respond(request):
        requests.append((request.method, request.url.path))
        path = request.url.path
        if request.method == "POST" and path == "/apps":
            return httpx.Response(
                201,
                json={
                    "appId": "app_created",
                    "orgId": "org_example",
                    "name": "sdk-example",
                    "createdAt": "2026-10-31T00:00:00Z",
                },
            )
        if request.method == "POST" and path == "/apps/app_created/channels":
            assert json.loads(request.content)["name"] == "sdk-example"
            return httpx.Response(
                201,
                json={
                    "appId": "app_created",
                    "channelId": "ch_created",
                    "orgId": "org_example",
                    "name": "sdk-example",
                    "createdAt": "2026-10-31T00:00:00Z",
                },
            )
        if request.method == "POST" and path == "/event":
            assert json.loads(request.content)["channel_id"] == (
                "ch_existing" if reuse_channel else "ch_created"
            )
            return httpx.Response(200, json={"eventId": "ev_accepted", "status": "queued"})
        if request.method == "GET" and path == "/events":
            # Fail after publishing to prove cleanup also runs when the example raises.
            if fail_search:
                raise RuntimeError("synthetic search failure")
            return httpx.Response(200, json={"events": []})
        if request.method == "DELETE":
            assert path in ("/apps/app_created/channels/ch_created", "/apps/app_created")
            return httpx.Response(200, json={"ok": True})
        raise AssertionError(f"Unexpected example request: {request.method} {path}")

    with respx.mock(assert_all_called=False) as router:
        router.route().mock(side_effect=respond)
        if fail_search:
            with pytest.raises(RuntimeError, match="synthetic search failure"):
                runpy.run_path(str(EXAMPLES / filename), run_name="__main__")
        else:
            runpy.run_path(str(EXAMPLES / filename), run_name="__main__")

    deleted = [path for method, path in requests if method == "DELETE"]
    assert deleted == (
        []
        if reuse_channel
        else [
            "/apps/app_created/channels/ch_created",
            "/apps/app_created",
        ]
    )
    if reuse_channel:
        assert all(path in ("/event", "/events") for _, path in requests)
