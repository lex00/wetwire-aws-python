"""PropertyTypes for AWS::BillingConductor::BillingGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccountGrouping(PropertyType):
    auto_associate: bool | None = None
    linked_account_ids: list[String] = field(default_factory=list)
    responsibility_transfer_arn: str | None = None


@dataclass
class ComputationPreference(PropertyType):
    pricing_plan_arn: str | None = None
