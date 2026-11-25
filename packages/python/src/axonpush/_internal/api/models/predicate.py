from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast


T = TypeVar("T", bound="Predicate")


@_attrs_define
class Predicate:
    """
    Attributes:
        all_ (list[Predicate] | None | Unset):
        any_ (list[Predicate] | None | Unset):
        field (str | Unset):
        op (str | Unset):
        value (Any | Unset):
    """

    all_: list[Predicate] | None | Unset = UNSET
    any_: list[Predicate] | None | Unset = UNSET
    field: str | Unset = UNSET
    op: str | Unset = UNSET
    value: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        all_: list[dict[str, Any]] | None | Unset
        if isinstance(self.all_, Unset):
            all_ = UNSET
        elif isinstance(self.all_, list):
            all_ = []
            for all_type_0_item_data in self.all_:
                all_type_0_item = all_type_0_item_data.to_dict()
                all_.append(all_type_0_item)

        else:
            all_ = self.all_

        any_: list[dict[str, Any]] | None | Unset
        if isinstance(self.any_, Unset):
            any_ = UNSET
        elif isinstance(self.any_, list):
            any_ = []
            for any_type_0_item_data in self.any_:
                any_type_0_item = any_type_0_item_data.to_dict()
                any_.append(any_type_0_item)

        else:
            any_ = self.any_

        field = self.field

        op = self.op

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if any_ is not UNSET:
            field_dict["any"] = any_
        if field is not UNSET:
            field_dict["field"] = field
        if op is not UNSET:
            field_dict["op"] = op
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_all_(data: object) -> list[Predicate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                all_type_0 = []
                _all_type_0 = data
                for all_type_0_item_data in _all_type_0:
                    all_type_0_item = Predicate.from_dict(all_type_0_item_data)

                    all_type_0.append(all_type_0_item)

                return all_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Predicate] | None | Unset, data)

        all_ = _parse_all_(d.pop("all", UNSET))

        def _parse_any_(data: object) -> list[Predicate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                any_type_0 = []
                _any_type_0 = data
                for any_type_0_item_data in _any_type_0:
                    any_type_0_item = Predicate.from_dict(any_type_0_item_data)

                    any_type_0.append(any_type_0_item)

                return any_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Predicate] | None | Unset, data)

        any_ = _parse_any_(d.pop("any", UNSET))

        field = d.pop("field", UNSET)

        op = d.pop("op", UNSET)

        value = d.pop("value", UNSET)

        predicate = cls(
            all_=all_,
            any_=any_,
            field=field,
            op=op,
            value=value,
        )

        return predicate
