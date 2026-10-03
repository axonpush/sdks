from enum import Enum


class ActivityViewType(str, Enum):
    BREAKDOWN = "breakdown"
    DIRECTORY = "directory"
    FUNNEL = "funnel"
    GRAPH = "graph"
    HEALTH = "health"
    INTERVAL = "interval"
    KPI = "kpi"
    LATENCY = "latency"
    RATE = "rate"
    TIMESERIES = "timeseries"

    def __str__(self) -> str:
        return str(self.value)
