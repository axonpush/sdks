from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.analytics_capability import AnalyticsCapability
    from ..models.audit_capability import AuditCapability
    from ..models.data_access_capability import DataAccessCapability


T = TypeVar("T", bound="Controls")


@_attrs_define
class Controls:
    """
    Attributes:
        analytics (AnalyticsCapability):
        audit_trail (AuditCapability):
        data_access (DataAccessCapability):
    """

    analytics: AnalyticsCapability
    audit_trail: AuditCapability
    data_access: DataAccessCapability

    def to_dict(self) -> dict[str, Any]:
        from ..models.analytics_capability import AnalyticsCapability
        from ..models.audit_capability import AuditCapability
        from ..models.data_access_capability import DataAccessCapability

        analytics = self.analytics.to_dict()

        audit_trail = self.audit_trail.to_dict()

        data_access = self.data_access.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "analytics": analytics,
                "auditTrail": audit_trail,
                "dataAccess": data_access,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.analytics_capability import AnalyticsCapability
        from ..models.audit_capability import AuditCapability
        from ..models.data_access_capability import DataAccessCapability

        d = dict(src_dict)
        analytics = AnalyticsCapability.from_dict(d.pop("analytics"))

        audit_trail = AuditCapability.from_dict(d.pop("auditTrail"))

        data_access = DataAccessCapability.from_dict(d.pop("dataAccess"))

        controls = cls(
            analytics=analytics,
            audit_trail=audit_trail,
            data_access=data_access,
        )

        return controls
