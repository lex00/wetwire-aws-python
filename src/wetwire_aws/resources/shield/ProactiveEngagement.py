"""PropertyTypes for AWS::Shield::ProactiveEngagement."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EmergencyContact(PropertyType):
    email_address: str | None = None
    contact_notes: str | None = None
    phone_number: str | None = None
