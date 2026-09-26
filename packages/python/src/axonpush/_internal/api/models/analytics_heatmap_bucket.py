from enum import Enum


class AnalyticsHeatmapBucket(str, Enum):
    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"

    def __str__(self) -> str:
        return str(self.value)
