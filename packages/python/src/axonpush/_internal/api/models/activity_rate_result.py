from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_outcome_count import ActivityOutcomeCount


T = TypeVar("T", bound="ActivityRateResult")


@_attrs_define
class ActivityRateResult:
    """
    Attributes:
        cancelled (int):
        denominator (int): success + failed
        expected (int): Unsuccessful in an expected way: validation errors, expected denials
        failed (int): Unexpected failures
        numerator (int): success
        pending (int): Still running; not counted
        small_sample (bool): The denominator is below the view's minCohort
        success (int):
        terminal (int): success + expected + cancelled + failed
        unknown (int): No outcome observed; not counted
        values (list[ActivityOutcomeCount] | None):
        rate (float | Unset): numerator / denominator
        terminal_rate (float | Unset): success / terminal
    """

    cancelled: int
    denominator: int
    expected: int
    failed: int
    numerator: int
    pending: int
    small_sample: bool
    success: int
    terminal: int
    unknown: int
    values: list[ActivityOutcomeCount] | None
    rate: float | Unset = UNSET
    terminal_rate: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_outcome_count import ActivityOutcomeCount

        cancelled = self.cancelled

        denominator = self.denominator

        expected = self.expected

        failed = self.failed

        numerator = self.numerator

        pending = self.pending

        small_sample = self.small_sample

        success = self.success

        terminal = self.terminal

        unknown = self.unknown

        values: list[dict[str, Any]] | None
        if isinstance(self.values, list):
            values = []
            for values_type_0_item_data in self.values:
                values_type_0_item = values_type_0_item_data.to_dict()
                values.append(values_type_0_item)

        else:
            values = self.values

        rate = self.rate

        terminal_rate = self.terminal_rate

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cancelled": cancelled,
                "denominator": denominator,
                "expected": expected,
                "failed": failed,
                "numerator": numerator,
                "pending": pending,
                "smallSample": small_sample,
                "success": success,
                "terminal": terminal,
                "unknown": unknown,
                "values": values,
            }
        )
        if rate is not UNSET:
            field_dict["rate"] = rate
        if terminal_rate is not UNSET:
            field_dict["terminalRate"] = terminal_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_outcome_count import ActivityOutcomeCount

        d = dict(src_dict)
        cancelled = d.pop("cancelled")

        denominator = d.pop("denominator")

        expected = d.pop("expected")

        failed = d.pop("failed")

        numerator = d.pop("numerator")

        pending = d.pop("pending")

        small_sample = d.pop("smallSample")

        success = d.pop("success")

        terminal = d.pop("terminal")

        unknown = d.pop("unknown")

        def _parse_values(data: object) -> list[ActivityOutcomeCount] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = []
                _values_type_0 = data
                for values_type_0_item_data in _values_type_0:
                    values_type_0_item = ActivityOutcomeCount.from_dict(values_type_0_item_data)

                    values_type_0.append(values_type_0_item)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityOutcomeCount] | None, data)

        values = _parse_values(d.pop("values"))

        rate = d.pop("rate", UNSET)

        terminal_rate = d.pop("terminalRate", UNSET)

        activity_rate_result = cls(
            cancelled=cancelled,
            denominator=denominator,
            expected=expected,
            failed=failed,
            numerator=numerator,
            pending=pending,
            small_sample=small_sample,
            success=success,
            terminal=terminal,
            unknown=unknown,
            values=values,
            rate=rate,
            terminal_rate=terminal_rate,
        )

        return activity_rate_result
