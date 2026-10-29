"""Generated typed operations facade; regenerate with tools/generate-operations.py."""

from __future__ import annotations
from collections.abc import Mapping
from typing import Any, TYPE_CHECKING
from axonpush._internal.api.models import (
    EraseEvidenceOutputBody,
    EventDTO,
    SessionEvidenceBody,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol
from axonpush._internal.api.api.telemetry import telemetry_content as _content_op
from axonpush._internal.api.api.telemetry import telemetry_timeline as _timeline_op
from axonpush._internal.api.api.telemetry import telemetry_erase as _erase_op


class Telemetry:
    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def content(self, event_id: str) -> EventDTO | None:
        """Read audited interaction content; recordings also require replay:read."""
        return self._client._invoke(_content_op, event_id=event_id)

    def timeline(
        self, session_id: str, params: Mapping[str, Any] | None = None
    ) -> SessionEvidenceBody | None:
        """Read a session's chronological interaction metadata."""
        return self._client._invoke(
            _timeline_op,
            session_id=session_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def erase(
        self, subject_type: str, subject_id: str, params: Mapping[str, Any] | None = None
    ) -> EraseEvidenceOutputBody | None:
        """Erase subject evidence and prevent delayed ingestion restoring it."""
        return self._client._invoke(
            _erase_op,
            subject_type=subject_type,
            subject_id=subject_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )


class AsyncTelemetry:
    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def content(self, event_id: str) -> EventDTO | None:
        """Read audited interaction content; recordings also require replay:read."""
        return await self._client._invoke(_content_op, event_id=event_id)

    async def timeline(
        self, session_id: str, params: Mapping[str, Any] | None = None
    ) -> SessionEvidenceBody | None:
        """Read a session's chronological interaction metadata."""
        return await self._client._invoke(
            _timeline_op,
            session_id=session_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def erase(
        self, subject_type: str, subject_id: str, params: Mapping[str, Any] | None = None
    ) -> EraseEvidenceOutputBody | None:
        """Erase subject evidence and prevent delayed ingestion restoring it."""
        return await self._client._invoke(
            _erase_op,
            subject_type=subject_type,
            subject_id=subject_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )
