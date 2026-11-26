from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stage import Stage


T = TypeVar("T", bound="Presentation")


@_attrs_define
class Presentation:
    """
    Attributes:
        title (str):
        stages (list[Stage] | None | Unset):
    """

    title: str
    stages: list[Stage] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.stage import Stage

        title = self.title

        stages: list[dict[str, Any]] | None | Unset
        if isinstance(self.stages, Unset):
            stages = UNSET
        elif isinstance(self.stages, list):
            stages = []
            for stages_type_0_item_data in self.stages:
                stages_type_0_item = stages_type_0_item_data.to_dict()
                stages.append(stages_type_0_item)

        else:
            stages = self.stages

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
            }
        )
        if stages is not UNSET:
            field_dict["stages"] = stages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stage import Stage

        d = dict(src_dict)
        title = d.pop("title")

        def _parse_stages(data: object) -> list[Stage] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stages_type_0 = []
                _stages_type_0 = data
                for stages_type_0_item_data in _stages_type_0:
                    stages_type_0_item = Stage.from_dict(stages_type_0_item_data)

                    stages_type_0.append(stages_type_0_item)

                return stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Stage] | None | Unset, data)

        stages = _parse_stages(d.pop("stages", UNSET))

        presentation = cls(
            title=title,
            stages=stages,
        )

        return presentation
