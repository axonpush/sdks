from enum import Enum


class ActivityAnalyticsFreshness(str, Enum):
    FRESH = "fresh"
    STALE = "stale"

    def __str__(self) -> str:
        return str(self.value)
