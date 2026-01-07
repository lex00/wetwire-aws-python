"""PropertyTypes for AWS::Greengrass::SubscriptionDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Subscription(PropertyType):
    id: DslValue[str] | None = None
    source: DslValue[str] | None = None
    subject: DslValue[str] | None = None
    target: DslValue[str] | None = None


@dataclass
class SubscriptionDefinitionVersion(PropertyType):
    subscriptions: list[DslValue[Subscription]] = field(default_factory=list)
