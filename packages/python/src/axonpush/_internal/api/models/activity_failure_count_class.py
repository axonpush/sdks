from enum import Enum


class ActivityFailureCountClass(str, Enum):
    EXPECTED_CHALLENGE = "expected_challenge"
    REJECTED = "rejected"
    SERVICE_ERROR = "service_error"
    UNCLASSIFIED = "unclassified"

    def __str__(self) -> str:
        return str(self.value)
