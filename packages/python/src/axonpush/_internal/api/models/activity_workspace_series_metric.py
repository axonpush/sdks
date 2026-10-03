from enum import Enum


class ActivityWorkspaceSeriesMetric(str, Enum):
    FUNNEL = "funnel"
    LAG = "lag"
    OUTCOMES = "outcomes"

    def __str__(self) -> str:
        return str(self.value)
