"""Channels resource — CRUD over channels nested within an app."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from axonpush._internal.api.api.channels import (
    channels_create as _create_op,
    channels_delete as _delete_op,
    channels_get as _get_op,
    channels_list as _list_op,
    channels_update as _update_op,
)
from axonpush._internal.api.models import (
    CreateChannelInputBody,
    ListChannelsOutputBody,
    OkOutputBody,
    UpdateChannelInputBody,
)
from axonpush.models import Channel

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


def _unwrap(result: ListChannelsOutputBody | None) -> List[Channel] | None:
    if result is None:
        return None
    return list(result.channels or [])


class Channels:
    """Synchronous channel CRUD (all operations are app-scoped)."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self, app_id: str) -> List[Channel] | None:
        """List the channels inside an app (envelope unwrapped)."""
        return self._client._invoke(_list_op, app_id=app_id, _coerce=_unwrap)

    def get(self, app_id: str, channel_id: str) -> Channel | None:
        """Fetch a single channel by id within an app."""
        return self._client._invoke(_get_op, app_id=app_id, channel_id=channel_id)

    def create(self, app_id: str, name: str) -> Channel | None:
        """Create a channel inside an app."""
        return self._client._invoke(
            _create_op, app_id=app_id, body=CreateChannelInputBody(name=name)
        )

    def update(self, app_id: str, channel_id: str, *, name: str) -> Channel | None:
        """Rename a channel."""
        return self._client._invoke(
            _update_op,
            app_id=app_id,
            channel_id=channel_id,
            body=UpdateChannelInputBody(name=name),
        )

    def delete(self, app_id: str, channel_id: str) -> OkOutputBody | None:
        """Delete a channel."""
        return self._client._invoke(_delete_op, app_id=app_id, channel_id=channel_id)


class AsyncChannels:
    """Async sibling of :class:`Channels`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self, app_id: str) -> List[Channel] | None:
        """See :meth:`Channels.list`."""
        return await self._client._invoke(_list_op, app_id=app_id, _coerce=_unwrap)

    async def get(self, app_id: str, channel_id: str) -> Channel | None:
        """See :meth:`Channels.get`."""
        return await self._client._invoke(_get_op, app_id=app_id, channel_id=channel_id)

    async def create(self, app_id: str, name: str) -> Channel | None:
        """See :meth:`Channels.create`."""
        return await self._client._invoke(
            _create_op, app_id=app_id, body=CreateChannelInputBody(name=name)
        )

    async def update(self, app_id: str, channel_id: str, *, name: str) -> Channel | None:
        """See :meth:`Channels.update`."""
        return await self._client._invoke(
            _update_op,
            app_id=app_id,
            channel_id=channel_id,
            body=UpdateChannelInputBody(name=name),
        )

    async def delete(self, app_id: str, channel_id: str) -> OkOutputBody | None:
        """See :meth:`Channels.delete`."""
        return await self._client._invoke(_delete_op, app_id=app_id, channel_id=channel_id)
