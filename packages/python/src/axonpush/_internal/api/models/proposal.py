from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
    from ..models.proposal_input import ProposalInput


T = TypeVar("T", bound="Proposal")


@_attrs_define
class Proposal:
    """
    Attributes:
        input_ (ProposalInput):
        name (str):
        request_id (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    input_: ProposalInput
    name: str
    request_id: str
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.proposal_input import ProposalInput

        input_ = self.input_.to_dict()

        name = self.name

        request_id = self.request_id

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "input": input_,
                "name": name,
                "request_id": request_id,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proposal_input import ProposalInput

        d = dict(src_dict)
        input_ = ProposalInput.from_dict(d.pop("input"))

        name = d.pop("name")

        request_id = d.pop("request_id")

        schema = d.pop("$schema", UNSET)

        proposal = cls(
            input_=input_,
            name=name,
            request_id=request_id,
            schema=schema,
        )

        return proposal
