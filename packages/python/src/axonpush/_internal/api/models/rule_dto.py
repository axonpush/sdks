from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RuleDTO")


@_attrs_define
class RuleDTO:
    """
    Attributes:
        action (str):
        created_at (str):
        detector (str):
        enabled (bool):
        name (str):
        pattern (str):
        rule_id (str):
        target (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    action: str
    created_at: str
    detector: str
    enabled: bool
    name: str
    pattern: str
    rule_id: str
    target: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        created_at = self.created_at

        detector = self.detector

        enabled = self.enabled

        name = self.name

        pattern = self.pattern

        rule_id = self.rule_id

        target = self.target

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "createdAt": created_at,
                "detector": detector,
                "enabled": enabled,
                "name": name,
                "pattern": pattern,
                "ruleId": rule_id,
                "target": target,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        created_at = d.pop("createdAt")

        detector = d.pop("detector")

        enabled = d.pop("enabled")

        name = d.pop("name")

        pattern = d.pop("pattern")

        rule_id = d.pop("ruleId")

        target = d.pop("target")

        schema = d.pop("$schema", UNSET)

        rule_dto = cls(
            action=action,
            created_at=created_at,
            detector=detector,
            enabled=enabled,
            name=name,
            pattern=pattern,
            rule_id=rule_id,
            target=target,
            schema=schema,
        )

        return rule_dto
