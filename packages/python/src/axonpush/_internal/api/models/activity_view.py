from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_view_type import ActivityViewType
from ..models.activity_view_window import ActivityViewWindow
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_view_filter import ActivityViewFilter


T = TypeVar("T", bound="ActivityView")


@_attrs_define
class ActivityView:
    """
    Attributes:
        id (str):
        title (str):
        type_ (ActivityViewType):
        entity (str | Unset):
        filter_ (ActivityViewFilter | Unset):
        funnel (str | Unset):
        key (str | Unset): Attribute key to group or measure by, when no role fits
        open_ (bool | Unset): Only entities not in a terminal state
        role (str | Unset): Attribute role to group or measure by
        state (list[str] | None | Unset): Only entities in these states
        window (ActivityViewWindow | Unset): Only entities with activity inside the window
    """

    id: str
    title: str
    type_: ActivityViewType
    entity: str | Unset = UNSET
    filter_: ActivityViewFilter | Unset = UNSET
    funnel: str | Unset = UNSET
    key: str | Unset = UNSET
    open_: bool | Unset = UNSET
    role: str | Unset = UNSET
    state: list[str] | None | Unset = UNSET
    window: ActivityViewWindow | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_view_filter import ActivityViewFilter

        id = self.id

        title = self.title

        type_ = self.type_.value

        entity = self.entity

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        funnel = self.funnel

        key = self.key

        open_ = self.open_

        role = self.role

        state: list[str] | None | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, list):
            state = self.state

        else:
            state = self.state

        window: str | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "title": title,
                "type": type_,
            }
        )
        if entity is not UNSET:
            field_dict["entity"] = entity
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if funnel is not UNSET:
            field_dict["funnel"] = funnel
        if key is not UNSET:
            field_dict["key"] = key
        if open_ is not UNSET:
            field_dict["open"] = open_
        if role is not UNSET:
            field_dict["role"] = role
        if state is not UNSET:
            field_dict["state"] = state
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_view_filter import ActivityViewFilter

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        type_ = ActivityViewType(d.pop("type"))

        entity = d.pop("entity", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: ActivityViewFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ActivityViewFilter.from_dict(_filter_)

        funnel = d.pop("funnel", UNSET)

        key = d.pop("key", UNSET)

        open_ = d.pop("open", UNSET)

        role = d.pop("role", UNSET)

        def _parse_state(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                state_type_0 = cast(list[str], data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        _window = d.pop("window", UNSET)
        window: ActivityViewWindow | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = ActivityViewWindow(_window)

        activity_view = cls(
            id=id,
            title=title,
            type_=type_,
            entity=entity,
            filter_=filter_,
            funnel=funnel,
            key=key,
            open_=open_,
            role=role,
            state=state,
            window=window,
        )

        return activity_view
