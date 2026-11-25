from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.action_decision_decision import ActionDecisionDecision
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.action_decision_input import ActionDecisionInput


T = TypeVar("T", bound="ActionDecision")


@_attrs_define
class ActionDecision:
    """
    Attributes:
        decision (ActionDecisionDecision):
        revision (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
        input_ (ActionDecisionInput | Unset):
    """

    decision: ActionDecisionDecision
    revision: int
    schema: str | Unset = UNSET
    input_: ActionDecisionInput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_decision_input import ActionDecisionInput

        decision = self.decision.value

        revision = self.revision

        schema = self.schema

        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "decision": decision,
                "revision": revision,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_decision_input import ActionDecisionInput

        d = dict(src_dict)
        decision = ActionDecisionDecision(d.pop("decision"))

        revision = d.pop("revision")

        schema = d.pop("$schema", UNSET)

        _input_ = d.pop("input", UNSET)
        input_: ActionDecisionInput | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = ActionDecisionInput.from_dict(_input_)

        action_decision = cls(
            decision=decision,
            revision=revision,
            schema=schema,
            input_=input_,
        )

        return action_decision
