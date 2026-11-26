from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyResult")


@_attrs_define
class VerifyResult:
    """
    Attributes:
        count (int):
        ok (bool):
        schema (str | Unset): A URL to the JSON Schema for this object.
        actual (str | Unset):
        broken_at_seq (int | Unset):
        expected (str | Unset):
    """

    count: int
    ok: bool
    schema: str | Unset = UNSET
    actual: str | Unset = UNSET
    broken_at_seq: int | Unset = UNSET
    expected: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        ok = self.ok

        schema = self.schema

        actual = self.actual

        broken_at_seq = self.broken_at_seq

        expected = self.expected

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "ok": ok,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if actual is not UNSET:
            field_dict["actual"] = actual
        if broken_at_seq is not UNSET:
            field_dict["brokenAtSeq"] = broken_at_seq
        if expected is not UNSET:
            field_dict["expected"] = expected

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count")

        ok = d.pop("ok")

        schema = d.pop("$schema", UNSET)

        actual = d.pop("actual", UNSET)

        broken_at_seq = d.pop("brokenAtSeq", UNSET)

        expected = d.pop("expected", UNSET)

        verify_result = cls(
            count=count,
            ok=ok,
            schema=schema,
            actual=actual,
            broken_at_seq=broken_at_seq,
            expected=expected,
        )

        return verify_result
