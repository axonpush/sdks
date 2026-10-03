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
        record_id (str | Unset):
        record_type (str | Unset):
        revision (int | Unset):
    """

    record_id: str | Unset = UNSET
    record_type: str | Unset = UNSET
    revision: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        record_id = self.record_id

        record_type = self.record_type

        revision = self.revision

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if record_id is not UNSET:
            field_dict["record_id"] = record_id
        if record_type is not UNSET:
            field_dict["record_type"] = record_type
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        record_id = d.pop("record_id", UNSET)

        record_type = d.pop("record_type", UNSET)

        revision = d.pop("revision", UNSET)

        activity_source = cls(
            record_id=record_id,
            record_type=record_type,
            revision=revision,
        )

        return activity_source
