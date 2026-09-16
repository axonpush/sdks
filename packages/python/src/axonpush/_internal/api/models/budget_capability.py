from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetCapability")


@_attrs_define
class BudgetCapability:
    """
    Attributes:
        enabled (bool):
        periods (list[str] | None):
    """

    enabled: bool
    periods: list[str] | None

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        periods: list[str] | None
        if isinstance(self.periods, list):
            periods = self.periods

        else:
            periods = self.periods

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
                "periods": periods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        def _parse_periods(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                periods_type_0 = cast(list[str], data)

                return periods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        periods = _parse_periods(d.pop("periods"))

        budget_capability = cls(
            enabled=enabled,
            periods=periods,
        )

        return budget_capability
