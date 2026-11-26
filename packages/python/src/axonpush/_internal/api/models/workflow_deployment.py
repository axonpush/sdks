from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.workflow_deployment_status import WorkflowDeploymentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_counts import DeploymentCounts
    from ..models.deployment_runtime import DeploymentRuntime
    from ..models.deployment_source import DeploymentSource


T = TypeVar("T", bound="WorkflowDeployment")


@_attrs_define
class WorkflowDeployment:
    """
    Attributes:
        environment (str):
        problems (list[str] | None):
        recent_results (DeploymentCounts):
        required_sources (list[DeploymentSource] | None):
        semantic_hash (str):
        status (WorkflowDeploymentStatus):
        title (str):
        updated_at (datetime.datetime):
        version_id (str):
        workflow (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        runtime (DeploymentRuntime | Unset):
    """

    environment: str
    problems: list[str] | None
    recent_results: DeploymentCounts
    required_sources: list[DeploymentSource] | None
    semantic_hash: str
    status: WorkflowDeploymentStatus
    title: str
    updated_at: datetime.datetime
    version_id: str
    workflow: str
    schema: str | Unset = UNSET
    runtime: DeploymentRuntime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.deployment_counts import DeploymentCounts
        from ..models.deployment_runtime import DeploymentRuntime
        from ..models.deployment_source import DeploymentSource

        environment = self.environment

        problems: list[str] | None
        if isinstance(self.problems, list):
            problems = self.problems

        else:
            problems = self.problems

        recent_results = self.recent_results.to_dict()

        required_sources: list[dict[str, Any]] | None
        if isinstance(self.required_sources, list):
            required_sources = []
            for required_sources_type_0_item_data in self.required_sources:
                required_sources_type_0_item = (
                    required_sources_type_0_item_data.to_dict()
                )
                required_sources.append(required_sources_type_0_item)

        else:
            required_sources = self.required_sources

        semantic_hash = self.semantic_hash

        status = self.status.value

        title = self.title

        updated_at = self.updated_at.isoformat()

        version_id = self.version_id

        workflow = self.workflow

        schema = self.schema

        runtime: dict[str, Any] | Unset = UNSET
        if not isinstance(self.runtime, Unset):
            runtime = self.runtime.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "environment": environment,
                "problems": problems,
                "recent_results": recent_results,
                "required_sources": required_sources,
                "semantic_hash": semantic_hash,
                "status": status,
                "title": title,
                "updated_at": updated_at,
                "version_id": version_id,
                "workflow": workflow,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if runtime is not UNSET:
            field_dict["runtime"] = runtime

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_counts import DeploymentCounts
        from ..models.deployment_runtime import DeploymentRuntime
        from ..models.deployment_source import DeploymentSource

        d = dict(src_dict)
        environment = d.pop("environment")

        def _parse_problems(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                problems_type_0 = cast(list[str], data)

                return problems_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        problems = _parse_problems(d.pop("problems"))

        recent_results = DeploymentCounts.from_dict(d.pop("recent_results"))

        def _parse_required_sources(data: object) -> list[DeploymentSource] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                required_sources_type_0 = []
                _required_sources_type_0 = data
                for required_sources_type_0_item_data in _required_sources_type_0:
                    required_sources_type_0_item = DeploymentSource.from_dict(
                        required_sources_type_0_item_data
                    )

                    required_sources_type_0.append(required_sources_type_0_item)

                return required_sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DeploymentSource] | None, data)

        required_sources = _parse_required_sources(d.pop("required_sources"))

        semantic_hash = d.pop("semantic_hash")

        status = WorkflowDeploymentStatus(d.pop("status"))

        title = d.pop("title")

        updated_at = isoparse(d.pop("updated_at"))

        version_id = d.pop("version_id")

        workflow = d.pop("workflow")

        schema = d.pop("$schema", UNSET)

        _runtime = d.pop("runtime", UNSET)
        runtime: DeploymentRuntime | Unset
        if isinstance(_runtime, Unset):
            runtime = UNSET
        else:
            runtime = DeploymentRuntime.from_dict(_runtime)

        workflow_deployment = cls(
            environment=environment,
            problems=problems,
            recent_results=recent_results,
            required_sources=required_sources,
            semantic_hash=semantic_hash,
            status=status,
            title=title,
            updated_at=updated_at,
            version_id=version_id,
            workflow=workflow,
            schema=schema,
            runtime=runtime,
        )

        return workflow_deployment
