from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_profile import ActivityProfile


T = TypeVar("T", bound="IdentifyOutputBody")


@_attrs_define
class IdentifyOutputBody:
    """
    Attributes:
        dropped (list[str] | None): Keys not in the entity's profile list; they were dropped and counted
        profile (ActivityProfile):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    dropped: list[str] | None
    profile: ActivityProfile
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_profile import ActivityProfile

        dropped: list[str] | None
        if isinstance(self.dropped, list):
            dropped = self.dropped

        else:
            dropped = self.dropped

        profile = self.profile.to_dict()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dropped": dropped,
                "profile": profile,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_profile import ActivityProfile

        d = dict(src_dict)

        def _parse_dropped(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dropped_type_0 = cast(list[str], data)

                return dropped_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        dropped = _parse_dropped(d.pop("dropped"))

        profile = ActivityProfile.from_dict(d.pop("profile"))

        schema = d.pop("$schema", UNSET)

        identify_output_body = cls(
            dropped=dropped,
            profile=profile,
            schema=schema,
        )

        return identify_output_body
