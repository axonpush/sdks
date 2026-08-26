from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prompt_version_dto_model_configuration import PromptVersionDtoModelConfiguration
    from ..models.prompt_version_dto_tool_configuration import PromptVersionDtoToolConfiguration


T = TypeVar("T", bound="PromptVersionDto")


@_attrs_define
class PromptVersionDto:
    """
    Attributes:
        content_hash (str):
        created_at (datetime.datetime):
        org_id (str):
        prompt_id (str):
        template (str):
        version (float):
        model_configuration (PromptVersionDtoModelConfiguration | Unset):
        note (str | Unset):
        tags (list[str] | Unset):
        tool_configuration (PromptVersionDtoToolConfiguration | Unset):
        variables (list[str] | Unset):
    """

    content_hash: str
    created_at: datetime.datetime
    org_id: str
    prompt_id: str
    template: str
    version: float
    model_configuration: PromptVersionDtoModelConfiguration | Unset = UNSET
    note: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    tool_configuration: PromptVersionDtoToolConfiguration | Unset = UNSET
    variables: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.prompt_version_dto_model_configuration import (
            PromptVersionDtoModelConfiguration,
        )
        from ..models.prompt_version_dto_tool_configuration import PromptVersionDtoToolConfiguration

        content_hash = self.content_hash

        created_at = self.created_at.isoformat()

        org_id = self.org_id

        prompt_id = self.prompt_id

        template = self.template

        version = self.version

        model_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.model_configuration, Unset):
            model_configuration = self.model_configuration.to_dict()

        note = self.note

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        tool_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_configuration, Unset):
            tool_configuration = self.tool_configuration.to_dict()

        variables: list[str] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentHash": content_hash,
                "createdAt": created_at,
                "orgId": org_id,
                "promptId": prompt_id,
                "template": template,
                "version": version,
            }
        )
        if model_configuration is not UNSET:
            field_dict["modelConfiguration"] = model_configuration
        if note is not UNSET:
            field_dict["note"] = note
        if tags is not UNSET:
            field_dict["tags"] = tags
        if tool_configuration is not UNSET:
            field_dict["toolConfiguration"] = tool_configuration
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.prompt_version_dto_model_configuration import (
            PromptVersionDtoModelConfiguration,
        )
        from ..models.prompt_version_dto_tool_configuration import PromptVersionDtoToolConfiguration

        d = dict(src_dict)
        content_hash = d.pop("contentHash")

        created_at = isoparse(d.pop("createdAt"))

        org_id = d.pop("orgId")

        prompt_id = d.pop("promptId")

        template = d.pop("template")

        version = d.pop("version")

        _model_configuration = d.pop("modelConfiguration", UNSET)
        model_configuration: PromptVersionDtoModelConfiguration | Unset
        if isinstance(_model_configuration, Unset):
            model_configuration = UNSET
        else:
            model_configuration = PromptVersionDtoModelConfiguration.from_dict(_model_configuration)

        note = d.pop("note", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _tool_configuration = d.pop("toolConfiguration", UNSET)
        tool_configuration: PromptVersionDtoToolConfiguration | Unset
        if isinstance(_tool_configuration, Unset):
            tool_configuration = UNSET
        else:
            tool_configuration = PromptVersionDtoToolConfiguration.from_dict(_tool_configuration)

        variables = cast(list[str], d.pop("variables", UNSET))

        prompt_version_dto = cls(
            content_hash=content_hash,
            created_at=created_at,
            org_id=org_id,
            prompt_id=prompt_id,
            template=template,
            version=version,
            model_configuration=model_configuration,
            note=note,
            tags=tags,
            tool_configuration=tool_configuration,
            variables=variables,
        )

        prompt_version_dto.additional_properties = d
        return prompt_version_dto

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
