from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentRuntime")


@_attrs_define
class DeploymentRuntime:
    """
    Attributes:
        handlers (list[str] | None):
        id (str):
        publisher (str):
        sources (list[str] | None):
        last_seen_at (datetime.datetime | Unset):
    """

    handlers: list[str] | None
    id: str
    publisher: str
    sources: list[str] | None
    last_seen_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        handlers: list[str] | None
        if isinstance(self.handlers, list):
            handlers = self.handlers

        else:
            handlers = self.handlers

        id = self.id

        publisher = self.publisher

        sources: list[str] | None
        if isinstance(self.sources, list):
            sources = self.sources

        else:
            sources = self.sources

        last_seen_at: str | Unset = UNSET
        if not isinstance(self.last_seen_at, Unset):
            last_seen_at = self.last_seen_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "handlers": handlers,
                "id": id,
                "publisher": publisher,
                "sources": sources,
            }
        )
        if last_seen_at is not UNSET:
            field_dict["last_seen_at"] = last_seen_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_handlers(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                handlers_type_0 = cast(list[str], data)

                return handlers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        handlers = _parse_handlers(d.pop("handlers"))

        id = d.pop("id")

        publisher = d.pop("publisher")

        def _parse_sources(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = cast(list[str], data)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        sources = _parse_sources(d.pop("sources"))

        _last_seen_at = d.pop("last_seen_at", UNSET)
        last_seen_at: datetime.datetime | Unset
        if isinstance(_last_seen_at, Unset):
            last_seen_at = UNSET
        else:
            last_seen_at = isoparse(_last_seen_at)

        deployment_runtime = cls(
            handlers=handlers,
            id=id,
            publisher=publisher,
            sources=sources,
            last_seen_at=last_seen_at,
        )

        return deployment_runtime
