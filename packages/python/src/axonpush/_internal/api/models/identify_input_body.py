from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identify_input_body_traits import IdentifyInputBodyTraits


T = TypeVar("T", bound="IdentifyInputBody")


@_attrs_define
class IdentifyInputBody:
    """
    Attributes:
        entity (str): Entity type declared in the active spec
        id (str): Opaque entity identifier, the same value sent in refs
        traits (IdentifyInputBodyTraits): Keys from the entity's profile list; null deletes a trait
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    entity: str
    id: str
    traits: IdentifyInputBodyTraits
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.identify_input_body_traits import IdentifyInputBodyTraits

        entity = self.entity

        id = self.id

        traits = self.traits.to_dict()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entity": entity,
                "id": id,
                "traits": traits,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identify_input_body_traits import IdentifyInputBodyTraits

        d = dict(src_dict)
        entity = d.pop("entity")

        id = d.pop("id")

        traits = IdentifyInputBodyTraits.from_dict(d.pop("traits"))

        schema = d.pop("$schema", UNSET)

        identify_input_body = cls(
            entity=entity,
            id=id,
            traits=traits,
            schema=schema,
        )

        return identify_input_body
