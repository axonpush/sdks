from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerJob")


@_attrs_define
class LedgerJob:
    """
    Attributes:
        created_at (datetime.datetime):
        cursor (str):
        id (str):
        kind (str):
        processed (int):
        recovery_required (bool):
        state (str):
        updated_at (datetime.datetime):
        schema (str | Unset): A URL to the JSON Schema for this object.
        error_code (str | Unset):
        result (Any | Unset):
    """

    created_at: datetime.datetime
    cursor: str
    id: str
    kind: str
    processed: int
    recovery_required: bool
    state: str
    updated_at: datetime.datetime
    schema: str | Unset = UNSET
    error_code: str | Unset = UNSET
    result: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        cursor = self.cursor

        id = self.id

        kind = self.kind

        processed = self.processed

        recovery_required = self.recovery_required

        state = self.state

        updated_at = self.updated_at.isoformat()

        schema = self.schema

        error_code = self.error_code

        result = self.result

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "createdAt": created_at,
                "cursor": cursor,
                "id": id,
                "kind": kind,
                "processed": processed,
                "recoveryRequired": recovery_required,
                "state": state,
                "updatedAt": updated_at,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        cursor = d.pop("cursor")

        id = d.pop("id")

        kind = d.pop("kind")

        processed = d.pop("processed")

        recovery_required = d.pop("recoveryRequired")

        state = d.pop("state")

        updated_at = isoparse(d.pop("updatedAt"))

        schema = d.pop("$schema", UNSET)

        error_code = d.pop("errorCode", UNSET)

        result = d.pop("result", UNSET)

        ledger_job = cls(
            created_at=created_at,
            cursor=cursor,
            id=id,
            kind=kind,
            processed=processed,
            recovery_required=recovery_required,
            state=state,
            updated_at=updated_at,
            schema=schema,
            error_code=error_code,
            result=result,
        )

        return ledger_job
