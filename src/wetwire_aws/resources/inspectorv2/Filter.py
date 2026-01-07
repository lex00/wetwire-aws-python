"""PropertyTypes for AWS::InspectorV2::Filter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DateFilter(PropertyType):
    end_inclusive: DslValue[int] | None = None
    start_inclusive: DslValue[int] | None = None


@dataclass
class FilterCriteria(PropertyType):
    aws_account_id: list[DslValue[StringFilter]] = field(default_factory=list)
    code_vulnerability_detector_name: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    code_vulnerability_detector_tags: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    code_vulnerability_file_path: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    component_id: list[DslValue[StringFilter]] = field(default_factory=list)
    component_type: list[DslValue[StringFilter]] = field(default_factory=list)
    ec2_instance_image_id: list[DslValue[StringFilter]] = field(default_factory=list)
    ec2_instance_subnet_id: list[DslValue[StringFilter]] = field(default_factory=list)
    ec2_instance_vpc_id: list[DslValue[StringFilter]] = field(default_factory=list)
    ecr_image_architecture: list[DslValue[StringFilter]] = field(default_factory=list)
    ecr_image_hash: list[DslValue[StringFilter]] = field(default_factory=list)
    ecr_image_pushed_at: list[DslValue[DateFilter]] = field(default_factory=list)
    ecr_image_registry: list[DslValue[StringFilter]] = field(default_factory=list)
    ecr_image_repository_name: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    ecr_image_tags: list[DslValue[StringFilter]] = field(default_factory=list)
    epss_score: list[DslValue[NumberFilter]] = field(default_factory=list)
    exploit_available: list[DslValue[StringFilter]] = field(default_factory=list)
    finding_arn: list[DslValue[StringFilter]] = field(default_factory=list)
    finding_status: list[DslValue[StringFilter]] = field(default_factory=list)
    finding_type: list[DslValue[StringFilter]] = field(default_factory=list)
    first_observed_at: list[DslValue[DateFilter]] = field(default_factory=list)
    fix_available: list[DslValue[StringFilter]] = field(default_factory=list)
    inspector_score: list[DslValue[NumberFilter]] = field(default_factory=list)
    lambda_function_execution_role_arn: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    lambda_function_last_modified_at: list[DslValue[DateFilter]] = field(
        default_factory=list
    )
    lambda_function_layers: list[DslValue[StringFilter]] = field(default_factory=list)
    lambda_function_name: list[DslValue[StringFilter]] = field(default_factory=list)
    lambda_function_runtime: list[DslValue[StringFilter]] = field(default_factory=list)
    last_observed_at: list[DslValue[DateFilter]] = field(default_factory=list)
    network_protocol: list[DslValue[StringFilter]] = field(default_factory=list)
    port_range: list[DslValue[PortRangeFilter]] = field(default_factory=list)
    related_vulnerabilities: list[DslValue[StringFilter]] = field(default_factory=list)
    resource_id: list[DslValue[StringFilter]] = field(default_factory=list)
    resource_tags: list[DslValue[MapFilter]] = field(default_factory=list)
    resource_type: list[DslValue[StringFilter]] = field(default_factory=list)
    severity: list[DslValue[StringFilter]] = field(default_factory=list)
    title: list[DslValue[StringFilter]] = field(default_factory=list)
    updated_at: list[DslValue[DateFilter]] = field(default_factory=list)
    vendor_severity: list[DslValue[StringFilter]] = field(default_factory=list)
    vulnerability_id: list[DslValue[StringFilter]] = field(default_factory=list)
    vulnerability_source: list[DslValue[StringFilter]] = field(default_factory=list)
    vulnerable_packages: list[DslValue[PackageFilter]] = field(default_factory=list)


@dataclass
class MapFilter(PropertyType):
    comparison: DslValue[str] | None = None
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class NumberFilter(PropertyType):
    lower_inclusive: DslValue[float] | None = None
    upper_inclusive: DslValue[float] | None = None


@dataclass
class PackageFilter(PropertyType):
    architecture: DslValue[StringFilter] | None = None
    epoch: DslValue[NumberFilter] | None = None
    file_path: DslValue[StringFilter] | None = None
    name: DslValue[StringFilter] | None = None
    release: DslValue[StringFilter] | None = None
    source_lambda_layer_arn: DslValue[StringFilter] | None = None
    source_layer_hash: DslValue[StringFilter] | None = None
    version: DslValue[StringFilter] | None = None


@dataclass
class PortRangeFilter(PropertyType):
    begin_inclusive: DslValue[int] | None = None
    end_inclusive: DslValue[int] | None = None


@dataclass
class StringFilter(PropertyType):
    comparison: DslValue[str] | None = None
    value: DslValue[str] | None = None
