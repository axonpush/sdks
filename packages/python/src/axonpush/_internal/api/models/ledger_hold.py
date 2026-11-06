from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerHold")


@_attrs_define
class LedgerHold:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        id (str):
        name (str):
        reason (str):
        state (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        agent_id (str | Unset):
        from_ (datetime.datetime | Unset):
        released_at (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
    """

    created_at: datetime.datetime
    created_by: str
    id: str
    name: str
    reason: str
    state: str
    schema: str | Unset = UNSET
    agent_id: str | Unset = UNSET
    from_: datetime.datetime | Unset = UNSET
    released_at: datetime.datetime | Unset = UNSET
    to: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        id = self.id

        name = self.name

        reason = self.reason

        state = self.state

        schema = self.schema

        agent_id = self.agent_id

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        released_at: str | Unset = UNSET
        if not isinstance(self.released_at, Unset):
            released_at = self.released_at.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "createdBy": created_by,
                "id": id,
                "name": name,
                "reason": reason,
                "state": state,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if from_ is not UNSET:
            field_dict["from"] = from_
        if released_at is not UNSET:
            field_dict["releasedAt"] = released_at
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        created_by = d.pop("createdBy")

        id = d.pop("id")

        name = d.pop("name")

        reason = d.pop("reason")

        state = d.pop("state")

        schema = d.pop("$schema", UNSET)

        agent_id = d.pop("agentId", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: datetime.datetime | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _released_at = d.pop("releasedAt", UNSET)
        released_at: datetime.datetime | Unset
        if isinstance(_released_at, Unset):
            released_at = UNSET
        else:
            released_at = isoparse(_released_at)

        _to = d.pop("to", UNSET)
        to: datetime.datetime | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        ledger_hold = cls(
            created_at=created_at,
            created_by=created_by,
            id=id,
            name=name,
            reason=reason,
            state=state,
            schema=schema,
            agent_id=agent_id,
            from_=from_,
            released_at=released_at,
            to=to,
        )

        return ledger_hold
