from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_budget import CostBudget


T = TypeVar("T", bound="ListOutputBody")


@_attrs_define
class ListOutputBody:
    """
    Attributes:
        budgets (list[CostBudget] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    budgets: list[CostBudget] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cost_budget import CostBudget

        budgets: list[dict[str, Any]] | None
        if isinstance(self.budgets, list):
            budgets = []
            for budgets_type_0_item_data in self.budgets:
                budgets_type_0_item = budgets_type_0_item_data.to_dict()
                budgets.append(budgets_type_0_item)

        else:
            budgets = self.budgets

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "budgets": budgets,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_budget import CostBudget

        d = dict(src_dict)

        def _parse_budgets(data: object) -> list[CostBudget] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                budgets_type_0 = []
                _budgets_type_0 = data
                for budgets_type_0_item_data in _budgets_type_0:
                    budgets_type_0_item = CostBudget.from_dict(budgets_type_0_item_data)

                    budgets_type_0.append(budgets_type_0_item)

                return budgets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CostBudget] | None, data)

        budgets = _parse_budgets(d.pop("budgets"))

        schema = d.pop("$schema", UNSET)

        list_output_body = cls(
            budgets=budgets,
            schema=schema,
        )

        return list_output_body
