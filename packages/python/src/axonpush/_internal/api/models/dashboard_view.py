from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spec import Spec


T = TypeVar("T", bound="DashboardView")


@_attrs_define
class DashboardView:
    """
    Attributes:
        created_at (str):
        dashboard_id (str):
        name (str):
        spec (Spec):
        updated_at (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        created_by (str | Unset):
        description (str | Unset):
    """

    created_at: str
    dashboard_id: str
    name: str
    spec: Spec
    updated_at: str
    schema: str | Unset = UNSET
    created_by: str | Unset = UNSET
    description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.spec import Spec

        created_at = self.created_at

        dashboard_id = self.dashboard_id

        name = self.name

        spec = self.spec.to_dict()

        updated_at = self.updated_at

        schema = self.schema

        created_by = self.created_by

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "dashboardId": dashboard_id,
                "name": name,
                "spec": spec,
                "updatedAt": updated_at,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spec import Spec

        d = dict(src_dict)
        created_at = d.pop("createdAt")

        dashboard_id = d.pop("dashboardId")

        name = d.pop("name")

        spec = Spec.from_dict(d.pop("spec"))

        updated_at = d.pop("updatedAt")

        schema = d.pop("$schema", UNSET)

        created_by = d.pop("createdBy", UNSET)

        description = d.pop("description", UNSET)

        dashboard_view = cls(
            created_at=created_at,
            dashboard_id=dashboard_id,
            name=name,
            spec=spec,
            updated_at=updated_at,
            schema=schema,
            created_by=created_by,
            description=description,
        )

        return dashboard_view
