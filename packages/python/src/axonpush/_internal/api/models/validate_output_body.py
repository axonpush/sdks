from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validate_output_body_status import ValidateOutputBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_issue import ActivityIssue


T = TypeVar("T", bound="ValidateOutputBody")


@_attrs_define
class ValidateOutputBody:
    """
    Attributes:
        issues (list[ActivityIssue] | None):
        status (ValidateOutputBodyStatus):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    issues: list[ActivityIssue] | None
    status: ValidateOutputBodyStatus
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_issue import ActivityIssue

        issues: list[dict[str, Any]] | None
        if isinstance(self.issues, list):
            issues = []
            for issues_type_0_item_data in self.issues:
                issues_type_0_item = issues_type_0_item_data.to_dict()
                issues.append(issues_type_0_item)

        else:
            issues = self.issues

        status = self.status.value

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "issues": issues,
                "status": status,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_issue import ActivityIssue

        d = dict(src_dict)

        def _parse_issues(data: object) -> list[ActivityIssue] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                issues_type_0 = []
                _issues_type_0 = data
                for issues_type_0_item_data in _issues_type_0:
                    issues_type_0_item = ActivityIssue.from_dict(issues_type_0_item_data)

                    issues_type_0.append(issues_type_0_item)

                return issues_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityIssue] | None, data)

        issues = _parse_issues(d.pop("issues"))

        status = ValidateOutputBodyStatus(d.pop("status"))

        schema = d.pop("$schema", UNSET)

        validate_output_body = cls(
            issues=issues,
            status=status,
            schema=schema,
        )

        return validate_output_body
