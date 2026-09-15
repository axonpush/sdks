"""Apps resource — CRUD over applications inside an organization."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from axonpush._internal.api.api.apps import (
    apps_create as _create_op,
    apps_delete as _delete_op,
    apps_get as _get_op,
    apps_list as _list_op,
    apps_update as _update_op,
)
from axonpush._internal.api.models import (
    CreateAppInputBody,
    ListAppsOutputBody,
    OkOutputBody,
    UpdateAppInputBody,
)
from axonpush.models import App

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


def _unwrap(result: ListAppsOutputBody | None) -> List[App] | None:
    if result is None:
        return None
    return list(result.apps or [])


class Apps:
    """Synchronous app CRUD."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> List[App] | None:
        """List all apps the caller's key can see (envelope unwrapped)."""
        return self._client._invoke(_list_op, _coerce=_unwrap)

    def get(self, app_id: str) -> App | None:
        """Fetch an app by id."""
        return self._client._invoke(_get_op, app_id=app_id)

    def create(self, name: str) -> App | None:
        """Create an app under the calling org."""
        return self._client._invoke(_create_op, body=CreateAppInputBody(name=name))

    def update(self, app_id: str, *, name: str) -> App | None:
        """Edit an app's name."""
        return self._client._invoke(_update_op, app_id=app_id, body=UpdateAppInputBody(name=name))

    def delete(self, app_id: str) -> OkOutputBody | None:
        """Delete an app."""
        return self._client._invoke(_delete_op, app_id=app_id)


class AsyncApps:
    """Async sibling of :class:`Apps`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> List[App] | None:
        """See :meth:`Apps.list`."""
        return await self._client._invoke(_list_op, _coerce=_unwrap)

    async def get(self, app_id: str) -> App | None:
        """See :meth:`Apps.get`."""
        return await self._client._invoke(_get_op, app_id=app_id)

    async def create(self, name: str) -> App | None:
        """See :meth:`Apps.create`."""
        return await self._client._invoke(_create_op, body=CreateAppInputBody(name=name))

    async def update(self, app_id: str, *, name: str) -> App | None:
        """See :meth:`Apps.update`."""
        return await self._client._invoke(
            _update_op, app_id=app_id, body=UpdateAppInputBody(name=name)
        )

    async def delete(self, app_id: str) -> OkOutputBody | None:
        """See :meth:`Apps.delete`."""
        return await self._client._invoke(_delete_op, app_id=app_id)
