"""PropertyTypes for AWS::Notifications::EventRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EventRuleStatusSummary(PropertyType):
    reason: str | None = None
    status: str | None = None
