from enum import Enum


class GovernPolicyBodyEnforcement(str, Enum):
    BLOCK = "block"
    ENFORCE = "enforce"
    VALUE_3 = ""
    WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
