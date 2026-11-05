from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceMetrics")


@_attrs_define
class ComplianceMetrics:
    """
    Attributes:
        decisions (int):
        denials (int):
        events (int):
        invalid (int):
        median_decision_ms (float):
        no_declared_task (int):
        notices (int):
        off_goal (int):
        override_rate (float):
        provenance (str):
        review_rate (float):
        tasks (int):
    """

    decisions: int
    denials: int
    events: int
    invalid: int
    median_decision_ms: float
    no_declared_task: int
    notices: int
    off_goal: int
    override_rate: float
    provenance: str
    review_rate: float
    tasks: int

    def to_dict(self) -> dict[str, Any]:
        decisions = self.decisions

        denials = self.denials

        events = self.events

        invalid = self.invalid

        median_decision_ms = self.median_decision_ms

        no_declared_task = self.no_declared_task

        notices = self.notices

        off_goal = self.off_goal

        override_rate = self.override_rate

        provenance = self.provenance

        review_rate = self.review_rate

        tasks = self.tasks

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "decisions": decisions,
                "denials": denials,
                "events": events,
                "invalid": invalid,
                "medianDecisionMs": median_decision_ms,
                "noDeclaredTask": no_declared_task,
                "notices": notices,
                "offGoal": off_goal,
                "overrideRate": override_rate,
                "provenance": provenance,
                "reviewRate": review_rate,
                "tasks": tasks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        decisions = d.pop("decisions")

        denials = d.pop("denials")

        events = d.pop("events")

        invalid = d.pop("invalid")

        median_decision_ms = d.pop("medianDecisionMs")

        no_declared_task = d.pop("noDeclaredTask")

        notices = d.pop("notices")

        off_goal = d.pop("offGoal")

        override_rate = d.pop("overrideRate")

        provenance = d.pop("provenance")

        review_rate = d.pop("reviewRate")

        tasks = d.pop("tasks")

        compliance_metrics = cls(
            decisions=decisions,
            denials=denials,
            events=events,
            invalid=invalid,
            median_decision_ms=median_decision_ms,
            no_declared_task=no_declared_task,
            notices=notices,
            off_goal=off_goal,
            override_rate=override_rate,
            provenance=provenance,
            review_rate=review_rate,
            tasks=tasks,
        )

        return compliance_metrics
