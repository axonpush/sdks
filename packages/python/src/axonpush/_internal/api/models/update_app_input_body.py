from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAppInputBody")


@_attrs_define
class UpdateAppInputBody:
    """
    Attributes:
        name (str):
        schema (str | Unset): A URL to the JSON Schema for this object.
        default_branch (str | Unset): Default branch (omit to leave unchanged)
        repo_url (str | Unset): Source repository URL for the coding-agent handoff (omit to leave unchanged)
    """

    name: str
    schema: str | Unset = UNSET
    default_branch: str | Unset = UNSET
    repo_url: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        schema = self.schema

        default_branch = self.default_branch

        repo_url = self.repo_url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if schema is not UNSET:
            field_dict["$schema"] = schema
        if default_branch is not UNSET:
            field_dict["defaultBranch"] = default_branch
        if repo_url is not UNSET:
            field_dict["repoUrl"] = repo_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        schema = d.pop("$schema", UNSET)

        default_branch = d.pop("defaultBranch", UNSET)

        repo_url = d.pop("repoUrl", UNSET)

        update_app_input_body = cls(
            name=name,
            schema=schema,
            default_branch=default_branch,
            repo_url=repo_url,
        )

        return update_app_input_body
