from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_draft_op import ActivityDraftOp


T = TypeVar("T", bound="OpsInputBody")


@_attrs_define
class OpsInputBody:
    """
    Attributes:
        ops (list[ActivityDraftOp] | None):
        version (int): The draft version you read; a mismatch returns 409 with the current draft
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    ops: list[ActivityDraftOp] | None
    version: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_draft_op import ActivityDraftOp

        ops: list[dict[str, Any]] | None
        if isinstance(self.ops, list):
            ops = []
            for ops_type_0_item_data in self.ops:
                ops_type_0_item = ops_type_0_item_data.to_dict()
                ops.append(ops_type_0_item)

        else:
            ops = self.ops

        version = self.version

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "ops": ops,
                "version": version,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_draft_op import ActivityDraftOp

        d = dict(src_dict)

        def _parse_ops(data: object) -> list[ActivityDraftOp] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ops_type_0 = []
                _ops_type_0 = data
                for ops_type_0_item_data in _ops_type_0:
                    ops_type_0_item = ActivityDraftOp.from_dict(ops_type_0_item_data)

                    ops_type_0.append(ops_type_0_item)

                return ops_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActivityDraftOp] | None, data)

        ops = _parse_ops(d.pop("ops"))

        version = d.pop("version")

        schema = d.pop("$schema", UNSET)

        ops_input_body = cls(
            ops=ops,
            version=version,
            schema=schema,
        )

        return ops_input_body
