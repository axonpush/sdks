from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meta import Meta


T = TypeVar("T", bound="Inclusion")


@_attrs_define
class Inclusion:
    """
    Attributes:
        meta (Meta):
        path (list[str] | None):
        root (str):
        schema (str):
        size (int):
    """

    meta: Meta
    path: list[str] | None
    root: str
    schema: str
    size: int

    def to_dict(self) -> dict[str, Any]:
        from ..models.meta import Meta

        meta = self.meta.to_dict()

        path: list[str] | None
        if isinstance(self.path, list):
            path = self.path

        else:
            path = self.path

        root = self.root

        schema = self.schema

        size = self.size

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "meta": meta,
                "path": path,
                "root": root,
                "schema": schema,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta import Meta

        d = dict(src_dict)
        meta = Meta.from_dict(d.pop("meta"))

        def _parse_path(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                path_type_0 = cast(list[str], data)

                return path_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        path = _parse_path(d.pop("path"))

        root = d.pop("root")

        schema = d.pop("schema")

        size = d.pop("size")

        inclusion = cls(
            meta=meta,
            path=path,
            root=root,
            schema=schema,
            size=size,
        )

        return inclusion
