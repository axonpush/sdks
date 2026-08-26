from enum import Enum


class DeploymentMode(str, Enum):
    CLOUD = "cloud"
    SELFHOST = "selfhost"

    def __str__(self) -> str:
        return str(self.value)
