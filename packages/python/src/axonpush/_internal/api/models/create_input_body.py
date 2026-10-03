from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_workspace_spec import ActivityWorkspaceSpec


T = TypeVar("T", bound="CreateInputBody")


@_attrs_define
class CreateInputBody:
    """
    Attributes:
        app_id (str):
        spec (ActivityWorkspaceSpec):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    app_id: str
    spec: ActivityWorkspaceSpec
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_workspace_spec import ActivityWorkspaceSpec

        app_id = self.app_id

        spec = self.spec.to_dict()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "appId": app_id,
                "spec": spec,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_workspace_spec import ActivityWorkspaceSpec

        d = dict(src_dict)
        app_id = d.pop("appId")

        spec = ActivityWorkspaceSpec.from_dict(d.pop("spec"))

        schema = d.pop("$schema", UNSET)

        create_input_body = cls(
            app_id=app_id,
            spec=spec,
            schema=schema,
        )

        return create_input_body
