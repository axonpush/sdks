from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.release_hour_dto import ReleaseHourDTO


T = TypeVar("T", bound="ReleaseDetailDTO")


@_attrs_define
class ReleaseDetailDTO:
    """
    Attributes:
        abnormal_sessions (int):
        crashed_sessions (int):
        crashed_users (int):
        errored_sessions (int):
        errors (int): Error events carrying this release in the window
        new_issues (int): Issues first seen in the window on this release
        release (str):
        series (list[ReleaseHourDTO] | None):
        sessions (int):
        users (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
        adoption_pct (float | Unset): Share of all sessions in the window
        crash_free_sessions_pct (float | Unset):
        crash_free_users_pct (float | Unset):
        first_seen (str | Unset):
        last_seen (str | Unset):
    """

    abnormal_sessions: int
    crashed_sessions: int
    crashed_users: int
    errored_sessions: int
    errors: int
    new_issues: int
    release: str
    series: list[ReleaseHourDTO] | None
    sessions: int
    users: int
    schema: str | Unset = UNSET
    adoption_pct: float | Unset = UNSET
    crash_free_sessions_pct: float | Unset = UNSET
    crash_free_users_pct: float | Unset = UNSET
    first_seen: str | Unset = UNSET
    last_seen: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.release_hour_dto import ReleaseHourDTO

        abnormal_sessions = self.abnormal_sessions

        crashed_sessions = self.crashed_sessions

        crashed_users = self.crashed_users

        errored_sessions = self.errored_sessions

        errors = self.errors

        new_issues = self.new_issues

        release = self.release

        series: list[dict[str, Any]] | None
        if isinstance(self.series, list):
            series = []
            for series_type_0_item_data in self.series:
                series_type_0_item = series_type_0_item_data.to_dict()
                series.append(series_type_0_item)

        else:
            series = self.series

        sessions = self.sessions

        users = self.users

        schema = self.schema

        adoption_pct = self.adoption_pct

        crash_free_sessions_pct = self.crash_free_sessions_pct

        crash_free_users_pct = self.crash_free_users_pct

        first_seen = self.first_seen

        last_seen = self.last_seen

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "abnormalSessions": abnormal_sessions,
                "crashedSessions": crashed_sessions,
                "crashedUsers": crashed_users,
                "erroredSessions": errored_sessions,
                "errors": errors,
                "newIssues": new_issues,
                "release": release,
                "series": series,
                "sessions": sessions,
                "users": users,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if adoption_pct is not UNSET:
            field_dict["adoptionPct"] = adoption_pct
        if crash_free_sessions_pct is not UNSET:
            field_dict["crashFreeSessionsPct"] = crash_free_sessions_pct
        if crash_free_users_pct is not UNSET:
            field_dict["crashFreeUsersPct"] = crash_free_users_pct
        if first_seen is not UNSET:
            field_dict["firstSeen"] = first_seen
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.release_hour_dto import ReleaseHourDTO

        d = dict(src_dict)
        abnormal_sessions = d.pop("abnormalSessions")

        crashed_sessions = d.pop("crashedSessions")

        crashed_users = d.pop("crashedUsers")

        errored_sessions = d.pop("erroredSessions")

        errors = d.pop("errors")

        new_issues = d.pop("newIssues")

        release = d.pop("release")

        def _parse_series(data: object) -> list[ReleaseHourDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_type_0 = []
                _series_type_0 = data
                for series_type_0_item_data in _series_type_0:
                    series_type_0_item = ReleaseHourDTO.from_dict(
                        series_type_0_item_data
                    )

                    series_type_0.append(series_type_0_item)

                return series_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ReleaseHourDTO] | None, data)

        series = _parse_series(d.pop("series"))

        sessions = d.pop("sessions")

        users = d.pop("users")

        schema = d.pop("$schema", UNSET)

        adoption_pct = d.pop("adoptionPct", UNSET)

        crash_free_sessions_pct = d.pop("crashFreeSessionsPct", UNSET)

        crash_free_users_pct = d.pop("crashFreeUsersPct", UNSET)

        first_seen = d.pop("firstSeen", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        release_detail_dto = cls(
            abnormal_sessions=abnormal_sessions,
            crashed_sessions=crashed_sessions,
            crashed_users=crashed_users,
            errored_sessions=errored_sessions,
            errors=errors,
            new_issues=new_issues,
            release=release,
            series=series,
            sessions=sessions,
            users=users,
            schema=schema,
            adoption_pct=adoption_pct,
            crash_free_sessions_pct=crash_free_sessions_pct,
            crash_free_users_pct=crash_free_users_pct,
            first_seen=first_seen,
            last_seen=last_seen,
        )

        return release_detail_dto
