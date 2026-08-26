from enum import Enum


class AnalyticsControllerTimeseriesInterval(str, Enum):
    DAY = "day"
    HOUR = "hour"

    def __str__(self) -> str:
        return str(self.value)
