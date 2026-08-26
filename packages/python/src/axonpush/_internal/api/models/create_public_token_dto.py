from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePublicTokenDto")


@_attrs_define
class CreatePublicTokenDto:
    """
    Attributes:
        channel_id (str):
        environment_id (str):
        name (str):
    """

    channel_id: str
    environment_id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        environment_id = self.environment_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelId": channel_id,
                "environmentId": environment_id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_id = d.pop("channelId")

        environment_id = d.pop("environmentId")

        name = d.pop("name")

        create_public_token_dto = cls(
            channel_id=channel_id,
            environment_id=environment_id,
            name=name,
        )

        create_public_token_dto.additional_properties = d
        return create_public_token_dto

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
