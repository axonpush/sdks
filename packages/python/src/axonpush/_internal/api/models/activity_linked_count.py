from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityLinkedCount")


@_attrs_define
class ActivityLinkedCount:
    """
    Attributes:
        attempts (int):
        linked (int):
        to (str):
        unlinked (int):
    """

    attempts: int
    linked: int
    to: str
    unlinked: int

    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        linked = self.linked

        to = self.to

        unlinked = self.unlinked

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attempts": attempts,
                "linked": linked,
                "to": to,
                "unlinked": unlinked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempts = d.pop("attempts")

        linked = d.pop("linked")

        to = d.pop("to")

        unlinked = d.pop("unlinked")

        activity_linked_count = cls(
            attempts=attempts,
            linked=linked,
            to=to,
            unlinked=unlinked,
        )

        return activity_linked_count
