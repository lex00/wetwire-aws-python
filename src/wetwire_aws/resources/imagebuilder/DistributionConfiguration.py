"""PropertyTypes for AWS::ImageBuilder::DistributionConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AmiDistributionConfiguration(PropertyType):
    ami_tags: dict[str, String] = field(default_factory=dict)
    description: str | None = None
    kms_key_id: str | None = None
    launch_permission_configuration: LaunchPermissionConfiguration | None = None
    name: str | None = None
    target_account_ids: list[String] = field(default_factory=list)


@dataclass
class ContainerDistributionConfiguration(PropertyType):
    container_tags: list[String] = field(default_factory=list)
    description: str | None = None
    target_repository: TargetContainerRepository | None = None


@dataclass
class Distribution(PropertyType):
    region: str | None = None
    ami_distribution_configuration: AmiDistributionConfiguration | None = None
    container_distribution_configuration: ContainerDistributionConfiguration | None = (
        None
    )
    fast_launch_configurations: list[FastLaunchConfiguration] = field(
        default_factory=list
    )
    launch_template_configurations: list[LaunchTemplateConfiguration] = field(
        default_factory=list
    )
    license_configuration_arns: list[String] = field(default_factory=list)
    ssm_parameter_configurations: list[SsmParameterConfiguration] = field(
        default_factory=list
    )


@dataclass
class FastLaunchConfiguration(PropertyType):
    account_id: str | None = None
    enabled: bool | None = None
    launch_template: FastLaunchLaunchTemplateSpecification | None = None
    max_parallel_launches: int | None = None
    snapshot_configuration: FastLaunchSnapshotConfiguration | None = None


@dataclass
class FastLaunchLaunchTemplateSpecification(PropertyType):
    launch_template_id: str | None = None
    launch_template_name: str | None = None
    launch_template_version: str | None = None


@dataclass
class FastLaunchSnapshotConfiguration(PropertyType):
    target_resource_count: int | None = None


@dataclass
class LaunchPermissionConfiguration(PropertyType):
    organization_arns: list[String] = field(default_factory=list)
    organizational_unit_arns: list[String] = field(default_factory=list)
    user_groups: list[String] = field(default_factory=list)
    user_ids: list[String] = field(default_factory=list)


@dataclass
class LaunchTemplateConfiguration(PropertyType):
    account_id: str | None = None
    launch_template_id: str | None = None
    set_default_version: bool | None = None


@dataclass
class SsmParameterConfiguration(PropertyType):
    parameter_name: str | None = None
    ami_account_id: str | None = None
    data_type: str | None = None


@dataclass
class TargetContainerRepository(PropertyType):
    repository_name: str | None = None
    service: str | None = None
