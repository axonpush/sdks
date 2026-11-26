from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityTemplateRef")


@_attrs_define
class ActivityTemplateRef:
    """
    Attributes:
        id (str):
        version (int):
    """

    id: str
    version: int

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        version = d.pop("version")

        activity_template_ref = cls(
            id=id,
            version=version,
        )

        return activity_template_ref
