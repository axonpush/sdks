from enum import Enum


class GateRunSource(str, Enum):
    API = "api"
    CLI = "cli"
    UI = "ui"

    def __str__(self) -> str:
        return str(self.value)
