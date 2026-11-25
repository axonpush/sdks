from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset


T = TypeVar("T", bound="AttachmentDTO")


@_attrs_define
class AttachmentDTO:
    """
    Attributes:
        attachment_type (str): event.attachment | event.minidump | event.view_hierarchy | ...
        content_type (str):
        created_at (str):
        filename (str):
        id (str):
        size (int):
        not_symbolicated (bool | Unset): Minidumps are stored raw, without native symbolication
        sentry_event_id (str | Unset):
        span_id (str | Unset):
        trace_id (str | Unset):
    """

    attachment_type: str
    content_type: str
    created_at: str
    filename: str
    id: str
    size: int
    not_symbolicated: bool | Unset = UNSET
    sentry_event_id: str | Unset = UNSET
    span_id: str | Unset = UNSET
    trace_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        attachment_type = self.attachment_type

        content_type = self.content_type

        created_at = self.created_at

        filename = self.filename

        id = self.id

        size = self.size

        not_symbolicated = self.not_symbolicated

        sentry_event_id = self.sentry_event_id

        span_id = self.span_id

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attachmentType": attachment_type,
                "contentType": content_type,
                "createdAt": created_at,
                "filename": filename,
                "id": id,
                "size": size,
            }
        )
        if not_symbolicated is not UNSET:
            field_dict["notSymbolicated"] = not_symbolicated
        if sentry_event_id is not UNSET:
            field_dict["sentryEventId"] = sentry_event_id
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attachment_type = d.pop("attachmentType")

        content_type = d.pop("contentType")

        created_at = d.pop("createdAt")

        filename = d.pop("filename")

        id = d.pop("id")

        size = d.pop("size")

        not_symbolicated = d.pop("notSymbolicated", UNSET)

        sentry_event_id = d.pop("sentryEventId", UNSET)

        span_id = d.pop("spanId", UNSET)

        trace_id = d.pop("traceId", UNSET)

        attachment_dto = cls(
            attachment_type=attachment_type,
            content_type=content_type,
            created_at=created_at,
            filename=filename,
            id=id,
            size=size,
            not_symbolicated=not_symbolicated,
            sentry_event_id=sentry_event_id,
            span_id=span_id,
            trace_id=trace_id,
        )

        return attachment_dto
