from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueBucketDTO")


@_attrs_define
class IssueBucketDTO:
    """
    Attributes:
        bucket (str):
        count (int):
    """

    bucket: str
    count: int

    def to_dict(self) -> dict[str, Any]:
        bucket = self.bucket

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bucket": bucket,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket = d.pop("bucket")

        count = d.pop("count")

        issue_bucket_dto = cls(
            bucket=bucket,
            count=count,
        )

        return issue_bucket_dto
