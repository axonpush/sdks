from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ledger_hold import LedgerHold


T = TypeVar("T", bound="HoldListOutputBody")


@_attrs_define
class HoldListOutputBody:
    """
    Attributes:
        holds (list[LedgerHold] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    holds: list[LedgerHold] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.ledger_hold import LedgerHold

        holds: list[dict[str, Any]] | None
        if isinstance(self.holds, list):
            holds = []
            for holds_type_0_item_data in self.holds:
                holds_type_0_item = holds_type_0_item_data.to_dict()
                holds.append(holds_type_0_item)

        else:
            holds = self.holds

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "holds": holds,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ledger_hold import LedgerHold

        d = dict(src_dict)

        def _parse_holds(data: object) -> list[LedgerHold] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                holds_type_0 = []
                _holds_type_0 = data
                for holds_type_0_item_data in _holds_type_0:
                    holds_type_0_item = LedgerHold.from_dict(holds_type_0_item_data)

                    holds_type_0.append(holds_type_0_item)

                return holds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LedgerHold] | None, data)

        holds = _parse_holds(d.pop("holds"))

        schema = d.pop("$schema", UNSET)

        hold_list_output_body = cls(
            holds=holds,
            schema=schema,
        )

        return hold_list_output_body
