from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.action_change import ActionChange
    from ..models.action_record_input import ActionRecordInput
    from ..models.action_record_observed import ActionRecordObserved
    from ..models.action_record_original import ActionRecordOriginal
    from ..models.action_record_output import ActionRecordOutput
    from ..models.obligation import Obligation


T = TypeVar("T", bound="ActionRecord")


@_attrs_define
class ActionRecord:
    """
    Attributes:
        actor (str):
        approved_at (datetime.datetime):
        case_id (str):
        case_key (str):
        handler (str):
        history (list[ActionChange] | None):
        id (str):
        input_ (ActionRecordInput):
        lease_until (datetime.datetime):
        name (str):
        operation (int):
        original (ActionRecordOriginal):
        request_hash (str):
        revision (int):
        status (str):
        version_id (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        mode (str | Unset):
        observed (ActionRecordObserved | Unset):
        output (ActionRecordOutput | Unset):
        reason (str | Unset):
        reviewer (str | Unset):
        verification (Obligation | Unset):
    """

    actor: str
    approved_at: datetime.datetime
    case_id: str
    case_key: str
    handler: str
    history: list[ActionChange] | None
    id: str
    input_: ActionRecordInput
    lease_until: datetime.datetime
    name: str
    operation: int
    original: ActionRecordOriginal
    request_hash: str
    revision: int
    status: str
    version_id: str
    schema: str | Unset = UNSET
    mode: str | Unset = UNSET
    observed: ActionRecordObserved | Unset = UNSET
    output: ActionRecordOutput | Unset = UNSET
    reason: str | Unset = UNSET
    reviewer: str | Unset = UNSET
    verification: Obligation | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_change import ActionChange
        from ..models.action_record_input import ActionRecordInput
        from ..models.action_record_observed import ActionRecordObserved
        from ..models.action_record_original import ActionRecordOriginal
        from ..models.action_record_output import ActionRecordOutput
        from ..models.obligation import Obligation

        actor = self.actor

        approved_at = self.approved_at.isoformat()

        case_id = self.case_id

        case_key = self.case_key

        handler = self.handler

        history: list[dict[str, Any]] | None
        if isinstance(self.history, list):
            history = []
            for history_type_0_item_data in self.history:
                history_type_0_item = history_type_0_item_data.to_dict()
                history.append(history_type_0_item)

        else:
            history = self.history

        id = self.id

        input_ = self.input_.to_dict()

        lease_until = self.lease_until.isoformat()

        name = self.name

        operation = self.operation

        original = self.original.to_dict()

        request_hash = self.request_hash

        revision = self.revision

        status = self.status

        version_id = self.version_id

        schema = self.schema

        mode = self.mode

        observed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.observed, Unset):
            observed = self.observed.to_dict()

        output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        reason = self.reason

        reviewer = self.reviewer

        verification: dict[str, Any] | Unset = UNSET
        if not isinstance(self.verification, Unset):
            verification = self.verification.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "actor": actor,
                "approved_at": approved_at,
                "case_id": case_id,
                "case_key": case_key,
                "handler": handler,
                "history": history,
                "id": id,
                "input": input_,
                "lease_until": lease_until,
                "name": name,
                "operation": operation,
                "original": original,
                "request_hash": request_hash,
                "revision": revision,
                "status": status,
                "version_id": version_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if mode is not UNSET:
            field_dict["mode"] = mode
        if observed is not UNSET:
            field_dict["observed"] = observed
        if output is not UNSET:
            field_dict["output"] = output
        if reason is not UNSET:
            field_dict["reason"] = reason
        if reviewer is not UNSET:
            field_dict["reviewer"] = reviewer
        if verification is not UNSET:
            field_dict["verification"] = verification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_change import ActionChange
        from ..models.action_record_input import ActionRecordInput
        from ..models.action_record_observed import ActionRecordObserved
        from ..models.action_record_original import ActionRecordOriginal
        from ..models.action_record_output import ActionRecordOutput
        from ..models.obligation import Obligation

        d = dict(src_dict)
        actor = d.pop("actor")

        approved_at = isoparse(d.pop("approved_at"))

        case_id = d.pop("case_id")

        case_key = d.pop("case_key")

        handler = d.pop("handler")

        def _parse_history(data: object) -> list[ActionChange] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                history_type_0 = []
                _history_type_0 = data
                for history_type_0_item_data in _history_type_0:
                    history_type_0_item = ActionChange.from_dict(history_type_0_item_data)

                    history_type_0.append(history_type_0_item)

                return history_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ActionChange] | None, data)

        history = _parse_history(d.pop("history"))

        id = d.pop("id")

        input_ = ActionRecordInput.from_dict(d.pop("input"))

        lease_until = isoparse(d.pop("lease_until"))

        name = d.pop("name")

        operation = d.pop("operation")

        original = ActionRecordOriginal.from_dict(d.pop("original"))

        request_hash = d.pop("request_hash")

        revision = d.pop("revision")

        status = d.pop("status")

        version_id = d.pop("version_id")

        schema = d.pop("$schema", UNSET)

        mode = d.pop("mode", UNSET)

        _observed = d.pop("observed", UNSET)
        observed: ActionRecordObserved | Unset
        if isinstance(_observed, Unset):
            observed = UNSET
        else:
            observed = ActionRecordObserved.from_dict(_observed)

        _output = d.pop("output", UNSET)
        output: ActionRecordOutput | Unset
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = ActionRecordOutput.from_dict(_output)

        reason = d.pop("reason", UNSET)

        reviewer = d.pop("reviewer", UNSET)

        _verification = d.pop("verification", UNSET)
        verification: Obligation | Unset
        if isinstance(_verification, Unset):
            verification = UNSET
        else:
            verification = Obligation.from_dict(_verification)

        action_record = cls(
            actor=actor,
            approved_at=approved_at,
            case_id=case_id,
            case_key=case_key,
            handler=handler,
            history=history,
            id=id,
            input_=input_,
            lease_until=lease_until,
            name=name,
            operation=operation,
            original=original,
            request_hash=request_hash,
            revision=revision,
            status=status,
            version_id=version_id,
            schema=schema,
            mode=mode,
            observed=observed,
            output=output,
            reason=reason,
            reviewer=reviewer,
            verification=verification,
        )

        return action_record
