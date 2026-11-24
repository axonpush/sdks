from enum import Enum


class MonitorCheckInSummaryDTOStatus(str, Enum):
    ERROR = "error"
    IN_PROGRESS = "in_progress"
    MISSED = "missed"
    OK = "ok"
    TIMEOUT = "timeout"

    def __str__(self) -> str:
        return str(self.value)
