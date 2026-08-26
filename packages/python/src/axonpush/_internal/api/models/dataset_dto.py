from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetDto")


@_attrs_define
class DatasetDto:
    """
    Attributes:
        created_at (datetime.datetime):
        dataset_id (str):
        item_count (float):
        latest_revision (float):
        name (str):
        org_id (str):
        updated_at (datetime.datetime):
        description (str | Unset):
    """

    created_at: datetime.datetime
    dataset_id: str
    item_count: float
    latest_revision: float
    name: str
    org_id: str
    updated_at: datetime.datetime
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        dataset_id = self.dataset_id

        item_count = self.item_count

        latest_revision = self.latest_revision

        name = self.name

        org_id = self.org_id

        updated_at = self.updated_at.isoformat()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "datasetId": dataset_id,
                "itemCount": item_count,
                "latestRevision": latest_revision,
                "name": name,
                "orgId": org_id,
                "updatedAt": updated_at,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        dataset_id = d.pop("datasetId")

        item_count = d.pop("itemCount")

        latest_revision = d.pop("latestRevision")

        name = d.pop("name")

        org_id = d.pop("orgId")

        updated_at = isoparse(d.pop("updatedAt"))

        description = d.pop("description", UNSET)

        dataset_dto = cls(
            created_at=created_at,
            dataset_id=dataset_id,
            item_count=item_count,
            latest_revision=latest_revision,
            name=name,
            org_id=org_id,
            updated_at=updated_at,
            description=description,
        )

        dataset_dto.additional_properties = d
        return dataset_dto

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
