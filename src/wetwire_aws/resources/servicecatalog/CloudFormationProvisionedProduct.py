"""PropertyTypes for AWS::ServiceCatalog::CloudFormationProvisionedProduct."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ProvisioningParameter(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ProvisioningPreferences(PropertyType):
    stack_set_accounts: list[DslValue[str]] = field(default_factory=list)
    stack_set_failure_tolerance_count: DslValue[int] | None = None
    stack_set_failure_tolerance_percentage: DslValue[int] | None = None
    stack_set_max_concurrency_count: DslValue[int] | None = None
    stack_set_max_concurrency_percentage: DslValue[int] | None = None
    stack_set_operation_type: DslValue[str] | None = None
    stack_set_regions: list[DslValue[str]] = field(default_factory=list)
