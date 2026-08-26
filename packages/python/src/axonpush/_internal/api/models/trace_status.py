from enum import Enum


class TraceStatus(str, Enum):
    ERROR = "error"
    OK = "ok"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
