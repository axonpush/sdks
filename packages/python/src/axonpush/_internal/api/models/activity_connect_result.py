from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_connect_key import ActivityConnectKey
    from ..models.activity_connect_otlp import ActivityConnectOTLP
    from ..models.activity_connect_result_env import ActivityConnectResultEnv
    from ..models.activity_connect_sdk import ActivityConnectSDK
    from ..models.activity_connect_workflow_runtime import (
        ActivityConnectWorkflowRuntime,
    )
    from ..models.link import Link


T = TypeVar("T", bound="ActivityConnectResult")


@_attrs_define
class ActivityConnectResult:
    """
    Attributes:
        api_url (str):
        created (bool): True when this call minted a new key
        env (ActivityConnectResultEnv): Variables to write to the app's git-ignored env file. Contains the secret only
            when created is true
        environment (str): Environment slug the key is bound to
        otlp (ActivityConnectOTLP):
        publish_key (ActivityConnectKey):
        purpose (str):
        sdk (ActivityConnectSDK):
        workspace_id (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        claim (Link | Unset):
        hint (str | Unset):
        revoked_key_ids (list[str] | None | Unset): Keys revoked by rotate
        sentry_dsn (str | Unset): Sentry SDK DSN; present only when this call minted it
        sentry_dsn_unavailable (str | Unset): Why sentryDsn is absent
        warnings (list[str] | None | Unset):
        workflow_runtime (ActivityConnectWorkflowRuntime | Unset):
    """

    api_url: str
    created: bool
    env: ActivityConnectResultEnv
    environment: str
    otlp: ActivityConnectOTLP
    publish_key: ActivityConnectKey
    purpose: str
    sdk: ActivityConnectSDK
    workspace_id: str
    schema: str | Unset = UNSET
    claim: Link | Unset = UNSET
    hint: str | Unset = UNSET
    revoked_key_ids: list[str] | None | Unset = UNSET
    sentry_dsn: str | Unset = UNSET
    sentry_dsn_unavailable: str | Unset = UNSET
    warnings: list[str] | None | Unset = UNSET
    workflow_runtime: ActivityConnectWorkflowRuntime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_connect_key import ActivityConnectKey
        from ..models.activity_connect_otlp import ActivityConnectOTLP
        from ..models.activity_connect_result_env import ActivityConnectResultEnv
        from ..models.activity_connect_sdk import ActivityConnectSDK
        from ..models.activity_connect_workflow_runtime import (
            ActivityConnectWorkflowRuntime,
        )
        from ..models.link import Link

        api_url = self.api_url

        created = self.created

        env = self.env.to_dict()

        environment = self.environment

        otlp = self.otlp.to_dict()

        publish_key = self.publish_key.to_dict()

        purpose = self.purpose

        sdk = self.sdk.to_dict()

        workspace_id = self.workspace_id

        schema = self.schema

        claim: dict[str, Any] | Unset = UNSET
        if not isinstance(self.claim, Unset):
            claim = self.claim.to_dict()

        hint = self.hint

        revoked_key_ids: list[str] | None | Unset
        if isinstance(self.revoked_key_ids, Unset):
            revoked_key_ids = UNSET
        elif isinstance(self.revoked_key_ids, list):
            revoked_key_ids = self.revoked_key_ids

        else:
            revoked_key_ids = self.revoked_key_ids

        sentry_dsn = self.sentry_dsn

        sentry_dsn_unavailable = self.sentry_dsn_unavailable

        warnings: list[str] | None | Unset
        if isinstance(self.warnings, Unset):
            warnings = UNSET
        elif isinstance(self.warnings, list):
            warnings = self.warnings

        else:
            warnings = self.warnings

        workflow_runtime: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow_runtime, Unset):
            workflow_runtime = self.workflow_runtime.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "apiUrl": api_url,
                "created": created,
                "env": env,
                "environment": environment,
                "otlp": otlp,
                "publishKey": publish_key,
                "purpose": purpose,
                "sdk": sdk,
                "workspaceId": workspace_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if claim is not UNSET:
            field_dict["claim"] = claim
        if hint is not UNSET:
            field_dict["hint"] = hint
        if revoked_key_ids is not UNSET:
            field_dict["revokedKeyIds"] = revoked_key_ids
        if sentry_dsn is not UNSET:
            field_dict["sentryDsn"] = sentry_dsn
        if sentry_dsn_unavailable is not UNSET:
            field_dict["sentryDsnUnavailable"] = sentry_dsn_unavailable
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if workflow_runtime is not UNSET:
            field_dict["workflowRuntime"] = workflow_runtime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_connect_key import ActivityConnectKey
        from ..models.activity_connect_otlp import ActivityConnectOTLP
        from ..models.activity_connect_result_env import ActivityConnectResultEnv
        from ..models.activity_connect_sdk import ActivityConnectSDK
        from ..models.activity_connect_workflow_runtime import (
            ActivityConnectWorkflowRuntime,
        )
        from ..models.link import Link

        d = dict(src_dict)
        api_url = d.pop("apiUrl")

        created = d.pop("created")

        env = ActivityConnectResultEnv.from_dict(d.pop("env"))

        environment = d.pop("environment")

        otlp = ActivityConnectOTLP.from_dict(d.pop("otlp"))

        publish_key = ActivityConnectKey.from_dict(d.pop("publishKey"))

        purpose = d.pop("purpose")

        sdk = ActivityConnectSDK.from_dict(d.pop("sdk"))

        workspace_id = d.pop("workspaceId")

        schema = d.pop("$schema", UNSET)

        _claim = d.pop("claim", UNSET)
        claim: Link | Unset
        if isinstance(_claim, Unset):
            claim = UNSET
        else:
            claim = Link.from_dict(_claim)

        hint = d.pop("hint", UNSET)

        def _parse_revoked_key_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                revoked_key_ids_type_0 = cast(list[str], data)

                return revoked_key_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        revoked_key_ids = _parse_revoked_key_ids(d.pop("revokedKeyIds", UNSET))

        sentry_dsn = d.pop("sentryDsn", UNSET)

        sentry_dsn_unavailable = d.pop("sentryDsnUnavailable", UNSET)

        def _parse_warnings(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                warnings_type_0 = cast(list[str], data)

                return warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        warnings = _parse_warnings(d.pop("warnings", UNSET))

        _workflow_runtime = d.pop("workflowRuntime", UNSET)
        workflow_runtime: ActivityConnectWorkflowRuntime | Unset
        if isinstance(_workflow_runtime, Unset):
            workflow_runtime = UNSET
        else:
            workflow_runtime = ActivityConnectWorkflowRuntime.from_dict(
                _workflow_runtime
            )

        activity_connect_result = cls(
            api_url=api_url,
            created=created,
            env=env,
            environment=environment,
            otlp=otlp,
            publish_key=publish_key,
            purpose=purpose,
            sdk=sdk,
            workspace_id=workspace_id,
            schema=schema,
            claim=claim,
            hint=hint,
            revoked_key_ids=revoked_key_ids,
            sentry_dsn=sentry_dsn,
            sentry_dsn_unavailable=sentry_dsn_unavailable,
            warnings=warnings,
            workflow_runtime=workflow_runtime,
        )

        return activity_connect_result
