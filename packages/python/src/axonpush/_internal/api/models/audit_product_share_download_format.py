from enum import Enum


class AuditProductShareDownloadFormat(str, Enum):
    JSON = "json"
    PDF = "pdf"

    def __str__(self) -> str:
        return str(self.value)
