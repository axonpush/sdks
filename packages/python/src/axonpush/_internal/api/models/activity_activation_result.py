from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityActivationResult")


@_attrs_define
class ActivityActivationResult:
    """
    Attributes:
        activated (int): Eligible entities that reached To within the window
        cohort (int):
        eligible (int):
        from_ (str):
        incomplete (int): Cohort entities still inside their window
        to (str):
        within_seconds (int):
        rate (float | Unset): activated / eligible; absent with no eligible entities
        small_cohort (bool | Unset): Fewer eligible entities than the minimum cohort: do not rank on this rate
    """

    activated: int
    cohort: int
    eligible: int
    from_: str
    incomplete: int
    to: str
    within_seconds: int
    rate: float | Unset = UNSET
    small_cohort: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        activated = self.activated

        cohort = self.cohort

        eligible = self.eligible

        from_ = self.from_

        incomplete = self.incomplete

        to = self.to

        within_seconds = self.within_seconds

        rate = self.rate

        small_cohort = self.small_cohort

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "activated": activated,
                "cohort": cohort,
                "eligible": eligible,
                "from": from_,
                "incomplete": incomplete,
                "to": to,
                "withinSeconds": within_seconds,
            }
        )
        if rate is not UNSET:
            field_dict["rate"] = rate
        if small_cohort is not UNSET:
            field_dict["smallCohort"] = small_cohort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activated = d.pop("activated")

        cohort = d.pop("cohort")

        eligible = d.pop("eligible")

        from_ = d.pop("from")

        incomplete = d.pop("incomplete")

        to = d.pop("to")

        within_seconds = d.pop("withinSeconds")

        rate = d.pop("rate", UNSET)

        small_cohort = d.pop("smallCohort", UNSET)

        activity_activation_result = cls(
            activated=activated,
            cohort=cohort,
            eligible=eligible,
            from_=from_,
            incomplete=incomplete,
            to=to,
            within_seconds=within_seconds,
            rate=rate,
            small_cohort=small_cohort,
        )

        return activity_activation_result
