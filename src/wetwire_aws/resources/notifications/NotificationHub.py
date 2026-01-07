"""PropertyTypes for AWS::Notifications::NotificationHub."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class NotificationHubStatusSummary(PropertyType):
    notification_hub_status: DslValue[str] | None = None
    notification_hub_status_reason: DslValue[str] | None = None
