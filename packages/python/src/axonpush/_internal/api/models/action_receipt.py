from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.action_receipt_result import ActionReceiptResult
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.action_receipt_observed import ActionReceiptObserved
    from ..models.action_receipt_output import ActionReceiptOutput


T = TypeVar("T", bound="ActionReceipt")


@_attrs_define
class ActionReceipt:
    """
    Attributes:
        result (ActionReceiptResult):
        revision (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
        observed (ActionReceiptObserved | Unset):
        output (ActionReceiptOutput | Unset):
    """

    result: ActionReceiptResult
    revision: int
    schema: str | Unset = UNSET
    observed: ActionReceiptObserved | Unset = UNSET
    output: ActionReceiptOutput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_receipt_observed import ActionReceiptObserved
        from ..models.action_receipt_output import ActionReceiptOutput

        result = self.result.value

        revision = self.revision

        schema = self.schema

        observed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.observed, Unset):
            observed = self.observed.to_dict()

        output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "result": result,
                "revision": revision,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if observed is not UNSET:
            field_dict["observed"] = observed
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_receipt_observed import ActionReceiptObserved
        from ..models.action_receipt_output import ActionReceiptOutput

        d = dict(src_dict)
        result = ActionReceiptResult(d.pop("result"))

        revision = d.pop("revision")

        schema = d.pop("$schema", UNSET)

        _observed = d.pop("observed", UNSET)
        observed: ActionReceiptObserved | Unset
        if isinstance(_observed, Unset):
            observed = UNSET
        else:
            observed = ActionReceiptObserved.from_dict(_observed)

        _output = d.pop("output", UNSET)
        output: ActionReceiptOutput | Unset
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = ActionReceiptOutput.from_dict(_output)

        action_receipt = cls(
            result=result,
            revision=revision,
            schema=schema,
            observed=observed,
            output=output,
        )

        return action_receipt
