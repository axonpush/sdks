from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_change import ActivityChange
    from ..models.activity_issue import ActivityIssue


T = TypeVar("T", bound="ChangesOutputBody")


@_attrs_define
class ChangesOutputBody:
    """
    Attributes:
        base_revision (str):
        changes (list[ActivityChange] | None):
        issues (list[ActivityIssue] | None):
        version (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    base_revision: str
    changes: list[ActivityChange] | None
    issues: list[ActivityIssue] | None
    version: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_change import ActivityChange
        from ..models.activity_issue import ActivityIssue

        base_revision = self.base_revision

        changes: list[dict[str, Any]] | None
        if isinstance(self.changes, list):
            changes = []
            for changes_type_0_item_data in self.changes:
                changes_type_0_item = changes_type_0_item_data.to_dict()
                changes.append(changes_type_0_item)

        else:
            changes = self.changes

        issues: list[dict[str, Any]] | None
        if isinstance(self.issues, list):
            issues = []
            for issues_type_0_item_data in self.issues:
                issues_type_0_item = issues_type_0_item_data.to_dict()
                issues.append(issues_type_0_item)

        else:
            issues = self.issues

        version = self.version

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "baseRevision": base_revision,
                "changes": changes,
                "issues": issues,
                "version": version,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_change import ActivityChange
        from ..models.activity_issue import ActivityIssue

        d = dict(src_dict)
        base_revision = d.pop("baseRevision")

        def _parse_changes(data: object) -> list[ActivityChange] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                changes_type_0 = []
                _changes_type_0 = data
                for changes_type_0_item_data in _changes_type_0:
                    changes_type_0_item = ActivityChange.from_dict(changes_type_0_item_data)

                    changes_type_0.append(changes_type_0_item)

                return changes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityChange] | None, data)

        changes = _parse_changes(d.pop("changes"))

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

        version = d.pop("version")

        schema = d.pop("$schema", UNSET)

        changes_output_body = cls(
            base_revision=base_revision,
            changes=changes,
            issues=issues,
            version=version,
            schema=schema,
        )

        return changes_output_body
