from enum import Enum


class UpdateInputBodyMetric(str, Enum):
    COST_USD = "cost_usd"
    CRASH_FREE_RATE = "crash_free_rate"
    ERROR_COUNT = "error_count"
    ERROR_RATE = "error_rate"
    LATENCY_MS = "latency_ms"
    LIFECYCLE_OPEN = "lifecycle_open"
    MONITOR_FAILED = "monitor_failed"

    def __str__(self) -> str:
        return str(self.value)
