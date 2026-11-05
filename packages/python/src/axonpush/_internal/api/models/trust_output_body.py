from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trust_output_body_gated_documents_type_0_item import (
        TrustOutputBodyGatedDocumentsType0Item,
    )
    from ..models.trust_output_body_sections import TrustOutputBodySections


T = TypeVar("T", bound="TrustOutputBody")


@_attrs_define
class TrustOutputBody:
    """
    Attributes:
        description (str):
        disclaimer (str):
        gated_documents (list[TrustOutputBodyGatedDocumentsType0Item] | None):
        sections (TrustOutputBodySections):
        slug (str):
        title (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    description: str
    disclaimer: str
    gated_documents: list[TrustOutputBodyGatedDocumentsType0Item] | None
    sections: TrustOutputBodySections
    slug: str
    title: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.trust_output_body_gated_documents_type_0_item import (
            TrustOutputBodyGatedDocumentsType0Item,
        )
        from ..models.trust_output_body_sections import TrustOutputBodySections

        description = self.description

        disclaimer = self.disclaimer

        gated_documents: list[dict[str, Any]] | None
        if isinstance(self.gated_documents, list):
            gated_documents = []
            for gated_documents_type_0_item_data in self.gated_documents:
                gated_documents_type_0_item = gated_documents_type_0_item_data.to_dict()
                gated_documents.append(gated_documents_type_0_item)

        else:
            gated_documents = self.gated_documents

        sections = self.sections.to_dict()

        slug = self.slug

        title = self.title

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "disclaimer": disclaimer,
                "gatedDocuments": gated_documents,
                "sections": sections,
                "slug": slug,
                "title": title,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trust_output_body_gated_documents_type_0_item import (
            TrustOutputBodyGatedDocumentsType0Item,
        )
        from ..models.trust_output_body_sections import TrustOutputBodySections

        d = dict(src_dict)
        description = d.pop("description")

        disclaimer = d.pop("disclaimer")

        def _parse_gated_documents(
            data: object,
        ) -> list[TrustOutputBodyGatedDocumentsType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                gated_documents_type_0 = []
                _gated_documents_type_0 = data
                for gated_documents_type_0_item_data in _gated_documents_type_0:
                    gated_documents_type_0_item = TrustOutputBodyGatedDocumentsType0Item.from_dict(
                        gated_documents_type_0_item_data
                    )

                    gated_documents_type_0.append(gated_documents_type_0_item)

                return gated_documents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TrustOutputBodyGatedDocumentsType0Item] | None, data)

        gated_documents = _parse_gated_documents(d.pop("gatedDocuments"))

        sections = TrustOutputBodySections.from_dict(d.pop("sections"))

        slug = d.pop("slug")

        title = d.pop("title")

        schema = d.pop("$schema", UNSET)

        trust_output_body = cls(
            description=description,
            disclaimer=disclaimer,
            gated_documents=gated_documents,
            sections=sections,
            slug=slug,
            title=title,
            schema=schema,
        )

        return trust_output_body
