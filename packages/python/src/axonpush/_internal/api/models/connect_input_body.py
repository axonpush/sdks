from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectInputBody")


@_attrs_define
class ConnectInputBody:
    """
    Attributes:
        schema (str | Unset): A URL to the JSON Schema for this object.
        environment (str | Unset): Environment slug or id; defaults to the organisation's default, else production
        purpose (str | Unset): Separates keys for different processes of one app, e.g. web or worker. Defaults to
            default
        rotate (bool | Unset): Revoke this environment and purpose's existing connect key and mint a new one
    """

    schema: str | Unset = UNSET
    environment: str | Unset = UNSET
    purpose: str | Unset = UNSET
    rotate: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        environment = self.environment

        purpose = self.purpose

        rotate = self.rotate

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if environment is not UNSET:
            field_dict["environment"] = environment
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if rotate is not UNSET:
            field_dict["rotate"] = rotate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        environment = d.pop("environment", UNSET)

        purpose = d.pop("purpose", UNSET)

        rotate = d.pop("rotate", UNSET)

        connect_input_body = cls(
            schema=schema,
            environment=environment,
            purpose=purpose,
            rotate=rotate,
        )

        return connect_input_body
