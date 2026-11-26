from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyCheckInputBody")


@_attrs_define
class PolicyCheckInputBody:
    """
    Attributes:
        subject_ref (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    subject_ref: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        subject_ref = self.subject_ref

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "subjectRef": subject_ref,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subject_ref = d.pop("subjectRef")

        schema = d.pop("$schema", UNSET)

        policy_check_input_body = cls(
            subject_ref=subject_ref,
            schema=schema,
        )

        return policy_check_input_body
