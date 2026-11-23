from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_dto import AttachmentDTO


T = TypeVar("T", bound="ListAttachmentsOutputBody")


@_attrs_define
class ListAttachmentsOutputBody:
    """
    Attributes:
        attachments (list[AttachmentDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    attachments: list[AttachmentDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.attachment_dto import AttachmentDTO

        attachments: list[dict[str, Any]] | None
        if isinstance(self.attachments, list):
            attachments = []
            for attachments_type_0_item_data in self.attachments:
                attachments_type_0_item = attachments_type_0_item_data.to_dict()
                attachments.append(attachments_type_0_item)

        else:
            attachments = self.attachments

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attachments": attachments,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_dto import AttachmentDTO

        d = dict(src_dict)

        def _parse_attachments(data: object) -> list[AttachmentDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachments_type_0 = []
                _attachments_type_0 = data
                for attachments_type_0_item_data in _attachments_type_0:
                    attachments_type_0_item = AttachmentDTO.from_dict(
                        attachments_type_0_item_data
                    )

                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AttachmentDTO] | None, data)

        attachments = _parse_attachments(d.pop("attachments"))

        schema = d.pop("$schema", UNSET)

        list_attachments_output_body = cls(
            attachments=attachments,
            schema=schema,
        )

        return list_attachments_output_body
