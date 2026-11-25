from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.input_ import Input


T = TypeVar("T", bound="SimulationInputBody")


@_attrs_define
class SimulationInputBody:
    """
    Attributes:
        input_ (Input):
        source (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    input_: Input
    source: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.input_ import Input

        input_ = self.input_.to_dict()

        source = self.source

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "input": input_,
                "source": source,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_ import Input

        d = dict(src_dict)
        input_ = Input.from_dict(d.pop("input"))

        source = d.pop("source")

        schema = d.pop("$schema", UNSET)

        simulation_input_body = cls(
            input_=input_,
            source=source,
            schema=schema,
        )

        return simulation_input_body
