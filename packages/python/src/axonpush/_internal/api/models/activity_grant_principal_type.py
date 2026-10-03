from enum import Enum


class ActivityGrantPrincipalType(str, Enum):
    APIKEY = "apikey"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
