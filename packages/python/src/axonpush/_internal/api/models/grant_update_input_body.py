from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GrantUpdateInputBody")


@_attrs_define
class GrantUpdateInputBody:
    """
    Attributes:
        values (list[str] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    values: list[str] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        values: list[str] | None
        if isinstance(self.values, list):
            values = self.values

        else:
            values = self.values

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "values": values,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

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

        schema = d.pop("$schema", UNSET)

        grant_update_input_body = cls(
            values=values,
            schema=schema,
        )

        return grant_update_input_body
