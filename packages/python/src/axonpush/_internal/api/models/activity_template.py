from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_workspace_spec import ActivityWorkspaceSpec


T = TypeVar("T", bound="ActivityTemplate")


@_attrs_define
class ActivityTemplate:
    """
    Attributes:
        id (str):
        spec (ActivityWorkspaceSpec):
        version (int):
        visibility (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    id: str
    spec: ActivityWorkspaceSpec
    version: int
    visibility: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_workspace_spec import ActivityWorkspaceSpec

        id = self.id

        spec = self.spec.to_dict()

        version = self.version

        visibility = self.visibility

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "spec": spec,
                "version": version,
                "visibility": visibility,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_workspace_spec import ActivityWorkspaceSpec

        d = dict(src_dict)
        id = d.pop("id")

        spec = ActivityWorkspaceSpec.from_dict(d.pop("spec"))

        version = d.pop("version")

        visibility = d.pop("visibility")

        schema = d.pop("$schema", UNSET)

        activity_template = cls(
            id=id,
            spec=spec,
            version=version,
            visibility=visibility,
            schema=schema,
        )

        return activity_template
