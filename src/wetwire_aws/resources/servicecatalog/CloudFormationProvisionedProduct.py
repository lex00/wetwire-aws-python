"""PropertyTypes for AWS::ServiceCatalog::CloudFormationProvisionedProduct."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ProvisioningParameter(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class ProvisioningPreferences(PropertyType):
    stack_set_accounts: list[String] = field(default_factory=list)
    stack_set_failure_tolerance_count: int | None = None
    stack_set_failure_tolerance_percentage: int | None = None
    stack_set_max_concurrency_count: int | None = None
    stack_set_max_concurrency_percentage: int | None = None
    stack_set_operation_type: str | None = None
    stack_set_regions: list[String] = field(default_factory=list)
