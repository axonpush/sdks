from enum import Enum


class ApiKeyScope(str, Enum):
    ACTIONSREAD = "actions:read"
    ACTIONSVERIFY = "actions:verify"
    ACTIONSWRITE = "actions:write"
    ACTION_CONTRACTSMANAGE = "action-contracts:manage"
    ALERTSMANAGE = "alerts:manage"
    ANALYTICSREAD = "analytics:read"
    APPSMANAGE = "apps:manage"
    ASSESSMENTSWRITE = "assessments:write"
    CHANNELSMANAGE = "channels:manage"
    EVALUATIONSMANAGE = "evaluations:manage"
    EVENTSREAD = "events:read"
    INTELLIGENCEMANAGE = "intelligence:manage"
    PROMPTSMANAGE = "prompts:manage"
    PUBLISH = "publish"
    SUBSCRIBE = "subscribe"
    TRACESREAD = "traces:read"
    WEBHOOKSMANAGE = "webhooks:manage"

    def __str__(self) -> str:
        return str(self.value)
