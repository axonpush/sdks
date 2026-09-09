from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.action_evidence_kind import ActionEvidenceKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_evidence_dto_payload import ActionEvidenceDtoPayload


T = TypeVar("T", bound="ActionEvidenceDto")


@_attrs_define
class ActionEvidenceDto:
    """
    Attributes:
        actor_id (str):
        event_id (str):
        kind (ActionEvidenceKind):
        payload (ActionEvidenceDtoPayload):
        received_at (datetime.datetime):
    """

    actor_id: str
    event_id: str
    kind: ActionEvidenceKind
    payload: ActionEvidenceDtoPayload
    received_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_evidence_dto_payload import ActionEvidenceDtoPayload

        actor_id = self.actor_id

        event_id = self.event_id

        kind = self.kind.value

        payload = self.payload.to_dict()

        received_at = self.received_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actorId": actor_id,
                "eventId": event_id,
                "kind": kind,
                "payload": payload,
                "receivedAt": received_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_evidence_dto_payload import ActionEvidenceDtoPayload

        d = dict(src_dict)
        actor_id = d.pop("actorId")

        event_id = d.pop("eventId")

        kind = ActionEvidenceKind(d.pop("kind"))

        payload = ActionEvidenceDtoPayload.from_dict(d.pop("payload"))

        received_at = isoparse(d.pop("receivedAt"))

        action_evidence_dto = cls(
            actor_id=actor_id,
            event_id=event_id,
            kind=kind,
            payload=payload,
            received_at=received_at,
        )

        action_evidence_dto.additional_properties = d
        return action_evidence_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
