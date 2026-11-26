from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Obligation")


@_attrs_define
class Obligation:
    """
    Attributes:
        decide_at (datetime.datetime):
        due_at (datetime.datetime):
        evidence_class (str):
        evidence_ids (list[str] | None):
        id (str):
        lifecycle (str):
        reason (str):
        requirement (str):
        state (str):
        timing (str):
        trigger_id (str):
        breach_observed_at (datetime.datetime | Unset):
    """

    decide_at: datetime.datetime
    due_at: datetime.datetime
    evidence_class: str
    evidence_ids: list[str] | None
    id: str
    lifecycle: str
    reason: str
    requirement: str
    state: str
    timing: str
    trigger_id: str
    breach_observed_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        decide_at = self.decide_at.isoformat()

        due_at = self.due_at.isoformat()

        evidence_class = self.evidence_class

        evidence_ids: list[str] | None
        if isinstance(self.evidence_ids, list):
            evidence_ids = self.evidence_ids

        else:
            evidence_ids = self.evidence_ids

        id = self.id

        lifecycle = self.lifecycle

        reason = self.reason

        requirement = self.requirement

        state = self.state

        timing = self.timing

        trigger_id = self.trigger_id

        breach_observed_at: str | Unset = UNSET
        if not isinstance(self.breach_observed_at, Unset):
            breach_observed_at = self.breach_observed_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "decide_at": decide_at,
                "due_at": due_at,
                "evidence_class": evidence_class,
                "evidence_ids": evidence_ids,
                "id": id,
                "lifecycle": lifecycle,
                "reason": reason,
                "requirement": requirement,
                "state": state,
                "timing": timing,
                "trigger_id": trigger_id,
            }
        )
        if breach_observed_at is not UNSET:
            field_dict["breach_observed_at"] = breach_observed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        decide_at = isoparse(d.pop("decide_at"))

        due_at = isoparse(d.pop("due_at"))

        evidence_class = d.pop("evidence_class")

        def _parse_evidence_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evidence_ids_type_0 = cast(list[str], data)

                return evidence_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        evidence_ids = _parse_evidence_ids(d.pop("evidence_ids"))

        id = d.pop("id")

        lifecycle = d.pop("lifecycle")

        reason = d.pop("reason")

        requirement = d.pop("requirement")

        state = d.pop("state")

        timing = d.pop("timing")

        trigger_id = d.pop("trigger_id")

        _breach_observed_at = d.pop("breach_observed_at", UNSET)
        breach_observed_at: datetime.datetime | Unset
        if isinstance(_breach_observed_at, Unset):
            breach_observed_at = UNSET
        else:
            breach_observed_at = isoparse(_breach_observed_at)

        obligation = cls(
            decide_at=decide_at,
            due_at=due_at,
            evidence_class=evidence_class,
            evidence_ids=evidence_ids,
            id=id,
            lifecycle=lifecycle,
            reason=reason,
            requirement=requirement,
            state=state,
            timing=timing,
            trigger_id=trigger_id,
            breach_observed_at=breach_observed_at,
        )

        return obligation
