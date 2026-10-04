from enum import Enum


class ActivityAttributeRole(str, Enum):
    ACTOR_SIDE = "actor_side"
    AVATAR = "avatar"
    CLIENT = "client"
    CLIENT_CONFIDENCE = "client_confidence"
    CONNECTION = "connection"
    DISPLAY_NAME = "display_name"
    DISPLAY_SUBTITLE = "display_subtitle"
    DURATION = "duration"
    EVIDENCE = "evidence"
    EXPECTED_DURATION = "expected_duration"
    LAST_ACTION = "last_action"
    NEXT_ACTOR = "next_actor"
    NOISE = "noise"
    OUTCOME = "outcome"
    STATE = "state"
    WAIT_REASON = "wait_reason"

    def __str__(self) -> str:
        return str(self.value)
