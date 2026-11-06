from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.write_output_body_data import WriteOutputBodyData


T = TypeVar("T", bound="WriteOutputBody")


@_attrs_define
class WriteOutputBody:
    """
    Attributes:
        created_at (datetime.datetime):
        data (WriteOutputBodyData):
        id (str):
        kind (str):
        state (str):
        updated_at (datetime.datetime):
        version (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
        access_token (str | Unset):
    """

    created_at: datetime.datetime
    data: WriteOutputBodyData
    id: str
    kind: str
    state: str
    updated_at: datetime.datetime
    version: int
    schema: str | Unset = UNSET
    access_token: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.write_output_body_data import WriteOutputBodyData

        created_at = self.created_at.isoformat()

        data = self.data.to_dict()

        id = self.id

        kind = self.kind

        state = self.state

        updated_at = self.updated_at.isoformat()

        version = self.version

        schema = self.schema

        access_token = self.access_token

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
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.write_output_body_data import WriteOutputBodyData

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        data = WriteOutputBodyData.from_dict(d.pop("data"))

        id = d.pop("id")

        kind = d.pop("kind")

        state = d.pop("state")

        updated_at = isoparse(d.pop("updatedAt"))

        version = d.pop("version")

        schema = d.pop("$schema", UNSET)

        access_token = d.pop("accessToken", UNSET)

        write_output_body = cls(
            created_at=created_at,
            data=data,
            id=id,
            kind=kind,
            state=state,
            updated_at=updated_at,
            version=version,
            schema=schema,
            access_token=access_token,
        )

        return write_output_body
