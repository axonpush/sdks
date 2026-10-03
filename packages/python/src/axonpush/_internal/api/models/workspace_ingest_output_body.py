from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_receipt import ActivityReceipt


T = TypeVar("T", bound="WorkspaceIngestOutputBody")


@_attrs_define
class WorkspaceIngestOutputBody:
    """
    Attributes:
        receipts (list[ActivityReceipt] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    receipts: list[ActivityReceipt] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_receipt import ActivityReceipt

        receipts: list[dict[str, Any]] | None
        if isinstance(self.receipts, list):
            receipts = []
            for receipts_type_0_item_data in self.receipts:
                receipts_type_0_item = receipts_type_0_item_data.to_dict()
                receipts.append(receipts_type_0_item)

        else:
            receipts = self.receipts

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "receipts": receipts,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_receipt import ActivityReceipt

        d = dict(src_dict)

        def _parse_receipts(data: object) -> list[ActivityReceipt] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                receipts_type_0 = []
                _receipts_type_0 = data
                for receipts_type_0_item_data in _receipts_type_0:
                    receipts_type_0_item = ActivityReceipt.from_dict(receipts_type_0_item_data)

                    receipts_type_0.append(receipts_type_0_item)

                return receipts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityReceipt] | None, data)

        receipts = _parse_receipts(d.pop("receipts"))

        schema = d.pop("$schema", UNSET)

        workspace_ingest_output_body = cls(
            receipts=receipts,
            schema=schema,
        )

        return workspace_ingest_output_body
