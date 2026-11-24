from enum import Enum


class FetchStatusOutputBodyState(str, Enum):
    FAILED = "failed"
    GONE = "gone"
    QUEUED = "queued"
    READY = "ready"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
