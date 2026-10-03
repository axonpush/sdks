from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.activity_observation_schema_version import ActivityObservationSchemaVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_activity import ActivityActivity
    from ..models.activity_actor import ActivityActor
    from ..models.activity_client import ActivityClient
    from ..models.activity_correlation import ActivityCorrelation
    from ..models.activity_pipeline_health import ActivityPipelineHealth
    from ..models.activity_source import ActivitySource


T = TypeVar("T", bound="ActivityObservation")


@_attrs_define
class ActivityObservation:
    """
    Attributes:
        activity (ActivityActivity):
        actor (ActivityActor):
        client (ActivityClient):
        correlation (ActivityCorrelation):
        event_name (str):
        occurred_at (datetime.datetime):
        schema_version (ActivityObservationSchemaVersion):
        service (str):
        source (ActivitySource):
        source_event_id (str):
        pipeline (ActivityPipelineHealth | Unset):
        release (str | Unset):
    """

    activity: ActivityActivity
    actor: ActivityActor
    client: ActivityClient
    correlation: ActivityCorrelation
    event_name: str
    occurred_at: datetime.datetime
    schema_version: ActivityObservationSchemaVersion
    service: str
    source: ActivitySource
    source_event_id: str
    pipeline: ActivityPipelineHealth | Unset = UNSET
    release: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_activity import ActivityActivity
        from ..models.activity_actor import ActivityActor
        from ..models.activity_client import ActivityClient
        from ..models.activity_correlation import ActivityCorrelation
        from ..models.activity_pipeline_health import ActivityPipelineHealth
        from ..models.activity_source import ActivitySource

        activity = self.activity.to_dict()

        actor = self.actor.to_dict()

        client = self.client.to_dict()

        correlation = self.correlation.to_dict()

        event_name = self.event_name

        occurred_at = self.occurred_at.isoformat()

        schema_version = self.schema_version.value

        service = self.service

        source = self.source.to_dict()

        source_event_id = self.source_event_id

        pipeline: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline, Unset):
            pipeline = self.pipeline.to_dict()

        release = self.release

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "activity": activity,
                "actor": actor,
                "client": client,
                "correlation": correlation,
                "event_name": event_name,
                "occurred_at": occurred_at,
                "schema_version": schema_version,
                "service": service,
                "source": source,
                "source_event_id": source_event_id,
            }
        )
        if pipeline is not UNSET:
            field_dict["pipeline"] = pipeline
        if release is not UNSET:
            field_dict["release"] = release

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_activity import ActivityActivity
        from ..models.activity_actor import ActivityActor
        from ..models.activity_client import ActivityClient
        from ..models.activity_correlation import ActivityCorrelation
        from ..models.activity_pipeline_health import ActivityPipelineHealth
        from ..models.activity_source import ActivitySource

        d = dict(src_dict)
        activity = ActivityActivity.from_dict(d.pop("activity"))

        actor = ActivityActor.from_dict(d.pop("actor"))

        client = ActivityClient.from_dict(d.pop("client"))

        correlation = ActivityCorrelation.from_dict(d.pop("correlation"))

        event_name = d.pop("event_name")

        occurred_at = isoparse(d.pop("occurred_at"))

        schema_version = ActivityObservationSchemaVersion(d.pop("schema_version"))

        service = d.pop("service")

        source = ActivitySource.from_dict(d.pop("source"))

        source_event_id = d.pop("source_event_id")

        _pipeline = d.pop("pipeline", UNSET)
        pipeline: ActivityPipelineHealth | Unset
        if isinstance(_pipeline, Unset):
            pipeline = UNSET
        else:
            pipeline = ActivityPipelineHealth.from_dict(_pipeline)

        release = d.pop("release", UNSET)

        activity_observation = cls(
            activity=activity,
            actor=actor,
            client=client,
            correlation=correlation,
            event_name=event_name,
            occurred_at=occurred_at,
            schema_version=schema_version,
            service=service,
            source=source,
            source_event_id=source_event_id,
            pipeline=pipeline,
            release=release,
        )

        return activity_observation
