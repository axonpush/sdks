from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_dto import OrgDTO


T = TypeVar("T", bound="SearchOrgsOutputBody")


@_attrs_define
class SearchOrgsOutputBody:
    """
    Attributes:
        orgs (list[OrgDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    orgs: list[OrgDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.org_dto import OrgDTO

        orgs: list[dict[str, Any]] | None
        if isinstance(self.orgs, list):
            orgs = []
            for orgs_type_0_item_data in self.orgs:
                orgs_type_0_item = orgs_type_0_item_data.to_dict()
                orgs.append(orgs_type_0_item)

        else:
            orgs = self.orgs

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "orgs": orgs,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.org_dto import OrgDTO

        d = dict(src_dict)

        def _parse_orgs(data: object) -> list[OrgDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                orgs_type_0 = []
                _orgs_type_0 = data
                for orgs_type_0_item_data in _orgs_type_0:
                    orgs_type_0_item = OrgDTO.from_dict(orgs_type_0_item_data)

                    orgs_type_0.append(orgs_type_0_item)

                return orgs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OrgDTO] | None, data)

        orgs = _parse_orgs(d.pop("orgs"))

        schema = d.pop("$schema", UNSET)

        search_orgs_output_body = cls(
            orgs=orgs,
            schema=schema,
        )

        return search_orgs_output_body
