"""Generated typed operations facade; regenerate with tools/generate-operations.py."""

from __future__ import annotations
from typing import Any, TYPE_CHECKING
from axonpush._internal.api.models import (
    ActivateInputBody,
    ActivityRevision,
    ActivityWorkspace,
    ActivityWorkspaceSpec,
    CreateInputBody,
    RevisionListOutputBody,
    WorkspaceEntitiesOutputBody,
    WorkspaceListOutputBody,
    WorkspacePreviewInputBody,
    WorkspaceStatusOutputBody,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol
from axonpush._internal.api.api.workspaces import workspaces_list as _list_op
from axonpush._internal.api.api.workspaces import workspaces_create as _create_op
from axonpush._internal.api.api.workspaces import workspaces_preview as _preview_op
from axonpush._internal.api.api.workspaces import workspaces_schema as _schema_op
from axonpush._internal.api.api.workspaces import workspaces_validate as _validate_op
from axonpush._internal.api.api.workspaces import workspaces_get as _get_op
from axonpush._internal.api.api.workspaces import workspaces_activate as _activate_op
from axonpush._internal.api.api.workspaces import workspaces_revisions as _revisions_op
from axonpush._internal.api.api.workspaces import workspaces_save_revision as _save_revision_op


class Workspaces:
    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> WorkspaceListOutputBody | None:
        """List organization workspaces."""
        return self._client._invoke(_list_op)

    def create(self, body: CreateInputBody) -> ActivityWorkspace | None:
        """Create an organization-owned workspace from a spec."""
        return self._client._invoke(_create_op, body=body)

    def preview(self, body: WorkspacePreviewInputBody) -> WorkspaceEntitiesOutputBody | None:
        """Preview a spec against synthetic metadata-only observations."""
        return self._client._invoke(_preview_op, body=body)

    def schema(self) -> Any | None:
        """Read the versioned declarative workspace JSON Schema."""
        return self._client._invoke(_schema_op)

    def validate(self, body: ActivityWorkspaceSpec) -> WorkspaceStatusOutputBody | None:
        """Validate a workspace spec without saving or executing it."""
        return self._client._invoke(_validate_op, body=body)

    def get(self, workspace_id: str) -> ActivityWorkspace | None:
        """Read workspace activation and rebuild state."""
        return self._client._invoke(_get_op, workspace_id=workspace_id)

    def activate(
        self, workspace_id: str, body: ActivateInputBody
    ) -> WorkspaceStatusOutputBody | None:
        """Build a revision before activation; use a previous revision for rollback."""
        return self._client._invoke(_activate_op, workspace_id=workspace_id, body=body)

    def revisions(self, workspace_id: str) -> RevisionListOutputBody | None:
        """List immutable spec revisions for diff, upgrade or rollback."""
        return self._client._invoke(_revisions_op, workspace_id=workspace_id)

    def save_revision(
        self, workspace_id: str, body: ActivityWorkspaceSpec
    ) -> ActivityRevision | None:
        """Save a validated immutable draft revision."""
        return self._client._invoke(_save_revision_op, workspace_id=workspace_id, body=body)


class AsyncWorkspaces:
    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> WorkspaceListOutputBody | None:
        """List organization workspaces."""
        return await self._client._invoke(_list_op)

    async def create(self, body: CreateInputBody) -> ActivityWorkspace | None:
        """Create an organization-owned workspace from a spec."""
        return await self._client._invoke(_create_op, body=body)

    async def preview(self, body: WorkspacePreviewInputBody) -> WorkspaceEntitiesOutputBody | None:
        """Preview a spec against synthetic metadata-only observations."""
        return await self._client._invoke(_preview_op, body=body)

    async def schema(self) -> Any | None:
        """Read the versioned declarative workspace JSON Schema."""
        return await self._client._invoke(_schema_op)

    async def validate(self, body: ActivityWorkspaceSpec) -> WorkspaceStatusOutputBody | None:
        """Validate a workspace spec without saving or executing it."""
        return await self._client._invoke(_validate_op, body=body)

    async def get(self, workspace_id: str) -> ActivityWorkspace | None:
        """Read workspace activation and rebuild state."""
        return await self._client._invoke(_get_op, workspace_id=workspace_id)

    async def activate(
        self, workspace_id: str, body: ActivateInputBody
    ) -> WorkspaceStatusOutputBody | None:
        """Build a revision before activation; use a previous revision for rollback."""
        return await self._client._invoke(_activate_op, workspace_id=workspace_id, body=body)

    async def revisions(self, workspace_id: str) -> RevisionListOutputBody | None:
        """List immutable spec revisions for diff, upgrade or rollback."""
        return await self._client._invoke(_revisions_op, workspace_id=workspace_id)

    async def save_revision(
        self, workspace_id: str, body: ActivityWorkspaceSpec
    ) -> ActivityRevision | None:
        """Save a validated immutable draft revision."""
        return await self._client._invoke(_save_revision_op, workspace_id=workspace_id, body=body)
