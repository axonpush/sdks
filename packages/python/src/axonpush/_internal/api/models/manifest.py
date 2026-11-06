from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_ import Object


T = TypeVar("T", bound="Manifest")


@_attrs_define
class Manifest:
    """
    Attributes:
        content (Object):
        lock_mode (str):
        locked_until (str):
        meta (Object):
        org_id (str):
        period (str):
        previous_hash (str):
        region (str):
        root (str):
        rows (int):
        schema (str):
        seal_hash (str):
        sealed_at (str):
        sequence (int):
    """

    content: Object
    lock_mode: str
    locked_until: str
    meta: Object
    org_id: str
    period: str
    previous_hash: str
    region: str
    root: str
    rows: int
    schema: str
    seal_hash: str
    sealed_at: str
    sequence: int

    def to_dict(self) -> dict[str, Any]:
        from ..models.object_ import Object

        content = self.content.to_dict()

        lock_mode = self.lock_mode

        locked_until = self.locked_until

        meta = self.meta.to_dict()

        org_id = self.org_id

        period = self.period

        previous_hash = self.previous_hash

        region = self.region

        root = self.root

        rows = self.rows

        schema = self.schema

        seal_hash = self.seal_hash

        sealed_at = self.sealed_at

        sequence = self.sequence

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "content": content,
                "lockMode": lock_mode,
                "lockedUntil": locked_until,
                "meta": meta,
                "orgId": org_id,
                "period": period,
                "previousHash": previous_hash,
                "region": region,
                "root": root,
                "rows": rows,
                "schema": schema,
                "sealHash": seal_hash,
                "sealedAt": sealed_at,
                "sequence": sequence,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_ import Object

        d = dict(src_dict)
        content = Object.from_dict(d.pop("content"))

        lock_mode = d.pop("lockMode")

        locked_until = d.pop("lockedUntil")

        meta = Object.from_dict(d.pop("meta"))

        org_id = d.pop("orgId")

        period = d.pop("period")

        previous_hash = d.pop("previousHash")

        region = d.pop("region")

        root = d.pop("root")

        rows = d.pop("rows")

        schema = d.pop("schema")

        seal_hash = d.pop("sealHash")

        sealed_at = d.pop("sealedAt")

        sequence = d.pop("sequence")

        manifest = cls(
            content=content,
            lock_mode=lock_mode,
            locked_until=locked_until,
            meta=meta,
            org_id=org_id,
            period=period,
            previous_hash=previous_hash,
            region=region,
            root=root,
            rows=rows,
            schema=schema,
            seal_hash=seal_hash,
            sealed_at=sealed_at,
            sequence=sequence,
        )

        return manifest
