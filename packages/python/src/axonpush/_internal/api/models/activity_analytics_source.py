from enum import Enum


class ActivityAnalyticsSource(str, Enum):
    PROJECTION = "projection"
    ROLLUP = "rollup"

    def __str__(self) -> str:
        return str(self.value)
