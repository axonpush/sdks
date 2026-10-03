from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_outcome_count_class import ActivityOutcomeCountClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityOutcomeCount")


@_attrs_define
class ActivityOutcomeCount:
    """
    Attributes:
        class_ (ActivityOutcomeCountClass):
        count (int):
        outcome (str):
        reason (str | Unset):
    """

    class_: ActivityOutcomeCountClass
    count: int
    outcome: str
    reason: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        class_ = self.class_.value

        count = self.count

        outcome = self.outcome

        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "class": class_,
                "count": count,
                "outcome": outcome,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        class_ = ActivityOutcomeCountClass(d.pop("class"))

        count = d.pop("count")

        outcome = d.pop("outcome")

        reason = d.pop("reason", UNSET)

        activity_outcome_count = cls(
            class_=class_,
            count=count,
            outcome=outcome,
            reason=reason,
        )

        return activity_outcome_count
