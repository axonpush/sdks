from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spec import Spec


T = TypeVar("T", bound="DashboardBody")


@_attrs_define
class DashboardBody:
    """
    Attributes:
        name (str):
        spec (Spec):
        schema (str | Unset): A URL to the JSON Schema for this object.
        description (str | Unset):
    """

    name: str
    spec: Spec
    schema: str | Unset = UNSET
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.spec import Spec

        name = self.name

        spec = self.spec.to_dict()

        schema = self.schema

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "spec": spec,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spec import Spec

        d = dict(src_dict)
        name = d.pop("name")

        spec = Spec.from_dict(d.pop("spec"))

        schema = d.pop("$schema", UNSET)

        description = d.pop("description", UNSET)

        dashboard_body = cls(
            name=name,
            spec=spec,
            schema=schema,
            description=description,
        )

        return dashboard_body
