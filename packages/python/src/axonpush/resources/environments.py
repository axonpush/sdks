"""Environments resource — list / create / update / delete / promote."""

from __future__ import annotations

from typing import TYPE_CHECKING, List

from axonpush._internal.api.api.environments import (
    environments_create as _create_op,
    environments_delete as _remove_op,
    environments_list as _list_op,
    environments_promote as _promote_op,
    environments_update as _update_op,
)
from axonpush._internal.api.models import (
    CreateEnvironmentInputBody,
    ListEnvironmentsOutputBody,
    OkOutputBody,
    UpdateEnvironmentInputBody,
)
from axonpush._internal.api.types import UNSET
from axonpush.models import Environment

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol


def _unwrap(result: ListEnvironmentsOutputBody | None) -> List[Environment] | None:
    if result is None:
        return None
    return list(result.environments or [])


def _build_create_dto(
    *,
    name: str,
    slug: str | None,
    color: str | None,
    is_production: bool | None,
    is_default: bool | None,
) -> CreateEnvironmentInputBody:
    return CreateEnvironmentInputBody(
        name=name,
        slug=slug if slug is not None else UNSET,
        color=color if color is not None else UNSET,
        is_production=is_production if is_production is not None else UNSET,
        is_default=is_default if is_default is not None else UNSET,
    )


def _build_update_dto(
    *,
    name: str | None,
    color: str | None,
    is_production: bool | None,
) -> UpdateEnvironmentInputBody:
    return UpdateEnvironmentInputBody(
        name=name if name is not None else UNSET,
        color=color if color is not None else UNSET,
        is_production=is_production if is_production is not None else UNSET,
    )


class Environments:
    """Synchronous environment management."""

    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> List[Environment] | None:
        """List environments for the caller's organization (envelope unwrapped)."""
        return self._client._invoke(_list_op, _coerce=_unwrap)

    def create(
        self,
        name: str,
        *,
        slug: str | None = None,
        color: str | None = None,
        is_production: bool | None = None,
        is_default: bool | None = None,
    ) -> Environment | None:
        """Create an environment.

        Args:
            name: Human-readable name.
            slug: URL-safe slug; derived from name when omitted.
            color: Optional UI tag colour (hex).
            is_production: Mark as production-class.
            is_default: Make this the default for un-tagged calls.
        """
        body = _build_create_dto(
            name=name,
            slug=slug,
            color=color,
            is_production=is_production,
            is_default=is_default,
        )
        return self._client._invoke(_create_op, body=body)

    def update(
        self,
        slug: str,
        *,
        name: str | None = None,
        color: str | None = None,
        is_production: bool | None = None,
    ) -> Environment | None:
        """Edit a mutable subset of environment fields (addressed by slug)."""
        body = _build_update_dto(name=name, color=color, is_production=is_production)
        return self._client._invoke(_update_op, slug=slug, body=body)

    def delete(self, slug: str) -> OkOutputBody | None:
        """Delete an environment by slug."""
        return self._client._invoke(_remove_op, slug=slug)

    def promote(self, slug: str) -> Environment | None:
        """Promote an environment (by slug) to the org-wide default."""
        return self._client._invoke(_promote_op, slug=slug)

    # Back-compat alias for the pre-rewrite method name.
    promote_to_default = promote


class AsyncEnvironments:
    """Async sibling of :class:`Environments`."""

    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> List[Environment] | None:
        """See :meth:`Environments.list`."""
        return await self._client._invoke(_list_op, _coerce=_unwrap)

    async def create(
        self,
        name: str,
        *,
        slug: str | None = None,
        color: str | None = None,
        is_production: bool | None = None,
        is_default: bool | None = None,
    ) -> Environment | None:
        """See :meth:`Environments.create`."""
        body = _build_create_dto(
            name=name,
            slug=slug,
            color=color,
            is_production=is_production,
            is_default=is_default,
        )
        return await self._client._invoke(_create_op, body=body)

    async def update(
        self,
        slug: str,
        *,
        name: str | None = None,
        color: str | None = None,
        is_production: bool | None = None,
    ) -> Environment | None:
        """See :meth:`Environments.update`."""
        body = _build_update_dto(name=name, color=color, is_production=is_production)
        return await self._client._invoke(_update_op, slug=slug, body=body)

    async def delete(self, slug: str) -> OkOutputBody | None:
        """See :meth:`Environments.delete`."""
        return await self._client._invoke(_remove_op, slug=slug)

    async def promote(self, slug: str) -> Environment | None:
        """See :meth:`Environments.promote`."""
        return await self._client._invoke(_promote_op, slug=slug)

    promote_to_default = promote
