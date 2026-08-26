from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackfillOnlineRuleDto")


@_attrs_define
class BackfillOnlineRuleDto:
    """
    Attributes:
        from_ (datetime.datetime):
        to (datetime.datetime):
        limit (float | Unset):  Default: 1000.0.
    """

    from_: datetime.datetime
    to: datetime.datetime
    limit: float | Unset = 1000.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = isoparse(d.pop("from"))

        to = isoparse(d.pop("to"))

        limit = d.pop("limit", UNSET)

        backfill_online_rule_dto = cls(
            from_=from_,
            to=to,
            limit=limit,
        )

        backfill_online_rule_dto.additional_properties = d
        return backfill_online_rule_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
