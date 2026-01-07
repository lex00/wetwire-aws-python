"""PropertyTypes for AWS::CloudFormation::StackSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoDeployment(PropertyType):
    depends_on: list[DslValue[str]] = field(default_factory=list)
    enabled: DslValue[bool] | None = None
    retain_stacks_on_account_removal: DslValue[bool] | None = None


@dataclass
class DeploymentTargets(PropertyType):
    account_filter_type: DslValue[str] | None = None
    accounts: list[DslValue[str]] = field(default_factory=list)
    accounts_url: DslValue[str] | None = None
    organizational_unit_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ManagedExecution(PropertyType):
    active: DslValue[bool] | None = None


@dataclass
class OperationPreferences(PropertyType):
    concurrency_mode: DslValue[str] | None = None
    failure_tolerance_count: DslValue[int] | None = None
    failure_tolerance_percentage: DslValue[int] | None = None
    max_concurrent_count: DslValue[int] | None = None
    max_concurrent_percentage: DslValue[int] | None = None
    region_concurrency_type: DslValue[str] | None = None
    region_order: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Parameter(PropertyType):
    parameter_key: DslValue[str] | None = None
    parameter_value: DslValue[str] | None = None


@dataclass
class StackInstances(PropertyType):
    deployment_targets: DslValue[DeploymentTargets] | None = None
    regions: list[DslValue[str]] = field(default_factory=list)
    parameter_overrides: list[DslValue[Parameter]] = field(default_factory=list)
