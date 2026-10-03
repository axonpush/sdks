"""Generated typed operations facade; regenerate with tools/generate-operations.py."""

from __future__ import annotations
from collections.abc import Mapping
from typing import Any, TYPE_CHECKING
from axonpush._internal.api.models import (
    ActivityReceipt,
    WorkspaceIngestInputBody,
    WorkspaceIngestOutputBody,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol
from axonpush._internal.api.api.ingest import observations_accept as _accept_op
from axonpush._internal.api.api.activity import observations_receipt as _receipt_op


class Observations:
    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def accept(
        self, workspace_id: str, body: WorkspaceIngestInputBody
    ) -> WorkspaceIngestOutputBody | None:
        """Store an idempotent metadata-only batch; projection occurs independently."""
        return self._client._invoke(_accept_op, workspace_id=workspace_id, body=body)

    def receipt(
        self, workspace_id: str, source_event_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivityReceipt | None:
        """Check storage and projection separately."""
        return self._client._invoke(
            _receipt_op,
            workspace_id=workspace_id,
            source_event_id=source_event_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )


class AsyncObservations:
    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def accept(
        self, workspace_id: str, body: WorkspaceIngestInputBody
    ) -> WorkspaceIngestOutputBody | None:
        """Store an idempotent metadata-only batch; projection occurs independently."""
        return await self._client._invoke(_accept_op, workspace_id=workspace_id, body=body)

    async def receipt(
        self, workspace_id: str, source_event_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivityReceipt | None:
        """Check storage and projection separately."""
        return await self._client._invoke(
            _receipt_op,
            workspace_id=workspace_id,
            source_event_id=source_event_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )
