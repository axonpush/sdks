from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.compliance_grant import ComplianceGrant


T = TypeVar("T", bound="PolicyOutputBody")


@_attrs_define
class PolicyOutputBody:
    """
    Attributes:
        agent_id (str):
        grants (list[ComplianceGrant] | None):
        mode (str):
        opt_out (bool):
        suspended (bool):
        version (int):
        schema (str | Unset): A URL to the JSON Schema for this object.
    """

    agent_id: str
    grants: list[ComplianceGrant] | None
    mode: str
    opt_out: bool
    suspended: bool
    version: int
    schema: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_grant import ComplianceGrant

        agent_id = self.agent_id

        grants: list[dict[str, Any]] | None
        if isinstance(self.grants, list):
            grants = []
            for grants_type_0_item_data in self.grants:
                grants_type_0_item = grants_type_0_item_data.to_dict()
                grants.append(grants_type_0_item)

        else:
            grants = self.grants

        mode = self.mode

        opt_out = self.opt_out

        suspended = self.suspended

        version = self.version

        schema = self.schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agentId": agent_id,
                "grants": grants,
                "mode": mode,
                "optOut": opt_out,
                "suspended": suspended,
                "version": version,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_grant import ComplianceGrant

        d = dict(src_dict)
        agent_id = d.pop("agentId")

        def _parse_grants(data: object) -> list[ComplianceGrant] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                grants_type_0 = []
                _grants_type_0 = data
                for grants_type_0_item_data in _grants_type_0:
                    grants_type_0_item = ComplianceGrant.from_dict(grants_type_0_item_data)

                    grants_type_0.append(grants_type_0_item)

                return grants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComplianceGrant] | None, data)

        grants = _parse_grants(d.pop("grants"))

        mode = d.pop("mode")

        opt_out = d.pop("optOut")

        suspended = d.pop("suspended")

        version = d.pop("version")

        schema = d.pop("$schema", UNSET)

        policy_output_body = cls(
            agent_id=agent_id,
            grants=grants,
            mode=mode,
            opt_out=opt_out,
            suspended=suspended,
            version=version,
            schema=schema,
        )

        return policy_output_body
