from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityGraphNode")


@_attrs_define
class ActivityGraphNode:
    """
    Attributes:
        entity_id (str):
        id (str): type:id
        type_ (str):
        client (str | Unset):
        last_activity_at (datetime.datetime | Unset):
        side (str | Unset):
        state (str | Unset):
    """

    entity_id: str
    id: str
    type_: str
    client: str | Unset = UNSET
    last_activity_at: datetime.datetime | Unset = UNSET
    side: str | Unset = UNSET
    state: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        entity_id = self.entity_id

        id = self.id

        type_ = self.type_

        client = self.client

        last_activity_at: str | Unset = UNSET
        if not isinstance(self.last_activity_at, Unset):
            last_activity_at = self.last_activity_at.isoformat()

        side = self.side

        state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entityId": entity_id,
                "id": id,
                "type": type_,
            }
        )
        if client is not UNSET:
            field_dict["client"] = client
        if last_activity_at is not UNSET:
            field_dict["lastActivityAt"] = last_activity_at
        if side is not UNSET:
            field_dict["side"] = side
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_id = d.pop("entityId")

        id = d.pop("id")

        type_ = d.pop("type")

        client = d.pop("client", UNSET)

        _last_activity_at = d.pop("lastActivityAt", UNSET)
        last_activity_at: datetime.datetime | Unset
        if isinstance(_last_activity_at, Unset):
            last_activity_at = UNSET
        else:
            last_activity_at = isoparse(_last_activity_at)

        side = d.pop("side", UNSET)

        state = d.pop("state", UNSET)

        activity_graph_node = cls(
            entity_id=entity_id,
            id=id,
            type_=type_,
            client=client,
            last_activity_at=last_activity_at,
            side=side,
            state=state,
        )

        return activity_graph_node
