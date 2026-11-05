from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicInputBody")


@_attrs_define
class PublicInputBody:
    """
    Attributes:
        email (str):
        kind (str):
        message (str):
        name (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        agent_id (str | Unset):
    """

    email: str
    kind: str
    message: str
    name: str
    schema: str | Unset = UNSET
    agent_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        kind = self.kind

        message = self.message

        name = self.name

        schema = self.schema

        agent_id = self.agent_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "email": email,
                "kind": kind,
                "message": message,
                "name": name,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        kind = d.pop("kind")

        message = d.pop("message")

        name = d.pop("name")

        schema = d.pop("$schema", UNSET)

        agent_id = d.pop("agentId", UNSET)

        public_input_body = cls(
            email=email,
            kind=kind,
            message=message,
            name=name,
            schema=schema,
            agent_id=agent_id,
        )

        return public_input_body
