from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compliance_record_data import ComplianceRecordData


T = TypeVar("T", bound="ComplianceRecord")


@_attrs_define
class ComplianceRecord:
    """
    Attributes:
        created_at (datetime.datetime):
        data (ComplianceRecordData):
        id (str):
        kind (str):
        state (str):
        updated_at (datetime.datetime):
        version (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    created_at: datetime.datetime
    data: ComplianceRecordData
    id: str
    kind: str
    state: str
    updated_at: datetime.datetime
    version: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_record_data import ComplianceRecordData

        created_at = self.created_at.isoformat()

        data = self.data.to_dict()

        id = self.id

        kind = self.kind

        state = self.state

        updated_at = self.updated_at.isoformat()

        version = self.version

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "data": data,
                "id": id,
                "kind": kind,
                "state": state,
                "updatedAt": updated_at,
                "version": version,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_record_data import ComplianceRecordData

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        data = ComplianceRecordData.from_dict(d.pop("data"))

        id = d.pop("id")

        kind = d.pop("kind")

        state = d.pop("state")

        updated_at = isoparse(d.pop("updatedAt"))

        version = d.pop("version")

        schema = d.pop("$schema", UNSET)

        compliance_record = cls(
            created_at=created_at,
            data=data,
            id=id,
            kind=kind,
            state=state,
            updated_at=updated_at,
            version=version,
            schema=schema,
        )

        return compliance_record
