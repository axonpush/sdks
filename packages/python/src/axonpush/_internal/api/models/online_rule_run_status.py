from enum import Enum


class OnlineRuleRunStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    QUEUED = "queued"
    RUNNING = "running"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
