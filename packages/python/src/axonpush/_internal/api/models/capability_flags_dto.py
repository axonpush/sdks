from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CapabilityFlagsDto")


@_attrs_define
class CapabilityFlagsDto:
    """
    Attributes:
        analytics_v2 (bool):
        assessments (bool):
        canonical_ingest (bool):
        evaluations (bool):
        failure_intelligence (bool):
        issues (bool):
        online_evaluations (bool):
        prompt_registry (bool):
        trace_intelligence (bool):
        trace_v2_read (bool):
        trace_v2_write (bool):
    """

    analytics_v2: bool
    assessments: bool
    canonical_ingest: bool
    evaluations: bool
    failure_intelligence: bool
    issues: bool
    online_evaluations: bool
    prompt_registry: bool
    trace_intelligence: bool
    trace_v2_read: bool
    trace_v2_write: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analytics_v2 = self.analytics_v2

        assessments = self.assessments

        canonical_ingest = self.canonical_ingest

        evaluations = self.evaluations

        failure_intelligence = self.failure_intelligence

        issues = self.issues

        online_evaluations = self.online_evaluations

        prompt_registry = self.prompt_registry

        trace_intelligence = self.trace_intelligence

        trace_v2_read = self.trace_v2_read

        trace_v2_write = self.trace_v2_write

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "analytics_v2": analytics_v2,
                "assessments": assessments,
                "canonical_ingest": canonical_ingest,
                "evaluations": evaluations,
                "failure_intelligence": failure_intelligence,
                "issues": issues,
                "online_evaluations": online_evaluations,
                "prompt_registry": prompt_registry,
                "trace_intelligence": trace_intelligence,
                "trace_v2_read": trace_v2_read,
                "trace_v2_write": trace_v2_write,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        analytics_v2 = d.pop("analytics_v2")

        assessments = d.pop("assessments")

        canonical_ingest = d.pop("canonical_ingest")

        evaluations = d.pop("evaluations")

        failure_intelligence = d.pop("failure_intelligence")

        issues = d.pop("issues")

        online_evaluations = d.pop("online_evaluations")

        prompt_registry = d.pop("prompt_registry")

        trace_intelligence = d.pop("trace_intelligence")

        trace_v2_read = d.pop("trace_v2_read")

        trace_v2_write = d.pop("trace_v2_write")

        capability_flags_dto = cls(
            analytics_v2=analytics_v2,
            assessments=assessments,
            canonical_ingest=canonical_ingest,
            evaluations=evaluations,
            failure_intelligence=failure_intelligence,
            issues=issues,
            online_evaluations=online_evaluations,
            prompt_registry=prompt_registry,
            trace_intelligence=trace_intelligence,
            trace_v2_read=trace_v2_read,
            trace_v2_write=trace_v2_write,
        )

        capability_flags_dto.additional_properties = d
        return capability_flags_dto

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
