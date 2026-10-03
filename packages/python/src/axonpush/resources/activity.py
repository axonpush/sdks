"""Generated typed operations facade; regenerate with tools/generate-operations.py."""

from __future__ import annotations
from collections.abc import Mapping
from typing import Any, TYPE_CHECKING
from axonpush._internal.api.models import (
    ActivityAnalytics,
    ActivityHealth,
    ActivitySummary,
    ActivityWorkspaceSeries,
    IdentifyInputBody,
    IdentifyOutputBody,
    ViewsOutputBody,
    WorkspaceEntitiesOutputBody,
    WorkspaceIncidentsOutputBody,
    WorkspaceStatusOutputBody,
    WorkspaceTimelineOutputBody,
)

if TYPE_CHECKING:
    from axonpush.resources._base import AsyncClientProtocol, SyncClientProtocol
from axonpush._internal.api.api.activity import activity_entities as _entities_op
from axonpush._internal.api.api.activity import activity_analytics as _analytics_op
from axonpush._internal.api.api.activity import activity_delete_entity as _delete_entity_op
from axonpush._internal.api.api.activity import activity_health as _health_op
from axonpush._internal.api.api.activity import activity_identify as _identify_op
from axonpush._internal.api.api.activity import activity_incidents as _incidents_op
from axonpush._internal.api.api.activity import activity_series as _series_op
from axonpush._internal.api.api.activity import activity_summary as _summary_op
from axonpush._internal.api.api.activity import activity_timeline as _timeline_op
from axonpush._internal.api.api.activity import activity_views as _views_op


class Activity:
    def __init__(self, client: SyncClientProtocol) -> None:
        self._client = client

    def entities(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceEntitiesOutputBody | None:
        """Read projected entities with their profiles; personal attributes are masked without profiles:read."""
        return self._client._invoke(
            _entities_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def analytics(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivityAnalytics | None:
        """Distinct funnel milestones, funnel splits and client breakdowns; snapshots never count."""
        return self._client._invoke(
            _analytics_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def delete_entity(
        self,
        workspace_id: str,
        entity_type: str,
        entity_id: str,
        params: Mapping[str, Any] | None = None,
    ) -> WorkspaceStatusOutputBody | None:
        """Erase an entity, everything linked to it and its profile, and install a replay tombstone."""
        return self._client._invoke(
            _delete_entity_op,
            workspace_id=workspace_id,
            entity_type=entity_type,
            entity_id=entity_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def health(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivityHealth | None:
        """Read storage and projection freshness, source heartbeat and undeclared attributes."""
        return self._client._invoke(
            _health_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def identify(self, workspace_id: str, body: IdentifyInputBody) -> IdentifyOutputBody | None:
        """Attach human-readable profile traits to an entity (merge; null deletes)."""
        return self._client._invoke(_identify_op, workspace_id=workspace_id, body=body)

    def incidents(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceIncidentsOutputBody | None:
        """Read lifecycle incidents and recovery without duplicate notifications."""
        return self._client._invoke(
            _incidents_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def series(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivityWorkspaceSeries | None:
        """Zero-filled time series: observations by the outcome role, distinct funnel entities by furthest stage, or source-to-view lag."""
        return self._client._invoke(
            _series_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def summary(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivitySummary | None:
        """Exact entity counts per state with a 15 minute activity window."""
        return self._client._invoke(
            _summary_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def timeline(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceTimelineOutputBody | None:
        """Follow chronological source evidence; filter with ref=type:id."""
        return self._client._invoke(
            _timeline_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    def views(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ViewsOutputBody | None:
        """Aggregate the spec's declared views (KPIs, breakdowns, latency, funnels) over the active revision."""
        return self._client._invoke(
            _views_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )


class AsyncActivity:
    def __init__(self, client: AsyncClientProtocol) -> None:
        self._client = client

    async def entities(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceEntitiesOutputBody | None:
        """Read projected entities with their profiles; personal attributes are masked without profiles:read."""
        return await self._client._invoke(
            _entities_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def analytics(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivityAnalytics | None:
        """Distinct funnel milestones, funnel splits and client breakdowns; snapshots never count."""
        return await self._client._invoke(
            _analytics_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def delete_entity(
        self,
        workspace_id: str,
        entity_type: str,
        entity_id: str,
        params: Mapping[str, Any] | None = None,
    ) -> WorkspaceStatusOutputBody | None:
        """Erase an entity, everything linked to it and its profile, and install a replay tombstone."""
        return await self._client._invoke(
            _delete_entity_op,
            workspace_id=workspace_id,
            entity_type=entity_type,
            entity_id=entity_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def health(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivityHealth | None:
        """Read storage and projection freshness, source heartbeat and undeclared attributes."""
        return await self._client._invoke(
            _health_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def identify(
        self, workspace_id: str, body: IdentifyInputBody
    ) -> IdentifyOutputBody | None:
        """Attach human-readable profile traits to an entity (merge; null deletes)."""
        return await self._client._invoke(_identify_op, workspace_id=workspace_id, body=body)

    async def incidents(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceIncidentsOutputBody | None:
        """Read lifecycle incidents and recovery without duplicate notifications."""
        return await self._client._invoke(
            _incidents_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def series(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivityWorkspaceSeries | None:
        """Zero-filled time series: observations by the outcome role, distinct funnel entities by furthest stage, or source-to-view lag."""
        return await self._client._invoke(
            _series_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def summary(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ActivitySummary | None:
        """Exact entity counts per state with a 15 minute activity window."""
        return await self._client._invoke(
            _summary_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def timeline(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> WorkspaceTimelineOutputBody | None:
        """Follow chronological source evidence; filter with ref=type:id."""
        return await self._client._invoke(
            _timeline_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )

    async def views(
        self, workspace_id: str, params: Mapping[str, Any] | None = None
    ) -> ViewsOutputBody | None:
        """Aggregate the spec's declared views (KPIs, breakdowns, latency, funnels) over the active revision."""
        return await self._client._invoke(
            _views_op,
            workspace_id=workspace_id,
            **{k: v for k, v in (params or {}).items() if v is not None},
        )
