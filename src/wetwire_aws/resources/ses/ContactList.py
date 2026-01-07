"""PropertyTypes for AWS::SES::ContactList."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Topic(PropertyType):
    default_subscription_status: DslValue[str] | None = None
    display_name: DslValue[str] | None = None
    topic_name: DslValue[str] | None = None
    description: DslValue[str] | None = None
