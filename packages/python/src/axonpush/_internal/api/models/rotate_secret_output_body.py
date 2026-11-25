from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="RotateSecretOutputBody")


@_attrs_define
class RotateSecretOutputBody:
    """
    Attributes:
        webhook_secret (str): The new signing secret; the previous one stops working immediately
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    webhook_secret: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        webhook_secret = self.webhook_secret

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "webhookSecret": webhook_secret,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_secret = d.pop("webhookSecret")

        schema = d.pop("$schema", UNSET)

        rotate_secret_output_body = cls(
            webhook_secret=webhook_secret,
            schema=schema,
        )

        return rotate_secret_output_body
