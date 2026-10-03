from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_entity_fields import ActivityEntityFields
    from ..models.activity_entity_versions import ActivityEntityVersions


T = TypeVar("T", bound="ActivityEntity")


@_attrs_define
class ActivityEntity:
    """
    Attributes:
        evidence (str):
        fields (ActivityEntityFields):
        id (str):
        occurred_at (datetime.datetime):
        received_at (datetime.datetime):
        snapshot (bool):
        type_ (str):
        versions (ActivityEntityVersions):
        last_activity_at (datetime.datetime | Unset):
    """

    evidence: str
    fields: ActivityEntityFields
    id: str
    occurred_at: datetime.datetime
    received_at: datetime.datetime
    snapshot: bool
    type_: str
    versions: ActivityEntityVersions
    last_activity_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_entity_fields import ActivityEntityFields
        from ..models.activity_entity_versions import ActivityEntityVersions

        evidence = self.evidence

        fields = self.fields.to_dict()

        id = self.id

        occurred_at = self.occurred_at.isoformat()

        received_at = self.received_at.isoformat()

        snapshot = self.snapshot

        type_ = self.type_

        versions = self.versions.to_dict()

        last_activity_at: str | Unset = UNSET
        if not isinstance(self.last_activity_at, Unset):
            last_activity_at = self.last_activity_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "evidence": evidence,
                "fields": fields,
                "id": id,
                "occurredAt": occurred_at,
                "receivedAt": received_at,
                "snapshot": snapshot,
                "type": type_,
                "versions": versions,
            }
        )
        if last_activity_at is not UNSET:
            field_dict["lastActivityAt"] = last_activity_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_entity_fields import ActivityEntityFields
        from ..models.activity_entity_versions import ActivityEntityVersions

        d = dict(src_dict)
        evidence = d.pop("evidence")

        fields = ActivityEntityFields.from_dict(d.pop("fields"))

        id = d.pop("id")

        occurred_at = isoparse(d.pop("occurredAt"))

        received_at = isoparse(d.pop("receivedAt"))

        snapshot = d.pop("snapshot")

        type_ = d.pop("type")

        versions = ActivityEntityVersions.from_dict(d.pop("versions"))

        _last_activity_at = d.pop("lastActivityAt", UNSET)
        last_activity_at: datetime.datetime | Unset
        if isinstance(_last_activity_at, Unset):
            last_activity_at = UNSET
        else:
            last_activity_at = isoparse(_last_activity_at)

        activity_entity = cls(
            evidence=evidence,
            fields=fields,
            id=id,
            occurred_at=occurred_at,
            received_at=received_at,
            snapshot=snapshot,
            type_=type_,
            versions=versions,
            last_activity_at=last_activity_at,
        )

        return activity_entity
