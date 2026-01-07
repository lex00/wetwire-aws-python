"""PropertyTypes for AWS::XRay::Group."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class InsightsConfiguration(PropertyType):
    insights_enabled: DslValue[bool] | None = None
    notifications_enabled: DslValue[bool] | None = None
