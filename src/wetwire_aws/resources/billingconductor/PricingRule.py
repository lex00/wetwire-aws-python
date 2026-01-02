"""PropertyTypes for AWS::BillingConductor::PricingRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FreeTier(PropertyType):
    activated: bool | None = None


@dataclass
class Tiering(PropertyType):
    free_tier: FreeTier | None = None
