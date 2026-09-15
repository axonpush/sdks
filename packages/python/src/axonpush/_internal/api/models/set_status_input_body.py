from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetStatusInputBody")


@_attrs_define
class SetStatusInputBody:
    """
    Attributes:
        subscription_status (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    subscription_status: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subscription_status = self.subscription_status

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "subscriptionStatus": subscription_status,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subscription_status = d.pop("subscriptionStatus")

        schema = d.pop("$schema", UNSET)

        set_status_input_body = cls(
            subscription_status=subscription_status,
            schema=schema,
        )

        return set_status_input_body
