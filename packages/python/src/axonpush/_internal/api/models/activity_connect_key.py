from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityConnectKey")


@_attrs_define
class ActivityConnectKey:
    """
    Attributes:
        created_at (str):
        id (str):
        name (str):
        scopes (list[str] | None):
        key (str | Unset): The raw key. Present only when this call minted it; it is never shown again
        start (str | Unset): First characters of the key, to recognise it
    """

    created_at: str
    id: str
    name: str
    scopes: list[str] | None
    key: str | Unset = UNSET
    start: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        name = self.name

        scopes: list[str] | None
        if isinstance(self.scopes, list):
            scopes = self.scopes

        else:
            scopes = self.scopes

        key = self.key

        start = self.start

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "id": id,
                "name": name,
                "scopes": scopes,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("createdAt")

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

        key = d.pop("key", UNSET)

        start = d.pop("start", UNSET)

        activity_connect_key = cls(
            created_at=created_at,
            id=id,
            name=name,
            scopes=scopes,
            key=key,
            start=start,
        )

        return activity_connect_key
