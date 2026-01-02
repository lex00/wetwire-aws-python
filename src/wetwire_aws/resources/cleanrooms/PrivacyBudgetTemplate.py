"""PropertyTypes for AWS::CleanRooms::PrivacyBudgetTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BudgetParameter(PropertyType):
    budget: int | None = None
    type_: str | None = None
    auto_refresh: str | None = None


@dataclass
class Parameters(PropertyType):
    budget_parameters: list[BudgetParameter] = field(default_factory=list)
    epsilon: int | None = None
    resource_arn: str | None = None
    users_noise_per_query: int | None = None
