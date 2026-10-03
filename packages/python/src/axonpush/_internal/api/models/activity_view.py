from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_view_type import ActivityViewType
from ..models.activity_view_window import ActivityViewWindow
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_event_match import ActivityEventMatch
    from ..models.activity_view_filter import ActivityViewFilter


T = TypeVar("T", bound="ActivityView")


@_attrs_define
class ActivityView:
    """
    Attributes:
        id (str):
        title (str):
        type_ (ActivityViewType):
        entities (list[str] | None | Unset): Graph: entity types drawn as nodes; default every declared entity
        entity (str | Unset):
        exclude (list[ActivityViewFilter] | None | Unset): Leave out entities matching any of these, e.g. discovery-only
            attempts
        filter_ (ActivityViewFilter | Unset):
        from_ (ActivityEventMatch | Unset):
        funnel (str | Unset):
        key (str | Unset): Attribute key to group or measure by, when no role fits. For a rate view: the reason
            attribute whose expected values classify an unsuccessful result as expected
        limit (int | Unset): Graph: maximum nodes, most recently active first; default 200
        min_cohort (int | Unset): Splits or samples smaller than this are flagged smallCohort; default 10
        open_ (bool | Unset): Only entities not in a terminal state
        role (str | Unset): Attribute role to group or measure by
        split_by (list[str] | None | Unset): Funnel: roles or attribute keys to split stages and activation by (e.g.
            client, actor_side). Timeseries: one role or key to split daily counts by
        state (list[str] | None | Unset): Only entities in these states
        to (ActivityEventMatch | Unset):
        window (ActivityViewWindow | Unset): Only entities with activity inside the window; for funnel, rate, interval
            and graph views the period measured
    """

    id: str
    title: str
    type_: ActivityViewType
    entities: list[str] | None | Unset = UNSET
    entity: str | Unset = UNSET
    exclude: list[ActivityViewFilter] | None | Unset = UNSET
    filter_: ActivityViewFilter | Unset = UNSET
    from_: ActivityEventMatch | Unset = UNSET
    funnel: str | Unset = UNSET
    key: str | Unset = UNSET
    limit: int | Unset = UNSET
    min_cohort: int | Unset = UNSET
    open_: bool | Unset = UNSET
    role: str | Unset = UNSET
    split_by: list[str] | None | Unset = UNSET
    state: list[str] | None | Unset = UNSET
    to: ActivityEventMatch | Unset = UNSET
    window: ActivityViewWindow | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_event_match import ActivityEventMatch
        from ..models.activity_view_filter import ActivityViewFilter

        id = self.id

        title = self.title

        type_ = self.type_.value

        entities: list[str] | None | Unset
        if isinstance(self.entities, Unset):
            entities = UNSET
        elif isinstance(self.entities, list):
            entities = self.entities

        else:
            entities = self.entities

        entity = self.entity

        exclude: list[dict[str, Any]] | None | Unset
        if isinstance(self.exclude, Unset):
            exclude = UNSET
        elif isinstance(self.exclude, list):
            exclude = []
            for exclude_type_0_item_data in self.exclude:
                exclude_type_0_item = exclude_type_0_item_data.to_dict()
                exclude.append(exclude_type_0_item)

        else:
            exclude = self.exclude

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        from_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        funnel = self.funnel

        key = self.key

        limit = self.limit

        min_cohort = self.min_cohort

        open_ = self.open_

        role = self.role

        split_by: list[str] | None | Unset
        if isinstance(self.split_by, Unset):
            split_by = UNSET
        elif isinstance(self.split_by, list):
            split_by = self.split_by

        else:
            split_by = self.split_by

        state: list[str] | None | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, list):
            state = self.state

        else:
            state = self.state

        to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

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
        if entities is not UNSET:
            field_dict["entities"] = entities
        if entity is not UNSET:
            field_dict["entity"] = entity
        if exclude is not UNSET:
            field_dict["exclude"] = exclude
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if from_ is not UNSET:
            field_dict["from"] = from_
        if funnel is not UNSET:
            field_dict["funnel"] = funnel
        if key is not UNSET:
            field_dict["key"] = key
        if limit is not UNSET:
            field_dict["limit"] = limit
        if min_cohort is not UNSET:
            field_dict["minCohort"] = min_cohort
        if open_ is not UNSET:
            field_dict["open"] = open_
        if role is not UNSET:
            field_dict["role"] = role
        if split_by is not UNSET:
            field_dict["splitBy"] = split_by
        if state is not UNSET:
            field_dict["state"] = state
        if to is not UNSET:
            field_dict["to"] = to
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_event_match import ActivityEventMatch
        from ..models.activity_view_filter import ActivityViewFilter

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        type_ = ActivityViewType(d.pop("type"))

        def _parse_entities(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                entities_type_0 = cast(list[str], data)

                return entities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        entities = _parse_entities(d.pop("entities", UNSET))

        entity = d.pop("entity", UNSET)

        def _parse_exclude(data: object) -> list[ActivityViewFilter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_type_0 = []
                _exclude_type_0 = data
                for exclude_type_0_item_data in _exclude_type_0:
                    exclude_type_0_item = ActivityViewFilter.from_dict(exclude_type_0_item_data)

                    exclude_type_0.append(exclude_type_0_item)

                return exclude_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityViewFilter] | None | Unset, data)

        exclude = _parse_exclude(d.pop("exclude", UNSET))

        _filter_ = d.pop("filter", UNSET)
        filter_: ActivityViewFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = ActivityViewFilter.from_dict(_filter_)

        _from_ = d.pop("from", UNSET)
        from_: ActivityEventMatch | Unset
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = ActivityEventMatch.from_dict(_from_)

        funnel = d.pop("funnel", UNSET)

        key = d.pop("key", UNSET)

        limit = d.pop("limit", UNSET)

        min_cohort = d.pop("minCohort", UNSET)

        open_ = d.pop("open", UNSET)

        role = d.pop("role", UNSET)

        def _parse_split_by(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                split_by_type_0 = cast(list[str], data)

                return split_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        split_by = _parse_split_by(d.pop("splitBy", UNSET))

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

        _to = d.pop("to", UNSET)
        to: ActivityEventMatch | Unset
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = ActivityEventMatch.from_dict(_to)

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
            entities=entities,
            entity=entity,
            exclude=exclude,
            filter_=filter_,
            from_=from_,
            funnel=funnel,
            key=key,
            limit=limit,
            min_cohort=min_cohort,
            open_=open_,
            role=role,
            split_by=split_by,
            state=state,
            to=to,
            window=window,
        )

        return activity_view
