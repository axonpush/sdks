from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.workflow_deployment import WorkflowDeployment


T = TypeVar("T", bound="DeploymentListOutputBody")


@_attrs_define
class DeploymentListOutputBody:
    """
    Attributes:
        deployments (list[WorkflowDeployment] | None):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    deployments: list[WorkflowDeployment] | None
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_deployment import WorkflowDeployment

        deployments: list[dict[str, Any]] | None
        if isinstance(self.deployments, list):
            deployments = []
            for deployments_type_0_item_data in self.deployments:
                deployments_type_0_item = deployments_type_0_item_data.to_dict()
                deployments.append(deployments_type_0_item)

        else:
            deployments = self.deployments

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "deployments": deployments,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_deployment import WorkflowDeployment

        d = dict(src_dict)

        def _parse_deployments(data: object) -> list[WorkflowDeployment] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                deployments_type_0 = []
                _deployments_type_0 = data
                for deployments_type_0_item_data in _deployments_type_0:
                    deployments_type_0_item = WorkflowDeployment.from_dict(
                        deployments_type_0_item_data
                    )

                    deployments_type_0.append(deployments_type_0_item)

                return deployments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[WorkflowDeployment] | None, data)

        deployments = _parse_deployments(d.pop("deployments"))

        schema = d.pop("$schema", UNSET)

        deployment_list_output_body = cls(
            deployments=deployments,
            schema=schema,
        )

        return deployment_list_output_body
