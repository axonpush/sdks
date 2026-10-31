"""Opt-in HTTP tests against an already-running local Go API and auth service.

See README.md in this directory. Credentials are supplied by the local stack;
these fixtures never read backend .env files, seed authentication tables, launch
servers, or change the caller's active organization. Only newly created test
app/channel resources are deleted on teardown.
"""

from __future__ import annotations

import ipaddress
import os
import uuid
from contextlib import ExitStack
from dataclasses import dataclass, field
from urllib.parse import urlsplit

import httpx
import pytest

from axonpush import AsyncAxonPush, AxonPush


@dataclass
class _BackendCreds:
    base_url: str
    api_key: str = field(repr=False)
    tenant_id: str
    app_id: str
    environment: str


@pytest.fixture(scope="session")
def backend():
    names = ("AXONPUSH_BASE_URL", "AXONPUSH_API_KEY", "AXONPUSH_TENANT_ID", "AXONPUSH_ENVIRONMENT")
    missing = [name for name in names if not os.environ.get(name)]
    if missing:
        pytest.fail("Local E2E tests require explicit " + ", ".join(missing))
    base_url = os.environ["AXONPUSH_BASE_URL"].rstrip("/")
    parsed = urlsplit(base_url)
    local = parsed.hostname == "localhost"
    if not local:
        try:
            local = ipaddress.ip_address(parsed.hostname or "").is_loopback
        except ValueError:
            pass
    if not local or parsed.scheme not in ("http", "https") or parsed.username or parsed.password:
        pytest.fail("E2E tests only accept an explicit loopback API URL without userinfo")
    # No credentials are attached to readiness requests, and redirects are not followed.
    httpx.get(base_url + "/healthz", timeout=5, follow_redirects=False).raise_for_status()
    api_key = os.environ["AXONPUSH_API_KEY"]
    tenant_id = os.environ["AXONPUSH_TENANT_ID"]
    suffix = uuid.uuid4().hex[:12]
    with (
        AxonPush(api_key=api_key, tenant_id=tenant_id, base_url=base_url, fail_open=False) as setup,
        ExitStack() as cleanup,
    ):
        app = setup.apps.create(name=f"sdk-e2e-{suffix}")
        assert app is not None
        cleanup.callback(setup.apps.delete, app.app_id)
        # Environment administration requires a browser session, not an API key.
        # Reuse the explicitly selected local environment without modifying it.
        yield _BackendCreds(
            base_url, api_key, tenant_id, app.app_id, os.environ["AXONPUSH_ENVIRONMENT"]
        )


@pytest.fixture()
def client(backend):
    with AxonPush(
        api_key=backend.api_key,
        tenant_id=backend.tenant_id,
        base_url=backend.base_url,
        environment=backend.environment,
        fail_open=False,
    ) as instance:
        yield instance


@pytest.fixture()
async def async_client(backend):
    async with AsyncAxonPush(
        api_key=backend.api_key,
        tenant_id=backend.tenant_id,
        base_url=backend.base_url,
        environment=backend.environment,
        fail_open=False,
    ) as instance:
        yield instance


@pytest.fixture()
def app(client, backend):
    return client.apps.get(backend.app_id)


@pytest.fixture()
def channel(client, backend):
    created = client.channels.create(backend.app_id, f"sdk-test-{uuid.uuid4().hex[:12]}")
    assert created is not None
    try:
        yield created
    finally:
        client.channels.delete(backend.app_id, created.channel_id)
