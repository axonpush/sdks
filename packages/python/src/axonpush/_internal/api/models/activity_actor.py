from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_actor_participant_side import ActivityActorParticipantSide
from ..models.activity_actor_type import ActivityActorType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityActor")


@_attrs_define
class ActivityActor:
    """
    Attributes:
        type_ (ActivityActorType):
        agent_id (str | Unset):
        initiating_agent_id (str | Unset):
        participant_side (ActivityActorParticipantSide | Unset):
        related_agent_ids (list[str] | None | Unset):
    """

    type_: ActivityActorType
    agent_id: str | Unset = UNSET
    initiating_agent_id: str | Unset = UNSET
    participant_side: ActivityActorParticipantSide | Unset = UNSET
    related_agent_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        agent_id = self.agent_id

        initiating_agent_id = self.initiating_agent_id

        participant_side: str | Unset = UNSET
        if not isinstance(self.participant_side, Unset):
            participant_side = self.participant_side.value

        related_agent_ids: list[str] | None | Unset
        if isinstance(self.related_agent_ids, Unset):
            related_agent_ids = UNSET
        elif isinstance(self.related_agent_ids, list):
            related_agent_ids = self.related_agent_ids

        else:
            related_agent_ids = self.related_agent_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if agent_id is not UNSET:
            field_dict["agent_id"] = agent_id
        if initiating_agent_id is not UNSET:
            field_dict["initiating_agent_id"] = initiating_agent_id
        if participant_side is not UNSET:
            field_dict["participant_side"] = participant_side
        if related_agent_ids is not UNSET:
            field_dict["related_agent_ids"] = related_agent_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = ActivityActorType(d.pop("type"))

        agent_id = d.pop("agent_id", UNSET)

        initiating_agent_id = d.pop("initiating_agent_id", UNSET)

        _participant_side = d.pop("participant_side", UNSET)
        participant_side: ActivityActorParticipantSide | Unset
        if isinstance(_participant_side, Unset):
            participant_side = UNSET
        else:
            participant_side = ActivityActorParticipantSide(_participant_side)

        def _parse_related_agent_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                related_agent_ids_type_0 = cast(list[str], data)

                return related_agent_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        related_agent_ids = _parse_related_agent_ids(d.pop("related_agent_ids", UNSET))

        activity_actor = cls(
            type_=type_,
            agent_id=agent_id,
            initiating_agent_id=initiating_agent_id,
            participant_side=participant_side,
            related_agent_ids=related_agent_ids,
        )

        return activity_actor
