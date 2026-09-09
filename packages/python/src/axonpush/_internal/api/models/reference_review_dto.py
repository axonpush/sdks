from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferenceReviewDto")


@_attrs_define
class ReferenceReviewDto:
    """
    Attributes:
        actor_id (str):
        reviewed_at (datetime.datetime):
        source_revision (float):
    """

    actor_id: str
    reviewed_at: datetime.datetime
    source_revision: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actor_id = self.actor_id

        reviewed_at = self.reviewed_at.isoformat()

        source_revision = self.source_revision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actorId": actor_id,
                "reviewedAt": reviewed_at,
                "sourceRevision": source_revision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        actor_id = d.pop("actorId")

        reviewed_at = isoparse(d.pop("reviewedAt"))

        source_revision = d.pop("sourceRevision")

        reference_review_dto = cls(
            actor_id=actor_id,
            reviewed_at=reviewed_at,
            source_revision=source_revision,
        )

        reference_review_dto.additional_properties = d
        return reference_review_dto

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
