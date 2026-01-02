"""PropertyTypes for AWS::Batch::ComputeEnvironment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ComputeResources(PropertyType):
    maxv_cpus: int | None = None
    subnets: list[String] = field(default_factory=list)
    type_: str | None = None
    allocation_strategy: str | None = None
    bid_percentage: int | None = None
    desiredv_cpus: int | None = None
    ec2_configuration: list[Ec2ConfigurationObject] = field(default_factory=list)
    ec2_key_pair: str | None = None
    image_id: str | None = None
    instance_role: str | None = None
    instance_types: list[String] = field(default_factory=list)
    launch_template: LaunchTemplateSpecification | None = None
    minv_cpus: int | None = None
    placement_group: str | None = None
    security_group_ids: list[String] = field(default_factory=list)
    spot_iam_fleet_role: str | None = None
    tags: dict[str, String] = field(default_factory=dict)
    update_to_latest_image_version: bool | None = None


@dataclass
class Ec2ConfigurationObject(PropertyType):
    image_type: str | None = None
    image_id_override: str | None = None
    image_kubernetes_version: str | None = None


@dataclass
class EksConfiguration(PropertyType):
    eks_cluster_arn: str | None = None
    kubernetes_namespace: str | None = None


@dataclass
class LaunchTemplateSpecification(PropertyType):
    launch_template_id: str | None = None
    launch_template_name: str | None = None
    overrides: list[LaunchTemplateSpecificationOverride] = field(default_factory=list)
    userdata_type: str | None = None
    version: str | None = None


@dataclass
class LaunchTemplateSpecificationOverride(PropertyType):
    launch_template_id: str | None = None
    launch_template_name: str | None = None
    target_instance_types: list[String] = field(default_factory=list)
    userdata_type: str | None = None
    version: str | None = None


@dataclass
class UpdatePolicy(PropertyType):
    job_execution_timeout_minutes: int | None = None
    terminate_jobs_on_update: bool | None = None
