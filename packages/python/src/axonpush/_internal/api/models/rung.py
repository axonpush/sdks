from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Rung")


@_attrs_define
class Rung:
    """
    Attributes:
        action (str):
        at_percent (int):
        block_mode (str | Unset):
        fallback_model (str | Unset):
    """

    action: str
    at_percent: int
    block_mode: str | Unset = UNSET
    fallback_model: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        at_percent = self.at_percent

        block_mode = self.block_mode

        fallback_model = self.fallback_model

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "at_percent": at_percent,
            }
        )
        if block_mode is not UNSET:
            field_dict["block_mode"] = block_mode
        if fallback_model is not UNSET:
            field_dict["fallback_model"] = fallback_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        at_percent = d.pop("at_percent")

        block_mode = d.pop("block_mode", UNSET)

        fallback_model = d.pop("fallback_model", UNSET)

        rung = cls(
            action=action,
            at_percent=at_percent,
            block_mode=block_mode,
            fallback_model=fallback_model,
        )

        return rung
