from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivitySource")


@_attrs_define
class ActivitySource:
    """
    Attributes:
        ref (str | Unset): Source record reference, e.g. table:id
        revision (int | Unset): Monotonic revision of that source record
    """

    ref: str | Unset = UNSET
    revision: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ref = self.ref

        revision = self.revision

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ref is not UNSET:
            field_dict["ref"] = ref
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ref = d.pop("ref", UNSET)

        revision = d.pop("revision", UNSET)

        activity_source = cls(
            ref=ref,
            revision=revision,
        )

        return activity_source
