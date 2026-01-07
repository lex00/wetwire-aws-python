"""PropertyTypes for AWS::CodeStarNotifications::NotificationRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Target(PropertyType):
    target_address: DslValue[str] | None = None
    target_type: DslValue[str] | None = None
