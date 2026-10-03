from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_draft import ActivityDraft
    from ..models.activity_issue import ActivityIssue


T = TypeVar("T", bound="ActivityDraftView")


@_attrs_define
class ActivityDraftView:
    """
    Attributes:
        draft (ActivityDraft):
        issues (list[ActivityIssue] | None): Validation issues in the draft; errors block activation, warnings mean a
            view or feature will render empty
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    draft: ActivityDraft
    issues: list[ActivityIssue] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_draft import ActivityDraft
        from ..models.activity_issue import ActivityIssue

        draft = self.draft.to_dict()

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
                "draft": draft,
                "issues": issues,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_draft import ActivityDraft
        from ..models.activity_issue import ActivityIssue

        d = dict(src_dict)
        draft = ActivityDraft.from_dict(d.pop("draft"))

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

        schema = d.pop("$schema", UNSET)

        activity_draft_view = cls(
            draft=draft,
            issues=issues,
            schema=schema,
        )

        return activity_draft_view
