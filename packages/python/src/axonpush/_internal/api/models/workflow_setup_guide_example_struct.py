from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset


T = TypeVar("T", bound="WorkflowSetupGuideExampleStruct")


@_attrs_define
class WorkflowSetupGuideExampleStruct:
    """
    Attributes:
        fixture (str):
        label (str):
        source (str):
    """

    fixture: str
    label: str
    source: str

    def to_dict(self) -> dict[str, Any]:
        fixture = self.fixture

        label = self.label

        source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fixture": fixture,
                "label": label,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fixture = d.pop("fixture")

        label = d.pop("label")

        source = d.pop("source")

        workflow_setup_guide_example_struct = cls(
            fixture=fixture,
            label=label,
            source=source,
        )

        return workflow_setup_guide_example_struct
