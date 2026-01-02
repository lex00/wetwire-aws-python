"""PropertyTypes for AWS::InspectorV2::Filter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DateFilter(PropertyType):
    end_inclusive: int | None = None
    start_inclusive: int | None = None


@dataclass
class FilterCriteria(PropertyType):
    aws_account_id: list[StringFilter] = field(default_factory=list)
    code_vulnerability_detector_name: list[StringFilter] = field(default_factory=list)
    code_vulnerability_detector_tags: list[StringFilter] = field(default_factory=list)
    code_vulnerability_file_path: list[StringFilter] = field(default_factory=list)
    component_id: list[StringFilter] = field(default_factory=list)
    component_type: list[StringFilter] = field(default_factory=list)
    ec2_instance_image_id: list[StringFilter] = field(default_factory=list)
    ec2_instance_subnet_id: list[StringFilter] = field(default_factory=list)
    ec2_instance_vpc_id: list[StringFilter] = field(default_factory=list)
    ecr_image_architecture: list[StringFilter] = field(default_factory=list)
    ecr_image_hash: list[StringFilter] = field(default_factory=list)
    ecr_image_pushed_at: list[DateFilter] = field(default_factory=list)
    ecr_image_registry: list[StringFilter] = field(default_factory=list)
    ecr_image_repository_name: list[StringFilter] = field(default_factory=list)
    ecr_image_tags: list[StringFilter] = field(default_factory=list)
    epss_score: list[NumberFilter] = field(default_factory=list)
    exploit_available: list[StringFilter] = field(default_factory=list)
    finding_arn: list[StringFilter] = field(default_factory=list)
    finding_status: list[StringFilter] = field(default_factory=list)
    finding_type: list[StringFilter] = field(default_factory=list)
    first_observed_at: list[DateFilter] = field(default_factory=list)
    fix_available: list[StringFilter] = field(default_factory=list)
    inspector_score: list[NumberFilter] = field(default_factory=list)
    lambda_function_execution_role_arn: list[StringFilter] = field(default_factory=list)
    lambda_function_last_modified_at: list[DateFilter] = field(default_factory=list)
    lambda_function_layers: list[StringFilter] = field(default_factory=list)
    lambda_function_name: list[StringFilter] = field(default_factory=list)
    lambda_function_runtime: list[StringFilter] = field(default_factory=list)
    last_observed_at: list[DateFilter] = field(default_factory=list)
    network_protocol: list[StringFilter] = field(default_factory=list)
    port_range: list[PortRangeFilter] = field(default_factory=list)
    related_vulnerabilities: list[StringFilter] = field(default_factory=list)
    resource_id: list[StringFilter] = field(default_factory=list)
    resource_tags: list[MapFilter] = field(default_factory=list)
    resource_type: list[StringFilter] = field(default_factory=list)
    severity: list[StringFilter] = field(default_factory=list)
    title: list[StringFilter] = field(default_factory=list)
    updated_at: list[DateFilter] = field(default_factory=list)
    vendor_severity: list[StringFilter] = field(default_factory=list)
    vulnerability_id: list[StringFilter] = field(default_factory=list)
    vulnerability_source: list[StringFilter] = field(default_factory=list)
    vulnerable_packages: list[PackageFilter] = field(default_factory=list)


@dataclass
class MapFilter(PropertyType):
    comparison: str | None = None
    key: str | None = None
    value: str | None = None


@dataclass
class NumberFilter(PropertyType):
    lower_inclusive: float | None = None
    upper_inclusive: float | None = None


@dataclass
class PackageFilter(PropertyType):
    architecture: StringFilter | None = None
    epoch: NumberFilter | None = None
    file_path: StringFilter | None = None
    name: StringFilter | None = None
    release: StringFilter | None = None
    source_lambda_layer_arn: StringFilter | None = None
    source_layer_hash: StringFilter | None = None
    version: StringFilter | None = None


@dataclass
class PortRangeFilter(PropertyType):
    begin_inclusive: int | None = None
    end_inclusive: int | None = None


@dataclass
class StringFilter(PropertyType):
    comparison: str | None = None
    value: str | None = None
