from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.selector import Selector


T = TypeVar("T", bound="Requirement")


@_attrs_define
class Requirement:
    """
    Attributes:
        evidence (Selector):
        fresh_for (str):
        grace (str):
        source (str):
        trigger (Selector):
        within (str):
        cancel (Selector | Unset):
        evidence_key (str | Unset):
        failure (Selector | Unset):
        max_matches (int | Unset):
    """

    evidence: Selector
    fresh_for: str
    grace: str
    source: str
    trigger: Selector
    within: str
    cancel: Selector | Unset = UNSET
    evidence_key: str | Unset = UNSET
    failure: Selector | Unset = UNSET
    max_matches: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.selector import Selector

        evidence = self.evidence.to_dict()

        fresh_for = self.fresh_for

        grace = self.grace

        source = self.source

        trigger = self.trigger.to_dict()

        within = self.within

        cancel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cancel, Unset):
            cancel = self.cancel.to_dict()

        evidence_key = self.evidence_key

        failure: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failure, Unset):
            failure = self.failure.to_dict()

        max_matches = self.max_matches

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "evidence": evidence,
                "fresh_for": fresh_for,
                "grace": grace,
                "source": source,
                "trigger": trigger,
                "within": within,
            }
        )
        if cancel is not UNSET:
            field_dict["cancel"] = cancel
        if evidence_key is not UNSET:
            field_dict["evidence_key"] = evidence_key
        if failure is not UNSET:
            field_dict["failure"] = failure
        if max_matches is not UNSET:
            field_dict["max_matches"] = max_matches

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.selector import Selector

        d = dict(src_dict)
        evidence = Selector.from_dict(d.pop("evidence"))

        fresh_for = d.pop("fresh_for")

        grace = d.pop("grace")

        source = d.pop("source")

        trigger = Selector.from_dict(d.pop("trigger"))

        within = d.pop("within")

        _cancel = d.pop("cancel", UNSET)
        cancel: Selector | Unset
        if isinstance(_cancel, Unset):
            cancel = UNSET
        else:
            cancel = Selector.from_dict(_cancel)

        evidence_key = d.pop("evidence_key", UNSET)

        _failure = d.pop("failure", UNSET)
        failure: Selector | Unset
        if isinstance(_failure, Unset):
            failure = UNSET
        else:
            failure = Selector.from_dict(_failure)

        max_matches = d.pop("max_matches", UNSET)

        requirement = cls(
            evidence=evidence,
            fresh_for=fresh_for,
            grace=grace,
            source=source,
            trigger=trigger,
            within=within,
            cancel=cancel,
            evidence_key=evidence_key,
            failure=failure,
            max_matches=max_matches,
        )

        return requirement
