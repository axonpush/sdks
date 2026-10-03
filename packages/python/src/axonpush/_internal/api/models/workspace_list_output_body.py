from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_workspace import ActivityWorkspace


T = TypeVar("T", bound="WorkspaceListOutputBody")


@_attrs_define
class WorkspaceListOutputBody:
    """
    Attributes:
        workspaces (list[ActivityWorkspace] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    workspaces: list[ActivityWorkspace] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_workspace import ActivityWorkspace

        workspaces: list[dict[str, Any]] | None
        if isinstance(self.workspaces, list):
            workspaces = []
            for workspaces_type_0_item_data in self.workspaces:
                workspaces_type_0_item = workspaces_type_0_item_data.to_dict()
                workspaces.append(workspaces_type_0_item)

        else:
            workspaces = self.workspaces

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspaces": workspaces,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_workspace import ActivityWorkspace

        d = dict(src_dict)

        def _parse_workspaces(data: object) -> list[ActivityWorkspace] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                workspaces_type_0 = []
                _workspaces_type_0 = data
                for workspaces_type_0_item_data in _workspaces_type_0:
                    workspaces_type_0_item = ActivityWorkspace.from_dict(
                        workspaces_type_0_item_data
                    )

                    workspaces_type_0.append(workspaces_type_0_item)

                return workspaces_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityWorkspace] | None, data)

        workspaces = _parse_workspaces(d.pop("workspaces"))

        schema = d.pop("$schema", UNSET)

        workspace_list_output_body = cls(
            workspaces=workspaces,
            schema=schema,
        )

        return workspace_list_output_body
