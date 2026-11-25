from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="MetricNameDTO")


@_attrs_define
class MetricNameDTO:
    """
    Attributes:
        count (int): Samples in the window
        last_seen (str):
        name (str):
        type_ (str): counter | gauge | distribution
        unit (str):
    """

    count: int
    last_seen: str
    name: str
    type_: str
    unit: str

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        last_seen = self.last_seen

        name = self.name

        type_ = self.type_

        unit = self.unit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "lastSeen": last_seen,
                "name": name,
                "type": type_,
                "unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        last_seen = d.pop("lastSeen")

        name = d.pop("name")

        type_ = d.pop("type")

        unit = d.pop("unit")

        metric_name_dto = cls(
            count=count,
            last_seen=last_seen,
            name=name,
            type_=type_,
            unit=unit,
        )

        return metric_name_dto
