from enum import Enum


class ActivityViewType(str, Enum):
    BREAKDOWN = "breakdown"
    DIRECTORY = "directory"
    FUNNEL = "funnel"
    HEALTH = "health"
    KPI = "kpi"
    LATENCY = "latency"
    TIMESERIES = "timeseries"

    def __str__(self) -> str:
        return str(self.value)
