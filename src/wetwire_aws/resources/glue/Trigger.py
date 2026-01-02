"""PropertyTypes for AWS::Glue::Trigger."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    arguments: dict[str, Any] | None = None
    crawler_name: str | None = None
    job_name: str | None = None
    notification_property: NotificationProperty | None = None
    security_configuration: str | None = None
    timeout: int | None = None


@dataclass
class Condition(PropertyType):
    crawl_state: str | None = None
    crawler_name: str | None = None
    job_name: str | None = None
    logical_operator: str | None = None
    state: str | None = None


@dataclass
class EventBatchingCondition(PropertyType):
    batch_size: int | None = None
    batch_window: int | None = None


@dataclass
class NotificationProperty(PropertyType):
    notify_delay_after: int | None = None


@dataclass
class Predicate(PropertyType):
    conditions: list[Condition] = field(default_factory=list)
    logical: str | None = None
