from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTokenInputBody")


@_attrs_define
class CreateTokenInputBody:
    """
    Attributes:
        channel_id (str): Channel the token can ingest into
        environment_id (str): Environment the token is bound to
        name (str): Human-readable token label
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    channel_id: str
    environment_id: str
    name: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        environment_id = self.environment_id

        name = self.name

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "channelId": channel_id,
                "environmentId": environment_id,
                "name": name,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_id = d.pop("channelId")

        environment_id = d.pop("environmentId")

        name = d.pop("name")

        schema = d.pop("$schema", UNSET)

        create_token_input_body = cls(
            channel_id=channel_id,
            environment_id=environment_id,
            name=name,
            schema=schema,
        )

        return create_token_input_body
