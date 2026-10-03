from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_failure_count_class import ActivityFailureCountClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityFailureCount")


@_attrs_define
class ActivityFailureCount:
    """
    Attributes:
        category (str):
        class_ (ActivityFailureCountClass):
        count (int):
    """

    category: str
    class_: ActivityFailureCountClass
    count: int

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        class_ = self.class_.value

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "category": category,
                "class": class_,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        class_ = ActivityFailureCountClass(d.pop("class"))

        count = d.pop("count")

        activity_failure_count = cls(
            category=category,
            class_=class_,
            count=count,
        )

        return activity_failure_count
