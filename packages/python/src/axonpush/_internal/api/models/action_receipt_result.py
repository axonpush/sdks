from enum import Enum


class ActionReceiptResult(str, Enum):
    ABSENT = "absent"
    AMBIGUOUS = "ambiguous"
    EXECUTED = "executed"
    FOUND = "found"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
