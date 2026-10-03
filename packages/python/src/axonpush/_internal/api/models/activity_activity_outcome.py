from enum import Enum


class ActivityActivityOutcome(str, Enum):
    ACCEPTED = "accepted"
    CANCELLED = "cancelled"
    COMMITTED = "committed"
    COMPLETED = "completed"
    FAILED = "failed"
    OBSERVED = "observed"
    QUEUED = "queued"
    RUNNING = "running"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
