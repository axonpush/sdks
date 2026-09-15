from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rule_dto import RuleDTO


T = TypeVar("T", bound="ListRulesOutputBody")


@_attrs_define
class ListRulesOutputBody:
    """
    Attributes:
        rules (list[RuleDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    rules: list[RuleDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.rule_dto import RuleDTO

        rules: list[dict[str, Any]] | None
        if isinstance(self.rules, list):
            rules = []
            for rules_type_0_item_data in self.rules:
                rules_type_0_item = rules_type_0_item_data.to_dict()
                rules.append(rules_type_0_item)

        else:
            rules = self.rules

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rules": rules,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rule_dto import RuleDTO

        d = dict(src_dict)

        def _parse_rules(data: object) -> list[RuleDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rules_type_0 = []
                _rules_type_0 = data
                for rules_type_0_item_data in _rules_type_0:
                    rules_type_0_item = RuleDTO.from_dict(rules_type_0_item_data)

                    rules_type_0.append(rules_type_0_item)

                return rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RuleDTO] | None, data)

        rules = _parse_rules(d.pop("rules"))

        schema = d.pop("$schema", UNSET)

        list_rules_output_body = cls(
            rules=rules,
            schema=schema,
        )

        return list_rules_output_body
