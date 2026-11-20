from enum import Enum


class EventDTOOrigin(str, Enum):
    ARCHIVE = "archive"

    def __str__(self) -> str:
        return str(self.value)
