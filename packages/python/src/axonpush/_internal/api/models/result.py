from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.obligation import Obligation


T = TypeVar("T", bound="Result")


@_attrs_define
class Result:
    """
    Attributes:
        case_id (str):
        evaluated_at (datetime.datetime):
        obligations (list[Obligation] | None):
        semantic_hash (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    case_id: str
    evaluated_at: datetime.datetime
    obligations: list[Obligation] | None
    semantic_hash: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.obligation import Obligation

        case_id = self.case_id

        evaluated_at = self.evaluated_at.isoformat()

        obligations: list[dict[str, Any]] | None
        if isinstance(self.obligations, list):
            obligations = []
            for obligations_type_0_item_data in self.obligations:
                obligations_type_0_item = obligations_type_0_item_data.to_dict()
                obligations.append(obligations_type_0_item)

        else:
            obligations = self.obligations

        semantic_hash = self.semantic_hash

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "case_id": case_id,
                "evaluated_at": evaluated_at,
                "obligations": obligations,
                "semantic_hash": semantic_hash,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.obligation import Obligation

        d = dict(src_dict)
        case_id = d.pop("case_id")

        evaluated_at = isoparse(d.pop("evaluated_at"))

        def _parse_obligations(data: object) -> list[Obligation] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                obligations_type_0 = []
                _obligations_type_0 = data
                for obligations_type_0_item_data in _obligations_type_0:
                    obligations_type_0_item = Obligation.from_dict(obligations_type_0_item_data)

                    obligations_type_0.append(obligations_type_0_item)

                return obligations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Obligation] | None, data)

        obligations = _parse_obligations(d.pop("obligations"))

        semantic_hash = d.pop("semantic_hash")

        schema = d.pop("$schema", UNSET)

        result = cls(
            case_id=case_id,
            evaluated_at=evaluated_at,
            obligations=obligations,
            semantic_hash=semantic_hash,
            schema=schema,
        )

        return result
