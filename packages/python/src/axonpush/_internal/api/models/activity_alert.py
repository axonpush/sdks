from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_view_filter import ActivityViewFilter


T = TypeVar("T", bound="ActivityAlert")


@_attrs_define
class ActivityAlert:
    """
    Attributes:
        after_seconds (int):
        entity (str):
        name (str):
        state (str): State that counts; may be empty when a filter is given, meaning any open state
        cooldown_seconds (int | Unset): After a notification, a reopened incident with the same deduplication key stays
            quiet this long; default 3600
        filter_ (ActivityViewFilter | Unset):
        min_count (int | Unset): Minimum sample: fire only when at least this many entities are affected
        silent (bool | Unset): Record the incident without notifying owners, admins or alert webhooks
        window_seconds (int | Unset): Only count entities that changed inside this window
    """

    after_seconds: int
    entity: str
    name: str
    state: str
    cooldown_seconds: int | Unset = UNSET
    filter_: ActivityViewFilter | Unset = UNSET
    min_count: int | Unset = UNSET
    silent: bool | Unset = UNSET
    window_seconds: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_view_filter import ActivityViewFilter

        after_seconds = self.after_seconds

        entity = self.entity

        name = self.name

        state = self.state

        cooldown_seconds = self.cooldown_seconds

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        min_count = self.min_count

        silent = self.silent

        window_seconds = self.window_seconds

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "afterSeconds": after_seconds,
                "entity": entity,
                "name": name,
                "state": state,
            }
        )
        if cooldown_seconds is not UNSET:
            field_dict["cooldownSeconds"] = cooldown_seconds
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if min_count is not UNSET:
            field_dict["minCount"] = min_count
        if silent is not UNSET:
            field_dict["silent"] = silent
        if window_seconds is not UNSET:
            field_dict["windowSeconds"] = window_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_view_filter import ActivityViewFilter

        d = dict(src_dict)
        after_seconds = d.pop("afterSeconds")

        entity = d.pop("entity")

        name = d.pop("name")

        state = d.pop("state")

        cooldown_seconds = d.pop("cooldownSeconds", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: ActivityViewFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ActivityViewFilter.from_dict(_filter_)

        min_count = d.pop("minCount", UNSET)

        silent = d.pop("silent", UNSET)

        window_seconds = d.pop("windowSeconds", UNSET)

        activity_alert = cls(
            after_seconds=after_seconds,
            entity=entity,
            name=name,
            state=state,
            cooldown_seconds=cooldown_seconds,
            filter_=filter_,
            min_count=min_count,
            silent=silent,
            window_seconds=window_seconds,
        )

        return activity_alert
