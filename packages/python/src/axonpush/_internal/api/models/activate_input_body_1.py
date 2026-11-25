from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="ActivateInputBody1")


@_attrs_define
class ActivateInputBody1:
    """
    Attributes:
        version_id (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    version_id: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        version_id = self.version_id

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "version_id": version_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version_id = d.pop("version_id")

        schema = d.pop("$schema", UNSET)

        activate_input_body_1 = cls(
            version_id=version_id,
            schema=schema,
        )

        return activate_input_body_1
