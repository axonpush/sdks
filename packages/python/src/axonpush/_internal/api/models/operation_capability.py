from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.operation_capability_availability import OperationCapabilityAvailability
from ..types import UNSET, Unset

T = TypeVar("T", bound="OperationCapability")


@_attrs_define
class OperationCapability:
    """
    Attributes:
        availability (OperationCapabilityAvailability):
        operation_id (str):
        reason (str | Unset):
    """

    availability: OperationCapabilityAvailability
    operation_id: str
    reason: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        availability = self.availability.value

        operation_id = self.operation_id

        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "availability": availability,
                "operationId": operation_id,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        availability = OperationCapabilityAvailability(d.pop("availability"))

        operation_id = d.pop("operationId")

        reason = d.pop("reason", UNSET)

        operation_capability = cls(
            availability=availability,
            operation_id=operation_id,
            reason=reason,
        )

        return operation_capability
