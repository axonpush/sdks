from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_prompt_version_dto_model_configuration import (
        CreatePromptVersionDtoModelConfiguration,
    )
    from ..models.create_prompt_version_dto_tool_configuration import (
        CreatePromptVersionDtoToolConfiguration,
    )


T = TypeVar("T", bound="CreatePromptVersionDto")


@_attrs_define
class CreatePromptVersionDto:
    """
    Attributes:
        template (str):
        model_configuration (CreatePromptVersionDtoModelConfiguration | Unset):
        note (str | Unset):
        tags (list[str] | Unset):
        tool_configuration (CreatePromptVersionDtoToolConfiguration | Unset):
        variables (list[str] | Unset):
    """

    template: str
    model_configuration: CreatePromptVersionDtoModelConfiguration | Unset = UNSET
    note: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    tool_configuration: CreatePromptVersionDtoToolConfiguration | Unset = UNSET
    variables: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_prompt_version_dto_model_configuration import (
            CreatePromptVersionDtoModelConfiguration,
        )
        from ..models.create_prompt_version_dto_tool_configuration import (
            CreatePromptVersionDtoToolConfiguration,
        )

        template = self.template

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
                "template": template,
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
        from ..models.create_prompt_version_dto_model_configuration import (
            CreatePromptVersionDtoModelConfiguration,
        )
        from ..models.create_prompt_version_dto_tool_configuration import (
            CreatePromptVersionDtoToolConfiguration,
        )

        d = dict(src_dict)
        template = d.pop("template")

        _model_configuration = d.pop("modelConfiguration", UNSET)
        model_configuration: CreatePromptVersionDtoModelConfiguration | Unset
        if isinstance(_model_configuration, Unset):
            model_configuration = UNSET
        else:
            model_configuration = CreatePromptVersionDtoModelConfiguration.from_dict(
                _model_configuration
            )

        note = d.pop("note", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _tool_configuration = d.pop("toolConfiguration", UNSET)
        tool_configuration: CreatePromptVersionDtoToolConfiguration | Unset
        if isinstance(_tool_configuration, Unset):
            tool_configuration = UNSET
        else:
            tool_configuration = CreatePromptVersionDtoToolConfiguration.from_dict(
                _tool_configuration
            )

        variables = cast(list[str], d.pop("variables", UNSET))

        create_prompt_version_dto = cls(
            template=template,
            model_configuration=model_configuration,
            note=note,
            tags=tags,
            tool_configuration=tool_configuration,
            variables=variables,
        )

        create_prompt_version_dto.additional_properties = d
        return create_prompt_version_dto

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
