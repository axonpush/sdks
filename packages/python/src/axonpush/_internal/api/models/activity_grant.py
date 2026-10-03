from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.activity_grant_principal_type import ActivityGrantPrincipalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityGrant")


@_attrs_define
class ActivityGrant:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        id (str):
        key (str): Scoping attribute (declared with scope: true)
        principal_id (str):
        principal_type (ActivityGrantPrincipalType):
        updated_at (datetime.datetime):
        values (list[str] | None):
        workspace_id (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    created_at: datetime.datetime
    created_by: str
    id: str
    key: str
    principal_id: str
    principal_type: ActivityGrantPrincipalType
    updated_at: datetime.datetime
    values: list[str] | None
    workspace_id: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        id = self.id

        key = self.key

        principal_id = self.principal_id

        principal_type = self.principal_type.value

        updated_at = self.updated_at.isoformat()

        values: list[str] | None
        if isinstance(self.values, list):
            values = self.values

        else:
            values = self.values

        workspace_id = self.workspace_id

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "createdBy": created_by,
                "id": id,
                "key": key,
                "principalId": principal_id,
                "principalType": principal_type,
                "updatedAt": updated_at,
                "values": values,
                "workspaceId": workspace_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        created_by = d.pop("createdBy")

        id = d.pop("id")

        key = d.pop("key")

        principal_id = d.pop("principalId")

        principal_type = ActivityGrantPrincipalType(d.pop("principalType"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_values(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = cast(list[str], data)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        values = _parse_values(d.pop("values"))

        workspace_id = d.pop("workspaceId")

        schema = d.pop("$schema", UNSET)

        activity_grant = cls(
            created_at=created_at,
            created_by=created_by,
            id=id,
            key=key,
            principal_id=principal_id,
            principal_type=principal_type,
            updated_at=updated_at,
            values=values,
            workspace_id=workspace_id,
            schema=schema,
        )

        return activity_grant
