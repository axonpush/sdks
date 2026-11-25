from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="CreateInputBody")


@_attrs_define
class CreateInputBody:
    """
    Attributes:
        name (str):
        scopes (list[str] | None): Any of events:publish, events:read, observe:read
        schema (str | Unset): A URL to the JSON Schema for this object.
        app_id (str | Unset): Bind the key to one application
        environment_id (str | Unset): Bind the key to one environment
    """

    name: str
    scopes: list[str] | None
    schema: str | Unset = UNSET
    app_id: str | Unset = UNSET
    environment_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scopes: list[str] | None
        if isinstance(self.scopes, list):
            scopes = self.scopes

        else:
            scopes = self.scopes

        schema = self.schema

        app_id = self.app_id

        environment_id = self.environment_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "scopes": scopes,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_scopes(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = cast(list[str], data)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        scopes = _parse_scopes(d.pop("scopes"))

        schema = d.pop("$schema", UNSET)

        app_id = d.pop("appId", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        create_input_body = cls(
            name=name,
            scopes=scopes,
            schema=schema,
            app_id=app_id,
            environment_id=environment_id,
        )

        return create_input_body
