from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TestOutputBody")


@_attrs_define
class TestOutputBody:
    """
    Attributes:
        delivery_id (str):
        signal (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    delivery_id: str
    signal: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        delivery_id = self.delivery_id

        signal = self.signal

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "deliveryId": delivery_id,
                "signal": signal,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delivery_id = d.pop("deliveryId")

        signal = d.pop("signal")

        schema = d.pop("$schema", UNSET)

        test_output_body = cls(
            delivery_id=delivery_id,
            signal=signal,
            schema=schema,
        )

        return test_output_body
