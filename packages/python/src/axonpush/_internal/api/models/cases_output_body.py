from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.case import Case


T = TypeVar("T", bound="CasesOutputBody")


@_attrs_define
class CasesOutputBody:
    """
    Attributes:
        cases (list[Case] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        next_cursor (str | Unset):
    """

    cases: list[Case] | None
    schema: str | Unset = UNSET
    next_cursor: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.case import Case

        cases: list[dict[str, Any]] | None
        if isinstance(self.cases, list):
            cases = []
            for cases_type_0_item_data in self.cases:
                cases_type_0_item = cases_type_0_item_data.to_dict()
                cases.append(cases_type_0_item)

        else:
            cases = self.cases

        schema = self.schema

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cases": cases,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.case import Case

        d = dict(src_dict)

        def _parse_cases(data: object) -> list[Case] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cases_type_0 = []
                _cases_type_0 = data
                for cases_type_0_item_data in _cases_type_0:
                    cases_type_0_item = Case.from_dict(cases_type_0_item_data)

                    cases_type_0.append(cases_type_0_item)

                return cases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Case] | None, data)

        cases = _parse_cases(d.pop("cases"))

        schema = d.pop("$schema", UNSET)

        next_cursor = d.pop("next_cursor", UNSET)

        cases_output_body = cls(
            cases=cases,
            schema=schema,
            next_cursor=next_cursor,
        )

        return cases_output_body
