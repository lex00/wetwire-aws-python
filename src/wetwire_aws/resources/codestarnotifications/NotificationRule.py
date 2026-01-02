"""PropertyTypes for AWS::CodeStarNotifications::NotificationRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Target(PropertyType):
    target_address: str | None = None
    target_type: str | None = None
