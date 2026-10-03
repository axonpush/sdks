from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityActivation")


@_attrs_define
class ActivityActivation:
    """
    Attributes:
        from_ (str): Stage that admits an entity to the cohort
        to (str): Stage that counts as activation
        within_seconds (int):
    """

    from_: str
    to: str
    within_seconds: int

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        to = self.to

        within_seconds = self.within_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "from": from_,
                "to": to,
                "withinSeconds": within_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from")

        to = d.pop("to")

        within_seconds = d.pop("withinSeconds")

        activity_activation = cls(
            from_=from_,
            to=to,
            within_seconds=within_seconds,
        )

        return activity_activation
