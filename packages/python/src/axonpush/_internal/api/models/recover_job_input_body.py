from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecoverJobInputBody")


@_attrs_define
class RecoverJobInputBody:
    """
    Attributes:
        confirm_worker_stopped (bool):
        reason (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    confirm_worker_stopped: bool
    reason: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        confirm_worker_stopped = self.confirm_worker_stopped

        reason = self.reason

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "confirmWorkerStopped": confirm_worker_stopped,
                "reason": reason,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirm_worker_stopped = d.pop("confirmWorkerStopped")

        reason = d.pop("reason")

        schema = d.pop("$schema", UNSET)

        recover_job_input_body = cls(
            confirm_worker_stopped=confirm_worker_stopped,
            reason=reason,
            schema=schema,
        )

        return recover_job_input_body
