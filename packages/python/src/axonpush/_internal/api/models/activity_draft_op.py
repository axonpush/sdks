from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, BinaryIO, Generator, TextIO, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_draft_op_op import ActivityDraftOpOp
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_alert import ActivityAlert
    from ..models.activity_attribute import ActivityAttribute
    from ..models.activity_entity_definition import ActivityEntityDefinition
    from ..models.activity_event_rule import ActivityEventRule
    from ..models.activity_funnel import ActivityFunnel
    from ..models.activity_view import ActivityView
    from ..models.activity_workspace_patch import ActivityWorkspacePatch


T = TypeVar("T", bound="ActivityDraftOp")


@_attrs_define
class ActivityDraftOp:
    """
    Attributes:
        op (ActivityDraftOpOp):
        alert (ActivityAlert | Unset):
        attribute (ActivityAttribute | Unset):
        entity (ActivityEntityDefinition | Unset):
        event (ActivityEventRule | Unset):
        funnel (ActivityFunnel | Unset):
        key (str | Unset): Attribute key (attribute.update/remove, entity.field.*, entity.profile.*)
        match (str | Unset): Event rule match (event.update/remove)
        name (str | Unset): Funnel or alert name, or view id (update/remove)
        type_ (str | Unset): Entity type the op targets
        view (ActivityView | Unset):
        workspace (ActivityWorkspacePatch | Unset):
    """

    op: ActivityDraftOpOp
    alert: ActivityAlert | Unset = UNSET
    attribute: ActivityAttribute | Unset = UNSET
    entity: ActivityEntityDefinition | Unset = UNSET
    event: ActivityEventRule | Unset = UNSET
    funnel: ActivityFunnel | Unset = UNSET
    key: str | Unset = UNSET
    match: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    view: ActivityView | Unset = UNSET
    workspace: ActivityWorkspacePatch | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.activity_alert import ActivityAlert
        from ..models.activity_attribute import ActivityAttribute
        from ..models.activity_entity_definition import ActivityEntityDefinition
        from ..models.activity_event_rule import ActivityEventRule
        from ..models.activity_funnel import ActivityFunnel
        from ..models.activity_view import ActivityView
        from ..models.activity_workspace_patch import ActivityWorkspacePatch

        op = self.op.value

        alert: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        attribute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attribute, Unset):
            attribute = self.attribute.to_dict()

        entity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        funnel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.funnel, Unset):
            funnel = self.funnel.to_dict()

        key = self.key

        match = self.match

        name = self.name

        type_ = self.type_

        view: dict[str, Any] | Unset = UNSET
        if not isinstance(self.view, Unset):
            view = self.view.to_dict()

        workspace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workspace, Unset):
            workspace = self.workspace.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "op": op,
            }
        )
        if alert is not UNSET:
            field_dict["alert"] = alert
        if attribute is not UNSET:
            field_dict["attribute"] = attribute
        if entity is not UNSET:
            field_dict["entity"] = entity
        if event is not UNSET:
            field_dict["event"] = event
        if funnel is not UNSET:
            field_dict["funnel"] = funnel
        if key is not UNSET:
            field_dict["key"] = key
        if match is not UNSET:
            field_dict["match"] = match
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if view is not UNSET:
            field_dict["view"] = view
        if workspace is not UNSET:
            field_dict["workspace"] = workspace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_alert import ActivityAlert
        from ..models.activity_attribute import ActivityAttribute
        from ..models.activity_entity_definition import ActivityEntityDefinition
        from ..models.activity_event_rule import ActivityEventRule
        from ..models.activity_funnel import ActivityFunnel
        from ..models.activity_view import ActivityView
        from ..models.activity_workspace_patch import ActivityWorkspacePatch

        d = dict(src_dict)
        op = ActivityDraftOpOp(d.pop("op"))

        _alert = d.pop("alert", UNSET)
        alert: ActivityAlert | Unset
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = ActivityAlert.from_dict(_alert)

        _attribute = d.pop("attribute", UNSET)
        attribute: ActivityAttribute | Unset
        if isinstance(_attribute, Unset):
            attribute = UNSET
        else:
            attribute = ActivityAttribute.from_dict(_attribute)

        _entity = d.pop("entity", UNSET)
        entity: ActivityEntityDefinition | Unset
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = ActivityEntityDefinition.from_dict(_entity)

        _event = d.pop("event", UNSET)
        event: ActivityEventRule | Unset
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = ActivityEventRule.from_dict(_event)

        _funnel = d.pop("funnel", UNSET)
        funnel: ActivityFunnel | Unset
        if isinstance(_funnel, Unset):
            funnel = UNSET
        else:
            funnel = ActivityFunnel.from_dict(_funnel)

        key = d.pop("key", UNSET)

        match = d.pop("match", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        _view = d.pop("view", UNSET)
        view: ActivityView | Unset
        if isinstance(_view, Unset):
            view = UNSET
        else:
            view = ActivityView.from_dict(_view)

        _workspace = d.pop("workspace", UNSET)
        workspace: ActivityWorkspacePatch | Unset
        if isinstance(_workspace, Unset):
            workspace = UNSET
        else:
            workspace = ActivityWorkspacePatch.from_dict(_workspace)

        activity_draft_op = cls(
            op=op,
            alert=alert,
            attribute=attribute,
            entity=entity,
            event=event,
            funnel=funnel,
            key=key,
            match=match,
            name=name,
            type_=type_,
            view=view,
            workspace=workspace,
        )

        return activity_draft_op
