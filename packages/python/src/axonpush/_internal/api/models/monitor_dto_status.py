from enum import Enum


class MonitorDTOStatus(str, Enum):
    ACTIVE = "active"
    ERROR = "error"
    MISSED = "missed"
    OK = "ok"
    TIMEOUT = "timeout"

    def __str__(self) -> str:
        return str(self.value)
