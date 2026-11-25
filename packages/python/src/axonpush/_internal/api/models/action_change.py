from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
    from ..models.action_change_input import ActionChangeInput


T = TypeVar("T", bound="ActionChange")


@_attrs_define
class ActionChange:
    """
    Attributes:
        actor (str):
        at (datetime.datetime):
        revision (int):
        status (str):
        input_ (ActionChangeInput | Unset):
    """

    actor: str
    at: datetime.datetime
    revision: int
    status: str
    input_: ActionChangeInput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_change_input import ActionChangeInput

        actor = self.actor

        at = self.at.isoformat()

        revision = self.revision

        status = self.status

        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "actor": actor,
                "at": at,
                "revision": revision,
                "status": status,
            }
        )
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_change_input import ActionChangeInput

        d = dict(src_dict)
        actor = d.pop("actor")

        at = isoparse(d.pop("at"))

        revision = d.pop("revision")

        status = d.pop("status")

        _input_ = d.pop("input", UNSET)
        input_: ActionChangeInput | Unset
        if isinstance(_input_, Unset):
            input_ = UNSET
        else:
            input_ = ActionChangeInput.from_dict(_input_)

        action_change = cls(
            actor=actor,
            at=at,
            revision=revision,
            status=status,
            input_=input_,
        )

        return action_change
