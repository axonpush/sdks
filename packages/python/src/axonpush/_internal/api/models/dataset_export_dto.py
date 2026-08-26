from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_export_format import DatasetExportFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetExportDto")


@_attrs_define
class DatasetExportDto:
    """
    Attributes:
        content (str):
        filename (str):
        format_ (DatasetExportFormat):
    """

    content: str
    filename: str
    format_: DatasetExportFormat
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        filename = self.filename

        format_ = self.format_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "filename": filename,
                "format": format_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        filename = d.pop("filename")

        format_ = DatasetExportFormat(d.pop("format"))

        dataset_export_dto = cls(
            content=content,
            filename=filename,
            format_=format_,
        )

        dataset_export_dto.additional_properties = d
        return dataset_export_dto

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
