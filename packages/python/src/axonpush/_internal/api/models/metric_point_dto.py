from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="MetricPointDTO")


@_attrs_define
class MetricPointDTO:
    """
    Attributes:
        bucket (str):
        count (int):
        value (float):
    """

    bucket: str
    count: int
    value: float

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        count = self.count

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bucket": bucket,
                "count": count,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        count = d.pop("count")

        value = d.pop("value")

        metric_point_dto = cls(
            bucket=bucket,
            count=count,
            value=value,
        )

        return metric_point_dto
