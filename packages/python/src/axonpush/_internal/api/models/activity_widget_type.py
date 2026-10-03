from enum import Enum


class ActivityWidgetType(str, Enum):
    BREAKDOWN = "breakdown"
    DIRECTORY = "directory"
    FUNNEL = "funnel"
    HEALTH = "health"
    KPI = "kpi"
    LATENCY = "latency"
    OPERATIONS = "operations"
    TIMELINE = "timeline"
    TIMESERIES = "timeseries"
    WORKFLOWS = "workflows"

    def __str__(self) -> str:
        return str(self.value)
