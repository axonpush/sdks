from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogDTO")


@_attrs_define
class LogDTO:
    """
    Attributes:
        action (str):
        actor_id (None | str):
        created_at (str):
        id (str):
        ip_address (None | str):
        metadata (Any):
        organization_id (str):
        resource_id (str):
        resource_type (str):
        actor_email (str | Unset):
        entry_hash (str | Unset):
        prev_hash (str | Unset):
        seq (int | Unset):
        source (str | Unset):
    """

    action: str
    actor_id: None | str
    created_at: str
    id: str
    ip_address: None | str
    metadata: Any
    organization_id: str
    resource_id: str
    resource_type: str
    actor_email: str | Unset = UNSET
    entry_hash: str | Unset = UNSET
    prev_hash: str | Unset = UNSET
    seq: int | Unset = UNSET
    source: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        actor_id: None | str
        actor_id = self.actor_id

        created_at = self.created_at

        id = self.id

        ip_address: None | str
        ip_address = self.ip_address

        metadata = self.metadata

        organization_id = self.organization_id

        resource_id = self.resource_id

        resource_type = self.resource_type

        actor_email = self.actor_email

        entry_hash = self.entry_hash

        prev_hash = self.prev_hash

        seq = self.seq

        source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
                "actorId": actor_id,
                "createdAt": created_at,
                "id": id,
                "ipAddress": ip_address,
                "metadata": metadata,
                "organizationId": organization_id,
                "resourceId": resource_id,
                "resourceType": resource_type,
            }
        )
        if actor_email is not UNSET:
            field_dict["actorEmail"] = actor_email
        if entry_hash is not UNSET:
            field_dict["entryHash"] = entry_hash
        if prev_hash is not UNSET:
            field_dict["prevHash"] = prev_hash
        if seq is not UNSET:
            field_dict["seq"] = seq
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        def _parse_actor_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        actor_id = _parse_actor_id(d.pop("actorId"))

        created_at = d.pop("createdAt")

        id = d.pop("id")

        def _parse_ip_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ip_address = _parse_ip_address(d.pop("ipAddress"))

        metadata = d.pop("metadata")

        organization_id = d.pop("organizationId")

        resource_id = d.pop("resourceId")

        resource_type = d.pop("resourceType")

        actor_email = d.pop("actorEmail", UNSET)

        entry_hash = d.pop("entryHash", UNSET)

        prev_hash = d.pop("prevHash", UNSET)

        seq = d.pop("seq", UNSET)

        source = d.pop("source", UNSET)

        log_dto = cls(
            action=action,
            actor_id=actor_id,
            created_at=created_at,
            id=id,
            ip_address=ip_address,
            metadata=metadata,
            organization_id=organization_id,
            resource_id=resource_id,
            resource_type=resource_type,
            actor_email=actor_email,
            entry_hash=entry_hash,
            prev_hash=prev_hash,
            seq=seq,
            source=source,
        )

        return log_dto
