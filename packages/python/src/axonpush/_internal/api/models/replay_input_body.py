from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplayInputBody")


@_attrs_define
class ReplayInputBody:
    """
    Attributes:
        apply (bool):
        now (datetime.datetime):
        version_id (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    apply: bool
    now: datetime.datetime
    version_id: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        apply = self.apply

        now = self.now.isoformat()

        version_id = self.version_id

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "apply": apply,
                "now": now,
                "version_id": version_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        apply = d.pop("apply")

        now = isoparse(d.pop("now"))

        version_id = d.pop("version_id")

        schema = d.pop("$schema", UNSET)

        replay_input_body = cls(
            apply=apply,
            now=now,
            version_id=version_id,
            schema=schema,
        )

        return replay_input_body
