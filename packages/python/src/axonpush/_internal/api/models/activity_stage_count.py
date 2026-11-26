from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityStageCount")


@_attrs_define
class ActivityStageCount:
    """
    Attributes:
        count (int):
        stage (str):
    """

    count: int
    stage: str

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        stage = self.stage

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "stage": stage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        stage = d.pop("stage")

        activity_stage_count = cls(
            count=count,
            stage=stage,
        )

        return activity_stage_count
