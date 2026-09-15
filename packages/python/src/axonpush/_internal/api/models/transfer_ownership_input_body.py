from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferOwnershipInputBody")


@_attrs_define
class TransferOwnershipInputBody:
    """
    Attributes:
        user_id (str): Member to promote to owner
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    user_id: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "userId": user_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        schema = d.pop("$schema", UNSET)

        transfer_ownership_input_body = cls(
            user_id=user_id,
            schema=schema,
        )

        return transfer_ownership_input_body
