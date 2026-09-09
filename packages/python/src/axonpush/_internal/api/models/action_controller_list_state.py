from enum import Enum


class ActionControllerListState(str, Enum):
    CONFIRMED = "confirmed"
    CONTRADICTED = "contradicted"
    PENDING = "pending"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
