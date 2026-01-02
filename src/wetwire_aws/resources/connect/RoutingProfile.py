"""PropertyTypes for AWS::Connect::RoutingProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CrossChannelBehavior(PropertyType):
    behavior_type: str | None = None


@dataclass
class MediaConcurrency(PropertyType):
    channel: str | None = None
    concurrency: int | None = None
    cross_channel_behavior: CrossChannelBehavior | None = None


@dataclass
class RoutingProfileManualAssignmentQueueConfig(PropertyType):
    queue_reference: RoutingProfileQueueReference | None = None


@dataclass
class RoutingProfileQueueConfig(PropertyType):
    delay: int | None = None
    priority: int | None = None
    queue_reference: RoutingProfileQueueReference | None = None


@dataclass
class RoutingProfileQueueReference(PropertyType):
    channel: str | None = None
    queue_arn: str | None = None
