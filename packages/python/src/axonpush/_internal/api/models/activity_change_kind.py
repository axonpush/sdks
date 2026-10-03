from enum import Enum


class ActivityChangeKind(str, Enum):
    ALERT = "alert"
    ATTRIBUTE = "attribute"
    ENTITY = "entity"
    EVENT = "event"
    FIELD = "field"
    FUNNEL = "funnel"
    PROFILE = "profile"
    VIEW = "view"
    WORKSPACE = "workspace"

    def __str__(self) -> str:
        return str(self.value)
