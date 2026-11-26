from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fact_schema_fields import FactSchemaFields


T = TypeVar("T", bound="FactSchema")


@_attrs_define
class FactSchema:
    """
    Attributes:
        fields (FactSchemaFields):
        evidence_class (str | Unset):
    """

    fields: FactSchemaFields
    evidence_class: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.fact_schema_fields import FactSchemaFields

        fields = self.fields.to_dict()

        evidence_class = self.evidence_class

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fields": fields,
            }
        )
        if evidence_class is not UNSET:
            field_dict["evidence_class"] = evidence_class

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fact_schema_fields import FactSchemaFields

        d = dict(src_dict)
        fields = FactSchemaFields.from_dict(d.pop("fields"))

        evidence_class = d.pop("evidence_class", UNSET)

        fact_schema = cls(
            fields=fields,
            evidence_class=evidence_class,
        )

        return fact_schema
