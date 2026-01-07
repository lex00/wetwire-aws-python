"""PropertyTypes for AWS::Notifications::EventRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EventRuleStatusSummary(PropertyType):
    reason: DslValue[str] | None = None
    status: DslValue[str] | None = None
