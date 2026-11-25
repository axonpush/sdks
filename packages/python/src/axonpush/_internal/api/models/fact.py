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
    from ..models.fact_fields import FactFields


T = TypeVar("T", bound="Fact")


@_attrs_define
class Fact:
    """
    Attributes:
        case_id (str):
        event (str):
        fields (FactFields):
        id (str):
        occurred_at (datetime.datetime):
        source (str):
        received_at (datetime.datetime | Unset):
        span_id (str | Unset):
        trace_id (str | Unset):
    """

    case_id: str
    event: str
    fields: FactFields
    id: str
    occurred_at: datetime.datetime
    source: str
    received_at: datetime.datetime | Unset = UNSET
    span_id: str | Unset = UNSET
    trace_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.fact_fields import FactFields

        case_id = self.case_id

        event = self.event

        fields = self.fields.to_dict()

        id = self.id

        occurred_at = self.occurred_at.isoformat()

        source = self.source

        received_at: str | Unset = UNSET
        if not isinstance(self.received_at, Unset):
            received_at = self.received_at.isoformat()

        span_id = self.span_id

        trace_id = self.trace_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "case_id": case_id,
                "event": event,
                "fields": fields,
                "id": id,
                "occurred_at": occurred_at,
                "source": source,
            }
        )
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if span_id is not UNSET:
            field_dict["span_id"] = span_id
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fact_fields import FactFields

        d = dict(src_dict)
        case_id = d.pop("case_id")

        event = d.pop("event")

        fields = FactFields.from_dict(d.pop("fields"))

        id = d.pop("id")

        occurred_at = isoparse(d.pop("occurred_at"))

        source = d.pop("source")

        _received_at = d.pop("received_at", UNSET)
        received_at: datetime.datetime | Unset
        if isinstance(_received_at, Unset):
            received_at = UNSET
        else:
            received_at = isoparse(_received_at)

        span_id = d.pop("span_id", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        fact = cls(
            case_id=case_id,
            event=event,
            fields=fields,
            id=id,
            occurred_at=occurred_at,
            source=source,
            received_at=received_at,
            span_id=span_id,
            trace_id=trace_id,
        )

        return fact
