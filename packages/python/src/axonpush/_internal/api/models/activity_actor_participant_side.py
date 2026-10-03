from enum import Enum


class ActivityActorParticipantSide(str, Enum):
    CANDIDATE = "candidate"
    COMPANY = "company"
    RECRUITER = "recruiter"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
