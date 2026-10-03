from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.grant_input_body_principal_type import GrantInputBodyPrincipalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GrantInputBody")


@_attrs_define
class GrantInputBody:
    """
    Attributes:
        key (str): Attribute declared with scope: true
        principal_id (str): Member user id or API key id
        principal_type (GrantInputBodyPrincipalType):
        values (list[str] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    key: str
    principal_id: str
    principal_type: GrantInputBodyPrincipalType
    values: list[str] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        principal_id = self.principal_id

        principal_type = self.principal_type.value

        values: list[str] | None
        if isinstance(self.values, list):
            values = self.values

        else:
            values = self.values

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "principalId": principal_id,
                "principalType": principal_type,
                "values": values,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        principal_id = d.pop("principalId")

        principal_type = GrantInputBodyPrincipalType(d.pop("principalType"))

        def _parse_values(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = cast(list[str], data)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        values = _parse_values(d.pop("values"))

        schema = d.pop("$schema", UNSET)

        grant_input_body = cls(
            key=key,
            principal_id=principal_id,
            principal_type=principal_type,
            values=values,
            schema=schema,
        )

        return grant_input_body
