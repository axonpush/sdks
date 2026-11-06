from enum import IntEnum


class LedgerPolicyUpdateDays(IntEnum):
    VALUE_30 = 30
    VALUE_180 = 180
    VALUE_365 = 365
    VALUE_2555 = 2555

    def __str__(self) -> str:
        return str(self.value)
