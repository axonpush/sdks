from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.violation_dto import ViolationDTO


T = TypeVar("T", bound="ListViolationsOutputBody")


@_attrs_define
class ListViolationsOutputBody:
    """
    Attributes:
        violations (list[ViolationDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    violations: list[ViolationDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.violation_dto import ViolationDTO

        violations: list[dict[str, Any]] | None
        if isinstance(self.violations, list):
            violations = []
            for violations_type_0_item_data in self.violations:
                violations_type_0_item = violations_type_0_item_data.to_dict()
                violations.append(violations_type_0_item)

        else:
            violations = self.violations

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "violations": violations,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.violation_dto import ViolationDTO

        d = dict(src_dict)

        def _parse_violations(data: object) -> list[ViolationDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                violations_type_0 = []
                _violations_type_0 = data
                for violations_type_0_item_data in _violations_type_0:
                    violations_type_0_item = ViolationDTO.from_dict(violations_type_0_item_data)

                    violations_type_0.append(violations_type_0_item)

                return violations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ViolationDTO] | None, data)

        violations = _parse_violations(d.pop("violations"))

        schema = d.pop("$schema", UNSET)

        list_violations_output_body = cls(
            violations=violations,
            schema=schema,
        )

        return list_violations_output_body
