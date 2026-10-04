from enum import Enum


class ActivitySummaryFreshness(str, Enum):
    CURRENT = "current"
    FRESH = "fresh"
    STALE = "stale"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
