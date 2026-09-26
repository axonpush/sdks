from enum import Enum


class PatchErrorInputBodyAction(str, Enum):
    ASSIGN = "assign"
    IGNORE = "ignore"
    MUTE = "mute"
    RESOLVE = "resolve"
    UNRESOLVE = "unresolve"

    def __str__(self) -> str:
        return str(self.value)
