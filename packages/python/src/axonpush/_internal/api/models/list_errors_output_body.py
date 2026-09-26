from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_issue_dto import ErrorIssueDTO


T = TypeVar("T", bound="ListErrorsOutputBody")


@_attrs_define
class ListErrorsOutputBody:
    """
    Attributes:
        issues (list[ErrorIssueDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    issues: list[ErrorIssueDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.error_issue_dto import ErrorIssueDTO

        issues: list[dict[str, Any]] | None
        if isinstance(self.issues, list):
            issues = []
            for issues_type_0_item_data in self.issues:
                issues_type_0_item = issues_type_0_item_data.to_dict()
                issues.append(issues_type_0_item)

        else:
            issues = self.issues

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "issues": issues,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_issue_dto import ErrorIssueDTO

        d = dict(src_dict)

        def _parse_issues(data: object) -> list[ErrorIssueDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                issues_type_0 = []
                _issues_type_0 = data
                for issues_type_0_item_data in _issues_type_0:
                    issues_type_0_item = ErrorIssueDTO.from_dict(issues_type_0_item_data)

                    issues_type_0.append(issues_type_0_item)

                return issues_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ErrorIssueDTO] | None, data)

        issues = _parse_issues(d.pop("issues"))

        schema = d.pop("$schema", UNSET)

        list_errors_output_body = cls(
            issues=issues,
            schema=schema,
        )

        return list_errors_output_body
