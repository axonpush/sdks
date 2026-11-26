from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusOutputBody")


@_attrs_define
class StatusOutputBody:
    """
    Attributes:
        status (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        case_key (str | Unset):
    """

    status: str
    schema: str | Unset = UNSET
    case_key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        schema = self.schema

        case_key = self.case_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if case_key is not UNSET:
            field_dict["case_key"] = case_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        schema = d.pop("$schema", UNSET)

        case_key = d.pop("case_key", UNSET)

        status_output_body = cls(
            status=status,
            schema=schema,
            case_key=case_key,
        )

        return status_output_body
