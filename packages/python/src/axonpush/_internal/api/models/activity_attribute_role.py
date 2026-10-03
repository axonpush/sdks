from enum import Enum


class ActivityAttributeRole(str, Enum):
    ACTOR_SIDE = "actor_side"
    AVATAR = "avatar"
    CLIENT = "client"
    CLIENT_CONFIDENCE = "client_confidence"
    DISPLAY_NAME = "display_name"
    DISPLAY_SUBTITLE = "display_subtitle"
    DURATION = "duration"
    EVIDENCE = "evidence"
    EXPECTED_DURATION = "expected_duration"
    NEXT_ACTOR = "next_actor"
    OUTCOME = "outcome"
    STATE = "state"
    WAIT_REASON = "wait_reason"

    def __str__(self) -> str:
        return str(self.value)
