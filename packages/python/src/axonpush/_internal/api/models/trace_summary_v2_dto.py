from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.trace_status import TraceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceSummaryV2Dto")


@_attrs_define
class TraceSummaryV2Dto:
    """
    Attributes:
        agents (list[str]):
        app_id (str):
        cache_read_tokens (float):
        cache_write_tokens (float):
        channel_id (str):
        duration_ms (float):
        end_time (datetime.datetime):
        error_count (float):
        event_count (float):
        handoff_count (float):
        input_tokens (float):
        last_seen_at (datetime.datetime):
        models (list[str]):
        output_tokens (float):
        prompt_ids (list[str]):
        prompt_version_ids (list[str]):
        providers (list[str]):
        reasoning_tokens (float):
        releases (list[str]):
        revision (str):
        semantic_kinds (list[str]):
        services (list[str]):
        session_ids (list[str]):
        start_time (datetime.datetime):
        status (TraceStatus):
        tool_call_count (float):
        tools (list[str]):
        total_tokens (float):
        trace_id (str):
        updated_at (datetime.datetime):
        user_ids (list[str]):
        cost_usd (float | None | Unset): Omitted when every underlying span has unknown pricing.
        environment_id (str | Unset):
        root_operation (str | Unset):
        score (float | None | Unset):
    """

    agents: list[str]
    app_id: str
    cache_read_tokens: float
    cache_write_tokens: float
    channel_id: str
    duration_ms: float
    end_time: datetime.datetime
    error_count: float
    event_count: float
    handoff_count: float
    input_tokens: float
    last_seen_at: datetime.datetime
    models: list[str]
    output_tokens: float
    prompt_ids: list[str]
    prompt_version_ids: list[str]
    providers: list[str]
    reasoning_tokens: float
    releases: list[str]
    revision: str
    semantic_kinds: list[str]
    services: list[str]
    session_ids: list[str]
    start_time: datetime.datetime
    status: TraceStatus
    tool_call_count: float
    tools: list[str]
    total_tokens: float
    trace_id: str
    updated_at: datetime.datetime
    user_ids: list[str]
    cost_usd: float | None | Unset = UNSET
    environment_id: str | Unset = UNSET
    root_operation: str | Unset = UNSET
    score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agents = self.agents

        app_id = self.app_id

        cache_read_tokens = self.cache_read_tokens

        cache_write_tokens = self.cache_write_tokens

        channel_id = self.channel_id

        duration_ms = self.duration_ms

        end_time = self.end_time.isoformat()

        error_count = self.error_count

        event_count = self.event_count

        handoff_count = self.handoff_count

        input_tokens = self.input_tokens

        last_seen_at = self.last_seen_at.isoformat()

        models = self.models

        output_tokens = self.output_tokens

        prompt_ids = self.prompt_ids

        prompt_version_ids = self.prompt_version_ids

        providers = self.providers

        reasoning_tokens = self.reasoning_tokens

        releases = self.releases

        revision = self.revision

        semantic_kinds = self.semantic_kinds

        services = self.services

        session_ids = self.session_ids

        start_time = self.start_time.isoformat()

        status = self.status.value

        tool_call_count = self.tool_call_count

        tools = self.tools

        total_tokens = self.total_tokens

        trace_id = self.trace_id

        updated_at = self.updated_at.isoformat()

        user_ids = self.user_ids

        cost_usd: float | None | Unset
        if isinstance(self.cost_usd, Unset):
            cost_usd = UNSET
        else:
            cost_usd = self.cost_usd

        environment_id = self.environment_id

        root_operation = self.root_operation

        score: float | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agents": agents,
                "appId": app_id,
                "cacheReadTokens": cache_read_tokens,
                "cacheWriteTokens": cache_write_tokens,
                "channelId": channel_id,
                "durationMs": duration_ms,
                "endTime": end_time,
                "errorCount": error_count,
                "eventCount": event_count,
                "handoffCount": handoff_count,
                "inputTokens": input_tokens,
                "lastSeenAt": last_seen_at,
                "models": models,
                "outputTokens": output_tokens,
                "promptIds": prompt_ids,
                "promptVersionIds": prompt_version_ids,
                "providers": providers,
                "reasoningTokens": reasoning_tokens,
                "releases": releases,
                "revision": revision,
                "semanticKinds": semantic_kinds,
                "services": services,
                "sessionIds": session_ids,
                "startTime": start_time,
                "status": status,
                "toolCallCount": tool_call_count,
                "tools": tools,
                "totalTokens": total_tokens,
                "traceId": trace_id,
                "updatedAt": updated_at,
                "userIds": user_ids,
            }
        )
        if cost_usd is not UNSET:
            field_dict["costUsd"] = cost_usd
        if environment_id is not UNSET:
            field_dict["environmentId"] = environment_id
        if root_operation is not UNSET:
            field_dict["rootOperation"] = root_operation
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agents = cast(list[str], d.pop("agents"))

        app_id = d.pop("appId")

        cache_read_tokens = d.pop("cacheReadTokens")

        cache_write_tokens = d.pop("cacheWriteTokens")

        channel_id = d.pop("channelId")

        duration_ms = d.pop("durationMs")

        end_time = isoparse(d.pop("endTime"))

        error_count = d.pop("errorCount")

        event_count = d.pop("eventCount")

        handoff_count = d.pop("handoffCount")

        input_tokens = d.pop("inputTokens")

        last_seen_at = isoparse(d.pop("lastSeenAt"))

        models = cast(list[str], d.pop("models"))

        output_tokens = d.pop("outputTokens")

        prompt_ids = cast(list[str], d.pop("promptIds"))

        prompt_version_ids = cast(list[str], d.pop("promptVersionIds"))

        providers = cast(list[str], d.pop("providers"))

        reasoning_tokens = d.pop("reasoningTokens")

        releases = cast(list[str], d.pop("releases"))

        revision = d.pop("revision")

        semantic_kinds = cast(list[str], d.pop("semanticKinds"))

        services = cast(list[str], d.pop("services"))

        session_ids = cast(list[str], d.pop("sessionIds"))

        start_time = isoparse(d.pop("startTime"))

        status = TraceStatus(d.pop("status"))

        tool_call_count = d.pop("toolCallCount")

        tools = cast(list[str], d.pop("tools"))

        total_tokens = d.pop("totalTokens")

        trace_id = d.pop("traceId")

        updated_at = isoparse(d.pop("updatedAt"))

        user_ids = cast(list[str], d.pop("userIds"))

        def _parse_cost_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cost_usd = _parse_cost_usd(d.pop("costUsd", UNSET))

        environment_id = d.pop("environmentId", UNSET)

        root_operation = d.pop("rootOperation", UNSET)

        def _parse_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        trace_summary_v2_dto = cls(
            agents=agents,
            app_id=app_id,
            cache_read_tokens=cache_read_tokens,
            cache_write_tokens=cache_write_tokens,
            channel_id=channel_id,
            duration_ms=duration_ms,
            end_time=end_time,
            error_count=error_count,
            event_count=event_count,
            handoff_count=handoff_count,
            input_tokens=input_tokens,
            last_seen_at=last_seen_at,
            models=models,
            output_tokens=output_tokens,
            prompt_ids=prompt_ids,
            prompt_version_ids=prompt_version_ids,
            providers=providers,
            reasoning_tokens=reasoning_tokens,
            releases=releases,
            revision=revision,
            semantic_kinds=semantic_kinds,
            services=services,
            session_ids=session_ids,
            start_time=start_time,
            status=status,
            tool_call_count=tool_call_count,
            tools=tools,
            total_tokens=total_tokens,
            trace_id=trace_id,
            updated_at=updated_at,
            user_ids=user_ids,
            cost_usd=cost_usd,
            environment_id=environment_id,
            root_operation=root_operation,
            score=score,
        )

        trace_summary_v2_dto.additional_properties = d
        return trace_summary_v2_dto

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
