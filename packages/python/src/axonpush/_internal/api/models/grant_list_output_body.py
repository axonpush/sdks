from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_grant import ActivityGrant


T = TypeVar("T", bound="GrantListOutputBody")


@_attrs_define
class GrantListOutputBody:
    """
    Attributes:
        grants (list[ActivityGrant] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    grants: list[ActivityGrant] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_grant import ActivityGrant

        grants: list[dict[str, Any]] | None
        if isinstance(self.grants, list):
            grants = []
            for grants_type_0_item_data in self.grants:
                grants_type_0_item = grants_type_0_item_data.to_dict()
                grants.append(grants_type_0_item)

        else:
            grants = self.grants

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "grants": grants,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_grant import ActivityGrant

        d = dict(src_dict)

        def _parse_grants(data: object) -> list[ActivityGrant] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                grants_type_0 = []
                _grants_type_0 = data
                for grants_type_0_item_data in _grants_type_0:
                    grants_type_0_item = ActivityGrant.from_dict(grants_type_0_item_data)

                    grants_type_0.append(grants_type_0_item)

                return grants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityGrant] | None, data)

        grants = _parse_grants(d.pop("grants"))

        schema = d.pop("$schema", UNSET)

        grant_list_output_body = cls(
            grants=grants,
            schema=schema,
        )

        return grant_list_output_body
