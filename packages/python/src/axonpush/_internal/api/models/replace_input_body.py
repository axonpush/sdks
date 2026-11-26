from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_workspace_spec import ActivityWorkspaceSpec


T = TypeVar("T", bound="ReplaceInputBody")


@_attrs_define
class ReplaceInputBody:
    """
    Attributes:
        spec (ActivityWorkspaceSpec):
        version (int): The draft version you edited
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    spec: ActivityWorkspaceSpec
    version: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_workspace_spec import ActivityWorkspaceSpec

        spec = self.spec.to_dict()

        version = self.version

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "spec": spec,
                "version": version,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_workspace_spec import ActivityWorkspaceSpec

        d = dict(src_dict)
        spec = ActivityWorkspaceSpec.from_dict(d.pop("spec"))

        version = d.pop("version")

        schema = d.pop("$schema", UNSET)

        replace_input_body = cls(
            spec=spec,
            version=version,
            schema=schema,
        )

        return replace_input_body
