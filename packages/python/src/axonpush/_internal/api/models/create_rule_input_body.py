from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_rule_input_body_action import CreateRuleInputBodyAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRuleInputBody")


@_attrs_define
class CreateRuleInputBody:
    """
    Attributes:
        action (CreateRuleInputBodyAction):
        detector (str): builtin detector name, or 'regex'/'keyword'
        name (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        pattern (str | Unset):
    """

    action: CreateRuleInputBodyAction
    detector: str
    name: str
    schema: str | Unset = UNSET
    pattern: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        detector = self.detector

        name = self.name

        schema = self.schema

        pattern = self.pattern

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "detector": detector,
                "name": name,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if pattern is not UNSET:
            field_dict["pattern"] = pattern

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = CreateRuleInputBodyAction(d.pop("action"))

        detector = d.pop("detector")

        name = d.pop("name")

        schema = d.pop("$schema", UNSET)

        pattern = d.pop("pattern", UNSET)

        create_rule_input_body = cls(
            action=action,
            detector=detector,
            name=name,
            schema=schema,
            pattern=pattern,
        )

        return create_rule_input_body
