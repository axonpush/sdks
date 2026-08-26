from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTraceIntelligenceBackfillDto")


@_attrs_define
class CreateTraceIntelligenceBackfillDto:
    """
    Attributes:
        app_id (str):
        environment_id (str):
        from_ (datetime.datetime):
        to (datetime.datetime):
        max_traces (float | Unset):  Default: 1000.0.
    """

    app_id: str
    environment_id: str
    from_: datetime.datetime
    to: datetime.datetime
    max_traces: float | Unset = 1000.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        environment_id = self.environment_id

        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        max_traces = self.max_traces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appId": app_id,
                "environmentId": environment_id,
                "from": from_,
                "to": to,
            }
        )
        if max_traces is not UNSET:
            field_dict["maxTraces"] = max_traces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("appId")

        environment_id = d.pop("environmentId")

        from_ = isoparse(d.pop("from"))

        to = isoparse(d.pop("to"))

        max_traces = d.pop("maxTraces", UNSET)

        create_trace_intelligence_backfill_dto = cls(
            app_id=app_id,
            environment_id=environment_id,
            from_=from_,
            to=to,
            max_traces=max_traces,
        )

        create_trace_intelligence_backfill_dto.additional_properties = d
        return create_trace_intelligence_backfill_dto

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
