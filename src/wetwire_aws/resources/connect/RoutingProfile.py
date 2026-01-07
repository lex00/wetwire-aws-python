"""PropertyTypes for AWS::Connect::RoutingProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CrossChannelBehavior(PropertyType):
    behavior_type: DslValue[str] | None = None


@dataclass
class MediaConcurrency(PropertyType):
    channel: DslValue[str] | None = None
    concurrency: DslValue[int] | None = None
    cross_channel_behavior: DslValue[CrossChannelBehavior] | None = None


@dataclass
class RoutingProfileManualAssignmentQueueConfig(PropertyType):
    queue_reference: DslValue[RoutingProfileQueueReference] | None = None


@dataclass
class RoutingProfileQueueConfig(PropertyType):
    delay: DslValue[int] | None = None
    priority: DslValue[int] | None = None
    queue_reference: DslValue[RoutingProfileQueueReference] | None = None


@dataclass
class RoutingProfileQueueReference(PropertyType):
    channel: DslValue[str] | None = None
    queue_arn: DslValue[str] | None = None
