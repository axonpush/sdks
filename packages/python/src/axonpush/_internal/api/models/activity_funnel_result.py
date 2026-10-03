from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_stage_count import ActivityStageCount


T = TypeVar("T", bound="ActivityFunnelResult")


@_attrs_define
class ActivityFunnelResult:
    """
    Attributes:
        name (str):
        stages (list[ActivityStageCount] | None):
    """

    name: str
    stages: list[ActivityStageCount] | None

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_stage_count import ActivityStageCount

        name = self.name

        stages: list[dict[str, Any]] | None
        if isinstance(self.stages, list):
            stages = []
            for stages_type_0_item_data in self.stages:
                stages_type_0_item = stages_type_0_item_data.to_dict()
                stages.append(stages_type_0_item)

        else:
            stages = self.stages

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "stages": stages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_stage_count import ActivityStageCount

        d = dict(src_dict)
        name = d.pop("name")

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

        activity_funnel_result = cls(
            name=name,
            stages=stages,
        )

        return activity_funnel_result
