from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key_scope import ApiKeyScope
    from ..models.controls import Controls
    from ..models.feature_flags import FeatureFlags
    from ..models.license_status import LicenseStatus


T = TypeVar("T", bound="CapabilitiesOutputBody")


@_attrs_define
class CapabilitiesOutputBody:
    """
    Attributes:
        api_key_scopes (list[ApiKeyScope] | None):
        controls (Controls):
        feature_flags (FeatureFlags):
        license_ (LicenseStatus):
        version (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    api_key_scopes: list[ApiKeyScope] | None
    controls: Controls
    feature_flags: FeatureFlags
    license_: LicenseStatus
    version: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_key_scope import ApiKeyScope
        from ..models.controls import Controls
        from ..models.feature_flags import FeatureFlags
        from ..models.license_status import LicenseStatus

        api_key_scopes: list[dict[str, Any]] | None
        if isinstance(self.api_key_scopes, list):
            api_key_scopes = []
            for api_key_scopes_type_0_item_data in self.api_key_scopes:
                api_key_scopes_type_0_item = api_key_scopes_type_0_item_data.to_dict()
                api_key_scopes.append(api_key_scopes_type_0_item)

        else:
            api_key_scopes = self.api_key_scopes

        controls = self.controls.to_dict()

        feature_flags = self.feature_flags.to_dict()

        license_ = self.license_.to_dict()

        version = self.version

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "apiKeyScopes": api_key_scopes,
                "controls": controls,
                "featureFlags": feature_flags,
                "license": license_,
                "version": version,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_scope import ApiKeyScope
        from ..models.controls import Controls
        from ..models.feature_flags import FeatureFlags
        from ..models.license_status import LicenseStatus

        d = dict(src_dict)

        def _parse_api_key_scopes(data: object) -> list[ApiKeyScope] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                api_key_scopes_type_0 = []
                _api_key_scopes_type_0 = data
                for api_key_scopes_type_0_item_data in _api_key_scopes_type_0:
                    api_key_scopes_type_0_item = ApiKeyScope.from_dict(
                        api_key_scopes_type_0_item_data
                    )

                    api_key_scopes_type_0.append(api_key_scopes_type_0_item)

                return api_key_scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApiKeyScope] | None, data)

        api_key_scopes = _parse_api_key_scopes(d.pop("apiKeyScopes"))

        controls = Controls.from_dict(d.pop("controls"))

        feature_flags = FeatureFlags.from_dict(d.pop("featureFlags"))

        license_ = LicenseStatus.from_dict(d.pop("license"))

        version = d.pop("version")

        schema = d.pop("$schema", UNSET)

        capabilities_output_body = cls(
            api_key_scopes=api_key_scopes,
            controls=controls,
            feature_flags=feature_flags,
            license_=license_,
            version=version,
            schema=schema,
        )

        return capabilities_output_body
