from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Meta")


@_attrs_define
class Meta:
    """
    Attributes:
        cipher_hash (str):
        ingested_at (str):
        key_id (str):
        ordinal (int):
        region (str):
    """

    cipher_hash: str
    ingested_at: str
    key_id: str
    ordinal: int
    region: str

    def to_dict(self) -> dict[str, Any]:
        cipher_hash = self.cipher_hash

        ingested_at = self.ingested_at

        key_id = self.key_id

        ordinal = self.ordinal

        region = self.region

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cipherHash": cipher_hash,
                "ingestedAt": ingested_at,
                "keyId": key_id,
                "ordinal": ordinal,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cipher_hash = d.pop("cipherHash")

        ingested_at = d.pop("ingestedAt")

        key_id = d.pop("keyId")

        ordinal = d.pop("ordinal")

        region = d.pop("region")

        meta = cls(
            cipher_hash=cipher_hash,
            ingested_at=ingested_at,
            key_id=key_id,
            ordinal=ordinal,
            region=region,
        )

        return meta
