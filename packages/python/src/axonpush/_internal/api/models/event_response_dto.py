from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_response_dto_metadata import EventResponseDtoMetadata
    from ..models.event_response_dto_payload import EventResponseDtoPayload


T = TypeVar("T", bound="EventResponseDto")


@_attrs_define
class EventResponseDto:
    """
    Attributes:
        app_id (str):
        channel_id (str):
        created_at (datetime.datetime):
        event_id (str):
        event_type (str):
        id (str):
        org_id (str):
        agent_id (str | Unset):
        cache_read_tokens (float | Unset):
        cache_write_tokens (float | Unset):
        cost_usd (float | Unset):
        duration_ms (float | Unset):
        end_time_unix_nano (str | Unset):
        environment_id (str | Unset):
        finish_reason (str | Unset): Model stop/finish reason, e.g. "stop", "length", "tool_calls".
        identifier (str | Unset):
        input_tokens (float | Unset):
        metadata (EventResponseDtoMetadata | Unset):
        occurred_at (datetime.datetime | Unset):
        operation_name (str | Unset):
        output_tokens (float | Unset):
        parent_event_id (str | Unset):
        parent_span_id (str | Unset):
        payload (EventResponseDtoPayload | Unset):
        provider_name (str | Unset):
        reasoning_tokens (float | Unset):
        request_model (str | Unset):
        response_model (str | Unset):
        semantic_kind (str | Unset):
        service_name (str | Unset):
        service_version (str | Unset):
        source (str | Unset):
        span_id (str | Unset):
        start_time_unix_nano (str | Unset):
        status (str | Unset):
        time_to_first_token_ms (float | Unset): Time-to-first-token latency in milliseconds (streamed LLM calls).
        tool_name (str | Unset):
        total_tokens (float | Unset):
        trace_id (str | Unset):
        ttl (float | Unset):
        updated_at (datetime.datetime | Unset):
    """

    app_id: str
    channel_id: str
    created_at: datetime.datetime
    event_id: str
    event_type: str
    id: str
    org_id: str
    agent_id: str | Unset = UNSET
    cache_read_tokens: float | Unset = UNSET
    cache_write_tokens: float | Unset = UNSET
    cost_usd: float | Unset = UNSET
    duration_ms: float | Unset = UNSET
    end_time_unix_nano: str | Unset = UNSET
    environment_id: str | Unset = UNSET
    finish_reason: str | Unset = UNSET
    identifier: str | Unset = UNSET
    input_tokens: float | Unset = UNSET
    metadata: EventResponseDtoMetadata | Unset = UNSET
    occurred_at: datetime.datetime | Unset = UNSET
    operation_name: str | Unset = UNSET
    output_tokens: float | Unset = UNSET
    parent_event_id: str | Unset = UNSET
    parent_span_id: str | Unset = UNSET
    payload: EventResponseDtoPayload | Unset = UNSET
    provider_name: str | Unset = UNSET
    reasoning_tokens: float | Unset = UNSET
    request_model: str | Unset = UNSET
    response_model: str | Unset = UNSET
    semantic_kind: str | Unset = UNSET
    service_name: str | Unset = UNSET
    service_version: str | Unset = UNSET
    source: str | Unset = UNSET
    span_id: str | Unset = UNSET
    start_time_unix_nano: str | Unset = UNSET
    status: str | Unset = UNSET
    time_to_first_token_ms: float | Unset = UNSET
    tool_name: str | Unset = UNSET
    total_tokens: float | Unset = UNSET
    trace_id: str | Unset = UNSET
    ttl: float | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_response_dto_metadata import EventResponseDtoMetadata
        from ..models.event_response_dto_payload import EventResponseDtoPayload

        app_id = self.app_id

        channel_id = self.channel_id

        created_at = self.created_at.isoformat()

        event_id = self.event_id

        event_type = self.event_type

        id = self.id

        org_id = self.org_id

        agent_id = self.agent_id

        cache_read_tokens = self.cache_read_tokens

        cache_write_tokens = self.cache_write_tokens

        cost_usd = self.cost_usd

        duration_ms = self.duration_ms

        end_time_unix_nano = self.end_time_unix_nano

        environment_id = self.environment_id

        finish_reason = self.finish_reason

        identifier = self.identifier

        input_tokens = self.input_tokens

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        operation_name = self.operation_name

        output_tokens = self.output_tokens

        parent_event_id = self.parent_event_id

        parent_span_id = self.parent_span_id

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        provider_name = self.provider_name

        reasoning_tokens = self.reasoning_tokens

        request_model = self.request_model

        response_model = self.response_model

        semantic_kind = self.semantic_kind

        service_name = self.service_name

        service_version = self.service_version

        source = self.source

        span_id = self.span_id

        start_time_unix_nano = self.start_time_unix_nano

        status = self.status

        time_to_first_token_ms = self.time_to_first_token_ms

        tool_name = self.tool_name

        total_tokens = self.total_tokens

        trace_id = self.trace_id

        ttl = self.ttl

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appId": app_id,
                "channelId": channel_id,
                "createdAt": created_at,
                "eventId": event_id,
                "eventType": event_type,
                "id": id,
                "orgId": org_id,
            }
        )
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if cache_read_tokens is not UNSET:
            field_dict["cacheReadTokens"] = cache_read_tokens
        if cache_write_tokens is not UNSET:
            field_dict["cacheWriteTokens"] = cache_write_tokens
        if cost_usd is not UNSET:
            field_dict["costUsd"] = cost_usd
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms
        if end_time_unix_nano is not UNSET:
            field_dict["endTimeUnixNano"] = end_time_unix_nano
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if finish_reason is not UNSET:
            field_dict["finishReason"] = finish_reason
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if input_tokens is not UNSET:
            field_dict["inputTokens"] = input_tokens
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if occurred_at is not UNSET:
            field_dict["occurredAt"] = occurred_at
        if operation_name is not UNSET:
            field_dict["operationName"] = operation_name
        if output_tokens is not UNSET:
            field_dict["outputTokens"] = output_tokens
        if parent_event_id is not UNSET:
            field_dict["parentEventId"] = parent_event_id
        if parent_span_id is not UNSET:
            field_dict["parentSpanId"] = parent_span_id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if provider_name is not UNSET:
            field_dict["providerName"] = provider_name
        if reasoning_tokens is not UNSET:
            field_dict["reasoningTokens"] = reasoning_tokens
        if request_model is not UNSET:
            field_dict["requestModel"] = request_model
        if response_model is not UNSET:
            field_dict["responseModel"] = response_model
        if semantic_kind is not UNSET:
            field_dict["semanticKind"] = semantic_kind
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if service_version is not UNSET:
            field_dict["serviceVersion"] = service_version
        if source is not UNSET:
            field_dict["source"] = source
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if start_time_unix_nano is not UNSET:
            field_dict["startTimeUnixNano"] = start_time_unix_nano
        if status is not UNSET:
            field_dict["status"] = status
        if time_to_first_token_ms is not UNSET:
            field_dict["timeToFirstTokenMs"] = time_to_first_token_ms
        if tool_name is not UNSET:
            field_dict["toolName"] = tool_name
        if total_tokens is not UNSET:
            field_dict["totalTokens"] = total_tokens
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_response_dto_metadata import EventResponseDtoMetadata
        from ..models.event_response_dto_payload import EventResponseDtoPayload

        d = dict(src_dict)
        app_id = d.pop("appId")

        channel_id = d.pop("channelId")

        created_at = isoparse(d.pop("createdAt"))

        event_id = d.pop("eventId")

        event_type = d.pop("eventType")

        id = d.pop("id")

        org_id = d.pop("orgId")

        agent_id = d.pop("agentId", UNSET)

        cache_read_tokens = d.pop("cacheReadTokens", UNSET)

        cache_write_tokens = d.pop("cacheWriteTokens", UNSET)

        cost_usd = d.pop("costUsd", UNSET)

        duration_ms = d.pop("durationMs", UNSET)

        end_time_unix_nano = d.pop("endTimeUnixNano", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        finish_reason = d.pop("finishReason", UNSET)

        identifier = d.pop("identifier", UNSET)

        input_tokens = d.pop("inputTokens", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: EventResponseDtoMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = EventResponseDtoMetadata.from_dict(_metadata)

        _occurred_at = d.pop("occurredAt", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at, Unset):
            occurred_at = UNSET
        else:
            occurred_at = isoparse(_occurred_at)

        operation_name = d.pop("operationName", UNSET)

        output_tokens = d.pop("outputTokens", UNSET)

        parent_event_id = d.pop("parentEventId", UNSET)

        parent_span_id = d.pop("parentSpanId", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: EventResponseDtoPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = EventResponseDtoPayload.from_dict(_payload)

        provider_name = d.pop("providerName", UNSET)

        reasoning_tokens = d.pop("reasoningTokens", UNSET)

        request_model = d.pop("requestModel", UNSET)

        response_model = d.pop("responseModel", UNSET)

        semantic_kind = d.pop("semanticKind", UNSET)

        service_name = d.pop("serviceName", UNSET)

        service_version = d.pop("serviceVersion", UNSET)

        source = d.pop("source", UNSET)

        span_id = d.pop("spanId", UNSET)

        start_time_unix_nano = d.pop("startTimeUnixNano", UNSET)

        status = d.pop("status", UNSET)

        time_to_first_token_ms = d.pop("timeToFirstTokenMs", UNSET)

        tool_name = d.pop("toolName", UNSET)

        total_tokens = d.pop("totalTokens", UNSET)

        trace_id = d.pop("traceId", UNSET)

        ttl = d.pop("ttl", UNSET)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        event_response_dto = cls(
            app_id=app_id,
            channel_id=channel_id,
            created_at=created_at,
            event_id=event_id,
            event_type=event_type,
            id=id,
            org_id=org_id,
            agent_id=agent_id,
            cache_read_tokens=cache_read_tokens,
            cache_write_tokens=cache_write_tokens,
            cost_usd=cost_usd,
            duration_ms=duration_ms,
            end_time_unix_nano=end_time_unix_nano,
            environment_id=environment_id,
            finish_reason=finish_reason,
            identifier=identifier,
            input_tokens=input_tokens,
            metadata=metadata,
            occurred_at=occurred_at,
            operation_name=operation_name,
            output_tokens=output_tokens,
            parent_event_id=parent_event_id,
            parent_span_id=parent_span_id,
            payload=payload,
            provider_name=provider_name,
            reasoning_tokens=reasoning_tokens,
            request_model=request_model,
            response_model=response_model,
            semantic_kind=semantic_kind,
            service_name=service_name,
            service_version=service_version,
            source=source,
            span_id=span_id,
            start_time_unix_nano=start_time_unix_nano,
            status=status,
            time_to_first_token_ms=time_to_first_token_ms,
            tool_name=tool_name,
            total_tokens=total_tokens,
            trace_id=trace_id,
            ttl=ttl,
            updated_at=updated_at,
        )

        event_response_dto.additional_properties = d
        return event_response_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
