from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObligationEvidenceStruct")


@_attrs_define
class ObligationEvidenceStruct:
    """
    Attributes:
        metric (str):
        min_count (int):
    """

    metric: str
    min_count: int

    def to_dict(self) -> dict[str, Any]:
        metric = self.metric

        min_count = self.min_count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "metric": metric,
                "minCount": min_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metric = d.pop("metric")

        min_count = d.pop("minCount")

        obligation_evidence_struct = cls(
            metric=metric,
            min_count=min_count,
        )

        return obligation_evidence_struct
