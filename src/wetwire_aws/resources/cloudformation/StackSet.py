"""PropertyTypes for AWS::CloudFormation::StackSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoDeployment(PropertyType):
    depends_on: list[String] = field(default_factory=list)
    enabled: bool | None = None
    retain_stacks_on_account_removal: bool | None = None


@dataclass
class DeploymentTargets(PropertyType):
    account_filter_type: str | None = None
    accounts: list[String] = field(default_factory=list)
    accounts_url: str | None = None
    organizational_unit_ids: list[String] = field(default_factory=list)


@dataclass
class ManagedExecution(PropertyType):
    active: bool | None = None


@dataclass
class OperationPreferences(PropertyType):
    concurrency_mode: str | None = None
    failure_tolerance_count: int | None = None
    failure_tolerance_percentage: int | None = None
    max_concurrent_count: int | None = None
    max_concurrent_percentage: int | None = None
    region_concurrency_type: str | None = None
    region_order: list[String] = field(default_factory=list)


@dataclass
class Parameter(PropertyType):
    parameter_key: str | None = None
    parameter_value: str | None = None


@dataclass
class StackInstances(PropertyType):
    deployment_targets: DeploymentTargets | None = None
    regions: list[String] = field(default_factory=list)
    parameter_overrides: list[Parameter] = field(default_factory=list)
