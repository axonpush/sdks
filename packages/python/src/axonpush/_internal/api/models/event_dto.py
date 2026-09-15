from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDTO")


@_attrs_define
class EventDTO:
    """
    Attributes:
        app_id (str):
        channel_id (str):
        created_at (str):
        event_id (str):
        event_type (str):
        occurred_at (str):
        org_id (str):
        payload_spilled (bool):
        source (str):
        agent_id (str | Unset):
        agent_name (str | Unset):
        attributes (Any | Unset):
        cache_read_tokens (int | Unset):
        cache_write_tokens (int | Unset):
        cost_source (str | Unset):
        cost_usd (float | Unset):
        duration_ms (float | Unset):
        environment_id (str | Unset):
        error_message (str | Unset):
        error_type (str | Unset):
        finish_reason (str | Unset):
        input_tokens (int | Unset):
        metadata (Any | Unset):
        operation_name (str | Unset):
        output_tokens (int | Unset):
        parent_span_id (str | Unset):
        payload (Any | Unset):
        provider_name (str | Unset):
        reasoning_tokens (int | Unset):
        request_model (str | Unset):
        resource_attributes (Any | Unset):
        response_model (str | Unset):
        semantic_kind (str | Unset):
        service_name (str | Unset):
        session_id (str | Unset):
        span_id (str | Unset):
        status (str | Unset):
        tool_name (str | Unset):
        total_tokens (int | Unset):
        trace_id (str | Unset):
        ttft_ms (float | Unset):
        user_id (str | Unset):
    """

    app_id: str
    channel_id: str
    created_at: str
    event_id: str
    event_type: str
    occurred_at: str
    org_id: str
    payload_spilled: bool
    source: str
    agent_id: str | Unset = UNSET
    agent_name: str | Unset = UNSET
    attributes: Any | Unset = UNSET
    cache_read_tokens: int | Unset = UNSET
    cache_write_tokens: int | Unset = UNSET
    cost_source: str | Unset = UNSET
    cost_usd: float | Unset = UNSET
    duration_ms: float | Unset = UNSET
    environment_id: str | Unset = UNSET
    error_message: str | Unset = UNSET
    error_type: str | Unset = UNSET
    finish_reason: str | Unset = UNSET
    input_tokens: int | Unset = UNSET
    metadata: Any | Unset = UNSET
    operation_name: str | Unset = UNSET
    output_tokens: int | Unset = UNSET
    parent_span_id: str | Unset = UNSET
    payload: Any | Unset = UNSET
    provider_name: str | Unset = UNSET
    reasoning_tokens: int | Unset = UNSET
    request_model: str | Unset = UNSET
    resource_attributes: Any | Unset = UNSET
    response_model: str | Unset = UNSET
    semantic_kind: str | Unset = UNSET
    service_name: str | Unset = UNSET
    session_id: str | Unset = UNSET
    span_id: str | Unset = UNSET
    status: str | Unset = UNSET
    tool_name: str | Unset = UNSET
    total_tokens: int | Unset = UNSET
    trace_id: str | Unset = UNSET
    ttft_ms: float | Unset = UNSET
    user_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        app_id = self.app_id

        channel_id = self.channel_id

        created_at = self.created_at

        event_id = self.event_id

        event_type = self.event_type

        occurred_at = self.occurred_at

        org_id = self.org_id

        payload_spilled = self.payload_spilled

        source = self.source

        agent_id = self.agent_id

        agent_name = self.agent_name

        attributes = self.attributes

        cache_read_tokens = self.cache_read_tokens

        cache_write_tokens = self.cache_write_tokens

        cost_source = self.cost_source

        cost_usd = self.cost_usd

        duration_ms = self.duration_ms

        environment_id = self.environment_id

        error_message = self.error_message

        error_type = self.error_type

        finish_reason = self.finish_reason

        input_tokens = self.input_tokens

        metadata = self.metadata

        operation_name = self.operation_name

        output_tokens = self.output_tokens

        parent_span_id = self.parent_span_id

        payload = self.payload

        provider_name = self.provider_name

        reasoning_tokens = self.reasoning_tokens

        request_model = self.request_model

        resource_attributes = self.resource_attributes

        response_model = self.response_model

        semantic_kind = self.semantic_kind

        service_name = self.service_name

        session_id = self.session_id

        span_id = self.span_id

        status = self.status

        tool_name = self.tool_name

        total_tokens = self.total_tokens

        trace_id = self.trace_id

        ttft_ms = self.ttft_ms

        user_id = self.user_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "appId": app_id,
                "channelId": channel_id,
                "createdAt": created_at,
                "eventId": event_id,
                "eventType": event_type,
                "occurredAt": occurred_at,
                "orgId": org_id,
                "payloadSpilled": payload_spilled,
                "source": source,
            }
        )
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if agent_name is not UNSET:
            field_dict["agentName"] = agent_name
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if cache_read_tokens is not UNSET:
            field_dict["cacheReadTokens"] = cache_read_tokens
        if cache_write_tokens is not UNSET:
            field_dict["cacheWriteTokens"] = cache_write_tokens
        if cost_source is not UNSET:
            field_dict["costSource"] = cost_source
        if cost_usd is not UNSET:
            field_dict["costUsd"] = cost_usd
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if error_type is not UNSET:
            field_dict["errorType"] = error_type
        if finish_reason is not UNSET:
            field_dict["finishReason"] = finish_reason
        if input_tokens is not UNSET:
            field_dict["inputTokens"] = input_tokens
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if operation_name is not UNSET:
            field_dict["operationName"] = operation_name
        if output_tokens is not UNSET:
            field_dict["outputTokens"] = output_tokens
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
        if resource_attributes is not UNSET:
            field_dict["resourceAttributes"] = resource_attributes
        if response_model is not UNSET:
            field_dict["responseModel"] = response_model
        if semantic_kind is not UNSET:
            field_dict["semanticKind"] = semantic_kind
        if service_name is not UNSET:
            field_dict["serviceName"] = service_name
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if span_id is not UNSET:
            field_dict["spanId"] = span_id
        if status is not UNSET:
            field_dict["status"] = status
        if tool_name is not UNSET:
            field_dict["toolName"] = tool_name
        if total_tokens is not UNSET:
            field_dict["totalTokens"] = total_tokens
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id
        if ttft_ms is not UNSET:
            field_dict["ttftMs"] = ttft_ms
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = d.pop("appId")

        channel_id = d.pop("channelId")

        created_at = d.pop("createdAt")

        event_id = d.pop("eventId")

        event_type = d.pop("eventType")

        occurred_at = d.pop("occurredAt")

        org_id = d.pop("orgId")

        payload_spilled = d.pop("payloadSpilled")

        source = d.pop("source")

        agent_id = d.pop("agentId", UNSET)

        agent_name = d.pop("agentName", UNSET)

        attributes = d.pop("attributes", UNSET)

        cache_read_tokens = d.pop("cacheReadTokens", UNSET)

        cache_write_tokens = d.pop("cacheWriteTokens", UNSET)

        cost_source = d.pop("costSource", UNSET)

        cost_usd = d.pop("costUsd", UNSET)

        duration_ms = d.pop("durationMs", UNSET)

        environment_id = d.pop("environmentId", UNSET)

        error_message = d.pop("errorMessage", UNSET)

        error_type = d.pop("errorType", UNSET)

        finish_reason = d.pop("finishReason", UNSET)

        input_tokens = d.pop("inputTokens", UNSET)

        metadata = d.pop("metadata", UNSET)

        operation_name = d.pop("operationName", UNSET)

        output_tokens = d.pop("outputTokens", UNSET)

        parent_span_id = d.pop("parentSpanId", UNSET)

        payload = d.pop("payload", UNSET)

        provider_name = d.pop("providerName", UNSET)

        reasoning_tokens = d.pop("reasoningTokens", UNSET)

        request_model = d.pop("requestModel", UNSET)

        resource_attributes = d.pop("resourceAttributes", UNSET)

        response_model = d.pop("responseModel", UNSET)

        semantic_kind = d.pop("semanticKind", UNSET)

        service_name = d.pop("serviceName", UNSET)

        session_id = d.pop("sessionId", UNSET)

        span_id = d.pop("spanId", UNSET)

        status = d.pop("status", UNSET)

        tool_name = d.pop("toolName", UNSET)

        total_tokens = d.pop("totalTokens", UNSET)

        trace_id = d.pop("traceId", UNSET)

        ttft_ms = d.pop("ttftMs", UNSET)

        user_id = d.pop("userId", UNSET)

        event_dto = cls(
            app_id=app_id,
            channel_id=channel_id,
            created_at=created_at,
            event_id=event_id,
            event_type=event_type,
            occurred_at=occurred_at,
            org_id=org_id,
            payload_spilled=payload_spilled,
            source=source,
            agent_id=agent_id,
            agent_name=agent_name,
            attributes=attributes,
            cache_read_tokens=cache_read_tokens,
            cache_write_tokens=cache_write_tokens,
            cost_source=cost_source,
            cost_usd=cost_usd,
            duration_ms=duration_ms,
            environment_id=environment_id,
            error_message=error_message,
            error_type=error_type,
            finish_reason=finish_reason,
            input_tokens=input_tokens,
            metadata=metadata,
            operation_name=operation_name,
            output_tokens=output_tokens,
            parent_span_id=parent_span_id,
            payload=payload,
            provider_name=provider_name,
            reasoning_tokens=reasoning_tokens,
            request_model=request_model,
            resource_attributes=resource_attributes,
            response_model=response_model,
            semantic_kind=semantic_kind,
            service_name=service_name,
            session_id=session_id,
            span_id=span_id,
            status=status,
            tool_name=tool_name,
            total_tokens=total_tokens,
            trace_id=trace_id,
            ttft_ms=ttft_ms,
            user_id=user_id,
        )

        return event_dto
