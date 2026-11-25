from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast


T = TypeVar("T", bound="SetupStep")


@_attrs_define
class SetupStep:
    """
    Attributes:
        complete_when (str):
        id (str):
        instruction (str):
        tools (list[str] | None):
    """

    complete_when: str
    id: str
    instruction: str
    tools: list[str] | None

    def to_dict(self) -> dict[str, Any]:
        complete_when = self.complete_when

        id = self.id

        instruction = self.instruction

        tools: list[str] | None
        if isinstance(self.tools, list):
            tools = self.tools

        else:
            tools = self.tools

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "complete_when": complete_when,
                "id": id,
                "instruction": instruction,
                "tools": tools,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        complete_when = d.pop("complete_when")

        id = d.pop("id")

        instruction = d.pop("instruction")

        def _parse_tools(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tools_type_0 = cast(list[str], data)

                return tools_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        tools = _parse_tools(d.pop("tools"))

        setup_step = cls(
            complete_when=complete_when,
            id=id,
            instruction=instruction,
            tools=tools,
        )

        return setup_step
