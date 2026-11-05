from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_input_body_data import PatchInputBodyData


T = TypeVar("T", bound="PatchInputBody")


@_attrs_define
class PatchInputBody:
    """
    Attributes:
        data (PatchInputBodyData):
        version (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
        state (str | Unset):
    """

    data: PatchInputBodyData
    version: int
    schema: str | Unset = UNSET
    state: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_input_body_data import PatchInputBodyData

        data = self.data.to_dict()

        version = self.version

        schema = self.schema

        state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "version": version,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_input_body_data import PatchInputBodyData

        d = dict(src_dict)
        data = PatchInputBodyData.from_dict(d.pop("data"))

        version = d.pop("version")

        schema = d.pop("$schema", UNSET)

        state = d.pop("state", UNSET)

        patch_input_body = cls(
            data=data,
            version=version,
            schema=schema,
            state=state,
        )

        return patch_input_body
