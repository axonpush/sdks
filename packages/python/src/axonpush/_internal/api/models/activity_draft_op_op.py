from enum import Enum


class ActivityDraftOpOp(str, Enum):
    ALERT_ADD = "alert.add"
    ALERT_REMOVE = "alert.remove"
    ALERT_UPDATE = "alert.update"
    ATTRIBUTE_ADD = "attribute.add"
    ATTRIBUTE_REMOVE = "attribute.remove"
    ATTRIBUTE_UPDATE = "attribute.update"
    ENTITY_ADD = "entity.add"
    ENTITY_FIELD_ADD = "entity.field.add"
    ENTITY_FIELD_REMOVE = "entity.field.remove"
    ENTITY_PROFILE_ADD = "entity.profile.add"
    ENTITY_PROFILE_REMOVE = "entity.profile.remove"
    ENTITY_REMOVE = "entity.remove"
    ENTITY_UPDATE = "entity.update"
    EVENT_ADD = "event.add"
    EVENT_REMOVE = "event.remove"
    EVENT_UPDATE = "event.update"
    FUNNEL_ADD = "funnel.add"
    FUNNEL_REMOVE = "funnel.remove"
    FUNNEL_UPDATE = "funnel.update"
    VIEW_ADD = "view.add"
    VIEW_REMOVE = "view.remove"
    VIEW_UPDATE = "view.update"
    WORKSPACE_UPDATE = "workspace.update"

    def __str__(self) -> str:
        return str(self.value)
