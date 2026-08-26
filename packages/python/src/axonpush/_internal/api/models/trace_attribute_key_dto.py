from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trace_attribute_scope import TraceAttributeScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceAttributeKeyDto")


@_attrs_define
class TraceAttributeKeyDto:
    """
    Attributes:
        count (float): Spans carrying the key, or traces for the resource scope.
        distinct_values (float): Approximate: derived from a `uniq` sketch, not the value set.
        key (str):
        numeric (bool): True when the key accepts attrMin/attrMax comparisons.
        scope (TraceAttributeScope):
    """

    count: float
    distinct_values: float
    key: str
    numeric: bool
    scope: TraceAttributeScope
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        distinct_values = self.distinct_values

        key = self.key

        numeric = self.numeric

        scope = self.scope.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "distinctValues": distinct_values,
                "key": key,
                "numeric": numeric,
                "scope": scope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        distinct_values = d.pop("distinctValues")

        key = d.pop("key")

        numeric = d.pop("numeric")

        scope = TraceAttributeScope(d.pop("scope"))

        trace_attribute_key_dto = cls(
            count=count,
            distinct_values=distinct_values,
            key=key,
            numeric=numeric,
            scope=scope,
        )

        trace_attribute_key_dto.additional_properties = d
        return trace_attribute_key_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
