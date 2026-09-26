from enum import Enum


class ErrorsListStatus(str, Enum):
    ALL = "all"
    IGNORED = "ignored"
    MUTED = "muted"
    RESOLVED = "resolved"
    UNRESOLVED = "unresolved"

    def __str__(self) -> str:
        return str(self.value)
