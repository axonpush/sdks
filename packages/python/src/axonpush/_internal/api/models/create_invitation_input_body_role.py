from enum import Enum


class CreateInvitationInputBodyRole(str, Enum):
    ADMIN = "admin"
    OWNER = "owner"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
