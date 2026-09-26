from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issue_bucket_dto import IssueBucketDTO


T = TypeVar("T", bound="ErrorIssueDTO")


@_attrs_define
class ErrorIssueDTO:
    """
    Attributes:
        count (int):
        culprit (str):
        error_type (str):
        fingerprint (str):
        first_seen (str):
        last_seen (str):
        message (str):
        operation (str):
        regressed (bool):
        service_name (str):
        sparkline (list[IssueBucketDTO] | None):
        status (str):
        title (str):
        trace_count (int):
        user_count (int):
        assignee (str | Unset):
    """

    count: int
    culprit: str
    error_type: str
    fingerprint: str
    first_seen: str
    last_seen: str
    message: str
    operation: str
    regressed: bool
    service_name: str
    sparkline: list[IssueBucketDTO] | None
    status: str
    title: str
    trace_count: int
    user_count: int
    assignee: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_bucket_dto import IssueBucketDTO

        count = self.count

        culprit = self.culprit

        error_type = self.error_type

        fingerprint = self.fingerprint

        first_seen = self.first_seen

        last_seen = self.last_seen

        message = self.message

        operation = self.operation

        regressed = self.regressed

        service_name = self.service_name

        sparkline: list[dict[str, Any]] | None
        if isinstance(self.sparkline, list):
            sparkline = []
            for sparkline_type_0_item_data in self.sparkline:
                sparkline_type_0_item = sparkline_type_0_item_data.to_dict()
                sparkline.append(sparkline_type_0_item)

        else:
            sparkline = self.sparkline

        status = self.status

        title = self.title

        trace_count = self.trace_count

        user_count = self.user_count

        assignee = self.assignee

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "culprit": culprit,
                "errorType": error_type,
                "fingerprint": fingerprint,
                "firstSeen": first_seen,
                "lastSeen": last_seen,
                "message": message,
                "operation": operation,
                "regressed": regressed,
                "serviceName": service_name,
                "sparkline": sparkline,
                "status": status,
                "title": title,
                "traceCount": trace_count,
                "userCount": user_count,
            }
        )
        if assignee is not UNSET:
            field_dict["assignee"] = assignee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_bucket_dto import IssueBucketDTO

        d = dict(src_dict)
        count = d.pop("count")

        culprit = d.pop("culprit")

        error_type = d.pop("errorType")

        fingerprint = d.pop("fingerprint")

        first_seen = d.pop("firstSeen")

        last_seen = d.pop("lastSeen")

        message = d.pop("message")

        operation = d.pop("operation")

        regressed = d.pop("regressed")

        service_name = d.pop("serviceName")

        def _parse_sparkline(data: object) -> list[IssueBucketDTO] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sparkline_type_0 = []
                _sparkline_type_0 = data
                for sparkline_type_0_item_data in _sparkline_type_0:
                    sparkline_type_0_item = IssueBucketDTO.from_dict(sparkline_type_0_item_data)

                    sparkline_type_0.append(sparkline_type_0_item)

                return sparkline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IssueBucketDTO] | None, data)

        sparkline = _parse_sparkline(d.pop("sparkline"))

        status = d.pop("status")

        title = d.pop("title")

        trace_count = d.pop("traceCount")

        user_count = d.pop("userCount")

        assignee = d.pop("assignee", UNSET)

        error_issue_dto = cls(
            count=count,
            culprit=culprit,
            error_type=error_type,
            fingerprint=fingerprint,
            first_seen=first_seen,
            last_seen=last_seen,
            message=message,
            operation=operation,
            regressed=regressed,
            service_name=service_name,
            sparkline=sparkline,
            status=status,
            title=title,
            trace_count=trace_count,
            user_count=user_count,
            assignee=assignee,
        )

        return error_issue_dto
