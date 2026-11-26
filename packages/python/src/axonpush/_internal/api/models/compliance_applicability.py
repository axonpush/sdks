from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComplianceApplicability")


@_attrs_define
class ComplianceApplicability:
    """
    Attributes:
        audience (list[str] | None):
        audiences (list[str] | None):
        decides_or_assists (list[str] | None):
        purposes (list[str] | None):
        regions (list[str] | None):
        risk_tiers (list[str] | None):
        roles (list[str] | None):
    """

    audience: list[str] | None
    audiences: list[str] | None
    decides_or_assists: list[str] | None
    purposes: list[str] | None
    regions: list[str] | None
    risk_tiers: list[str] | None
    roles: list[str] | None

    def to_dict(self) -> dict[str, Any]:
        audience: list[str] | None
        if isinstance(self.audience, list):
            audience = self.audience

        else:
            audience = self.audience

        audiences: list[str] | None
        if isinstance(self.audiences, list):
            audiences = self.audiences

        else:
            audiences = self.audiences

        decides_or_assists: list[str] | None
        if isinstance(self.decides_or_assists, list):
            decides_or_assists = self.decides_or_assists

        else:
            decides_or_assists = self.decides_or_assists

        purposes: list[str] | None
        if isinstance(self.purposes, list):
            purposes = self.purposes

        else:
            purposes = self.purposes

        regions: list[str] | None
        if isinstance(self.regions, list):
            regions = self.regions

        else:
            regions = self.regions

        risk_tiers: list[str] | None
        if isinstance(self.risk_tiers, list):
            risk_tiers = self.risk_tiers

        else:
            risk_tiers = self.risk_tiers

        roles: list[str] | None
        if isinstance(self.roles, list):
            roles = self.roles

        else:
            roles = self.roles

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "audience": audience,
                "audiences": audiences,
                "decidesOrAssists": decides_or_assists,
                "purposes": purposes,
                "regions": regions,
                "riskTiers": risk_tiers,
                "roles": roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_audience(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                audience_type_0 = cast(list[str], data)

                return audience_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        audience = _parse_audience(d.pop("audience"))

        def _parse_audiences(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                audiences_type_0 = cast(list[str], data)

                return audiences_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        audiences = _parse_audiences(d.pop("audiences"))

        def _parse_decides_or_assists(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                decides_or_assists_type_0 = cast(list[str], data)

                return decides_or_assists_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        decides_or_assists = _parse_decides_or_assists(d.pop("decidesOrAssists"))

        def _parse_purposes(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                purposes_type_0 = cast(list[str], data)

                return purposes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        purposes = _parse_purposes(d.pop("purposes"))

        def _parse_regions(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                regions_type_0 = cast(list[str], data)

                return regions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        regions = _parse_regions(d.pop("regions"))

        def _parse_risk_tiers(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                risk_tiers_type_0 = cast(list[str], data)

                return risk_tiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        risk_tiers = _parse_risk_tiers(d.pop("riskTiers"))

        def _parse_roles(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                roles_type_0 = cast(list[str], data)

                return roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        roles = _parse_roles(d.pop("roles"))

        compliance_applicability = cls(
            audience=audience,
            audiences=audiences,
            decides_or_assists=decides_or_assists,
            purposes=purposes,
            regions=regions,
            risk_tiers=risk_tiers,
            roles=roles,
        )

        return compliance_applicability
