from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_export_format import DatasetExportFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImportDatasetRevisionDto")


@_attrs_define
class ImportDatasetRevisionDto:
    """
    Attributes:
        content (str): UTF-8 JSONL or CSV content.
        format_ (DatasetExportFormat):
        note (str | Unset):
    """

    content: str
    format_: DatasetExportFormat
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        format_ = self.format_.value

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "format": format_,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        format_ = DatasetExportFormat(d.pop("format"))

        note = d.pop("note", UNSET)

        import_dataset_revision_dto = cls(
            content=content,
            format_=format_,
            note=note,
        )

        import_dataset_revision_dto.additional_properties = d
        return import_dataset_revision_dto

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
