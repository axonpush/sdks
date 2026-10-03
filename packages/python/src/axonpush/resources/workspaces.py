"""Generated typed operations facade; regenerate with tools/generate-operations.py."""

from __future__ import annotations
from collections.abc import Mapping
from typing import Any, TYPE_CHECKING
from axonpush._internal.api.models import (
    ActivateDraftInputBody,
    ActivateDraftOutputBody,
    ActivateInputBody,
    ActivityCatalog,
    ActivityConnectResult,
    ActivityDescription,
    ActivityDraftView,
    ActivityRevision,
    ActivityWorkspace,
    ActivityWorkspaceSpec,
    ChangesOutputBody,
    ConnectInputBody,
    CreateInputBody,
    OpsInputBody,
    ReplaceInputBody,
    RevisionListOutputBody,
    ValidateOutputBody,
    WorkspaceEntitiesOutputBody,
    WorkspaceListOutputBody,
    WorkspacePreviewInputBody,
    WorkspaceStatusOutputBody,
)
from axonpush._internal.api.types import UNSET, Unset

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol
from axonpush._internal.api.api.workspaces import workspaces_list as _list_op
from axonpush._internal.api.api.workspaces import workspaces_create as _create_op
from axonpush._internal.api.api.workspaces import workspaces_preview as _preview_op
from axonpush._internal.api.api.workspaces import workspaces_schema as _schema_op
from axonpush._internal.api.api.workspaces import workspaces_validate as _validate_op
from axonpush._internal.api.api.workspaces import workspaces_get as _get_op
from axonpush._internal.api.api.workspaces import workspaces_activate as _activate_op
from axonpush._internal.api.api.workspaces import workspaces_catalog as _catalog_op
from axonpush._internal.api.api.workspaces import workspaces_connect as _connect_op
from axonpush._internal.api.api.workspaces import workspaces_describe as _describe_op
from axonpush._internal.api.api.workspaces import workspaces_discard_draft as _discard_draft_op
from axonpush._internal.api.api.workspaces import workspaces_draft as _draft_op
from axonpush._internal.api.api.workspaces import workspaces_replace_draft as _replace_draft_op
from axonpush._internal.api.api.workspaces import workspaces_activate_draft as _activate_draft_op
from axonpush._internal.api.api.workspaces import workspaces_draft_changes as _draft_changes_op
from axonpush._internal.api.api.workspaces import workspaces_apply_draft_ops as _apply_draft_ops_op
from axonpush._internal.api.api.workspaces import workspaces_revisions as _revisions_op
from axonpush._internal.api.api.workspaces import workspaces_save_revision as _save_revision_op


class Workspaces:
    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def list(self) -> WorkspaceListOutputBody | None:
        """List organization workspaces."""
        return self._client._invoke(_list_op)

    def create(self, body: CreateInputBody) -> ActivityWorkspace | None:
        """Create a workspace for an application, from a full or blank spec."""
        return self._client._invoke(_create_op, body=body)

    def preview(self, body: WorkspacePreviewInputBody) -> WorkspaceEntitiesOutputBody | None:
        """Preview the entities a spec projects from sample observations; nothing is stored."""
        return self._client._invoke(_preview_op, body=body)

    def schema(self) -> Any | None:
        """Read the workspace spec JSON Schema."""
        return self._client._invoke(_schema_op)

    def validate(self, body: ActivityWorkspaceSpec) -> ValidateOutputBody | None:
        """Validate a workspace spec without saving it; returns every issue."""
        return self._client._invoke(_validate_op, body=body)

    def get(self, workspace_id: str) -> ActivityWorkspace | None:
        """Read workspace activation and rebuild state."""
        return self._client._invoke(_get_op, workspace_id=workspace_id)

    def activate(
        self, workspace_id: str, body: ActivateInputBody
    ) -> WorkspaceStatusOutputBody | None:
        """Build a revision before activation; use a previous revision for rollback."""
        return self._client._invoke(_activate_op, workspace_id=workspace_id, body=body)

    def catalog(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivityCatalog | None:
        """Events actually received: counts, refs and attribute keys seen (declared and undeclared) and which entities consume each event."""
        return self._client._invoke(
            _catalog_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def connect(self, workspace_id: str, body: ConnectInputBody) -> ActivityConnectResult | None:
        """Mint the application's publish key and return its env, OTLP, Sentry and SDK setup."""
        return self._client._invoke(_connect_op, workspace_id=workspace_id, body=body)

    def describe(self, workspace_id: str) -> ActivityDescription | None:
        """Start here: explains this workspace in plain language plus the spec format, roles and draft ops an agent uses to change it."""
        return self._client._invoke(_describe_op, workspace_id=workspace_id)

    def discard_draft(self, workspace_id: str) -> WorkspaceStatusOutputBody | None:
        """Discard the shared draft."""
        return self._client._invoke(_discard_draft_op, workspace_id=workspace_id)

    def draft(self, workspace_id: str) -> ActivityDraftView | None:
        """Read the shared draft of the workspace spec (created from the active spec on first read)."""
        return self._client._invoke(_draft_op, workspace_id=workspace_id)

    def replace_draft(self, workspace_id: str, body: ReplaceInputBody) -> ActivityDraftView | None:
        """Replace the whole draft spec (JSON editor); 409 with the current draft on a version mismatch."""
        return self._client._invoke(_replace_draft_op, workspace_id=workspace_id, body=body)

    def activate_draft(
        self, workspace_id: str, body: ActivateDraftInputBody | Unset = UNSET
    ) -> ActivateDraftOutputBody | None:
        """Save the draft as a revision and rebuild projections with it; the draft is then cleared."""
        return self._client._invoke(_activate_draft_op, workspace_id=workspace_id, body=body)

    def draft_changes(self, workspace_id: str) -> ChangesOutputBody | None:
        """List, in plain language, what the draft changes against the current spec."""
        return self._client._invoke(_draft_changes_op, workspace_id=workspace_id)

    def apply_draft_ops(self, workspace_id: str, body: OpsInputBody) -> ActivityDraftView | None:
        """Apply typed edits to the shared draft atomically."""
        return self._client._invoke(_apply_draft_ops_op, workspace_id=workspace_id, body=body)

    def revisions(self, workspace_id: str) -> RevisionListOutputBody | None:
        """List immutable spec revisions for diff, upgrade or rollback."""
        return self._client._invoke(_revisions_op, workspace_id=workspace_id)

    def save_revision(
        self, workspace_id: str, body: ActivityWorkspaceSpec
    ) -> ActivityRevision | None:
        """Save a validated immutable revision."""
        return self._client._invoke(_save_revision_op, workspace_id=workspace_id, body=body)


class AsyncWorkspaces:
    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def list(self) -> WorkspaceListOutputBody | None:
        """List organization workspaces."""
        return await self._client._invoke(_list_op)

    async def create(self, body: CreateInputBody) -> ActivityWorkspace | None:
        """Create a workspace for an application, from a full or blank spec."""
        return await self._client._invoke(_create_op, body=body)

    async def preview(self, body: WorkspacePreviewInputBody) -> WorkspaceEntitiesOutputBody | None:
        """Preview the entities a spec projects from sample observations; nothing is stored."""
        return await self._client._invoke(_preview_op, body=body)

    async def schema(self) -> Any | None:
        """Read the workspace spec JSON Schema."""
        return await self._client._invoke(_schema_op)

    async def validate(self, body: ActivityWorkspaceSpec) -> ValidateOutputBody | None:
        """Validate a workspace spec without saving it; returns every issue."""
        return await self._client._invoke(_validate_op, body=body)

    async def get(self, workspace_id: str) -> ActivityWorkspace | None:
        """Read workspace activation and rebuild state."""
        return await self._client._invoke(_get_op, workspace_id=workspace_id)

    async def activate(
        self, workspace_id: str, body: ActivateInputBody
    ) -> WorkspaceStatusOutputBody | None:
        """Build a revision before activation; use a previous revision for rollback."""
        return await self._client._invoke(_activate_op, workspace_id=workspace_id, body=body)

    async def catalog(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivityCatalog | None:
        """Events actually received: counts, refs and attribute keys seen (declared and undeclared) and which entities consume each event."""
        return await self._client._invoke(
            _catalog_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def connect(
        self, workspace_id: str, body: ConnectInputBody
    ) -> ActivityConnectResult | None:
        """Mint the application's publish key and return its env, OTLP, Sentry and SDK setup."""
        return await self._client._invoke(_connect_op, workspace_id=workspace_id, body=body)

    async def describe(self, workspace_id: str) -> ActivityDescription | None:
        """Start here: explains this workspace in plain language plus the spec format, roles and draft ops an agent uses to change it."""
        return await self._client._invoke(_describe_op, workspace_id=workspace_id)

    async def discard_draft(self, workspace_id: str) -> WorkspaceStatusOutputBody | None:
        """Discard the shared draft."""
        return await self._client._invoke(_discard_draft_op, workspace_id=workspace_id)

    async def draft(self, workspace_id: str) -> ActivityDraftView | None:
        """Read the shared draft of the workspace spec (created from the active spec on first read)."""
        return await self._client._invoke(_draft_op, workspace_id=workspace_id)

    async def replace_draft(
        self, workspace_id: str, body: ReplaceInputBody
    ) -> ActivityDraftView | None:
        """Replace the whole draft spec (JSON editor); 409 with the current draft on a version mismatch."""
        return await self._client._invoke(_replace_draft_op, workspace_id=workspace_id, body=body)

    async def activate_draft(
        self, workspace_id: str, body: ActivateDraftInputBody | Unset = UNSET
    ) -> ActivateDraftOutputBody | None:
        """Save the draft as a revision and rebuild projections with it; the draft is then cleared."""
        return await self._client._invoke(_activate_draft_op, workspace_id=workspace_id, body=body)

    async def draft_changes(self, workspace_id: str) -> ChangesOutputBody | None:
        """List, in plain language, what the draft changes against the current spec."""
        return await self._client._invoke(_draft_changes_op, workspace_id=workspace_id)

    async def apply_draft_ops(
        self, workspace_id: str, body: OpsInputBody
    ) -> ActivityDraftView | None:
        """Apply typed edits to the shared draft atomically."""
        return await self._client._invoke(_apply_draft_ops_op, workspace_id=workspace_id, body=body)

    async def revisions(self, workspace_id: str) -> RevisionListOutputBody | None:
        """List immutable spec revisions for diff, upgrade or rollback."""
        return await self._client._invoke(_revisions_op, workspace_id=workspace_id)

    async def save_revision(
        self, workspace_id: str, body: ActivityWorkspaceSpec
    ) -> ActivityRevision | None:
        """Save a validated immutable revision."""
        return await self._client._invoke(_save_revision_op, workspace_id=workspace_id, body=body)
