from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Disposition")


@_attrs_define
class Disposition:
    """
    Attributes:
        actor (str):
        at (datetime.datetime):
        reason (str):
        state (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        owner (str | Unset):
    """

    actor: str
    at: datetime.datetime
    reason: str
    state: str
    schema: str | Unset = UNSET
    owner: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        actor = self.actor

        at = self.at.isoformat()

        reason = self.reason

        state = self.state

        schema = self.schema

        owner = self.owner

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "actor": actor,
                "at": at,
                "reason": reason,
                "state": state,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if owner is not UNSET:
            field_dict["owner"] = owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        actor = d.pop("actor")

        at = isoparse(d.pop("at"))

        reason = d.pop("reason")

        state = d.pop("state")

        schema = d.pop("$schema", UNSET)

        owner = d.pop("owner", UNSET)

        disposition = cls(
            actor=actor,
            at=at,
            reason=reason,
            state=state,
            schema=schema,
            owner=owner,
        )

        return disposition
