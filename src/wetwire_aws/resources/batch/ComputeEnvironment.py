"""PropertyTypes for AWS::Batch::ComputeEnvironment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ComputeResources(PropertyType):
    maxv_cpus: DslValue[int] | None = None
    subnets: list[DslValue[str]] = field(default_factory=list)
    type_: DslValue[str] | None = None
    allocation_strategy: DslValue[str] | None = None
    bid_percentage: DslValue[int] | None = None
    desiredv_cpus: DslValue[int] | None = None
    ec2_configuration: list[DslValue[Ec2ConfigurationObject]] = field(
        default_factory=list
    )
    ec2_key_pair: DslValue[str] | None = None
    image_id: DslValue[str] | None = None
    instance_role: DslValue[str] | None = None
    instance_types: list[DslValue[str]] = field(default_factory=list)
    launch_template: DslValue[LaunchTemplateSpecification] | None = None
    minv_cpus: DslValue[int] | None = None
    placement_group: DslValue[str] | None = None
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    spot_iam_fleet_role: DslValue[str] | None = None
    tags: dict[str, DslValue[str]] = field(default_factory=dict)
    update_to_latest_image_version: DslValue[bool] | None = None


@dataclass
class Ec2ConfigurationObject(PropertyType):
    image_type: DslValue[str] | None = None
    image_id_override: DslValue[str] | None = None
    image_kubernetes_version: DslValue[str] | None = None


@dataclass
class EksConfiguration(PropertyType):
    eks_cluster_arn: DslValue[str] | None = None
    kubernetes_namespace: DslValue[str] | None = None


@dataclass
class LaunchTemplateSpecification(PropertyType):
    launch_template_id: DslValue[str] | None = None
    launch_template_name: DslValue[str] | None = None
    overrides: list[DslValue[LaunchTemplateSpecificationOverride]] = field(
        default_factory=list
    )
    userdata_type: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class LaunchTemplateSpecificationOverride(PropertyType):
    launch_template_id: DslValue[str] | None = None
    launch_template_name: DslValue[str] | None = None
    target_instance_types: list[DslValue[str]] = field(default_factory=list)
    userdata_type: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class UpdatePolicy(PropertyType):
    job_execution_timeout_minutes: DslValue[int] | None = None
    terminate_jobs_on_update: DslValue[bool] | None = None
