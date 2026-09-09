from enum import Enum


class ActionCheckState(str, Enum):
    CONFLICT = "conflict"
    MATCH = "match"
    PENDING = "pending"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
