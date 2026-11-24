from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link import Link


T = TypeVar("T", bound="CreatedKey")


@_attrs_define
class CreatedKey:
    """
    Attributes:
        id (str):
        name (str):
        scopes (list[str] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
        claim (Link | Unset):
        key (str | Unset): The raw key, shown once. Never returned to agents
    """

    id: str
    name: str
    scopes: list[str] | None
    schema: str | Unset = UNSET
    claim: Link | Unset = UNSET
    key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.link import Link

        id = self.id

        name = self.name

        scopes: list[str] | None
        if isinstance(self.scopes, list):
            scopes = self.scopes

        else:
            scopes = self.scopes

        schema = self.schema

        claim: dict[str, Any] | Unset = UNSET
        if not isinstance(self.claim, Unset):
            claim = self.claim.to_dict()

        key = self.key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "name": name,
                "scopes": scopes,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if claim is not UNSET:
            field_dict["claim"] = claim
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.link import Link

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_scopes(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = cast(list[str], data)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        scopes = _parse_scopes(d.pop("scopes"))

        schema = d.pop("$schema", UNSET)

        _claim = d.pop("claim", UNSET)
        claim: Link | Unset
        if isinstance(_claim, Unset):
            claim = UNSET
        else:
            claim = Link.from_dict(_claim)

        key = d.pop("key", UNSET)

        created_key = cls(
            id=id,
            name=name,
            scopes=scopes,
            schema=schema,
            claim=claim,
            key=key,
        )

        return created_key
