"""PropertyTypes for AWS::IoT::BillingGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BillingGroupProperties(PropertyType):
    billing_group_description: str | None = None
