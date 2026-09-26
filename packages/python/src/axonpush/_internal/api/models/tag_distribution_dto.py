from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag_value_count_dto import TagValueCountDTO


T = TypeVar("T", bound="TagDistributionDTO")


@_attrs_define
class TagDistributionDTO:
    """
    Attributes:
        key (str):
        values (list[TagValueCountDTO] | None):
    """

    key: str
    values: list[TagValueCountDTO] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.tag_value_count_dto import TagValueCountDTO

        key = self.key

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
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tag_value_count_dto import TagValueCountDTO

        d = dict(src_dict)
        key = d.pop("key")

        def _parse_values(data: object) -> list[TagValueCountDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = []
                _values_type_0 = data
                for values_type_0_item_data in _values_type_0:
                    values_type_0_item = TagValueCountDTO.from_dict(values_type_0_item_data)

                    values_type_0.append(values_type_0_item)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TagValueCountDTO] | None, data)

        values = _parse_values(d.pop("values"))

        tag_distribution_dto = cls(
            key=key,
            values=values,
        )

        return tag_distribution_dto
