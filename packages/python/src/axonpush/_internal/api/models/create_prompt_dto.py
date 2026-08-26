from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_prompt_dto_model_configuration import CreatePromptDtoModelConfiguration
    from ..models.create_prompt_dto_tool_configuration import CreatePromptDtoToolConfiguration


T = TypeVar("T", bound="CreatePromptDto")


@_attrs_define
class CreatePromptDto:
    """
    Attributes:
        name (str):
        template (str):
        description (str | Unset):
        model_configuration (CreatePromptDtoModelConfiguration | Unset):
        note (str | Unset):
        tags (list[str] | Unset):
        tool_configuration (CreatePromptDtoToolConfiguration | Unset):
        variables (list[str] | Unset):
    """

    name: str
    template: str
    description: str | Unset = UNSET
    model_configuration: CreatePromptDtoModelConfiguration | Unset = UNSET
    note: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    tool_configuration: CreatePromptDtoToolConfiguration | Unset = UNSET
    variables: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_prompt_dto_model_configuration import CreatePromptDtoModelConfiguration
        from ..models.create_prompt_dto_tool_configuration import CreatePromptDtoToolConfiguration

        name = self.name

        template = self.template

        description = self.description

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
                "name": name,
                "template": template,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
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
        from ..models.create_prompt_dto_model_configuration import CreatePromptDtoModelConfiguration
        from ..models.create_prompt_dto_tool_configuration import CreatePromptDtoToolConfiguration

        d = dict(src_dict)
        name = d.pop("name")

        template = d.pop("template")

        description = d.pop("description", UNSET)

        _model_configuration = d.pop("modelConfiguration", UNSET)
        model_configuration: CreatePromptDtoModelConfiguration | Unset
        if isinstance(_model_configuration, Unset):
            model_configuration = UNSET
        else:
            model_configuration = CreatePromptDtoModelConfiguration.from_dict(_model_configuration)

        note = d.pop("note", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        _tool_configuration = d.pop("toolConfiguration", UNSET)
        tool_configuration: CreatePromptDtoToolConfiguration | Unset
        if isinstance(_tool_configuration, Unset):
            tool_configuration = UNSET
        else:
            tool_configuration = CreatePromptDtoToolConfiguration.from_dict(_tool_configuration)

        variables = cast(list[str], d.pop("variables", UNSET))

        create_prompt_dto = cls(
            name=name,
            template=template,
            description=description,
            model_configuration=model_configuration,
            note=note,
            tags=tags,
            tool_configuration=tool_configuration,
            variables=variables,
        )

        create_prompt_dto.additional_properties = d
        return create_prompt_dto

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
