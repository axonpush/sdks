from enum import Enum


class LedgerPolicyUpdateLockMode(str, Enum):
    COMPLIANCE = "COMPLIANCE"
    GOVERNANCE = "GOVERNANCE"

    def __str__(self) -> str:
        return str(self.value)
