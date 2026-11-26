from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.activity_draft_updated_source import ActivityDraftUpdatedSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_workspace_spec import ActivityWorkspaceSpec


T = TypeVar("T", bound="ActivityDraft")


@_attrs_define
class ActivityDraft:
    """
    Attributes:
        base_revision (str): Revision the draft started from; changes are listed against the current active or building
            revision
        spec (ActivityWorkspaceSpec):
        updated_at (datetime.datetime):
        updated_by (str):
        updated_source (ActivityDraftUpdatedSource):
        version (int): Send this back with ops; it increments on every edit
        workspace_id (str):
        updated_client (str | Unset): MCP client name when the edit came from a coding agent
    """

    base_revision: str
    spec: ActivityWorkspaceSpec
    updated_at: datetime.datetime
    updated_by: str
    updated_source: ActivityDraftUpdatedSource
    version: int
    workspace_id: str
    updated_client: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_workspace_spec import ActivityWorkspaceSpec

        base_revision = self.base_revision

        spec = self.spec.to_dict()

        updated_at = self.updated_at.isoformat()

        updated_by = self.updated_by

        updated_source = self.updated_source.value

        version = self.version

        workspace_id = self.workspace_id

        updated_client = self.updated_client

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "baseRevision": base_revision,
                "spec": spec,
                "updatedAt": updated_at,
                "updatedBy": updated_by,
                "updatedSource": updated_source,
                "version": version,
                "workspaceId": workspace_id,
            }
        )
        if updated_client is not UNSET:
            field_dict["updatedClient"] = updated_client

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_workspace_spec import ActivityWorkspaceSpec

        d = dict(src_dict)
        base_revision = d.pop("baseRevision")

        spec = ActivityWorkspaceSpec.from_dict(d.pop("spec"))

        updated_at = isoparse(d.pop("updatedAt"))

        updated_by = d.pop("updatedBy")

        updated_source = ActivityDraftUpdatedSource(d.pop("updatedSource"))

        version = d.pop("version")

        workspace_id = d.pop("workspaceId")

        updated_client = d.pop("updatedClient", UNSET)

        activity_draft = cls(
            base_revision=base_revision,
            spec=spec,
            updated_at=updated_at,
            updated_by=updated_by,
            updated_source=updated_source,
            version=version,
            workspace_id=workspace_id,
            updated_client=updated_client,
        )

        return activity_draft
