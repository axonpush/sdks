from enum import Enum


class CreateInputBody1Metric(str, Enum):
    COST_USD = "cost_usd"
    ERROR_COUNT = "error_count"
    ERROR_RATE = "error_rate"
    LATENCY_MS = "latency_ms"
    LIFECYCLE_OPEN = "lifecycle_open"

    def __str__(self) -> str:
        return str(self.value)
