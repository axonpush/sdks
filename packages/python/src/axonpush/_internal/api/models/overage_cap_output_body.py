from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OverageCapOutputBody")


@_attrs_define
class OverageCapOutputBody:
    """
    Attributes:
        cap_usd (int | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    cap_usd: int | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cap_usd: int | None
        cap_usd = self.cap_usd

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "capUsd": cap_usd,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cap_usd(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        cap_usd = _parse_cap_usd(d.pop("capUsd"))

        schema = d.pop("$schema", UNSET)

        overage_cap_output_body = cls(
            cap_usd=cap_usd,
            schema=schema,
        )

        return overage_cap_output_body
