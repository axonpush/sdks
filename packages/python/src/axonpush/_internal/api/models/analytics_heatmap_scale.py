from enum import Enum


class AnalyticsHeatmapScale(str, Enum):
    LINEAR = "linear"
    LOG = "log"

    def __str__(self) -> str:
        return str(self.value)
