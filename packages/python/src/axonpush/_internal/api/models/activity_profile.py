from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_profile_traits import ActivityProfileTraits


T = TypeVar("T", bound="ActivityProfile")


@_attrs_define
class ActivityProfile:
    """
    Attributes:
        entity (str):
        id (str):
        traits (ActivityProfileTraits):
        updated_at (datetime.datetime):
        masked (list[str] | None | Unset):
    """

    entity: str
    id: str
    traits: ActivityProfileTraits
    updated_at: datetime.datetime
    masked: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_profile_traits import ActivityProfileTraits

        entity = self.entity

        id = self.id

        traits = self.traits.to_dict()

        updated_at = self.updated_at.isoformat()

        masked: list[str] | None | Unset
        if isinstance(self.masked, Unset):
            masked = UNSET
        elif isinstance(self.masked, list):
            masked = self.masked

        else:
            masked = self.masked

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entity": entity,
                "id": id,
                "traits": traits,
                "updatedAt": updated_at,
            }
        )
        if masked is not UNSET:
            field_dict["masked"] = masked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_profile_traits import ActivityProfileTraits

        d = dict(src_dict)
        entity = d.pop("entity")

        id = d.pop("id")

        traits = ActivityProfileTraits.from_dict(d.pop("traits"))

        updated_at = isoparse(d.pop("updatedAt"))

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

        activity_profile = cls(
            entity=entity,
            id=id,
            traits=traits,
            updated_at=updated_at,
            masked=masked,
        )

        return activity_profile
