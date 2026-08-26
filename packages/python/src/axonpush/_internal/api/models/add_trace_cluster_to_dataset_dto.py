from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddTraceClusterToDatasetDto")


@_attrs_define
class AddTraceClusterToDatasetDto:
    """
    Attributes:
        dataset_id (str):
        max_traces (float | Unset):  Default: 100.0.
        note (str | Unset):
    """

    dataset_id: str
    max_traces: float | Unset = 100.0
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        max_traces = self.max_traces

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
            }
        )
        if max_traces is not UNSET:
            field_dict["maxTraces"] = max_traces
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        max_traces = d.pop("maxTraces", UNSET)

        note = d.pop("note", UNSET)

        add_trace_cluster_to_dataset_dto = cls(
            dataset_id=dataset_id,
            max_traces=max_traces,
            note=note,
        )

        add_trace_cluster_to_dataset_dto.additional_properties = d
        return add_trace_cluster_to_dataset_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
