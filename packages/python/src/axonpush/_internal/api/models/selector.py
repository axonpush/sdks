from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.predicate import Predicate
    from ..models.selector_match import SelectorMatch


T = TypeVar("T", bound="Selector")


@_attrs_define
class Selector:
    """
    Attributes:
        event (str):
        match (SelectorMatch | Unset):
        where (Predicate | Unset):
    """

    event: str
    match: SelectorMatch | Unset = UNSET
    where: Predicate | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.predicate import Predicate
        from ..models.selector_match import SelectorMatch

        event = self.event

        match: dict[str, Any] | Unset = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.to_dict()

        where: dict[str, Any] | Unset = UNSET
        if not isinstance(self.where, Unset):
            where = self.where.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "event": event,
            }
        )
        if match is not UNSET:
            field_dict["match"] = match
        if where is not UNSET:
            field_dict["where"] = where

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.predicate import Predicate
        from ..models.selector_match import SelectorMatch

        d = dict(src_dict)
        event = d.pop("event")

        _match = d.pop("match", UNSET)
        match: SelectorMatch | Unset
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = SelectorMatch.from_dict(_match)

        _where = d.pop("where", UNSET)
        where: Predicate | Unset
        if isinstance(_where, Unset):
            where = UNSET
        else:
            where = Predicate.from_dict(_where)

        selector = cls(
            event=event,
            match=match,
            where=where,
        )

        return selector
