"""PropertyTypes for AWS::Greengrass::SubscriptionDefinitionVersion."""

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
