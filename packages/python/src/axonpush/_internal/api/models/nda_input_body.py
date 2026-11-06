from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NdaInputBody")


@_attrs_define
class NdaInputBody:
    """
    Attributes:
        accepted (bool):
        terms_hash (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    accepted: bool
    terms_hash: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        accepted = self.accepted

        terms_hash = self.terms_hash

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accepted": accepted,
                "termsHash": terms_hash,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accepted = d.pop("accepted")

        terms_hash = d.pop("termsHash")

        schema = d.pop("$schema", UNSET)

        nda_input_body = cls(
            accepted=accepted,
            terms_hash=terms_hash,
            schema=schema,
        )

        return nda_input_body
