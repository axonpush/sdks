from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.definition import Definition


T = TypeVar("T", bound="DefinitionListBody")


@_attrs_define
class DefinitionListBody:
    """
    Attributes:
        definitions (list[Definition] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    definitions: list[Definition] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.definition import Definition

        definitions: list[dict[str, Any]] | None
        if isinstance(self.definitions, list):
            definitions = []
            for definitions_type_0_item_data in self.definitions:
                definitions_type_0_item = definitions_type_0_item_data.to_dict()
                definitions.append(definitions_type_0_item)

        else:
            definitions = self.definitions

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "definitions": definitions,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.definition import Definition

        d = dict(src_dict)

        def _parse_definitions(data: object) -> list[Definition] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                definitions_type_0 = []
                _definitions_type_0 = data
                for definitions_type_0_item_data in _definitions_type_0:
                    definitions_type_0_item = Definition.from_dict(definitions_type_0_item_data)

                    definitions_type_0.append(definitions_type_0_item)

                return definitions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Definition] | None, data)

        definitions = _parse_definitions(d.pop("definitions"))

        schema = d.pop("$schema", UNSET)

        definition_list_body = cls(
            definitions=definitions,
            schema=schema,
        )

        return definition_list_body
