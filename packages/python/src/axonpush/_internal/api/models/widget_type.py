from enum import Enum


class WidgetType(str, Enum):
    BREAKDOWN = "breakdown"
    KPI = "kpi"
    LATENCY = "latency"
    TIMESERIES = "timeseries"

    def __str__(self) -> str:
        return str(self.value)
