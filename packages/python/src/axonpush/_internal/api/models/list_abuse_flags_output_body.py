from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abuse_flag_dto import AbuseFlagDTO


T = TypeVar("T", bound="ListAbuseFlagsOutputBody")


@_attrs_define
class ListAbuseFlagsOutputBody:
    """
    Attributes:
        flags (list[AbuseFlagDTO] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    flags: list[AbuseFlagDTO] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.abuse_flag_dto import AbuseFlagDTO

        flags: list[dict[str, Any]] | None
        if isinstance(self.flags, list):
            flags = []
            for flags_type_0_item_data in self.flags:
                flags_type_0_item = flags_type_0_item_data.to_dict()
                flags.append(flags_type_0_item)

        else:
            flags = self.flags

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "flags": flags,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abuse_flag_dto import AbuseFlagDTO

        d = dict(src_dict)

        def _parse_flags(data: object) -> list[AbuseFlagDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                flags_type_0 = []
                _flags_type_0 = data
                for flags_type_0_item_data in _flags_type_0:
                    flags_type_0_item = AbuseFlagDTO.from_dict(flags_type_0_item_data)

                    flags_type_0.append(flags_type_0_item)

                return flags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AbuseFlagDTO] | None, data)

        flags = _parse_flags(d.pop("flags"))

        schema = d.pop("$schema", UNSET)

        list_abuse_flags_output_body = cls(
            flags=flags,
            schema=schema,
        )

        return list_abuse_flags_output_body
