from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeploymentPreview")


@_attrs_define
class DeploymentPreview:
    """
    Attributes:
        compatible_runtime_ids (list[str] | None):
        required_handlers (list[str] | None):
        required_sources (list[str] | None):
        semantic_changed (bool):
        semantic_hash (str):
        source_changed (bool):
        source_hash (str):
        title (str):
        warnings (list[str] | None):
        workflow (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        current_semantic_hash (str | Unset):
        current_version_id (str | Unset):
    """

    compatible_runtime_ids: list[str] | None
    required_handlers: list[str] | None
    required_sources: list[str] | None
    semantic_changed: bool
    semantic_hash: str
    source_changed: bool
    source_hash: str
    title: str
    warnings: list[str] | None
    workflow: str
    schema: str | Unset = UNSET
    current_semantic_hash: str | Unset = UNSET
    current_version_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        compatible_runtime_ids: list[str] | None
        if isinstance(self.compatible_runtime_ids, list):
            compatible_runtime_ids = self.compatible_runtime_ids

        else:
            compatible_runtime_ids = self.compatible_runtime_ids

        required_handlers: list[str] | None
        if isinstance(self.required_handlers, list):
            required_handlers = self.required_handlers

        else:
            required_handlers = self.required_handlers

        required_sources: list[str] | None
        if isinstance(self.required_sources, list):
            required_sources = self.required_sources

        else:
            required_sources = self.required_sources

        semantic_changed = self.semantic_changed

        semantic_hash = self.semantic_hash

        source_changed = self.source_changed

        source_hash = self.source_hash

        title = self.title

        warnings: list[str] | None
        if isinstance(self.warnings, list):
            warnings = self.warnings

        else:
            warnings = self.warnings

        workflow = self.workflow

        schema = self.schema

        current_semantic_hash = self.current_semantic_hash

        current_version_id = self.current_version_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "compatible_runtime_ids": compatible_runtime_ids,
                "required_handlers": required_handlers,
                "required_sources": required_sources,
                "semantic_changed": semantic_changed,
                "semantic_hash": semantic_hash,
                "source_changed": source_changed,
                "source_hash": source_hash,
                "title": title,
                "warnings": warnings,
                "workflow": workflow,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if current_semantic_hash is not UNSET:
            field_dict["current_semantic_hash"] = current_semantic_hash
        if current_version_id is not UNSET:
            field_dict["current_version_id"] = current_version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_compatible_runtime_ids(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compatible_runtime_ids_type_0 = cast(list[str], data)

                return compatible_runtime_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        compatible_runtime_ids = _parse_compatible_runtime_ids(
            d.pop("compatible_runtime_ids")
        )

        def _parse_required_handlers(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                required_handlers_type_0 = cast(list[str], data)

                return required_handlers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        required_handlers = _parse_required_handlers(d.pop("required_handlers"))

        def _parse_required_sources(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                required_sources_type_0 = cast(list[str], data)

                return required_sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        required_sources = _parse_required_sources(d.pop("required_sources"))

        semantic_changed = d.pop("semantic_changed")

        semantic_hash = d.pop("semantic_hash")

        source_changed = d.pop("source_changed")

        source_hash = d.pop("source_hash")

        title = d.pop("title")

        def _parse_warnings(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = cast(list[str], data)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        warnings = _parse_warnings(d.pop("warnings"))

        workflow = d.pop("workflow")

        schema = d.pop("$schema", UNSET)

        current_semantic_hash = d.pop("current_semantic_hash", UNSET)

        current_version_id = d.pop("current_version_id", UNSET)

        deployment_preview = cls(
            compatible_runtime_ids=compatible_runtime_ids,
            required_handlers=required_handlers,
            required_sources=required_sources,
            semantic_changed=semantic_changed,
            semantic_hash=semantic_hash,
            source_changed=source_changed,
            source_hash=source_hash,
            title=title,
            warnings=warnings,
            workflow=workflow,
            schema=schema,
            current_semantic_hash=current_semantic_hash,
            current_version_id=current_version_id,
        )

        return deployment_preview
