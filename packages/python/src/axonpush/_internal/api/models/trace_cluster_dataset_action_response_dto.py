from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceClusterDatasetActionResponseDto")


@_attrs_define
class TraceClusterDatasetActionResponseDto:
    """
    Attributes:
        dataset_id (str):
        item_count (float):
        revision (float):
    """

    dataset_id: str
    item_count: float
    revision: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_id = self.dataset_id

        item_count = self.item_count

        revision = self.revision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "datasetId": dataset_id,
                "itemCount": item_count,
                "revision": revision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dataset_id = d.pop("datasetId")

        item_count = d.pop("itemCount")

        revision = d.pop("revision")

        trace_cluster_dataset_action_response_dto = cls(
            dataset_id=dataset_id,
            item_count=item_count,
            revision=revision,
        )

        trace_cluster_dataset_action_response_dto.additional_properties = d
        return trace_cluster_dataset_action_response_dto

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
