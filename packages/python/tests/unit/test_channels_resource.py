"""Unit tests for ``Channels`` / ``AsyncChannels`` resources."""

from __future__ import annotations

from typing import Any, Awaitable, Callable

import pytest

from axonpush._internal.api.api.channels import (
    channels_create as _create_op,
    channels_delete as _delete_op,
    channels_get as _get_op,
    channels_list as _list_op,
    channels_update as _update_op,
)
from axonpush._internal.api.models import (
    ChannelDTO,
    CreateChannelInputBody,
    ListChannelsOutputBody,
    UpdateChannelInputBody,
)
from axonpush.resources.channels import AsyncChannels, Channels

APP_ID = "app-uuid-aaaa"
CHANNEL_ID = "ch-uuid-bbbb"


def _channel() -> ChannelDTO:
    return ChannelDTO(
        app_id=APP_ID, channel_id=CHANNEL_ID, created_at="t", name="alerts", org_id="o"
    )


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


class TestSyncChannels:
    def test_list_unwraps_envelope(self) -> None:
        fake = FakeSyncClient(return_value=ListChannelsOutputBody(channels=[_channel()]))
        result = Channels(fake).list(APP_ID)
        op, kwargs = fake.calls[0]
        assert op is _list_op
        assert kwargs == {"app_id": APP_ID}
        assert result[0].channel_id == CHANNEL_ID

    def test_get_dispatches_get_op(self) -> None:
        fake = FakeSyncClient()
        Channels(fake).get(APP_ID, CHANNEL_ID)
        op, kwargs = fake.calls[0]
        assert op is _get_op
        assert kwargs == {"app_id": APP_ID, "channel_id": CHANNEL_ID}

    def test_create_builds_dto(self) -> None:
        fake = FakeSyncClient()
        Channels(fake).create(APP_ID, "alerts")
        op, kwargs = fake.calls[0]
        assert op is _create_op
        assert kwargs["app_id"] == APP_ID
        body = kwargs["body"]
        assert isinstance(body, CreateChannelInputBody)
        assert body.name == "alerts"

    def test_update_dispatches_update_op(self) -> None:
        fake = FakeSyncClient()
        Channels(fake).update(APP_ID, CHANNEL_ID, name="renamed")
        op, kwargs = fake.calls[0]
        assert op is _update_op
        assert kwargs["app_id"] == APP_ID
        assert kwargs["channel_id"] == CHANNEL_ID
        assert isinstance(kwargs["body"], UpdateChannelInputBody)
        assert kwargs["body"].name == "renamed"

    def test_delete_dispatches_delete_op(self) -> None:
        fake = FakeSyncClient()
        Channels(fake).delete(APP_ID, CHANNEL_ID)
        op, kwargs = fake.calls[0]
        assert op is _delete_op
        assert kwargs == {"app_id": APP_ID, "channel_id": CHANNEL_ID}


class TestAsyncChannels:
    @pytest.mark.asyncio
    async def test_create_dispatches_asyncio_op(self) -> None:
        fake = FakeAsyncClient()
        await AsyncChannels(fake).create(APP_ID, "alerts")
        op, kwargs = fake.calls[0]
        assert op is _create_op
        assert isinstance(kwargs["body"], CreateChannelInputBody)

    @pytest.mark.asyncio
    async def test_get_dispatches_asyncio_op(self) -> None:
        fake = FakeAsyncClient()
        await AsyncChannels(fake).get(APP_ID, CHANNEL_ID)
        op, kwargs = fake.calls[0]
        assert op is _get_op
        assert kwargs == {"app_id": APP_ID, "channel_id": CHANNEL_ID}
