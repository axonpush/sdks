from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOutputBody1")


@_attrs_define
class CreateOutputBody1:
    """
    Attributes:
        ok (bool):
        request_id (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    ok: bool
    request_id: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        request_id = self.request_id

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ok": ok,
                "requestId": request_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        request_id = d.pop("requestId")

        schema = d.pop("$schema", UNSET)

        create_output_body_1 = cls(
            ok=ok,
            request_id=request_id,
            schema=schema,
        )

        return create_output_body_1
