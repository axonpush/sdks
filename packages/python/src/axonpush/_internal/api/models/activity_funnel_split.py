from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_failure_count import ActivityFailureCount
    from ..models.activity_stage_count import ActivityStageCount


T = TypeVar("T", bound="ActivityFunnelSplit")


@_attrs_define
class ActivityFunnelSplit:
    """
    Attributes:
        entities (int):
        failure_categories (list[ActivityFailureCount] | None):
        failures (int):
        funnel (str):
        key (str):
        rejected (int):
        service_errors (int):
        stages (list[ActivityStageCount] | None):
        unclassified_failures (int):
        value (str):
    """

    entities: int
    failure_categories: list[ActivityFailureCount] | None
    failures: int
    funnel: str
    key: str
    rejected: int
    service_errors: int
    stages: list[ActivityStageCount] | None
    unclassified_failures: int
    value: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_failure_count import ActivityFailureCount
        from ..models.activity_stage_count import ActivityStageCount

        entities = self.entities

        failure_categories: list[dict[str, Any]] | None
        if isinstance(self.failure_categories, list):
            failure_categories = []
            for failure_categories_type_0_item_data in self.failure_categories:
                failure_categories_type_0_item = failure_categories_type_0_item_data.to_dict()
                failure_categories.append(failure_categories_type_0_item)

        else:
            failure_categories = self.failure_categories

        failures = self.failures

        funnel = self.funnel

        key = self.key

        rejected = self.rejected

        service_errors = self.service_errors

        stages: list[dict[str, Any]] | None
        if isinstance(self.stages, list):
            stages = []
            for stages_type_0_item_data in self.stages:
                stages_type_0_item = stages_type_0_item_data.to_dict()
                stages.append(stages_type_0_item)

        else:
            stages = self.stages

        unclassified_failures = self.unclassified_failures

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entities": entities,
                "failureCategories": failure_categories,
                "failures": failures,
                "funnel": funnel,
                "key": key,
                "rejected": rejected,
                "serviceErrors": service_errors,
                "stages": stages,
                "unclassifiedFailures": unclassified_failures,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_failure_count import ActivityFailureCount
        from ..models.activity_stage_count import ActivityStageCount

        d = dict(src_dict)
        entities = d.pop("entities")

        def _parse_failure_categories(data: object) -> list[ActivityFailureCount] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                failure_categories_type_0 = []
                _failure_categories_type_0 = data
                for failure_categories_type_0_item_data in _failure_categories_type_0:
                    failure_categories_type_0_item = ActivityFailureCount.from_dict(
                        failure_categories_type_0_item_data
                    )

                    failure_categories_type_0.append(failure_categories_type_0_item)

                return failure_categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityFailureCount] | None, data)

        failure_categories = _parse_failure_categories(d.pop("failureCategories"))

        failures = d.pop("failures")

        funnel = d.pop("funnel")

        key = d.pop("key")

        rejected = d.pop("rejected")

        service_errors = d.pop("serviceErrors")

        def _parse_stages(data: object) -> list[ActivityStageCount] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stages_type_0 = []
                _stages_type_0 = data
                for stages_type_0_item_data in _stages_type_0:
                    stages_type_0_item = ActivityStageCount.from_dict(stages_type_0_item_data)

                    stages_type_0.append(stages_type_0_item)

                return stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityStageCount] | None, data)

        stages = _parse_stages(d.pop("stages"))

        unclassified_failures = d.pop("unclassifiedFailures")

        value = d.pop("value")

        activity_funnel_split = cls(
            entities=entities,
            failure_categories=failure_categories,
            failures=failures,
            funnel=funnel,
            key=key,
            rejected=rejected,
            service_errors=service_errors,
            stages=stages,
            unclassified_failures=unclassified_failures,
            value=value,
        )

        return activity_funnel_split
