from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset_item_input_dto_attachments import DatasetItemInputDtoAttachments
    from ..models.dataset_item_input_dto_expected_output import DatasetItemInputDtoExpectedOutput
    from ..models.dataset_item_input_dto_input import DatasetItemInputDtoInput
    from ..models.dataset_item_input_dto_metadata import DatasetItemInputDtoMetadata
    from ..models.dataset_item_input_dto_tool_trajectory import DatasetItemInputDtoToolTrajectory


T = TypeVar("T", bound="DatasetItemInputDto")


@_attrs_define
class DatasetItemInputDto:
    """
    Attributes:
        input_ (DatasetItemInputDtoInput): Redacted before persistence according to the organization policy.
        attachments (DatasetItemInputDtoAttachments | Unset):
        expected_output (DatasetItemInputDtoExpectedOutput | Unset):
        item_id (str | Unset):
        metadata (DatasetItemInputDtoMetadata | Unset):
        source_span_id (str | Unset):
        source_trace_id (str | Unset):
        tool_trajectory (DatasetItemInputDtoToolTrajectory | Unset):
    """

    input_: DatasetItemInputDtoInput
    attachments: DatasetItemInputDtoAttachments | Unset = UNSET
    expected_output: DatasetItemInputDtoExpectedOutput | Unset = UNSET
    item_id: str | Unset = UNSET
    metadata: DatasetItemInputDtoMetadata | Unset = UNSET
    source_span_id: str | Unset = UNSET
    source_trace_id: str | Unset = UNSET
    tool_trajectory: DatasetItemInputDtoToolTrajectory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dataset_item_input_dto_attachments import DatasetItemInputDtoAttachments
        from ..models.dataset_item_input_dto_expected_output import (
            DatasetItemInputDtoExpectedOutput,
        )
        from ..models.dataset_item_input_dto_input import DatasetItemInputDtoInput
        from ..models.dataset_item_input_dto_metadata import DatasetItemInputDtoMetadata
        from ..models.dataset_item_input_dto_tool_trajectory import (
            DatasetItemInputDtoToolTrajectory,
        )

        input_ = self.input_.to_dict()

        attachments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments.to_dict()

        expected_output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expected_output, Unset):
            expected_output = self.expected_output.to_dict()

        item_id = self.item_id

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        source_span_id = self.source_span_id

        source_trace_id = self.source_trace_id

        tool_trajectory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_trajectory, Unset):
            tool_trajectory = self.tool_trajectory.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
            }
        )
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if expected_output is not UNSET:
            field_dict["expectedOutput"] = expected_output
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if source_span_id is not UNSET:
            field_dict["sourceSpanId"] = source_span_id
        if source_trace_id is not UNSET:
            field_dict["sourceTraceId"] = source_trace_id
        if tool_trajectory is not UNSET:
            field_dict["toolTrajectory"] = tool_trajectory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dataset_item_input_dto_attachments import DatasetItemInputDtoAttachments
        from ..models.dataset_item_input_dto_expected_output import (
            DatasetItemInputDtoExpectedOutput,
        )
        from ..models.dataset_item_input_dto_input import DatasetItemInputDtoInput
        from ..models.dataset_item_input_dto_metadata import DatasetItemInputDtoMetadata
        from ..models.dataset_item_input_dto_tool_trajectory import (
            DatasetItemInputDtoToolTrajectory,
        )

        d = dict(src_dict)
        input_ = DatasetItemInputDtoInput.from_dict(d.pop("input"))

        _attachments = d.pop("attachments", UNSET)
        attachments: DatasetItemInputDtoAttachments | Unset
        if isinstance(_attachments, Unset):
            attachments = UNSET
        else:
            attachments = DatasetItemInputDtoAttachments.from_dict(_attachments)

        _expected_output = d.pop("expectedOutput", UNSET)
        expected_output: DatasetItemInputDtoExpectedOutput | Unset
        if isinstance(_expected_output, Unset):
            expected_output = UNSET
        else:
            expected_output = DatasetItemInputDtoExpectedOutput.from_dict(_expected_output)

        item_id = d.pop("itemId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: DatasetItemInputDtoMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DatasetItemInputDtoMetadata.from_dict(_metadata)

        source_span_id = d.pop("sourceSpanId", UNSET)

        source_trace_id = d.pop("sourceTraceId", UNSET)

        _tool_trajectory = d.pop("toolTrajectory", UNSET)
        tool_trajectory: DatasetItemInputDtoToolTrajectory | Unset
        if isinstance(_tool_trajectory, Unset):
            tool_trajectory = UNSET
        else:
            tool_trajectory = DatasetItemInputDtoToolTrajectory.from_dict(_tool_trajectory)

        dataset_item_input_dto = cls(
            input_=input_,
            attachments=attachments,
            expected_output=expected_output,
            item_id=item_id,
            metadata=metadata,
            source_span_id=source_span_id,
            source_trace_id=source_trace_id,
            tool_trajectory=tool_trajectory,
        )

        dataset_item_input_dto.additional_properties = d
        return dataset_item_input_dto

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
