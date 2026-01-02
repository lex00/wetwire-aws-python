"""PropertyTypes for AWS::SES::VdmAttributes."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DashboardAttributes(PropertyType):
    engagement_metrics: str | None = None


@dataclass
class GuardianAttributes(PropertyType):
    optimized_shared_delivery: str | None = None
