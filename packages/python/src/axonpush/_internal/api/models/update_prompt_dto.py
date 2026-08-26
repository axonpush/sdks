from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePromptDto")


@_attrs_define
class UpdatePromptDto:
    """
    Attributes:
        archived (bool | Unset):
        description (str | Unset):
        name (str | Unset):
        tags (list[str] | Unset):
    """

    archived: bool | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        archived = self.archived

        description = self.description

        name = self.name

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived is not UNSET:
            field_dict["archived"] = archived
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        update_prompt_dto = cls(
            archived=archived,
            description=description,
            name=name,
            tags=tags,
        )

        update_prompt_dto.additional_properties = d
        return update_prompt_dto

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
