from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInputBody3")


@_attrs_define
class CreateInputBody3:
    """
    Attributes:
        company (str):
        email (str):
        use_case (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        name (str | Unset):
    """

    company: str
    email: str
    use_case: str
    schema: str | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        company = self.company

        email = self.email

        use_case = self.use_case

        schema = self.schema

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "company": company,
                "email": email,
                "useCase": use_case,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company = d.pop("company")

        email = d.pop("email")

        use_case = d.pop("useCase")

        schema = d.pop("$schema", UNSET)

        name = d.pop("name", UNSET)

        create_input_body_3 = cls(
            company=company,
            email=email,
            use_case=use_case,
            schema=schema,
            name=name,
        )

        return create_input_body_3
