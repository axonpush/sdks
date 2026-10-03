"""Generated typed operations facade; regenerate with tools/generate-operations.py."""

from __future__ import annotations
from typing import TYPE_CHECKING
from axonpush._internal.api.models import (
    ActivityTemplate,
    WorkspaceStatusOutputBody,
    WorkspaceTemplateListOutputBody,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol
from axonpush._internal.api.api.templates import templates_list as _list_op
from axonpush._internal.api.api.templates import templates_publish as _publish_op


class Templates:
    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> WorkspaceTemplateListOutputBody | None:
        """Discover public and organization-private immutable business templates."""
        return self._client._invoke(_list_op)

    def publish(self, body: ActivityTemplate) -> WorkspaceStatusOutputBody | None:
        """Publish immutable configuration only; never production data."""
        return self._client._invoke(_publish_op, body=body)


class AsyncTemplates:
    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> WorkspaceTemplateListOutputBody | None:
        """Discover public and organization-private immutable business templates."""
        return await self._client._invoke(_list_op)

    async def publish(self, body: ActivityTemplate) -> WorkspaceStatusOutputBody | None:
        """Publish immutable configuration only; never production data."""
        return await self._client._invoke(_publish_op, body=body)
