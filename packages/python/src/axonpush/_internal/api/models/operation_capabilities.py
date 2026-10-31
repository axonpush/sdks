from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.operation_capability import OperationCapability


T = TypeVar("T", bound="OperationCapabilities")


@_attrs_define
class OperationCapabilities:
    """
    Attributes:
        operations (list[OperationCapability] | None):
        registry_revision (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    operations: list[OperationCapability] | None
    registry_revision: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.operation_capability import OperationCapability

        operations: list[dict[str, Any]] | None
        if isinstance(self.operations, list):
            operations = []
            for operations_type_0_item_data in self.operations:
                operations_type_0_item = operations_type_0_item_data.to_dict()
                operations.append(operations_type_0_item)

        else:
            operations = self.operations

        registry_revision = self.registry_revision

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "operations": operations,
                "registryRevision": registry_revision,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.operation_capability import OperationCapability

        d = dict(src_dict)

        def _parse_operations(data: object) -> list[OperationCapability] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                operations_type_0 = []
                _operations_type_0 = data
                for operations_type_0_item_data in _operations_type_0:
                    operations_type_0_item = OperationCapability.from_dict(
                        operations_type_0_item_data
                    )

                    operations_type_0.append(operations_type_0_item)

                return operations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OperationCapability] | None, data)

        operations = _parse_operations(d.pop("operations"))

        registry_revision = d.pop("registryRevision")

        schema = d.pop("$schema", UNSET)

        operation_capabilities = cls(
            operations=operations,
            registry_revision=registry_revision,
            schema=schema,
        )

        return operation_capabilities
