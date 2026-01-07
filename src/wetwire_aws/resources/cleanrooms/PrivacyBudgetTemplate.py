"""PropertyTypes for AWS::CleanRooms::PrivacyBudgetTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BudgetParameter(PropertyType):
    budget: DslValue[int] | None = None
    type_: DslValue[str] | None = None
    auto_refresh: DslValue[str] | None = None


@dataclass
class Parameters(PropertyType):
    budget_parameters: list[DslValue[BudgetParameter]] = field(default_factory=list)
    epsilon: DslValue[int] | None = None
    resource_arn: DslValue[str] | None = None
    users_noise_per_query: DslValue[int] | None = None
