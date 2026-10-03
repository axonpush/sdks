from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityWorkspacePatch")


@_attrs_define
class ActivityWorkspacePatch:
    """
    Attributes:
        description (str | Unset):
        heartbeat (str | Unset):
        name (str | Unset):
    """

    description: str | Unset = UNSET
    heartbeat: str | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        heartbeat = self.heartbeat

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if heartbeat is not UNSET:
            field_dict["heartbeat"] = heartbeat
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        heartbeat = d.pop("heartbeat", UNSET)

        name = d.pop("name", UNSET)

        activity_workspace_patch = cls(
            description=description,
            heartbeat=heartbeat,
            name=name,
        )

        return activity_workspace_patch
