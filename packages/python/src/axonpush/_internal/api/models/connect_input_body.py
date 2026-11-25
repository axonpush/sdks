from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="ConnectInputBody")


@_attrs_define
class ConnectInputBody:
    """
    Attributes:
        schema (str | Unset): A URL to the JSON Schema for this object.
        environment (str | Unset): Environment slug or id; defaults to the organisation's default, else production
        handlers (list[str] | None | Unset): Action handler IDs owned by this runtime
        purpose (str | Unset): Separates keys for different processes of one app, e.g. web or worker. Defaults to
            default
        rotate (bool | Unset): Revoke this environment and purpose's existing connect key and mint a new one
        sources (list[str] | None | Unset): Evidence source IDs owned by this runtime
        workflow (str | Unset): Workflow ID when purpose is workflow_runtime
    """

    schema: str | Unset = UNSET
    environment: str | Unset = UNSET
    handlers: list[str] | None | Unset = UNSET
    purpose: str | Unset = UNSET
    rotate: bool | Unset = UNSET
    sources: list[str] | None | Unset = UNSET
    workflow: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        schema = self.schema

        environment = self.environment

        handlers: list[str] | None | Unset
        if isinstance(self.handlers, Unset):
            handlers = UNSET
        elif isinstance(self.handlers, list):
            handlers = self.handlers

        else:
            handlers = self.handlers

        purpose = self.purpose

        rotate = self.rotate

        sources: list[str] | None | Unset
        if isinstance(self.sources, Unset):
            sources = UNSET
        elif isinstance(self.sources, list):
            sources = self.sources

        else:
            sources = self.sources

        workflow = self.workflow

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if environment is not UNSET:
            field_dict["environment"] = environment
        if handlers is not UNSET:
            field_dict["handlers"] = handlers
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if rotate is not UNSET:
            field_dict["rotate"] = rotate
        if sources is not UNSET:
            field_dict["sources"] = sources
        if workflow is not UNSET:
            field_dict["workflow"] = workflow

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        environment = d.pop("environment", UNSET)

        def _parse_handlers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                handlers_type_0 = cast(list[str], data)

                return handlers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        handlers = _parse_handlers(d.pop("handlers", UNSET))

        purpose = d.pop("purpose", UNSET)

        rotate = d.pop("rotate", UNSET)

        def _parse_sources(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = cast(list[str], data)

                return sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        sources = _parse_sources(d.pop("sources", UNSET))

        workflow = d.pop("workflow", UNSET)

        connect_input_body = cls(
            schema=schema,
            environment=environment,
            handlers=handlers,
            purpose=purpose,
            rotate=rotate,
            sources=sources,
            workflow=workflow,
        )

        return connect_input_body
