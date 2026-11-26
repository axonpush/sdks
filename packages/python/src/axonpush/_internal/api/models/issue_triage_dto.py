from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueTriageDTO")


@_attrs_define
class IssueTriageDTO:
    """
    Attributes:
        fingerprint (str):
        regressed (bool):
        status (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        assignee (str | Unset):
        resolved_at (str | Unset):
        resolved_in_release (str | Unset):
        snooze_until (str | Unset):
    """

    fingerprint: str
    regressed: bool
    status: str
    schema: str | Unset = UNSET
    assignee: str | Unset = UNSET
    resolved_at: str | Unset = UNSET
    resolved_in_release: str | Unset = UNSET
    snooze_until: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        fingerprint = self.fingerprint

        regressed = self.regressed

        status = self.status

        schema = self.schema

        assignee = self.assignee

        resolved_at = self.resolved_at

        resolved_in_release = self.resolved_in_release

        snooze_until = self.snooze_until

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fingerprint": fingerprint,
                "regressed": regressed,
                "status": status,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if resolved_at is not UNSET:
            field_dict["resolvedAt"] = resolved_at
        if resolved_in_release is not UNSET:
            field_dict["resolvedInRelease"] = resolved_in_release
        if snooze_until is not UNSET:
            field_dict["snoozeUntil"] = snooze_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fingerprint = d.pop("fingerprint")

        regressed = d.pop("regressed")

        status = d.pop("status")

        schema = d.pop("$schema", UNSET)

        assignee = d.pop("assignee", UNSET)

        resolved_at = d.pop("resolvedAt", UNSET)

        resolved_in_release = d.pop("resolvedInRelease", UNSET)

        snooze_until = d.pop("snoozeUntil", UNSET)

        issue_triage_dto = cls(
            fingerprint=fingerprint,
            regressed=regressed,
            status=status,
            schema=schema,
            assignee=assignee,
            resolved_at=resolved_at,
            resolved_in_release=resolved_in_release,
            snooze_until=snooze_until,
        )

        return issue_triage_dto
