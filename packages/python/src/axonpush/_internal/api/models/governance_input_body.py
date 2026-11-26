from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GovernanceInputBody")


@_attrs_define
class GovernanceInputBody:
    """
    Attributes:
        confirm (bool): Confirm shortening and preserving an immutable timestamped reason until the original expiry
        reason (str):
        retain_until (datetime.datetime):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    confirm: bool
    reason: str
    retain_until: datetime.datetime
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        confirm = self.confirm

        reason = self.reason

        retain_until = self.retain_until.isoformat()

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "confirm": confirm,
                "reason": reason,
                "retainUntil": retain_until,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirm = d.pop("confirm")

        reason = d.pop("reason")

        retain_until = isoparse(d.pop("retainUntil"))

        schema = d.pop("$schema", UNSET)

        governance_input_body = cls(
            confirm=confirm,
            reason=reason,
            retain_until=retain_until,
            schema=schema,
        )

        return governance_input_body
