from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityIncident")


@_attrs_define
class ActivityIncident:
    """
    Attributes:
        affected (int):
        affected_ids (list[str] | None): Up to 20 affected entity ids, oldest first
        checked_at (datetime.datetime):
        entity (str):
        id (str):
        name (str):
        opened_at (datetime.datetime):
        resolved_at (datetime.datetime | None):
    """

    affected: int
    affected_ids: list[str] | None
    checked_at: datetime.datetime
    entity: str
    id: str
    name: str
    opened_at: datetime.datetime
    resolved_at: datetime.datetime | None

    def to_dict(self) -> dict[str, Any]:
        affected = self.affected

        affected_ids: list[str] | None
        if isinstance(self.affected_ids, list):
            affected_ids = self.affected_ids

        else:
            affected_ids = self.affected_ids

        checked_at = self.checked_at.isoformat()

        entity = self.entity

        id = self.id

        name = self.name

        opened_at = self.opened_at.isoformat()

        resolved_at: None | str
        if isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "affected": affected,
                "affectedIds": affected_ids,
                "checkedAt": checked_at,
                "entity": entity,
                "id": id,
                "name": name,
                "openedAt": opened_at,
                "resolvedAt": resolved_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected = d.pop("affected")

        def _parse_affected_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                affected_ids_type_0 = cast(list[str], data)

                return affected_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        affected_ids = _parse_affected_ids(d.pop("affectedIds"))

        checked_at = isoparse(d.pop("checkedAt"))

        entity = d.pop("entity")

        id = d.pop("id")

        name = d.pop("name")

        opened_at = isoparse(d.pop("openedAt"))

        def _parse_resolved_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = isoparse(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        resolved_at = _parse_resolved_at(d.pop("resolvedAt"))

        activity_incident = cls(
            affected=affected,
            affected_ids=affected_ids,
            checked_at=checked_at,
            entity=entity,
            id=id,
            name=name,
            opened_at=opened_at,
            resolved_at=resolved_at,
        )

        return activity_incident
