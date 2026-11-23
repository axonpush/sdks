from enum import Enum


class ActionDecisionDecision(str, Enum):
    APPROVE = "approve"
    CORRECT = "correct"
    RECHECK = "recheck"
    REJECT = "reject"

    def __str__(self) -> str:
        return str(self.value)
