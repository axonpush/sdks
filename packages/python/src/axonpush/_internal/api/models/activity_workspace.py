from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityWorkspace")


@_attrs_define
class ActivityWorkspace:
    """
    Attributes:
        active_revision (None | str):
        app_id (str):
        created_at (datetime.datetime):
        generation (int):
        id (str):
        name (str):
        requested_revision (None | str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    active_revision: None | str
    app_id: str
    created_at: datetime.datetime
    generation: int
    id: str
    name: str
    requested_revision: None | str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        active_revision: None | str
        active_revision = self.active_revision

        app_id = self.app_id

        created_at = self.created_at.isoformat()

        generation = self.generation

        id = self.id

        name = self.name

        requested_revision: None | str
        requested_revision = self.requested_revision

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "activeRevision": active_revision,
                "appId": app_id,
                "createdAt": created_at,
                "generation": generation,
                "id": id,
                "name": name,
                "requestedRevision": requested_revision,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_active_revision(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        active_revision = _parse_active_revision(d.pop("activeRevision"))

        app_id = d.pop("appId")

        created_at = isoparse(d.pop("createdAt"))

        generation = d.pop("generation")

        id = d.pop("id")

        name = d.pop("name")

        def _parse_requested_revision(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        requested_revision = _parse_requested_revision(d.pop("requestedRevision"))

        schema = d.pop("$schema", UNSET)

        activity_workspace = cls(
            active_revision=active_revision,
            app_id=app_id,
            created_at=created_at,
            generation=generation,
            id=id,
            name=name,
            requested_revision=requested_revision,
            schema=schema,
        )

        return activity_workspace
