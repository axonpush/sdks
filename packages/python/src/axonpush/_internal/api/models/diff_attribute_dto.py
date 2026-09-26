from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diff_value_dto import DiffValueDTO


T = TypeVar("T", bound="DiffAttributeDTO")


@_attrs_define
class DiffAttributeDTO:
    """
    Attributes:
        key (str):
        score (float):
        values (list[DiffValueDTO] | None):
    """

    key: str
    score: float
    values: list[DiffValueDTO] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.diff_value_dto import DiffValueDTO

        key = self.key

        score = self.score

        values: list[dict[str, Any]] | None
        if isinstance(self.values, list):
            values = []
            for values_type_0_item_data in self.values:
                values_type_0_item = values_type_0_item_data.to_dict()
                values.append(values_type_0_item)

        else:
            values = self.values

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "score": score,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diff_value_dto import DiffValueDTO

        d = dict(src_dict)
        key = d.pop("key")

        score = d.pop("score")

        def _parse_values(data: object) -> list[DiffValueDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = []
                _values_type_0 = data
                for values_type_0_item_data in _values_type_0:
                    values_type_0_item = DiffValueDTO.from_dict(values_type_0_item_data)

                    values_type_0.append(values_type_0_item)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DiffValueDTO] | None, data)

        values = _parse_values(d.pop("values"))

        diff_attribute_dto = cls(
            key=key,
            score=score,
            values=values,
        )

        return diff_attribute_dto
