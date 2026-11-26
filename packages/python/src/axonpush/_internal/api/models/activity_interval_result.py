from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityIntervalResult")


@_attrs_define
class ActivityIntervalResult:
    """
    Attributes:
        cohort (int): From events inside the window
        completed (int): Of those, how many reached To
        from_ (str):
        open_ (int): Still waiting for To
        small_sample (bool): Fewer completed intervals than the view's minCohort
        to (str):
        p_50_seconds (float | Unset):
        p_95_seconds (float | Unset):
    """

    cohort: int
    completed: int
    from_: str
    open_: int
    small_sample: bool
    to: str
    p_50_seconds: float | Unset = UNSET
    p_95_seconds: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cohort = self.cohort

        completed = self.completed

        from_ = self.from_

        open_ = self.open_

        small_sample = self.small_sample

        to = self.to

        p_50_seconds = self.p_50_seconds

        p_95_seconds = self.p_95_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cohort": cohort,
                "completed": completed,
                "from": from_,
                "open": open_,
                "smallSample": small_sample,
                "to": to,
            }
        )
        if p_50_seconds is not UNSET:
            field_dict["p50Seconds"] = p_50_seconds
        if p_95_seconds is not UNSET:
            field_dict["p95Seconds"] = p_95_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cohort = d.pop("cohort")

        completed = d.pop("completed")

        from_ = d.pop("from")

        open_ = d.pop("open")

        small_sample = d.pop("smallSample")

        to = d.pop("to")

        p_50_seconds = d.pop("p50Seconds", UNSET)

        p_95_seconds = d.pop("p95Seconds", UNSET)

        activity_interval_result = cls(
            cohort=cohort,
            completed=completed,
            from_=from_,
            open_=open_,
            small_sample=small_sample,
            to=to,
            p_50_seconds=p_50_seconds,
            p_95_seconds=p_95_seconds,
        )

        return activity_interval_result
