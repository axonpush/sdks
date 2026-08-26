from enum import Enum


class AnalyticsControllerBreakdownDimension(str, Enum):
    AGENT = "agent"
    ENVIRONMENT = "environment"
    MODEL = "model"
    PROMPT = "prompt"
    PROMPT_VERSION = "prompt_version"
    PROVIDER = "provider"
    RELEASE = "release"
    SEMANTIC_KIND = "semantic_kind"
    SERVICE = "service"
    STATUS = "status"
    TOOL = "tool"

    def __str__(self) -> str:
        return str(self.value)
