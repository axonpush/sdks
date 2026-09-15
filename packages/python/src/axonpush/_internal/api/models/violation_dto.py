from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ViolationDTO")


@_attrs_define
class ViolationDTO:
    """
    Attributes:
        action (str):
        detector (str):
        occurred_at (str):
        rule_id (str):
        rule_name (str):
        violation_id (str):
        app_id (str | Unset):
        channel_id (str | Unset):
    """

    action: str
    detector: str
    occurred_at: str
    rule_id: str
    rule_name: str
    violation_id: str
    app_id: str | Unset = UNSET
    channel_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        detector = self.detector

        occurred_at = self.occurred_at

        rule_id = self.rule_id

        rule_name = self.rule_name

        violation_id = self.violation_id

        app_id = self.app_id

        channel_id = self.channel_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "detector": detector,
                "occurredAt": occurred_at,
                "ruleId": rule_id,
                "ruleName": rule_name,
                "violationId": violation_id,
            }
        )
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        detector = d.pop("detector")

        occurred_at = d.pop("occurredAt")

        rule_id = d.pop("ruleId")

        rule_name = d.pop("ruleName")

        violation_id = d.pop("violationId")

        app_id = d.pop("appId", UNSET)

        channel_id = d.pop("channelId", UNSET)

        violation_dto = cls(
            action=action,
            detector=detector,
            occurred_at=occurred_at,
            rule_id=rule_id,
            rule_name=rule_name,
            violation_id=violation_id,
            app_id=app_id,
            channel_id=channel_id,
        )

        return violation_dto
