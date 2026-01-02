"""PropertyTypes for AWS::XRay::Group."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class InsightsConfiguration(PropertyType):
    insights_enabled: bool | None = None
    notifications_enabled: bool | None = None
