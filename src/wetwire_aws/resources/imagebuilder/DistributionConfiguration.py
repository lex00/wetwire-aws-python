"""PropertyTypes for AWS::ImageBuilder::DistributionConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AmiDistributionConfiguration(PropertyType):
    ami_tags: dict[str, DslValue[str]] = field(default_factory=dict)
    description: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None
    launch_permission_configuration: DslValue[LaunchPermissionConfiguration] | None = (
        None
    )
    name: DslValue[str] | None = None
    target_account_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ContainerDistributionConfiguration(PropertyType):
    container_tags: list[DslValue[str]] = field(default_factory=list)
    description: DslValue[str] | None = None
    target_repository: DslValue[TargetContainerRepository] | None = None


@dataclass
class Distribution(PropertyType):
    region: DslValue[str] | None = None
    ami_distribution_configuration: DslValue[AmiDistributionConfiguration] | None = None
    container_distribution_configuration: (
        DslValue[ContainerDistributionConfiguration] | None
    ) = None
    fast_launch_configurations: list[DslValue[FastLaunchConfiguration]] = field(
        default_factory=list
    )
    launch_template_configurations: list[DslValue[LaunchTemplateConfiguration]] = field(
        default_factory=list
    )
    license_configuration_arns: list[DslValue[str]] = field(default_factory=list)
    ssm_parameter_configurations: list[DslValue[SsmParameterConfiguration]] = field(
        default_factory=list
    )


@dataclass
class FastLaunchConfiguration(PropertyType):
    account_id: DslValue[str] | None = None
    enabled: DslValue[bool] | None = None
    launch_template: DslValue[FastLaunchLaunchTemplateSpecification] | None = None
    max_parallel_launches: DslValue[int] | None = None
    snapshot_configuration: DslValue[FastLaunchSnapshotConfiguration] | None = None


@dataclass
class FastLaunchLaunchTemplateSpecification(PropertyType):
    launch_template_id: DslValue[str] | None = None
    launch_template_name: DslValue[str] | None = None
    launch_template_version: DslValue[str] | None = None


@dataclass
class FastLaunchSnapshotConfiguration(PropertyType):
    target_resource_count: DslValue[int] | None = None


@dataclass
class LaunchPermissionConfiguration(PropertyType):
    organization_arns: list[DslValue[str]] = field(default_factory=list)
    organizational_unit_arns: list[DslValue[str]] = field(default_factory=list)
    user_groups: list[DslValue[str]] = field(default_factory=list)
    user_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class LaunchTemplateConfiguration(PropertyType):
    account_id: DslValue[str] | None = None
    launch_template_id: DslValue[str] | None = None
    set_default_version: DslValue[bool] | None = None


@dataclass
class SsmParameterConfiguration(PropertyType):
    parameter_name: DslValue[str] | None = None
    ami_account_id: DslValue[str] | None = None
    data_type: DslValue[str] | None = None


@dataclass
class TargetContainerRepository(PropertyType):
    repository_name: DslValue[str] | None = None
    service: DslValue[str] | None = None
