"""PropertyTypes for AWS::BillingConductor::BillingGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccountGrouping(PropertyType):
    auto_associate: DslValue[bool] | None = None
    linked_account_ids: list[DslValue[str]] = field(default_factory=list)
    responsibility_transfer_arn: DslValue[str] | None = None


@dataclass
class ComputationPreference(PropertyType):
    pricing_plan_arn: DslValue[str] | None = None
