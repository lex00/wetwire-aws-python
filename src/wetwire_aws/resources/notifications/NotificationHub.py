"""PropertyTypes for AWS::Notifications::NotificationHub."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class NotificationHubStatusSummary(PropertyType):
    notification_hub_status: str | None = None
    notification_hub_status_reason: str | None = None
