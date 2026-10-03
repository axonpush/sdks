from enum import Enum


class ActivityAttributeType(str, Enum):
    BOOL = "bool"
    DURATION = "duration"
    ENUM = "enum"
    NUMBER = "number"
    REF = "ref"
    TEXT = "text"
    TIME = "time"

    def __str__(self) -> str:
        return str(self.value)
