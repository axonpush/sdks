from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_change_kind import ActivityChangeKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityChange")


@_attrs_define
class ActivityChange:
    """
    Attributes:
        kind (ActivityChangeKind):
        text (str):
    """

    kind: ActivityChangeKind
    text: str

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        text = self.text

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = ActivityChangeKind(d.pop("kind"))

        text = d.pop("text")

        activity_change = cls(
            kind=kind,
            text=text,
        )

        return activity_change
