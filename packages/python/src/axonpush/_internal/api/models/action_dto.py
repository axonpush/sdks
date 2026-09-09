from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.action_review_state import ActionReviewState
from ..models.action_verification_state import ActionVerificationState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_action_contract_dto import CreateActionContractDto
    from ..models.observe_action_dto import ObserveActionDto
    from ..models.register_action_dto import RegisterActionDto


T = TypeVar("T", bound="ActionDto")


@_attrs_define
class ActionDto:
    """
    Attributes:
        action_id (str):
        contract (CreateActionContractDto):
        created_at (datetime.datetime):
        registration (RegisterActionDto):
        review_state (ActionReviewState):
        state (ActionVerificationState):
        updated_at (datetime.datetime):
        verification_due_at (datetime.datetime):
        latest_observation (ObserveActionDto | Unset):
    """

    action_id: str
    contract: CreateActionContractDto
    created_at: datetime.datetime
    registration: RegisterActionDto
    review_state: ActionReviewState
    state: ActionVerificationState
    updated_at: datetime.datetime
    verification_due_at: datetime.datetime
    latest_observation: ObserveActionDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_action_contract_dto import CreateActionContractDto
        from ..models.observe_action_dto import ObserveActionDto
        from ..models.register_action_dto import RegisterActionDto

        action_id = self.action_id

        contract = self.contract.to_dict()

        created_at = self.created_at.isoformat()

        registration = self.registration.to_dict()

        review_state = self.review_state.value

        state = self.state.value

        updated_at = self.updated_at.isoformat()

        verification_due_at = self.verification_due_at.isoformat()

        latest_observation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_observation, Unset):
            latest_observation = self.latest_observation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionId": action_id,
                "contract": contract,
                "createdAt": created_at,
                "registration": registration,
                "reviewState": review_state,
                "state": state,
                "updatedAt": updated_at,
                "verificationDueAt": verification_due_at,
            }
        )
        if latest_observation is not UNSET:
            field_dict["latestObservation"] = latest_observation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_action_contract_dto import CreateActionContractDto
        from ..models.observe_action_dto import ObserveActionDto
        from ..models.register_action_dto import RegisterActionDto

        d = dict(src_dict)
        action_id = d.pop("actionId")

        contract = CreateActionContractDto.from_dict(d.pop("contract"))

        created_at = isoparse(d.pop("createdAt"))

        registration = RegisterActionDto.from_dict(d.pop("registration"))

        review_state = ActionReviewState(d.pop("reviewState"))

        state = ActionVerificationState(d.pop("state"))

        updated_at = isoparse(d.pop("updatedAt"))

        verification_due_at = isoparse(d.pop("verificationDueAt"))

        _latest_observation = d.pop("latestObservation", UNSET)
        latest_observation: ObserveActionDto | Unset
        if isinstance(_latest_observation, Unset):
            latest_observation = UNSET
        else:
            latest_observation = ObserveActionDto.from_dict(_latest_observation)

        action_dto = cls(
            action_id=action_id,
            contract=contract,
            created_at=created_at,
            registration=registration,
            review_state=review_state,
            state=state,
            updated_at=updated_at,
            verification_due_at=verification_due_at,
            latest_observation=latest_observation,
        )

        action_dto.additional_properties = d
        return action_dto

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
