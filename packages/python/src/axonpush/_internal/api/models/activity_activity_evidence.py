from enum import Enum


class ActivityActivityEvidence(str, Enum):
    AGENT_REPORTED = "agent_reported"
    DERIVED = "derived"
    RECONSTRUCTED = "reconstructed"
    SERVER_OBSERVED = "server_observed"

    def __str__(self) -> str:
        return str(self.value)
