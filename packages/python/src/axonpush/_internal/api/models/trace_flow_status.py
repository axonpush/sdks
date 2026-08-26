from enum import Enum


class TraceFlowStatus(str, Enum):
    CONSENT_REQUIRED = "consent_required"
    FAILED = "failed"
    INSUFFICIENT_COHORT = "insufficient_cohort"
    PROCESSING = "processing"
    PROVIDER_NOT_CONFIGURED = "provider_not_configured"
    READY = "ready"

    def __str__(self) -> str:
        return str(self.value)
