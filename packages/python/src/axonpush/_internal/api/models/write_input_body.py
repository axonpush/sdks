from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.write_input_body_data import WriteInputBodyData


T = TypeVar("T", bound="WriteInputBody")


@_attrs_define
class WriteInputBody:
    """
    Attributes:
        data (WriteInputBodyData):
        schema (str | Unset): A URL to the JSON Schema for this object.
        id (str | Unset):
        state (str | Unset):
    """

    data: WriteInputBodyData
    schema: str | Unset = UNSET
    id: str | Unset = UNSET
    state: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.write_input_body_data import WriteInputBodyData

        data = self.data.to_dict()

        schema = self.schema

        id = self.id

        state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.write_input_body_data import WriteInputBodyData

        d = dict(src_dict)
        data = WriteInputBodyData.from_dict(d.pop("data"))

        schema = d.pop("$schema", UNSET)

        id = d.pop("id", UNSET)

        state = d.pop("state", UNSET)

        write_input_body = cls(
            data=data,
            schema=schema,
            id=id,
            state=state,
        )

        return write_input_body
