from enum import Enum


class AnalyticsOverviewBucket(str, Enum):
    DAY = "day"
    HOUR = "hour"

    def __str__(self) -> str:
        return str(self.value)
