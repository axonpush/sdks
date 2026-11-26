from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_issue_severity import ActivityIssueSeverity
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityIssue")


@_attrs_define
class ActivityIssue:
    """
    Attributes:
        message (str):
        path (str):
        severity (ActivityIssueSeverity):
    """

    message: str
    path: str
    severity: ActivityIssueSeverity

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        path = self.path

        severity = self.severity.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "message": message,
                "path": path,
                "severity": severity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        path = d.pop("path")

        severity = ActivityIssueSeverity(d.pop("severity"))

        activity_issue = cls(
            message=message,
            path=path,
            severity=severity,
        )

        return activity_issue
