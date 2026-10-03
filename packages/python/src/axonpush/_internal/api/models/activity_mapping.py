from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_mapping_fields import ActivityMappingFields
    from ..models.activity_mapping_values import ActivityMappingValues


T = TypeVar("T", bound="ActivityMapping")


@_attrs_define
class ActivityMapping:
    """
    Attributes:
        entity (str):
        event (str):
        id_path (str):
        fields (ActivityMappingFields | Unset):
        values (ActivityMappingValues | Unset):
    """

    entity: str
    event: str
    id_path: str
    fields: ActivityMappingFields | Unset = UNSET
    values: ActivityMappingValues | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_mapping_fields import ActivityMappingFields
        from ..models.activity_mapping_values import ActivityMappingValues

        entity = self.entity

        event = self.event

        id_path = self.id_path

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entity": entity,
                "event": event,
                "idPath": id_path,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_mapping_fields import ActivityMappingFields
        from ..models.activity_mapping_values import ActivityMappingValues

        d = dict(src_dict)
        entity = d.pop("entity")

        event = d.pop("event")

        id_path = d.pop("idPath")

        _fields = d.pop("fields", UNSET)
        fields: ActivityMappingFields | Unset
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = ActivityMappingFields.from_dict(_fields)

        _values = d.pop("values", UNSET)
        values: ActivityMappingValues | Unset
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = ActivityMappingValues.from_dict(_values)

        activity_mapping = cls(
            entity=entity,
            event=event,
            id_path=id_path,
            fields=fields,
            values=values,
        )

        return activity_mapping
