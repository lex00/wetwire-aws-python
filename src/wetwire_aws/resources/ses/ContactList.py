"""PropertyTypes for AWS::SES::ContactList."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Topic(PropertyType):
    default_subscription_status: str | None = None
    display_name: str | None = None
    topic_name: str | None = None
    description: str | None = None
