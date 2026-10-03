"""Generated typed operations facade; regenerate with tools/generate-operations.py."""

from __future__ import annotations
from collections.abc import Mapping
from typing import Any, TYPE_CHECKING
from axonpush._internal.api.models import (
    ActivityAnalytics,
    WorkspaceEntitiesOutputBody,
    WorkspaceIncidentsOutputBody,
    WorkspaceStatusOutputBody,
    WorkspaceTimelineOutputBody,
    WorkspaceWidgetsOutputBody,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol
from axonpush._internal.api.api.activity import activity_entities as _entities_op
from axonpush._internal.api.api.activity import activity_delete_agent as _delete_agent_op
from axonpush._internal.api.api.activity import activity_analytics as _analytics_op
from axonpush._internal.api.api.activity import activity_health as _health_op
from axonpush._internal.api.api.activity import activity_incidents as _incidents_op
from axonpush._internal.api.api.activity import activity_summary as _summary_op
from axonpush._internal.api.api.activity import activity_timeline as _timeline_op
from axonpush._internal.api.api.activity import activity_widgets as _widgets_op


class Activity:
    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def entities(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceEntitiesOutputBody | None:
        """Read exact scoped business entities and concurrent operations."""
        return self._client._invoke(
            _entities_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def delete_agent(
        self, workspace_id: str, agent_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceStatusOutputBody | None:
        """Delete agent evidence and install a replay tombstone."""
        return self._client._invoke(
            _delete_agent_op,
            workspace_id=workspace_id,
            agent_id=agent_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def analytics(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivityAnalytics | None:
        """Distinct lifecycle milestones and client activation; snapshots never count as joins."""
        return self._client._invoke(
            _analytics_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def health(self, workspace_id: str, params: Mapping[str, Any] | None = None) -> Any | None:
        """Read independent storage and projection freshness."""
        return self._client._invoke(
            _health_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def incidents(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceIncidentsOutputBody | None:
        """Read lifecycle incidents and recovery without duplicate notifications."""
        return self._client._invoke(
            _incidents_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def summary(self, workspace_id: str, params: Mapping[str, Any] | None = None) -> Any | None:
        """Exact distinct entity counts with a visible 15 minute activity window."""
        return self._client._invoke(
            _summary_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def timeline(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceTimelineOutputBody | None:
        """Follow chronological source evidence across traces."""
        return self._client._invoke(
            _timeline_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def widgets(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceWidgetsOutputBody | None:
        """Aggregate configured business widgets over the active entity revision."""
        return self._client._invoke(
            _widgets_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )


class AsyncActivity:
    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def entities(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceEntitiesOutputBody | None:
        """Read exact scoped business entities and concurrent operations."""
        return await self._client._invoke(
            _entities_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def delete_agent(
        self, workspace_id: str, agent_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceStatusOutputBody | None:
        """Delete agent evidence and install a replay tombstone."""
        return await self._client._invoke(
            _delete_agent_op,
            workspace_id=workspace_id,
            agent_id=agent_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def analytics(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivityAnalytics | None:
        """Distinct lifecycle milestones and client activation; snapshots never count as joins."""
        return await self._client._invoke(
            _analytics_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def health(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> Any | None:
        """Read independent storage and projection freshness."""
        return await self._client._invoke(
            _health_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def incidents(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceIncidentsOutputBody | None:
        """Read lifecycle incidents and recovery without duplicate notifications."""
        return await self._client._invoke(
            _incidents_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def summary(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> Any | None:
        """Exact distinct entity counts with a visible 15 minute activity window."""
        return await self._client._invoke(
            _summary_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def timeline(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceTimelineOutputBody | None:
        """Follow chronological source evidence across traces."""
        return await self._client._invoke(
            _timeline_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def widgets(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceWidgetsOutputBody | None:
        """Aggregate configured business widgets over the active entity revision."""
        return await self._client._invoke(
            _widgets_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )
