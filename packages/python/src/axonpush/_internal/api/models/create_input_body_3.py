from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_input_body_3_category import CreateInputBody3Category
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_input_body_3_context import CreateInputBody3Context


T = TypeVar("T", bound="CreateInputBody3")


@_attrs_define
class CreateInputBody3:
    """
    Attributes:
        message (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        category (CreateInputBody3Category | Unset):
        context (CreateInputBody3Context | Unset):
    """

    message: str
    schema: str | Unset = UNSET
    category: CreateInputBody3Category | Unset = UNSET
    context: CreateInputBody3Context | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_input_body_3_context import CreateInputBody3Context

        message = self.message

        schema = self.schema

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "message": message,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if category is not UNSET:
            field_dict["category"] = category
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_input_body_3_context import CreateInputBody3Context

        d = dict(src_dict)
        message = d.pop("message")

        schema = d.pop("$schema", UNSET)

        _category = d.pop("category", UNSET)
        category: CreateInputBody3Category | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CreateInputBody3Category(_category)

        _context = d.pop("context", UNSET)
        context: CreateInputBody3Context | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = CreateInputBody3Context.from_dict(_context)

        create_input_body_3 = cls(
            message=message,
            schema=schema,
            category=category,
            context=context,
        )

        return create_input_body_3
