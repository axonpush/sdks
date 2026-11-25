from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="WorkflowCaseUsage")


@_attrs_define
class WorkflowCaseUsage:
    """
    Attributes:
        enforced (bool):
        limit (int | None):
        period (str):
        remaining (int | None):
        resets_at (str):
        used (int):
    """

    enforced: bool
    limit: int | None
    period: str
    remaining: int | None
    resets_at: str
    used: int

    def to_dict(self) -> dict[str, Any]:
        enforced = self.enforced

        limit: int | None
        limit = self.limit

        period = self.period

        remaining: int | None
        remaining = self.remaining

        resets_at = self.resets_at

        used = self.used

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enforced": enforced,
                "limit": limit,
                "period": period,
                "remaining": remaining,
                "resetsAt": resets_at,
                "used": used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enforced = d.pop("enforced")

        def _parse_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        limit = _parse_limit(d.pop("limit"))

        period = d.pop("period")

        def _parse_remaining(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        remaining = _parse_remaining(d.pop("remaining"))

        resets_at = d.pop("resetsAt")

        used = d.pop("used")

        workflow_case_usage = cls(
            enforced=enforced,
            limit=limit,
            period=period,
            remaining=remaining,
            resets_at=resets_at,
            used=used,
        )

        return workflow_case_usage
