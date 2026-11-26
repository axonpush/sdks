from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_bootstrap_failed import SessionBootstrapFailed


T = TypeVar("T", bound="SessionBootstrap")


@_attrs_define
class SessionBootstrap:
    """
    Attributes:
        schema (str | Unset): A URL to the JSON Schema for this object.
        capabilities (Any | Unset): Body of GET /capabilities
        environments (Any | Unset): Body of GET /environments
        failed (SessionBootstrapFailed | Unset): HTTP status of each part that failed, by field
        feature_flags (Any | Unset): Body of GET /feature-flags/me
        me (Any | Unset): Body of GET /user/me
        organizations (Any | Unset): Body of GET /users/me/organizations
        workspaces (Any | Unset): Body of GET /workspaces
    """

    schema: str | Unset = UNSET
    capabilities: Any | Unset = UNSET
    environments: Any | Unset = UNSET
    failed: SessionBootstrapFailed | Unset = UNSET
    feature_flags: Any | Unset = UNSET
    me: Any | Unset = UNSET
    organizations: Any | Unset = UNSET
    workspaces: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_bootstrap_failed import SessionBootstrapFailed

        schema = self.schema

        capabilities = self.capabilities

        environments = self.environments

        failed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.failed, Unset):
            failed = self.failed.to_dict()

        feature_flags = self.feature_flags

        me = self.me

        organizations = self.organizations

        workspaces = self.workspaces

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if environments is not UNSET:
            field_dict["environments"] = environments
        if failed is not UNSET:
            field_dict["failed"] = failed
        if feature_flags is not UNSET:
            field_dict["featureFlags"] = feature_flags
        if me is not UNSET:
            field_dict["me"] = me
        if organizations is not UNSET:
            field_dict["organizations"] = organizations
        if workspaces is not UNSET:
            field_dict["workspaces"] = workspaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_bootstrap_failed import SessionBootstrapFailed

        d = dict(src_dict)
        schema = d.pop("$schema", UNSET)

        capabilities = d.pop("capabilities", UNSET)

        environments = d.pop("environments", UNSET)

        _failed = d.pop("failed", UNSET)
        failed: SessionBootstrapFailed | Unset
        if isinstance(_failed, Unset):
            failed = UNSET
        else:
            failed = SessionBootstrapFailed.from_dict(_failed)

        feature_flags = d.pop("featureFlags", UNSET)

        me = d.pop("me", UNSET)

        organizations = d.pop("organizations", UNSET)

        workspaces = d.pop("workspaces", UNSET)

        session_bootstrap = cls(
            schema=schema,
            capabilities=capabilities,
            environments=environments,
            failed=failed,
            feature_flags=feature_flags,
            me=me,
            organizations=organizations,
            workspaces=workspaces,
        )

        return session_bootstrap
