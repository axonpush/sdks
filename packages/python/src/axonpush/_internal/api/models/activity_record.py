from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_observation import ActivityObservation


T = TypeVar("T", bound="ActivityRecord")


@_attrs_define
class ActivityRecord:
    """
    Attributes:
        observation (ActivityObservation):
        projected_at (datetime.datetime | None):
        received_at (datetime.datetime):
    """

    observation: ActivityObservation
    projected_at: datetime.datetime | None
    received_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_observation import ActivityObservation

        observation = self.observation.to_dict()

        projected_at: None | str
        if isinstance(self.projected_at, datetime.datetime):
            projected_at = self.projected_at.isoformat()
        else:
            projected_at = self.projected_at

        received_at = self.received_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "observation": observation,
                "projectedAt": projected_at,
                "receivedAt": received_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_observation import ActivityObservation

        d = dict(src_dict)
        observation = ActivityObservation.from_dict(d.pop("observation"))

        def _parse_projected_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                projected_at_type_0 = isoparse(data)

                return projected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        projected_at = _parse_projected_at(d.pop("projectedAt"))

        received_at = isoparse(d.pop("receivedAt"))

        activity_record = cls(
            observation=observation,
            projected_at=projected_at,
            received_at=received_at,
        )

        return activity_record
