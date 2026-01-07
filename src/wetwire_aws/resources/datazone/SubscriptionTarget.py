"""PropertyTypes for AWS::DataZone::SubscriptionTarget."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class SubscriptionTargetForm(PropertyType):
    content: DslValue[str] | None = None
    form_name: DslValue[str] | None = None
