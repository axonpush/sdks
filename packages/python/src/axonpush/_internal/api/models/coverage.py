from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Coverage")


@_attrs_define
class Coverage:
    """
    Attributes:
        checked_at (datetime.datetime):
        complete_through (datetime.datetime):
        healthy (bool):
        source (str):
    """

    checked_at: datetime.datetime
    complete_through: datetime.datetime
    healthy: bool
    source: str

    def to_dict(self) -> dict[str, Any]:
        checked_at = self.checked_at.isoformat()

        complete_through = self.complete_through.isoformat()

        healthy = self.healthy

        source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "checked_at": checked_at,
                "complete_through": complete_through,
                "healthy": healthy,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        checked_at = isoparse(d.pop("checked_at"))

        complete_through = isoparse(d.pop("complete_through"))

        healthy = d.pop("healthy")

        source = d.pop("source")

        coverage = cls(
            checked_at=checked_at,
            complete_through=complete_through,
            healthy=healthy,
            source=source,
        )

        return coverage
