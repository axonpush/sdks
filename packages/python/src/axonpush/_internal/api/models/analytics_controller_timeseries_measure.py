from enum import Enum


class AnalyticsControllerTimeseriesMeasure(str, Enum):
    COST = "cost"
    ERRORS = "errors"
    LATENCY_AVG = "latency_avg"
    LATENCY_P50 = "latency_p50"
    LATENCY_P95 = "latency_p95"
    LATENCY_P99 = "latency_p99"
    SCORE = "score"
    SUCCESS_RATE = "success_rate"
    TOKENS = "tokens"
    TRACES = "traces"

    def __str__(self) -> str:
        return str(self.value)
