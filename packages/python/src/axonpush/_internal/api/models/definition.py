from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bundle import Bundle


T = TypeVar("T", bound="Definition")


@_attrs_define
class Definition:
    """
    Attributes:
        bundle (Bundle):
        id (str):
        source (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    bundle: Bundle
    id: str
    source: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.bundle import Bundle

        bundle = self.bundle.to_dict()

        id = self.id

        source = self.source

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bundle": bundle,
                "id": id,
                "source": source,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bundle import Bundle

        d = dict(src_dict)
        bundle = Bundle.from_dict(d.pop("bundle"))

        id = d.pop("id")

        source = d.pop("source")

        schema = d.pop("$schema", UNSET)

        definition = cls(
            bundle=bundle,
            id=id,
            source=source,
            schema=schema,
        )

        return definition
