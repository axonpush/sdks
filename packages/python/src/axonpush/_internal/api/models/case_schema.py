from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.case_schema_fields import CaseSchemaFields


T = TypeVar("T", bound="CaseSchema")


@_attrs_define
class CaseSchema:
    """
    Attributes:
        key (str):
        fields (CaseSchemaFields | Unset):
    """

    key: str
    fields: CaseSchemaFields | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.case_schema_fields import CaseSchemaFields

        key = self.key

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.case_schema_fields import CaseSchemaFields

        d = dict(src_dict)
        key = d.pop("key")

        _fields = d.pop("fields", UNSET)
        fields: CaseSchemaFields | Unset
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = CaseSchemaFields.from_dict(_fields)

        case_schema = cls(
            key=key,
            fields=fields,
        )

        return case_schema
