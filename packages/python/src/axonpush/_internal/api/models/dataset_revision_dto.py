from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DatasetRevisionDto")


@_attrs_define
class DatasetRevisionDto:
    """
    Attributes:
        content_hash (str):
        created_at (datetime.datetime):
        dataset_id (str):
        item_count (float):
        org_id (str):
        revision (float):
        source (str):
    """

    content_hash: str
    created_at: datetime.datetime
    dataset_id: str
    item_count: float
    org_id: str
    revision: float
    source: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_hash = self.content_hash

        created_at = self.created_at.isoformat()

        dataset_id = self.dataset_id

        item_count = self.item_count

        org_id = self.org_id

        revision = self.revision

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contentHash": content_hash,
                "createdAt": created_at,
                "datasetId": dataset_id,
                "itemCount": item_count,
                "orgId": org_id,
                "revision": revision,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_hash = d.pop("contentHash")

        created_at = isoparse(d.pop("createdAt"))

        dataset_id = d.pop("datasetId")

        item_count = d.pop("itemCount")

        org_id = d.pop("orgId")

        revision = d.pop("revision")

        source = d.pop("source")

        dataset_revision_dto = cls(
            content_hash=content_hash,
            created_at=created_at,
            dataset_id=dataset_id,
            item_count=item_count,
            org_id=org_id,
            revision=revision,
            source=source,
        )

        dataset_revision_dto.additional_properties = d
        return dataset_revision_dto

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
