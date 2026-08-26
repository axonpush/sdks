from enum import Enum


class ContentCaptureMode(str, Enum):
    FULL = "full"
    METADATA_ONLY = "metadata_only"
    REDACTED = "redacted"

    def __str__(self) -> str:
        return str(self.value)
