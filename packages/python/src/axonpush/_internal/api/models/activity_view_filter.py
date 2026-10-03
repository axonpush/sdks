from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityViewFilter")


@_attrs_define
class ActivityViewFilter:
    """
    Attributes:
        values (list[str] | None):
        key (str | Unset):
        role (str | Unset):
    """

    values: list[str] | None
    key: str | Unset = UNSET
    role: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        values: list[str] | None
        if isinstance(self.values, list):
            values = self.values

        else:
            values = self.values

        key = self.key

        role = self.role

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "values": values,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_values(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = cast(list[str], data)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        values = _parse_values(d.pop("values"))

        key = d.pop("key", UNSET)

        role = d.pop("role", UNSET)

        activity_view_filter = cls(
            values=values,
            key=key,
            role=role,
        )

        return activity_view_filter
