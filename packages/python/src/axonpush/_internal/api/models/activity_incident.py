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
        checked_at (datetime.datetime):
        entity (str):
        id (str):
        name (str):
        opened_at (datetime.datetime):
        resolved_at (datetime.datetime | None):
    """

    affected: int
    checked_at: datetime.datetime
    entity: str
    id: str
    name: str
    opened_at: datetime.datetime
    resolved_at: datetime.datetime | None

    def to_dict(self) -> dict[str, Any]:
        affected = self.affected

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
            checked_at=checked_at,
            entity=entity,
            id=id,
            name=name,
            opened_at=opened_at,
            resolved_at=resolved_at,
        )

        return activity_incident
