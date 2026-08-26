from enum import Enum


class AlertMetric(str, Enum):
    COST_USD = "cost_usd"
    ERROR_COUNT = "error_count"
    ERROR_RATE = "error_rate"
    LATENCY_MS = "latency_ms"
    SCORE = "score"

    def __str__(self) -> str:
        return str(self.value)
