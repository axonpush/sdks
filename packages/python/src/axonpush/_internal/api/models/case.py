from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.case_dispositions import CaseDispositions
    from ..models.input_ import Input
    from ..models.result import Result


T = TypeVar("T", bound="Case")


@_attrs_define
class Case:
    """
    Attributes:
        dispositions (CaseDispositions):
        input_ (Input):
        key (str):
        pending (bool):
        result (Result):
        revision (int):
        version_id (str):
        workflow (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    dispositions: CaseDispositions
    input_: Input
    key: str
    pending: bool
    result: Result
    revision: int
    version_id: str
    workflow: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.case_dispositions import CaseDispositions
        from ..models.input_ import Input
        from ..models.result import Result

        dispositions = self.dispositions.to_dict()

        input_ = self.input_.to_dict()

        key = self.key

        pending = self.pending

        result = self.result.to_dict()

        revision = self.revision

        version_id = self.version_id

        workflow = self.workflow

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dispositions": dispositions,
                "input": input_,
                "key": key,
                "pending": pending,
                "result": result,
                "revision": revision,
                "version_id": version_id,
                "workflow": workflow,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.case_dispositions import CaseDispositions
        from ..models.input_ import Input
        from ..models.result import Result

        d = dict(src_dict)
        dispositions = CaseDispositions.from_dict(d.pop("dispositions"))

        input_ = Input.from_dict(d.pop("input"))

        key = d.pop("key")

        pending = d.pop("pending")

        result = Result.from_dict(d.pop("result"))

        revision = d.pop("revision")

        version_id = d.pop("version_id")

        workflow = d.pop("workflow")

        schema = d.pop("$schema", UNSET)

        case = cls(
            dispositions=dispositions,
            input_=input_,
            key=key,
            pending=pending,
            result=result,
            revision=revision,
            version_id=version_id,
            workflow=workflow,
            schema=schema,
        )

        return case
