from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_aggregates import ActivityAggregates
    from ..models.activity_entity_fields import ActivityEntityFields
    from ..models.activity_entity_profile import ActivityEntityProfile
    from ..models.activity_entity_versions import ActivityEntityVersions


T = TypeVar("T", bound="ActivityEntity")


@_attrs_define
class ActivityEntity:
    """
    Attributes:
        fields (ActivityEntityFields):
        id (str):
        occurred_at (datetime.datetime):
        received_at (datetime.datetime):
        snapshot (bool):
        type_ (str):
        versions (ActivityEntityVersions):
        aggregates (ActivityAggregates | Unset):
        evidence (str | Unset):
        last_activity_at (datetime.datetime | Unset):
        links (list[str] | None | Unset): type:id of entities this one references, used for filtering and erasure
        masked (list[str] | None | Unset): Personal attribute keys hidden from this caller
        observed_state (str | Unset): Last observed state of a stale entity
        profile (ActivityEntityProfile | Unset):
        stale (bool | Unset): An open state outlived its expected duration without a terminal event: the state reads
            stale and freshness is unknown, not failed
    """

    fields: ActivityEntityFields
    id: str
    occurred_at: datetime.datetime
    received_at: datetime.datetime
    snapshot: bool
    type_: str
    versions: ActivityEntityVersions
    aggregates: ActivityAggregates | Unset = UNSET
    evidence: str | Unset = UNSET
    last_activity_at: datetime.datetime | Unset = UNSET
    links: list[str] | None | Unset = UNSET
    masked: list[str] | None | Unset = UNSET
    observed_state: str | Unset = UNSET
    profile: ActivityEntityProfile | Unset = UNSET
    stale: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_aggregates import ActivityAggregates
        from ..models.activity_entity_fields import ActivityEntityFields
        from ..models.activity_entity_profile import ActivityEntityProfile
        from ..models.activity_entity_versions import ActivityEntityVersions

        fields = self.fields.to_dict()

        id = self.id

        occurred_at = self.occurred_at.isoformat()

        received_at = self.received_at.isoformat()

        snapshot = self.snapshot

        type_ = self.type_

        versions = self.versions.to_dict()

        aggregates: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aggregates, Unset):
            aggregates = self.aggregates.to_dict()

        evidence = self.evidence

        last_activity_at: str | Unset = UNSET
        if not isinstance(self.last_activity_at, Unset):
            last_activity_at = self.last_activity_at.isoformat()

        links: list[str] | None | Unset
        if isinstance(self.links, Unset):
            links = UNSET
        elif isinstance(self.links, list):
            links = self.links

        else:
            links = self.links

        masked: list[str] | None | Unset
        if isinstance(self.masked, Unset):
            masked = UNSET
        elif isinstance(self.masked, list):
            masked = self.masked

        else:
            masked = self.masked

        observed_state = self.observed_state

        profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        stale = self.stale

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fields": fields,
                "id": id,
                "occurredAt": occurred_at,
                "receivedAt": received_at,
                "snapshot": snapshot,
                "type": type_,
                "versions": versions,
            }
        )
        if aggregates is not UNSET:
            field_dict["aggregates"] = aggregates
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if last_activity_at is not UNSET:
            field_dict["lastActivityAt"] = last_activity_at
        if links is not UNSET:
            field_dict["links"] = links
        if masked is not UNSET:
            field_dict["masked"] = masked
        if observed_state is not UNSET:
            field_dict["observedState"] = observed_state
        if profile is not UNSET:
            field_dict["profile"] = profile
        if stale is not UNSET:
            field_dict["stale"] = stale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_aggregates import ActivityAggregates
        from ..models.activity_entity_fields import ActivityEntityFields
        from ..models.activity_entity_profile import ActivityEntityProfile
        from ..models.activity_entity_versions import ActivityEntityVersions

        d = dict(src_dict)
        fields = ActivityEntityFields.from_dict(d.pop("fields"))

        id = d.pop("id")

        occurred_at = isoparse(d.pop("occurredAt"))

        received_at = isoparse(d.pop("receivedAt"))

        snapshot = d.pop("snapshot")

        type_ = d.pop("type")

        versions = ActivityEntityVersions.from_dict(d.pop("versions"))

        _aggregates = d.pop("aggregates", UNSET)
        aggregates: ActivityAggregates | Unset
        if isinstance(_aggregates, Unset):
            aggregates = UNSET
        else:
            aggregates = ActivityAggregates.from_dict(_aggregates)

        evidence = d.pop("evidence", UNSET)

        _last_activity_at = d.pop("lastActivityAt", UNSET)
        last_activity_at: datetime.datetime | Unset
        if isinstance(_last_activity_at, Unset):
            last_activity_at = UNSET
        else:
            last_activity_at = isoparse(_last_activity_at)

        def _parse_links(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                links_type_0 = cast(list[str], data)

                return links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        links = _parse_links(d.pop("links", UNSET))

        def _parse_masked(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                masked_type_0 = cast(list[str], data)

                return masked_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        masked = _parse_masked(d.pop("masked", UNSET))

        observed_state = d.pop("observedState", UNSET)

        _profile = d.pop("profile", UNSET)
        profile: ActivityEntityProfile | Unset
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = ActivityEntityProfile.from_dict(_profile)

        stale = d.pop("stale", UNSET)

        activity_entity = cls(
            fields=fields,
            id=id,
            occurred_at=occurred_at,
            received_at=received_at,
            snapshot=snapshot,
            type_=type_,
            versions=versions,
            aggregates=aggregates,
            evidence=evidence,
            last_activity_at=last_activity_at,
            links=links,
            masked=masked,
            observed_state=observed_state,
            profile=profile,
            stale=stale,
        )

        return activity_entity
