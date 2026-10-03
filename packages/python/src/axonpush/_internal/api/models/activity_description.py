from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_op_doc import ActivityOpDoc
    from ..models.activity_role_doc import ActivityRoleDoc
    from ..models.activity_workspace import ActivityWorkspace


T = TypeVar("T", bound="ActivityDescription")


@_attrs_define
class ActivityDescription:
    """
    Attributes:
        ops (list[ActivityOpDoc] | None):
        reference (str): The spec and observation format
        roles (list[ActivityRoleDoc] | None):
        summary (list[str] | None): One plain sentence per part of the current spec
        types (list[str] | None):
        workspace (ActivityWorkspace):
        schema (str | Unset): A URL to the JSON Schema for this object.
        draft (str | Unset): Pending draft status, if any
    """

    ops: list[ActivityOpDoc] | None
    reference: str
    roles: list[ActivityRoleDoc] | None
    summary: list[str] | None
    types: list[str] | None
    workspace: ActivityWorkspace
    schema: str | Unset = UNSET
    draft: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_op_doc import ActivityOpDoc
        from ..models.activity_role_doc import ActivityRoleDoc
        from ..models.activity_workspace import ActivityWorkspace

        ops: list[dict[str, Any]] | None
        if isinstance(self.ops, list):
            ops = []
            for ops_type_0_item_data in self.ops:
                ops_type_0_item = ops_type_0_item_data.to_dict()
                ops.append(ops_type_0_item)

        else:
            ops = self.ops

        reference = self.reference

        roles: list[dict[str, Any]] | None
        if isinstance(self.roles, list):
            roles = []
            for roles_type_0_item_data in self.roles:
                roles_type_0_item = roles_type_0_item_data.to_dict()
                roles.append(roles_type_0_item)

        else:
            roles = self.roles

        summary: list[str] | None
        if isinstance(self.summary, list):
            summary = self.summary

        else:
            summary = self.summary

        types: list[str] | None
        if isinstance(self.types, list):
            types = self.types

        else:
            types = self.types

        workspace = self.workspace.to_dict()

        schema = self.schema

        draft = self.draft

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ops": ops,
                "reference": reference,
                "roles": roles,
                "summary": summary,
                "types": types,
                "workspace": workspace,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if draft is not UNSET:
            field_dict["draft"] = draft

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_op_doc import ActivityOpDoc
        from ..models.activity_role_doc import ActivityRoleDoc
        from ..models.activity_workspace import ActivityWorkspace

        d = dict(src_dict)

        def _parse_ops(data: object) -> list[ActivityOpDoc] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ops_type_0 = []
                _ops_type_0 = data
                for ops_type_0_item_data in _ops_type_0:
                    ops_type_0_item = ActivityOpDoc.from_dict(ops_type_0_item_data)

                    ops_type_0.append(ops_type_0_item)

                return ops_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityOpDoc] | None, data)

        ops = _parse_ops(d.pop("ops"))

        reference = d.pop("reference")

        def _parse_roles(data: object) -> list[ActivityRoleDoc] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                roles_type_0 = []
                _roles_type_0 = data
                for roles_type_0_item_data in _roles_type_0:
                    roles_type_0_item = ActivityRoleDoc.from_dict(roles_type_0_item_data)

                    roles_type_0.append(roles_type_0_item)

                return roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityRoleDoc] | None, data)

        roles = _parse_roles(d.pop("roles"))

        def _parse_summary(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                summary_type_0 = cast(list[str], data)

                return summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        summary = _parse_summary(d.pop("summary"))

        def _parse_types(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                types_type_0 = cast(list[str], data)

                return types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        types = _parse_types(d.pop("types"))

        workspace = ActivityWorkspace.from_dict(d.pop("workspace"))

        schema = d.pop("$schema", UNSET)

        draft = d.pop("draft", UNSET)

        activity_description = cls(
            ops=ops,
            reference=reference,
            roles=roles,
            summary=summary,
            types=types,
            workspace=workspace,
            schema=schema,
            draft=draft,
        )

        return activity_description
