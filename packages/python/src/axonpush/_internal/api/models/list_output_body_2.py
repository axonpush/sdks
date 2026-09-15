from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_dto import LogDTO


T = TypeVar("T", bound="ListOutputBody2")


@_attrs_define
class ListOutputBody2:
    """
    Attributes:
        data (list[LogDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    data: list[LogDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.log_dto import LogDTO

        data: list[dict[str, Any]] | None
        if isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.log_dto import LogDTO

        d = dict(src_dict)

        def _parse_data(data: object) -> list[LogDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = LogDTO.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LogDTO] | None, data)

        data = _parse_data(d.pop("data"))

        schema = d.pop("$schema", UNSET)

        list_output_body_2 = cls(
            data=data,
            schema=schema,
        )

        return list_output_body_2
