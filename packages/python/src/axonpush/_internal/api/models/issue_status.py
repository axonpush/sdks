from enum import Enum


class IssueStatus(str, Enum):
    DISMISSED = "dismissed"
    MERGED = "merged"
    OPEN = "open"
    REGRESSED = "regressed"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
