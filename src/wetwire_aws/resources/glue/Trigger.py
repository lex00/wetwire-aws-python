"""PropertyTypes for AWS::Glue::Trigger."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    arguments: DslValue[dict[str, Any]] | None = None
    crawler_name: DslValue[str] | None = None
    job_name: DslValue[str] | None = None
    notification_property: DslValue[NotificationProperty] | None = None
    security_configuration: DslValue[str] | None = None
    timeout: DslValue[int] | None = None


@dataclass
class Condition(PropertyType):
    crawl_state: DslValue[str] | None = None
    crawler_name: DslValue[str] | None = None
    job_name: DslValue[str] | None = None
    logical_operator: DslValue[str] | None = None
    state: DslValue[str] | None = None


@dataclass
class EventBatchingCondition(PropertyType):
    batch_size: DslValue[int] | None = None
    batch_window: DslValue[int] | None = None


@dataclass
class NotificationProperty(PropertyType):
    notify_delay_after: DslValue[int] | None = None


@dataclass
class Predicate(PropertyType):
    conditions: list[DslValue[Condition]] = field(default_factory=list)
    logical: DslValue[str] | None = None
