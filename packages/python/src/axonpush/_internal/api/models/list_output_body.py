from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.policy import Policy


T = TypeVar("T", bound="ListOutputBody")


@_attrs_define
class ListOutputBody:
    """
    Attributes:
        policies (list[Policy] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    policies: list[Policy] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.policy import Policy

        policies: list[dict[str, Any]] | None
        if isinstance(self.policies, list):
            policies = []
            for policies_type_0_item_data in self.policies:
                policies_type_0_item = policies_type_0_item_data.to_dict()
                policies.append(policies_type_0_item)

        else:
            policies = self.policies

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "policies": policies,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy import Policy

        d = dict(src_dict)

        def _parse_policies(data: object) -> list[Policy] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policies_type_0 = []
                _policies_type_0 = data
                for policies_type_0_item_data in _policies_type_0:
                    policies_type_0_item = Policy.from_dict(policies_type_0_item_data)

                    policies_type_0.append(policies_type_0_item)

                return policies_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Policy] | None, data)

        policies = _parse_policies(d.pop("policies"))

        schema = d.pop("$schema", UNSET)

        list_output_body = cls(
            policies=policies,
            schema=schema,
        )

        return list_output_body
