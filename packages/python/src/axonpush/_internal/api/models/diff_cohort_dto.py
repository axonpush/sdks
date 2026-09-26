from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiffCohortDTO")


@_attrs_define
class DiffCohortDTO:
    """
    Attributes:
        api_key (str | Unset):
        app (str | Unset):
        channel (str | Unset):
        environment (str | Unset):
        error_type (str | Unset):
        errors_only (bool | Unset): Keep only error events in this cohort
        filter_tag_key (str | Unset):
        filter_tag_value (str | Unset):
        max_duration_ms (float | Unset): Keep only events at most this many ms (<=0 disables)
        min_duration_ms (float | Unset): Keep only events at least this many ms (<=0 disables)
        model (str | Unset):
        operation (str | Unset):
        provider (str | Unset):
        service (str | Unset):
        since (str | Unset): Window start (RFC3339); defaults to 24h before until
        source (str | Unset):
        until (str | Unset): Window end (RFC3339); defaults to now
        user (str | Unset):
    """

    api_key: str | Unset = UNSET
    app: str | Unset = UNSET
    channel: str | Unset = UNSET
    environment: str | Unset = UNSET
    error_type: str | Unset = UNSET
    errors_only: bool | Unset = UNSET
    filter_tag_key: str | Unset = UNSET
    filter_tag_value: str | Unset = UNSET
    max_duration_ms: float | Unset = UNSET
    min_duration_ms: float | Unset = UNSET
    model: str | Unset = UNSET
    operation: str | Unset = UNSET
    provider: str | Unset = UNSET
    service: str | Unset = UNSET
    since: str | Unset = UNSET
    source: str | Unset = UNSET
    until: str | Unset = UNSET
    user: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        app = self.app

        channel = self.channel

        environment = self.environment

        error_type = self.error_type

        errors_only = self.errors_only

        filter_tag_key = self.filter_tag_key

        filter_tag_value = self.filter_tag_value

        max_duration_ms = self.max_duration_ms

        min_duration_ms = self.min_duration_ms

        model = self.model

        operation = self.operation

        provider = self.provider

        service = self.service

        since = self.since

        source = self.source

        until = self.until

        user = self.user

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if app is not UNSET:
            field_dict["app"] = app
        if channel is not UNSET:
            field_dict["channel"] = channel
        if environment is not UNSET:
            field_dict["environment"] = environment
        if error_type is not UNSET:
            field_dict["errorType"] = error_type
        if errors_only is not UNSET:
            field_dict["errorsOnly"] = errors_only
        if filter_tag_key is not UNSET:
            field_dict["filterTagKey"] = filter_tag_key
        if filter_tag_value is not UNSET:
            field_dict["filterTagValue"] = filter_tag_value
        if max_duration_ms is not UNSET:
            field_dict["maxDurationMs"] = max_duration_ms
        if min_duration_ms is not UNSET:
            field_dict["minDurationMs"] = min_duration_ms
        if model is not UNSET:
            field_dict["model"] = model
        if operation is not UNSET:
            field_dict["operation"] = operation
        if provider is not UNSET:
            field_dict["provider"] = provider
        if service is not UNSET:
            field_dict["service"] = service
        if since is not UNSET:
            field_dict["since"] = since
        if source is not UNSET:
            field_dict["source"] = source
        if until is not UNSET:
            field_dict["until"] = until
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey", UNSET)

        app = d.pop("app", UNSET)

        channel = d.pop("channel", UNSET)

        environment = d.pop("environment", UNSET)

        error_type = d.pop("errorType", UNSET)

        errors_only = d.pop("errorsOnly", UNSET)

        filter_tag_key = d.pop("filterTagKey", UNSET)

        filter_tag_value = d.pop("filterTagValue", UNSET)

        max_duration_ms = d.pop("maxDurationMs", UNSET)

        min_duration_ms = d.pop("minDurationMs", UNSET)

        model = d.pop("model", UNSET)

        operation = d.pop("operation", UNSET)

        provider = d.pop("provider", UNSET)

        service = d.pop("service", UNSET)

        since = d.pop("since", UNSET)

        source = d.pop("source", UNSET)

        until = d.pop("until", UNSET)

        user = d.pop("user", UNSET)

        diff_cohort_dto = cls(
            api_key=api_key,
            app=app,
            channel=channel,
            environment=environment,
            error_type=error_type,
            errors_only=errors_only,
            filter_tag_key=filter_tag_key,
            filter_tag_value=filter_tag_value,
            max_duration_ms=max_duration_ms,
            min_duration_ms=min_duration_ms,
            model=model,
            operation=operation,
            provider=provider,
            service=service,
            since=since,
            source=source,
            until=until,
            user=user,
        )

        return diff_cohort_dto
