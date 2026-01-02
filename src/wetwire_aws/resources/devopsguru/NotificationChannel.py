"""PropertyTypes for AWS::DevOpsGuru::NotificationChannel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class NotificationChannelConfig(PropertyType):
    filters: NotificationFilterConfig | None = None
    sns: SnsChannelConfig | None = None


@dataclass
class NotificationFilterConfig(PropertyType):
    message_types: list[String] = field(default_factory=list)
    severities: list[String] = field(default_factory=list)


@dataclass
class SnsChannelConfig(PropertyType):
    topic_arn: str | None = None
