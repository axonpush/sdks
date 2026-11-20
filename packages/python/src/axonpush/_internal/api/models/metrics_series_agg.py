from enum import Enum


class MetricsSeriesAgg(str, Enum):
    AVG = "avg"
    COUNT = "count"
    MAX = "max"
    MIN = "min"
    P50 = "p50"
    P95 = "p95"
    SUM = "sum"

    def __str__(self) -> str:
        return str(self.value)
