from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.contract import Contract


T = TypeVar("T", bound="Bundle")


@_attrs_define
class Bundle:
    """
    Attributes:
        compiler_version (str):
        contract (Contract):
        semantic_hash (str):
        source_hash (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    compiler_version: str
    contract: Contract
    semantic_hash: str
    source_hash: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.contract import Contract

        compiler_version = self.compiler_version

        contract = self.contract.to_dict()

        semantic_hash = self.semantic_hash

        source_hash = self.source_hash

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "compiler_version": compiler_version,
                "contract": contract,
                "semantic_hash": semantic_hash,
                "source_hash": source_hash,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contract import Contract

        d = dict(src_dict)
        compiler_version = d.pop("compiler_version")

        contract = Contract.from_dict(d.pop("contract"))

        semantic_hash = d.pop("semantic_hash")

        source_hash = d.pop("source_hash")

        schema = d.pop("$schema", UNSET)

        bundle = cls(
            compiler_version=compiler_version,
            contract=contract,
            semantic_hash=semantic_hash,
            source_hash=source_hash,
            schema=schema,
        )

        return bundle
