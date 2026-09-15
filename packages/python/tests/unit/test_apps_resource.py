"""Unit tests for ``Apps`` / ``AsyncApps`` resources."""

from __future__ import annotations

from typing import Any, Awaitable, Callable

import pytest

from axonpush._internal.api.api.apps import (
    apps_create as _create_op,
    apps_delete as _delete_op,
    apps_get as _get_op,
    apps_list as _list_op,
    apps_update as _update_op,
)
from axonpush._internal.api.models import (
    AppDTO,
    CreateAppInputBody,
    ListAppsOutputBody,
    UpdateAppInputBody,
)
from axonpush.resources.apps import Apps, AsyncApps

APP_ID = "app-uuid-aaaa"


def _app(app_id: str = APP_ID) -> AppDTO:
    return AppDTO(app_id=app_id, created_at="t", name="n", org_id="o")


class FakeSyncClient:
    def __init__(self, return_value: Any = None) -> None:
        self.calls: list[tuple[Callable[..., Any], dict[str, Any]]] = []
        self.return_value = return_value

    def _invoke(self, op: Callable[..., Any], /, _coerce: Any = None, **kwargs: Any) -> Any:
        self.calls.append((op, kwargs))
        return _coerce(self.return_value) if _coerce else self.return_value


class FakeAsyncClient:
    def __init__(self, return_value: Any = None) -> None:
        self.calls: list[tuple[Callable[..., Awaitable[Any]], dict[str, Any]]] = []
        self.return_value = return_value

    async def _invoke(
        self, op: Callable[..., Awaitable[Any]], /, _coerce: Any = None, **kwargs: Any
    ) -> Any:
        self.calls.append((op, kwargs))
        return _coerce(self.return_value) if _coerce else self.return_value


class TestSyncApps:
    def test_list_unwraps_envelope(self) -> None:
        fake = FakeSyncClient(return_value=ListAppsOutputBody(apps=[_app()]))
        result = Apps(fake).list()
        op, kwargs = fake.calls[0]
        assert op is _list_op
        assert kwargs == {}
        assert isinstance(result, list)
        assert result[0].app_id == APP_ID

    def test_get_dispatches_get_op(self) -> None:
        fake = FakeSyncClient()
        Apps(fake).get(APP_ID)
        op, kwargs = fake.calls[0]
        assert op is _get_op
        assert kwargs == {"app_id": APP_ID}

    def test_create_builds_dto(self) -> None:
        fake = FakeSyncClient()
        Apps(fake).create("checkout-prod")
        op, kwargs = fake.calls[0]
        assert op is _create_op
        body = kwargs["body"]
        assert isinstance(body, CreateAppInputBody)
        assert body.name == "checkout-prod"

    def test_update_passes_id_and_body(self) -> None:
        fake = FakeSyncClient()
        Apps(fake).update(APP_ID, name="renamed")
        op, kwargs = fake.calls[0]
        assert op is _update_op
        assert kwargs["app_id"] == APP_ID
        assert isinstance(kwargs["body"], UpdateAppInputBody)
        assert kwargs["body"].name == "renamed"

    def test_delete_dispatches_delete_op(self) -> None:
        fake = FakeSyncClient()
        Apps(fake).delete(APP_ID)
        op, kwargs = fake.calls[0]
        assert op is _delete_op
        assert kwargs == {"app_id": APP_ID}


class TestAsyncApps:
    @pytest.mark.asyncio
    async def test_list_dispatches_asyncio_op(self) -> None:
        fake = FakeAsyncClient(return_value=ListAppsOutputBody(apps=[]))
        result = await AsyncApps(fake).list()
        op, kwargs = fake.calls[0]
        assert op is _list_op
        assert kwargs == {}
        assert result == []

    @pytest.mark.asyncio
    async def test_create_dispatches_asyncio_op(self) -> None:
        fake = FakeAsyncClient()
        await AsyncApps(fake).create("svc-a")
        op, kwargs = fake.calls[0]
        assert op is _create_op
        assert isinstance(kwargs["body"], CreateAppInputBody)
