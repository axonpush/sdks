from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.action_record import ActionRecord


T = TypeVar("T", bound="ClaimResponseBody")


@_attrs_define
class ClaimResponseBody:
    """
    Attributes:
        schema (str | Unset): A URL to the JSON Schema for this object.
        action (ActionRecord | Unset):
    """

    schema: str | Unset = UNSET
    action: ActionRecord | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_record import ActionRecord

        schema = self.schema

        action: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if action is not UNSET:
            field_dict["action"] = action

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_record import ActionRecord

        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        _action = d.pop("action", UNSET)
        action: ActionRecord | Unset
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ActionRecord.from_dict(_action)

        claim_response_body = cls(
            schema=schema,
            action=action,
        )

        return claim_response_body
