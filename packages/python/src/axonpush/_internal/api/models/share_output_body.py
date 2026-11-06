from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.share_output_body_grant import ShareOutputBodyGrant
    from ..models.share_output_body_packs_type_0_item import ShareOutputBodyPacksType0Item


T = TypeVar("T", bound="ShareOutputBody")


@_attrs_define
class ShareOutputBody:
    """
    Attributes:
        grant (ShareOutputBodyGrant):
        packs (list[ShareOutputBodyPacksType0Item] | None):
        read_only (bool):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    grant: ShareOutputBodyGrant
    packs: list[ShareOutputBodyPacksType0Item] | None
    read_only: bool
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.share_output_body_grant import ShareOutputBodyGrant
        from ..models.share_output_body_packs_type_0_item import ShareOutputBodyPacksType0Item

        grant = self.grant.to_dict()

        packs: list[dict[str, Any]] | None
        if isinstance(self.packs, list):
            packs = []
            for packs_type_0_item_data in self.packs:
                packs_type_0_item = packs_type_0_item_data.to_dict()
                packs.append(packs_type_0_item)

        else:
            packs = self.packs

        read_only = self.read_only

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "grant": grant,
                "packs": packs,
                "readOnly": read_only,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.share_output_body_grant import ShareOutputBodyGrant
        from ..models.share_output_body_packs_type_0_item import ShareOutputBodyPacksType0Item

        d = dict(src_dict)
        grant = ShareOutputBodyGrant.from_dict(d.pop("grant"))

        def _parse_packs(data: object) -> list[ShareOutputBodyPacksType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                packs_type_0 = []
                _packs_type_0 = data
                for packs_type_0_item_data in _packs_type_0:
                    packs_type_0_item = ShareOutputBodyPacksType0Item.from_dict(
                        packs_type_0_item_data
                    )

                    packs_type_0.append(packs_type_0_item)

                return packs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ShareOutputBodyPacksType0Item] | None, data)

        packs = _parse_packs(d.pop("packs"))

        read_only = d.pop("readOnly")

        schema = d.pop("$schema", UNSET)

        share_output_body = cls(
            grant=grant,
            packs=packs,
            read_only=read_only,
            schema=schema,
        )

        return share_output_body
