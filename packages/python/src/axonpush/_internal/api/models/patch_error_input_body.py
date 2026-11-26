from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_error_input_body_action import PatchErrorInputBodyAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchErrorInputBody")


@_attrs_define
class PatchErrorInputBody:
    """
    Attributes:
        action (PatchErrorInputBodyAction): Triage action to apply
        schema (str | Unset): A URL to the JSON Schema for this object.
        assignee (str | Unset): User id to assign (for action=assign)
        resolved_in_release (str | Unset): Release the fix ships in (for action=resolve)
        snooze_until (str | Unset): RFC3339 time to auto-unmute (for action=mute)
        snooze_until_count (int | Unset): Re-alert after this many new occurrences (for action=mute)
        snooze_until_users (int | Unset): Re-alert after this many affected users (for action=mute)
    """

    action: PatchErrorInputBodyAction
    schema: str | Unset = UNSET
    assignee: str | Unset = UNSET
    resolved_in_release: str | Unset = UNSET
    snooze_until: str | Unset = UNSET
    snooze_until_count: int | Unset = UNSET
    snooze_until_users: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        schema = self.schema

        assignee = self.assignee

        resolved_in_release = self.resolved_in_release

        snooze_until = self.snooze_until

        snooze_until_count = self.snooze_until_count

        snooze_until_users = self.snooze_until_users

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if resolved_in_release is not UNSET:
            field_dict["resolvedInRelease"] = resolved_in_release
        if snooze_until is not UNSET:
            field_dict["snoozeUntil"] = snooze_until
        if snooze_until_count is not UNSET:
            field_dict["snoozeUntilCount"] = snooze_until_count
        if snooze_until_users is not UNSET:
            field_dict["snoozeUntilUsers"] = snooze_until_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = PatchErrorInputBodyAction(d.pop("action"))

        schema = d.pop("$schema", UNSET)

        assignee = d.pop("assignee", UNSET)

        resolved_in_release = d.pop("resolvedInRelease", UNSET)

        snooze_until = d.pop("snoozeUntil", UNSET)

        snooze_until_count = d.pop("snoozeUntilCount", UNSET)

        snooze_until_users = d.pop("snoozeUntilUsers", UNSET)

        patch_error_input_body = cls(
            action=action,
            schema=schema,
            assignee=assignee,
            resolved_in_release=resolved_in_release,
            snooze_until=snooze_until,
            snooze_until_count=snooze_until_count,
            snooze_until_users=snooze_until_users,
        )

        return patch_error_input_body
