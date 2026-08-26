from enum import Enum


class LicenseStatus(str, Enum):
    ACTIVE = "active"
    GRACE = "grace"
    STOPPED = "stopped"
    UNLICENSED = "unlicensed"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
