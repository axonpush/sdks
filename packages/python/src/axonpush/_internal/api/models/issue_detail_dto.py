from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.breadcrumb_dto import BreadcrumbDTO
    from ..models.error_issue_dto import ErrorIssueDTO
    from ..models.event_dto import EventDTO
    from ..models.issue_bucket_dto import IssueBucketDTO
    from ..models.stack_frame_dto import StackFrameDTO
    from ..models.tag_distribution_dto import TagDistributionDTO


T = TypeVar("T", bound="IssueDetailDTO")


@_attrs_define
class IssueDetailDTO:
    """
    Attributes:
        affected_trace_ids (list[str] | None):
        breadcrumbs (list[BreadcrumbDTO] | None):
        issue (ErrorIssueDTO):
        occurrences (list[IssueBucketDTO] | None):
        stack (list[StackFrameDTO] | None):
        tags (list[TagDistributionDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        resolved_at (str | Unset):
        resolved_in_release (str | Unset):
        sample_event (EventDTO | Unset):
        snooze_until (str | Unset):
    """

    affected_trace_ids: list[str] | None
    breadcrumbs: list[BreadcrumbDTO] | None
    issue: ErrorIssueDTO
    occurrences: list[IssueBucketDTO] | None
    stack: list[StackFrameDTO] | None
    tags: list[TagDistributionDTO] | None
    schema: str | Unset = UNSET
    resolved_at: str | Unset = UNSET
    resolved_in_release: str | Unset = UNSET
    sample_event: EventDTO | Unset = UNSET
    snooze_until: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.breadcrumb_dto import BreadcrumbDTO
        from ..models.error_issue_dto import ErrorIssueDTO
        from ..models.event_dto import EventDTO
        from ..models.issue_bucket_dto import IssueBucketDTO
        from ..models.stack_frame_dto import StackFrameDTO
        from ..models.tag_distribution_dto import TagDistributionDTO

        affected_trace_ids: list[str] | None
        if isinstance(self.affected_trace_ids, list):
            affected_trace_ids = self.affected_trace_ids

        else:
            affected_trace_ids = self.affected_trace_ids

        breadcrumbs: list[dict[str, Any]] | None
        if isinstance(self.breadcrumbs, list):
            breadcrumbs = []
            for breadcrumbs_type_0_item_data in self.breadcrumbs:
                breadcrumbs_type_0_item = breadcrumbs_type_0_item_data.to_dict()
                breadcrumbs.append(breadcrumbs_type_0_item)

        else:
            breadcrumbs = self.breadcrumbs

        issue = self.issue.to_dict()

        occurrences: list[dict[str, Any]] | None
        if isinstance(self.occurrences, list):
            occurrences = []
            for occurrences_type_0_item_data in self.occurrences:
                occurrences_type_0_item = occurrences_type_0_item_data.to_dict()
                occurrences.append(occurrences_type_0_item)

        else:
            occurrences = self.occurrences

        stack: list[dict[str, Any]] | None
        if isinstance(self.stack, list):
            stack = []
            for stack_type_0_item_data in self.stack:
                stack_type_0_item = stack_type_0_item_data.to_dict()
                stack.append(stack_type_0_item)

        else:
            stack = self.stack

        tags: list[dict[str, Any]] | None
        if isinstance(self.tags, list):
            tags = []
            for tags_type_0_item_data in self.tags:
                tags_type_0_item = tags_type_0_item_data.to_dict()
                tags.append(tags_type_0_item)

        else:
            tags = self.tags

        schema = self.schema

        resolved_at = self.resolved_at

        resolved_in_release = self.resolved_in_release

        sample_event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sample_event, Unset):
            sample_event = self.sample_event.to_dict()

        snooze_until = self.snooze_until

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "affectedTraceIds": affected_trace_ids,
                "breadcrumbs": breadcrumbs,
                "issue": issue,
                "occurrences": occurrences,
                "stack": stack,
                "tags": tags,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if resolved_at is not UNSET:
            field_dict["resolvedAt"] = resolved_at
        if resolved_in_release is not UNSET:
            field_dict["resolvedInRelease"] = resolved_in_release
        if sample_event is not UNSET:
            field_dict["sampleEvent"] = sample_event
        if snooze_until is not UNSET:
            field_dict["snoozeUntil"] = snooze_until

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.breadcrumb_dto import BreadcrumbDTO
        from ..models.error_issue_dto import ErrorIssueDTO
        from ..models.event_dto import EventDTO
        from ..models.issue_bucket_dto import IssueBucketDTO
        from ..models.stack_frame_dto import StackFrameDTO
        from ..models.tag_distribution_dto import TagDistributionDTO

        d = dict(src_dict)

        def _parse_affected_trace_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                affected_trace_ids_type_0 = cast(list[str], data)

                return affected_trace_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        affected_trace_ids = _parse_affected_trace_ids(d.pop("affectedTraceIds"))

        def _parse_breadcrumbs(data: object) -> list[BreadcrumbDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                breadcrumbs_type_0 = []
                _breadcrumbs_type_0 = data
                for breadcrumbs_type_0_item_data in _breadcrumbs_type_0:
                    breadcrumbs_type_0_item = BreadcrumbDTO.from_dict(breadcrumbs_type_0_item_data)

                    breadcrumbs_type_0.append(breadcrumbs_type_0_item)

                return breadcrumbs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BreadcrumbDTO] | None, data)

        breadcrumbs = _parse_breadcrumbs(d.pop("breadcrumbs"))

        issue = ErrorIssueDTO.from_dict(d.pop("issue"))

        def _parse_occurrences(data: object) -> list[IssueBucketDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                occurrences_type_0 = []
                _occurrences_type_0 = data
                for occurrences_type_0_item_data in _occurrences_type_0:
                    occurrences_type_0_item = IssueBucketDTO.from_dict(occurrences_type_0_item_data)

                    occurrences_type_0.append(occurrences_type_0_item)

                return occurrences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IssueBucketDTO] | None, data)

        occurrences = _parse_occurrences(d.pop("occurrences"))

        def _parse_stack(data: object) -> list[StackFrameDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stack_type_0 = []
                _stack_type_0 = data
                for stack_type_0_item_data in _stack_type_0:
                    stack_type_0_item = StackFrameDTO.from_dict(stack_type_0_item_data)

                    stack_type_0.append(stack_type_0_item)

                return stack_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StackFrameDTO] | None, data)

        stack = _parse_stack(d.pop("stack"))

        def _parse_tags(data: object) -> list[TagDistributionDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = []
                _tags_type_0 = data
                for tags_type_0_item_data in _tags_type_0:
                    tags_type_0_item = TagDistributionDTO.from_dict(tags_type_0_item_data)

                    tags_type_0.append(tags_type_0_item)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TagDistributionDTO] | None, data)

        tags = _parse_tags(d.pop("tags"))

        schema = d.pop("$schema", UNSET)

        resolved_at = d.pop("resolvedAt", UNSET)

        resolved_in_release = d.pop("resolvedInRelease", UNSET)

        _sample_event = d.pop("sampleEvent", UNSET)
        sample_event: EventDTO | Unset
        if isinstance(_sample_event, Unset):
            sample_event = UNSET
        else:
            sample_event = EventDTO.from_dict(_sample_event)

        snooze_until = d.pop("snoozeUntil", UNSET)

        issue_detail_dto = cls(
            affected_trace_ids=affected_trace_ids,
            breadcrumbs=breadcrumbs,
            issue=issue,
            occurrences=occurrences,
            stack=stack,
            tags=tags,
            schema=schema,
            resolved_at=resolved_at,
            resolved_in_release=resolved_in_release,
            sample_event=sample_event,
            snooze_until=snooze_until,
        )

        return issue_detail_dto
