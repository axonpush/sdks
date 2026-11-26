from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertOccurrenceDTO")


@_attrs_define
class AlertOccurrenceDTO:
    """
    Attributes:
        fired_at (str):
        metric (str):
        occurrence_id (str):
        state (str):
        threshold (float):
        value (float):
        message (str | Unset):
    """

    fired_at: str
    metric: str
    occurrence_id: str
    state: str
    threshold: float
    value: float
    message: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        fired_at = self.fired_at

        metric = self.metric

        occurrence_id = self.occurrence_id

        state = self.state

        threshold = self.threshold

        value = self.value

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "firedAt": fired_at,
                "metric": metric,
                "occurrenceId": occurrence_id,
                "state": state,
                "threshold": threshold,
                "value": value,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fired_at = d.pop("firedAt")

        metric = d.pop("metric")

        occurrence_id = d.pop("occurrenceId")

        state = d.pop("state")

        threshold = d.pop("threshold")

        value = d.pop("value")

        message = d.pop("message", UNSET)

        alert_occurrence_dto = cls(
            fired_at=fired_at,
            metric=metric,
            occurrence_id=occurrence_id,
            state=state,
            threshold=threshold,
            value=value,
            message=message,
        )

        return alert_occurrence_dto
