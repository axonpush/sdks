from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PromptDto")


@_attrs_define
class PromptDto:
    """
    Attributes:
        archived (bool):
        created_at (datetime.datetime):
        latest_version (float):
        name (str):
        org_id (str):
        prompt_id (str):
        tags (list[str]):
        updated_at (datetime.datetime):
        description (str | Unset):
    """

    archived: bool
    created_at: datetime.datetime
    latest_version: float
    name: str
    org_id: str
    prompt_id: str
    tags: list[str]
    updated_at: datetime.datetime
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived = self.archived

        created_at = self.created_at.isoformat()

        latest_version = self.latest_version

        name = self.name

        org_id = self.org_id

        prompt_id = self.prompt_id

        tags = self.tags

        updated_at = self.updated_at.isoformat()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "archived": archived,
                "createdAt": created_at,
                "latestVersion": latest_version,
                "name": name,
                "orgId": org_id,
                "promptId": prompt_id,
                "tags": tags,
                "updatedAt": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archived = d.pop("archived")

        created_at = isoparse(d.pop("createdAt"))

        latest_version = d.pop("latestVersion")

        name = d.pop("name")

        org_id = d.pop("orgId")

        prompt_id = d.pop("promptId")

        tags = cast(list[str], d.pop("tags"))

        updated_at = isoparse(d.pop("updatedAt"))

        description = d.pop("description", UNSET)

        prompt_dto = cls(
            archived=archived,
            created_at=created_at,
            latest_version=latest_version,
            name=name,
            org_id=org_id,
            prompt_id=prompt_id,
            tags=tags,
            updated_at=updated_at,
            description=description,
        )

        prompt_dto.additional_properties = d
        return prompt_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
