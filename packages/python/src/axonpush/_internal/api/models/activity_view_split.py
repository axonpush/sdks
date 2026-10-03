from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_activation_result import ActivityActivationResult
    from ..models.activity_stage_count import ActivityStageCount
    from ..models.activity_view_split_values import ActivityViewSplitValues


T = TypeVar("T", bound="ActivityViewSplit")


@_attrs_define
class ActivityViewSplit:
    """
    Attributes:
        entities (int):
        small_cohort (bool): Fewer entities than the view's minCohort: do not rank on it
        stages (list[ActivityStageCount] | None):
        values (ActivityViewSplitValues): Split key to value; unknown when the entity has none
        activation (ActivityActivationResult | Unset):
        completion (float | Unset): Entities reaching the last stage / entities reaching the first
    """

    entities: int
    small_cohort: bool
    stages: list[ActivityStageCount] | None
    values: ActivityViewSplitValues
    activation: ActivityActivationResult | Unset = UNSET
    completion: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_activation_result import ActivityActivationResult
        from ..models.activity_stage_count import ActivityStageCount
        from ..models.activity_view_split_values import ActivityViewSplitValues

        entities = self.entities

        small_cohort = self.small_cohort

        stages: list[dict[str, Any]] | None
        if isinstance(self.stages, list):
            stages = []
            for stages_type_0_item_data in self.stages:
                stages_type_0_item = stages_type_0_item_data.to_dict()
                stages.append(stages_type_0_item)

        else:
            stages = self.stages

        values = self.values.to_dict()

        activation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.activation, Unset):
            activation = self.activation.to_dict()

        completion = self.completion

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entities": entities,
                "smallCohort": small_cohort,
                "stages": stages,
                "values": values,
            }
        )
        if activation is not UNSET:
            field_dict["activation"] = activation
        if completion is not UNSET:
            field_dict["completion"] = completion

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_activation_result import ActivityActivationResult
        from ..models.activity_stage_count import ActivityStageCount
        from ..models.activity_view_split_values import ActivityViewSplitValues

        d = dict(src_dict)
        entities = d.pop("entities")

        small_cohort = d.pop("smallCohort")

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

        values = ActivityViewSplitValues.from_dict(d.pop("values"))

        _activation = d.pop("activation", UNSET)
        activation: ActivityActivationResult | Unset
        if isinstance(_activation, Unset):
            activation = UNSET
        else:
            activation = ActivityActivationResult.from_dict(_activation)

        completion = d.pop("completion", UNSET)

        activity_view_split = cls(
            entities=entities,
            small_cohort=small_cohort,
            stages=stages,
            values=values,
            activation=activation,
            completion=completion,
        )

        return activity_view_split
