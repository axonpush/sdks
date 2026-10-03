from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_event_rule_set import ActivityEventRuleSet


T = TypeVar("T", bound="ActivityEventRule")


@_attrs_define
class ActivityEventRule:
    """
    Attributes:
        match (str): Exact event name, or a prefix ending in * (the most specific matching rule wins)
        erase (bool | Unset): The event erases the referenced entity, everything linked to it, and its profile
        only (list[str] | None | Unset): Restrict which entity fields this event updates from attributes
        passive (bool | Unset): The event updates the entity but does not count as activity
        set_ (ActivityEventRuleSet | Unset): Literal field values assigned when the rule matches
    """

    match: str
    erase: bool | Unset = UNSET
    only: list[str] | None | Unset = UNSET
    passive: bool | Unset = UNSET
    set_: ActivityEventRuleSet | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_event_rule_set import ActivityEventRuleSet

        match = self.match

        erase = self.erase

        only: list[str] | None | Unset
        if isinstance(self.only, Unset):
            only = UNSET
        elif isinstance(self.only, list):
            only = self.only

        else:
            only = self.only

        passive = self.passive

        set_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.set_, Unset):
            set_ = self.set_.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "match": match,
            }
        )
        if erase is not UNSET:
            field_dict["erase"] = erase
        if only is not UNSET:
            field_dict["only"] = only
        if passive is not UNSET:
            field_dict["passive"] = passive
        if set_ is not UNSET:
            field_dict["set"] = set_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_event_rule_set import ActivityEventRuleSet

        d = dict(src_dict)
        match = d.pop("match")

        erase = d.pop("erase", UNSET)

        def _parse_only(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                only_type_0 = cast(list[str], data)

                return only_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        only = _parse_only(d.pop("only", UNSET))

        passive = d.pop("passive", UNSET)

        _set_ = d.pop("set", UNSET)
        set_: ActivityEventRuleSet | Unset
        if isinstance(_set_, Unset):
            set_ = UNSET
        else:
            set_ = ActivityEventRuleSet.from_dict(_set_)

        activity_event_rule = cls(
            match=match,
            erase=erase,
            only=only,
            passive=passive,
            set_=set_,
        )

        return activity_event_rule
