from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_aggregates_open_by_type import ActivityAggregatesOpenByType


T = TypeVar("T", bound="ActivityAggregates")


@_attrs_define
class ActivityAggregates:
    """
    Attributes:
        open_by_type (ActivityAggregatesOpenByType): Linked entities per rollup type that are neither terminal nor stale
        wait_key (str | Unset): Attribute key waitingOn was read from
        waiting_on (str | Unset): Latest explicit wait among open linked entities, from the wait_reason or next_actor
            role
    """

    open_by_type: ActivityAggregatesOpenByType
    wait_key: str | Unset = UNSET
    waiting_on: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_aggregates_open_by_type import ActivityAggregatesOpenByType

        open_by_type = self.open_by_type.to_dict()

        wait_key = self.wait_key

        waiting_on = self.waiting_on

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "openByType": open_by_type,
            }
        )
        if wait_key is not UNSET:
            field_dict["waitKey"] = wait_key
        if waiting_on is not UNSET:
            field_dict["waitingOn"] = waiting_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_aggregates_open_by_type import ActivityAggregatesOpenByType

        d = dict(src_dict)
        open_by_type = ActivityAggregatesOpenByType.from_dict(d.pop("openByType"))

        wait_key = d.pop("waitKey", UNSET)

        waiting_on = d.pop("waitingOn", UNSET)

        activity_aggregates = cls(
            open_by_type=open_by_type,
            wait_key=wait_key,
            waiting_on=waiting_on,
        )

        return activity_aggregates
