from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_activity_evidence import ActivityActivityEvidence
from ..models.activity_activity_next_actor import ActivityActivityNextActor
from ..models.activity_activity_outcome import ActivityActivityOutcome
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityActivity")


@_attrs_define
class ActivityActivity:
    """
    Attributes:
        evidence (ActivityActivityEvidence):
        family (str):
        outcome (ActivityActivityOutcome):
        action (str | Unset):
        attempts (int | Unset):
        duration_ms (float | Unset):
        error_category (str | Unset):
        expected_seconds (int | Unset):
        input_tokens (int | Unset):
        join_method (str | Unset):
        model (str | Unset):
        next_actor (ActivityActivityNextActor | Unset):
        output_tokens (int | Unset):
        registration_source (str | Unset):
        snapshot (bool | Unset):
        state (str | Unset):
        transport (str | Unset):
    """

    evidence: ActivityActivityEvidence
    family: str
    outcome: ActivityActivityOutcome
    action: str | Unset = UNSET
    attempts: int | Unset = UNSET
    duration_ms: float | Unset = UNSET
    error_category: str | Unset = UNSET
    expected_seconds: int | Unset = UNSET
    input_tokens: int | Unset = UNSET
    join_method: str | Unset = UNSET
    model: str | Unset = UNSET
    next_actor: ActivityActivityNextActor | Unset = UNSET
    output_tokens: int | Unset = UNSET
    registration_source: str | Unset = UNSET
    snapshot: bool | Unset = UNSET
    state: str | Unset = UNSET
    transport: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        evidence = self.evidence.value

        family = self.family

        outcome = self.outcome.value

        action = self.action

        attempts = self.attempts

        duration_ms = self.duration_ms

        error_category = self.error_category

        expected_seconds = self.expected_seconds

        input_tokens = self.input_tokens

        join_method = self.join_method

        model = self.model

        next_actor: str | Unset = UNSET
        if not isinstance(self.next_actor, Unset):
            next_actor = self.next_actor.value

        output_tokens = self.output_tokens

        registration_source = self.registration_source

        snapshot = self.snapshot

        state = self.state

        transport = self.transport

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "evidence": evidence,
                "family": family,
                "outcome": outcome,
            }
        )
        if action is not UNSET:
            field_dict["action"] = action
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if error_category is not UNSET:
            field_dict["error_category"] = error_category
        if expected_seconds is not UNSET:
            field_dict["expected_seconds"] = expected_seconds
        if input_tokens is not UNSET:
            field_dict["input_tokens"] = input_tokens
        if join_method is not UNSET:
            field_dict["join_method"] = join_method
        if model is not UNSET:
            field_dict["model"] = model
        if next_actor is not UNSET:
            field_dict["next_actor"] = next_actor
        if output_tokens is not UNSET:
            field_dict["output_tokens"] = output_tokens
        if registration_source is not UNSET:
            field_dict["registration_source"] = registration_source
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot
        if state is not UNSET:
            field_dict["state"] = state
        if transport is not UNSET:
            field_dict["transport"] = transport

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        evidence = ActivityActivityEvidence(d.pop("evidence"))

        family = d.pop("family")

        outcome = ActivityActivityOutcome(d.pop("outcome"))

        action = d.pop("action", UNSET)

        attempts = d.pop("attempts", UNSET)

        duration_ms = d.pop("duration_ms", UNSET)

        error_category = d.pop("error_category", UNSET)

        expected_seconds = d.pop("expected_seconds", UNSET)

        input_tokens = d.pop("input_tokens", UNSET)

        join_method = d.pop("join_method", UNSET)

        model = d.pop("model", UNSET)

        _next_actor = d.pop("next_actor", UNSET)
        next_actor: ActivityActivityNextActor | Unset
        if isinstance(_next_actor, Unset):
            next_actor = UNSET
        else:
            next_actor = ActivityActivityNextActor(_next_actor)

        output_tokens = d.pop("output_tokens", UNSET)

        registration_source = d.pop("registration_source", UNSET)

        snapshot = d.pop("snapshot", UNSET)

        state = d.pop("state", UNSET)

        transport = d.pop("transport", UNSET)

        activity_activity = cls(
            evidence=evidence,
            family=family,
            outcome=outcome,
            action=action,
            attempts=attempts,
            duration_ms=duration_ms,
            error_category=error_category,
            expected_seconds=expected_seconds,
            input_tokens=input_tokens,
            join_method=join_method,
            model=model,
            next_actor=next_actor,
            output_tokens=output_tokens,
            registration_source=registration_source,
            snapshot=snapshot,
            state=state,
            transport=transport,
        )

        return activity_activity
