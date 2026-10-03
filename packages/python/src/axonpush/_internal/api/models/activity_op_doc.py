from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityOpDoc")


@_attrs_define
class ActivityOpDoc:
    """
    Attributes:
        description (str):
        example (str):
        op (str):
    """

    description: str
    example: str
    op: str

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        example = self.example

        op = self.op

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "example": example,
                "op": op,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        example = d.pop("example")

        op = d.pop("op")

        activity_op_doc = cls(
            description=description,
            example=example,
            op=op,
        )

        return activity_op_doc
