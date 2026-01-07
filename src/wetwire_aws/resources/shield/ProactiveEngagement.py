"""PropertyTypes for AWS::Shield::ProactiveEngagement."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EmergencyContact(PropertyType):
    email_address: DslValue[str] | None = None
    contact_notes: DslValue[str] | None = None
    phone_number: DslValue[str] | None = None
