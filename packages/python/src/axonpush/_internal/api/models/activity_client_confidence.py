from enum import Enum


class ActivityClientConfidence(str, Enum):
    AUTHENTICATED_REGISTRATION_UNVERIFIED_VENDOR = "authenticated_registration_unverified_vendor"
    INFERRED = "inferred"
    SELF_REPORTED = "self_reported"
    UNKNOWN = "unknown"
    VERIFIED_REGISTRATION = "verified_registration"

    def __str__(self) -> str:
        return str(self.value)
