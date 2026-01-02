"""PropertyTypes for AWS::Greengrass::SubscriptionDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Subscription(PropertyType):
    id: str | None = None
    source: str | None = None
    subject: str | None = None
    target: str | None = None


@dataclass
class SubscriptionDefinitionVersion(PropertyType):
    subscriptions: list[Subscription] = field(default_factory=list)
