from enum import Enum


class AnalyticsBreakdownDimension(str, Enum):
    AGENT = "agent"
    APIKEY = "apiKey"
    APP = "app"
    CHANNEL = "channel"
    ERRORTYPE = "errorType"
    EVENTTYPE = "eventType"
    FINISHREASON = "finishReason"
    MODEL = "model"
    OPERATION = "operation"
    PROVIDER = "provider"
    SEMANTICKIND = "semanticKind"
    SERVICE = "service"
    SOURCE = "source"
    STATUS = "status"
    TAG = "tag"
    TOOL = "tool"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
