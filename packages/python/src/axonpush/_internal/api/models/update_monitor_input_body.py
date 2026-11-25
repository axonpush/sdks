from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="UpdateMonitorInputBody")


@_attrs_define
class UpdateMonitorInputBody:
    """
    Attributes:
        schema (str | Unset): A URL to the JSON Schema for this object.
        muted (bool | Unset): Mute stops missed-run tracking and monitor_failed alerts
    """

    schema: str | Unset = UNSET
    muted: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        muted = self.muted

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if muted is not UNSET:
            field_dict["muted"] = muted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        muted = d.pop("muted", UNSET)

        update_monitor_input_body = cls(
            schema=schema,
            muted=muted,
        )

        return update_monitor_input_body
