from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceGrant")


@_attrs_define
class ComplianceGrant:
    """
    Attributes:
        agent_id (str):
        enforcement (str):
        mode (str):
        rule (str):
        system (str):
        tool (str):
    """

    agent_id: str
    enforcement: str
    mode: str
    rule: str
    system: str
    tool: str

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        enforcement = self.enforcement

        mode = self.mode

        rule = self.rule

        system = self.system

        tool = self.tool

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agentId": agent_id,
                "enforcement": enforcement,
                "mode": mode,
                "rule": rule,
                "system": system,
                "tool": tool,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_id = d.pop("agentId")

        enforcement = d.pop("enforcement")

        mode = d.pop("mode")

        rule = d.pop("rule")

        system = d.pop("system")

        tool = d.pop("tool")

        compliance_grant = cls(
            agent_id=agent_id,
            enforcement=enforcement,
            mode=mode,
            rule=rule,
            system=system,
            tool=tool,
        )

        return compliance_grant
