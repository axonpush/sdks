from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityFunnel")


@_attrs_define
class ActivityFunnel:
    """
    Attributes:
        entity (str):
        name (str):
        stages (list[str] | None):
    """

    entity: str
    name: str
    stages: list[str] | None

    def to_dict(self) -> dict[str, Any]:
        entity = self.entity

        name = self.name

        stages: list[str] | None
        if isinstance(self.stages, list):
            stages = self.stages

        else:
            stages = self.stages

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entity": entity,
                "name": name,
                "stages": stages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity = d.pop("entity")

        name = d.pop("name")

        def _parse_stages(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                stages_type_0 = cast(list[str], data)

                return stages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        stages = _parse_stages(d.pop("stages"))

        activity_funnel = cls(
            entity=entity,
            name=name,
            stages=stages,
        )

        return activity_funnel
