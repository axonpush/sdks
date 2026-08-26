from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_revision_source import DatasetRevisionSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_item_input_dto import DatasetItemInputDto


T = TypeVar("T", bound="CreateDatasetRevisionDto")


@_attrs_define
class CreateDatasetRevisionDto:
    """
    Attributes:
        items (list[DatasetItemInputDto]):
        note (str | Unset):
        source (DatasetRevisionSource | Unset):
    """

    items: list[DatasetItemInputDto]
    note: str | Unset = UNSET
    source: DatasetRevisionSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_item_input_dto import DatasetItemInputDto

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        note = self.note

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_item_input_dto import DatasetItemInputDto

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = DatasetItemInputDto.from_dict(items_item_data)

            items.append(items_item)

        note = d.pop("note", UNSET)

        _source = d.pop("source", UNSET)
        source: DatasetRevisionSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = DatasetRevisionSource(_source)

        create_dataset_revision_dto = cls(
            items=items,
            note=note,
            source=source,
        )

        create_dataset_revision_dto.additional_properties = d
        return create_dataset_revision_dto

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
