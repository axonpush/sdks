from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateHoldInputBody")


@_attrs_define
class CreateHoldInputBody:
    """
    Attributes:
        name (str):
        reason (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        agent_id (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
    """

    name: str
    reason: str
    schema: str | Unset = UNSET
    agent_id: str | Unset = UNSET
    from_: datetime.datetime | Unset = UNSET
    to: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        reason = self.reason

        schema = self.schema

        agent_id = self.agent_id

        from_: str | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.isoformat()

        to: str | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "reason": reason,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        reason = d.pop("reason")

        schema = d.pop("$schema", UNSET)

        agent_id = d.pop("agentId", UNSET)

        _from_ = d.pop("from", UNSET)
        from_: datetime.datetime | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = isoparse(_from_)

        _to = d.pop("to", UNSET)
        to: datetime.datetime | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = isoparse(_to)

        create_hold_input_body = cls(
            name=name,
            reason=reason,
            schema=schema,
            agent_id=agent_id,
            from_=from_,
            to=to,
        )

        return create_hold_input_body
