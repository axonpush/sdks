from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_group_dto import TraceGroupDTO


T = TypeVar("T", bound="TraceGroupsBody")


@_attrs_define
class TraceGroupsBody:
    """
    Attributes:
        failed_traces (int):
        finished_traces (int):
        groups (list[TraceGroupDTO] | None):
        since (str):
        total_groups (int):
        total_traces (int):
        until (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    failed_traces: int
    finished_traces: int
    groups: list[TraceGroupDTO] | None
    since: str
    total_groups: int
    total_traces: int
    until: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_group_dto import TraceGroupDTO

        failed_traces = self.failed_traces

        finished_traces = self.finished_traces

        groups: list[dict[str, Any]] | None
        if isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = groups_type_0_item_data.to_dict()
                groups.append(groups_type_0_item)

        else:
            groups = self.groups

        since = self.since

        total_groups = self.total_groups

        total_traces = self.total_traces

        until = self.until

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "failedTraces": failed_traces,
                "finishedTraces": finished_traces,
                "groups": groups,
                "since": since,
                "totalGroups": total_groups,
                "totalTraces": total_traces,
                "until": until,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_group_dto import TraceGroupDTO

        d = dict(src_dict)
        failed_traces = d.pop("failedTraces")

        finished_traces = d.pop("finishedTraces")

        def _parse_groups(data: object) -> list[TraceGroupDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in _groups_type_0:
                    groups_type_0_item = TraceGroupDTO.from_dict(groups_type_0_item_data)

                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TraceGroupDTO] | None, data)

        groups = _parse_groups(d.pop("groups"))

        since = d.pop("since")

        total_groups = d.pop("totalGroups")

        total_traces = d.pop("totalTraces")

        until = d.pop("until")

        schema = d.pop("$schema", UNSET)

        trace_groups_body = cls(
            failed_traces=failed_traces,
            finished_traces=finished_traces,
            groups=groups,
            since=since,
            total_groups=total_groups,
            total_traces=total_traces,
            until=until,
            schema=schema,
        )

        return trace_groups_body
