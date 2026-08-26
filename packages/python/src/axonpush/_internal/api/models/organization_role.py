from enum import Enum


class OrganizationRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
