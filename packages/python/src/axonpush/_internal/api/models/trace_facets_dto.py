from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_facet_value_dto import TraceFacetValueDto


T = TypeVar("T", bound="TraceFacetsDto")


@_attrs_define
class TraceFacetsDto:
    """
    Attributes:
        agent (list[TraceFacetValueDto] | Unset):
        model (list[TraceFacetValueDto] | Unset):
        provider (list[TraceFacetValueDto] | Unset):
        release (list[TraceFacetValueDto] | Unset):
        semantic_kind (list[TraceFacetValueDto] | Unset):
        service (list[TraceFacetValueDto] | Unset):
        tool (list[TraceFacetValueDto] | Unset):
    """

    agent: list[TraceFacetValueDto] | Unset = UNSET
    model: list[TraceFacetValueDto] | Unset = UNSET
    provider: list[TraceFacetValueDto] | Unset = UNSET
    release: list[TraceFacetValueDto] | Unset = UNSET
    semantic_kind: list[TraceFacetValueDto] | Unset = UNSET
    service: list[TraceFacetValueDto] | Unset = UNSET
    tool: list[TraceFacetValueDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_facet_value_dto import TraceFacetValueDto

        agent: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.agent, Unset):
            agent = []
            for agent_item_data in self.agent:
                agent_item = agent_item_data.to_dict()
                agent.append(agent_item)

        model: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.model, Unset):
            model = []
            for model_item_data in self.model:
                model_item = model_item_data.to_dict()
                model.append(model_item)

        provider: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = []
            for provider_item_data in self.provider:
                provider_item = provider_item_data.to_dict()
                provider.append(provider_item)

        release: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.release, Unset):
            release = []
            for release_item_data in self.release:
                release_item = release_item_data.to_dict()
                release.append(release_item)

        semantic_kind: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.semantic_kind, Unset):
            semantic_kind = []
            for semantic_kind_item_data in self.semantic_kind:
                semantic_kind_item = semantic_kind_item_data.to_dict()
                semantic_kind.append(semantic_kind_item)

        service: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service, Unset):
            service = []
            for service_item_data in self.service:
                service_item = service_item_data.to_dict()
                service.append(service_item)

        tool: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tool, Unset):
            tool = []
            for tool_item_data in self.tool:
                tool_item = tool_item_data.to_dict()
                tool.append(tool_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent is not UNSET:
            field_dict["agent"] = agent
        if model is not UNSET:
            field_dict["model"] = model
        if provider is not UNSET:
            field_dict["provider"] = provider
        if release is not UNSET:
            field_dict["release"] = release
        if semantic_kind is not UNSET:
            field_dict["semanticKind"] = semantic_kind
        if service is not UNSET:
            field_dict["service"] = service
        if tool is not UNSET:
            field_dict["tool"] = tool

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_facet_value_dto import TraceFacetValueDto

        d = dict(src_dict)
        _agent = d.pop("agent", UNSET)
        agent: list[TraceFacetValueDto] | Unset = UNSET
        if _agent is not UNSET:
            agent = []
            for agent_item_data in _agent:
                agent_item = TraceFacetValueDto.from_dict(agent_item_data)

                agent.append(agent_item)

        _model = d.pop("model", UNSET)
        model: list[TraceFacetValueDto] | Unset = UNSET
        if _model is not UNSET:
            model = []
            for model_item_data in _model:
                model_item = TraceFacetValueDto.from_dict(model_item_data)

                model.append(model_item)

        _provider = d.pop("provider", UNSET)
        provider: list[TraceFacetValueDto] | Unset = UNSET
        if _provider is not UNSET:
            provider = []
            for provider_item_data in _provider:
                provider_item = TraceFacetValueDto.from_dict(provider_item_data)

                provider.append(provider_item)

        _release = d.pop("release", UNSET)
        release: list[TraceFacetValueDto] | Unset = UNSET
        if _release is not UNSET:
            release = []
            for release_item_data in _release:
                release_item = TraceFacetValueDto.from_dict(release_item_data)

                release.append(release_item)

        _semantic_kind = d.pop("semanticKind", UNSET)
        semantic_kind: list[TraceFacetValueDto] | Unset = UNSET
        if _semantic_kind is not UNSET:
            semantic_kind = []
            for semantic_kind_item_data in _semantic_kind:
                semantic_kind_item = TraceFacetValueDto.from_dict(semantic_kind_item_data)

                semantic_kind.append(semantic_kind_item)

        _service = d.pop("service", UNSET)
        service: list[TraceFacetValueDto] | Unset = UNSET
        if _service is not UNSET:
            service = []
            for service_item_data in _service:
                service_item = TraceFacetValueDto.from_dict(service_item_data)

                service.append(service_item)

        _tool = d.pop("tool", UNSET)
        tool: list[TraceFacetValueDto] | Unset = UNSET
        if _tool is not UNSET:
            tool = []
            for tool_item_data in _tool:
                tool_item = TraceFacetValueDto.from_dict(tool_item_data)

                tool.append(tool_item)

        trace_facets_dto = cls(
            agent=agent,
            model=model,
            provider=provider,
            release=release,
            semantic_kind=semantic_kind,
            service=service,
            tool=tool,
        )

        trace_facets_dto.additional_properties = d
        return trace_facets_dto

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
