from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trust_write_input_body_data import TrustWriteInputBodyData


T = TypeVar("T", bound="TrustWriteInputBody")


@_attrs_define
class TrustWriteInputBody:
    """
    Attributes:
        data (TrustWriteInputBodyData):
        version (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    data: TrustWriteInputBodyData
    version: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.trust_write_input_body_data import TrustWriteInputBodyData

        data = self.data.to_dict()

        version = self.version

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "version": version,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trust_write_input_body_data import TrustWriteInputBodyData

        d = dict(src_dict)
        data = TrustWriteInputBodyData.from_dict(d.pop("data"))

        version = d.pop("version")

        schema = d.pop("$schema", UNSET)

        trust_write_input_body = cls(
            data=data,
            version=version,
            schema=schema,
        )

        return trust_write_input_body
