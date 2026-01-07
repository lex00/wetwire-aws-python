"""PropertyTypes for AWS::DevOpsGuru::NotificationChannel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class NotificationChannelConfig(PropertyType):
    filters: DslValue[NotificationFilterConfig] | None = None
    sns: DslValue[SnsChannelConfig] | None = None


@dataclass
class NotificationFilterConfig(PropertyType):
    message_types: list[DslValue[str]] = field(default_factory=list)
    severities: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SnsChannelConfig(PropertyType):
    topic_arn: DslValue[str] | None = None
