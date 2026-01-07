"""PropertyTypes for AWS::BillingConductor::PricingRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FreeTier(PropertyType):
    activated: DslValue[bool] | None = None


@dataclass
class Tiering(PropertyType):
    free_tier: DslValue[FreeTier] | None = None
