from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_workspace_spec import ActivityWorkspaceSpec


T = TypeVar("T", bound="ActivityRevision")


@_attrs_define
class ActivityRevision:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        id (str):
        spec (ActivityWorkspaceSpec):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    created_at: datetime.datetime
    created_by: str
    id: str
    spec: ActivityWorkspaceSpec
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_workspace_spec import ActivityWorkspaceSpec

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        id = self.id

        spec = self.spec.to_dict()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "createdBy": created_by,
                "id": id,
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
        created_at = isoparse(d.pop("createdAt"))

        created_by = d.pop("createdBy")

        id = d.pop("id")

        spec = ActivityWorkspaceSpec.from_dict(d.pop("spec"))

        schema = d.pop("$schema", UNSET)

        activity_revision = cls(
            created_at=created_at,
            created_by=created_by,
            id=id,
            spec=spec,
            schema=schema,
        )

        return activity_revision
