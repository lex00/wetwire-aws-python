"""PropertyTypes for AWS::DataZone::SubscriptionTarget."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SubscriptionTargetForm(PropertyType):
    content: str | None = None
    form_name: str | None = None
