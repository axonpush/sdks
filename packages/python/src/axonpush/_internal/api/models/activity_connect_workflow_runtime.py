from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityConnectWorkflowRuntime")


@_attrs_define
class ActivityConnectWorkflowRuntime:
    """
    Attributes:
        handlers (list[str] | None):
        id (str):
        sources (list[str] | None):
        workflow (str):
    """

    handlers: list[str] | None
    id: str
    sources: list[str] | None
    workflow: str

    def to_dict(self) -> dict[str, Any]:
        handlers: list[str] | None
        if isinstance(self.handlers, list):
            handlers = self.handlers

        else:
            handlers = self.handlers

        id = self.id

        sources: list[str] | None
        if isinstance(self.sources, list):
            sources = self.sources

        else:
            sources = self.sources

        workflow = self.workflow

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "handlers": handlers,
                "id": id,
                "sources": sources,
                "workflow": workflow,
            }
        )

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

        workflow = d.pop("workflow")

        activity_connect_workflow_runtime = cls(
            handlers=handlers,
            id=id,
            sources=sources,
            workflow=workflow,
        )

        return activity_connect_workflow_runtime
