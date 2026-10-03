from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityBreakdown")


@_attrs_define
class ActivityBreakdown:
    """
    Attributes:
        active15m (int):
        agents (int):
        client (str):
        side (str):
    """

    active15m: int
    agents: int
    client: str
    side: str

    def to_dict(self) -> dict[str, Any]:
        active15m = self.active15m

        agents = self.agents

        client = self.client

        side = self.side

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "active15m": active15m,
                "agents": agents,
                "client": client,
                "side": side,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active15m = d.pop("active15m")

        agents = d.pop("agents")

        client = d.pop("client")

        side = d.pop("side")

        activity_breakdown = cls(
            active15m=active15m,
            agents=agents,
            client=client,
            side=side,
        )

        return activity_breakdown
