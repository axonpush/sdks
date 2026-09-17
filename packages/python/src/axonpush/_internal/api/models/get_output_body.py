from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.decision_dto import DecisionDTO


T = TypeVar("T", bound="GetOutputBody")


@_attrs_define
class GetOutputBody:
    """
    Attributes:
        decisions (list[DecisionDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    decisions: list[DecisionDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.decision_dto import DecisionDTO

        decisions: list[dict[str, Any]] | None
        if isinstance(self.decisions, list):
            decisions = []
            for decisions_type_0_item_data in self.decisions:
                decisions_type_0_item = decisions_type_0_item_data.to_dict()
                decisions.append(decisions_type_0_item)

        else:
            decisions = self.decisions

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "decisions": decisions,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.decision_dto import DecisionDTO

        d = dict(src_dict)

        def _parse_decisions(data: object) -> list[DecisionDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                decisions_type_0 = []
                _decisions_type_0 = data
                for decisions_type_0_item_data in _decisions_type_0:
                    decisions_type_0_item = DecisionDTO.from_dict(decisions_type_0_item_data)

                    decisions_type_0.append(decisions_type_0_item)

                return decisions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DecisionDTO] | None, data)

        decisions = _parse_decisions(d.pop("decisions"))

        schema = d.pop("$schema", UNSET)

        get_output_body = cls(
            decisions=decisions,
            schema=schema,
        )

        return get_output_body
