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
    from ..models.activity_observation_attributes import ActivityObservationAttributes
    from ..models.activity_observation_refs import ActivityObservationRefs
    from ..models.activity_source import ActivitySource


T = TypeVar("T", bound="ActivityObservation")


@_attrs_define
class ActivityObservation:
    """
    Attributes:
        event (str):
        occurred_at (datetime.datetime):
        schema_version (ActivityObservationSchemaVersion):
        source_event_id (str):
        attributes (ActivityObservationAttributes | Unset):
        environment (str | Unset):
        refs (ActivityObservationRefs | Unset): Entity type to opaque identifier
        snapshot (bool | Unset): Reconstructed state rather than live activity
        source (ActivitySource | Unset):
        span_id (str | Unset):
        trace_id (str | Unset):
    """

    event: str
    occurred_at: datetime.datetime
    schema_version: ActivityObservationSchemaVersion
    source_event_id: str
    attributes: ActivityObservationAttributes | Unset = UNSET
    environment: str | Unset = UNSET
    refs: ActivityObservationRefs | Unset = UNSET
    snapshot: bool | Unset = UNSET
    source: ActivitySource | Unset = UNSET
    span_id: str | Unset = UNSET
    trace_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_observation_attributes import ActivityObservationAttributes
        from ..models.activity_observation_refs import ActivityObservationRefs
        from ..models.activity_source import ActivitySource

        event = self.event

        occurred_at = self.occurred_at.isoformat()

        schema_version = self.schema_version.value

        source_event_id = self.source_event_id

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        environment = self.environment

        refs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.refs, Unset):
            refs = self.refs.to_dict()

        snapshot = self.snapshot

        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        span_id = self.span_id

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "event": event,
                "occurred_at": occurred_at,
                "schema_version": schema_version,
                "source_event_id": source_event_id,
            }
        )
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if environment is not UNSET:
            field_dict["environment"] = environment
        if refs is not UNSET:
            field_dict["refs"] = refs
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot
        if source is not UNSET:
            field_dict["source"] = source
        if span_id is not UNSET:
            field_dict["span_id"] = span_id
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_observation_attributes import ActivityObservationAttributes
        from ..models.activity_observation_refs import ActivityObservationRefs
        from ..models.activity_source import ActivitySource

        d = dict(src_dict)
        event = d.pop("event")

        occurred_at = isoparse(d.pop("occurred_at"))

        schema_version = ActivityObservationSchemaVersion(d.pop("schema_version"))

        source_event_id = d.pop("source_event_id")

        _attributes = d.pop("attributes", UNSET)
        attributes: ActivityObservationAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ActivityObservationAttributes.from_dict(_attributes)

        environment = d.pop("environment", UNSET)

        _refs = d.pop("refs", UNSET)
        refs: ActivityObservationRefs | Unset
        if isinstance(_refs, Unset):
            refs = UNSET
        else:
            refs = ActivityObservationRefs.from_dict(_refs)

        snapshot = d.pop("snapshot", UNSET)

        _source = d.pop("source", UNSET)
        source: ActivitySource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ActivitySource.from_dict(_source)

        span_id = d.pop("span_id", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        activity_observation = cls(
            event=event,
            occurred_at=occurred_at,
            schema_version=schema_version,
            source_event_id=source_event_id,
            attributes=attributes,
            environment=environment,
            refs=refs,
            snapshot=snapshot,
            source=source,
            span_id=span_id,
            trace_id=trace_id,
        )

        return activity_observation
