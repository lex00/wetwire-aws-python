"""PropertyTypes for AWS::SecurityHub::Insight."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AwsSecurityFindingFilters(PropertyType):
    aws_account_id: list[DslValue[StringFilter]] = field(default_factory=list)
    aws_account_name: list[DslValue[StringFilter]] = field(default_factory=list)
    company_name: list[DslValue[StringFilter]] = field(default_factory=list)
    compliance_associated_standards_id: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    compliance_security_control_id: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    compliance_security_control_parameters_name: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    compliance_security_control_parameters_value: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    compliance_status: list[DslValue[StringFilter]] = field(default_factory=list)
    confidence: list[DslValue[NumberFilter]] = field(default_factory=list)
    created_at: list[DslValue[DateFilter]] = field(default_factory=list)
    criticality: list[DslValue[NumberFilter]] = field(default_factory=list)
    description: list[DslValue[StringFilter]] = field(default_factory=list)
    finding_provider_fields_confidence: list[DslValue[NumberFilter]] = field(
        default_factory=list
    )
    finding_provider_fields_criticality: list[DslValue[NumberFilter]] = field(
        default_factory=list
    )
    finding_provider_fields_related_findings_id: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    finding_provider_fields_related_findings_product_arn: list[
        DslValue[StringFilter]
    ] = field(default_factory=list)
    finding_provider_fields_severity_label: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    finding_provider_fields_severity_original: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    finding_provider_fields_types: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    first_observed_at: list[DslValue[DateFilter]] = field(default_factory=list)
    generator_id: list[DslValue[StringFilter]] = field(default_factory=list)
    id: list[DslValue[StringFilter]] = field(default_factory=list)
    last_observed_at: list[DslValue[DateFilter]] = field(default_factory=list)
    malware_name: list[DslValue[StringFilter]] = field(default_factory=list)
    malware_path: list[DslValue[StringFilter]] = field(default_factory=list)
    malware_state: list[DslValue[StringFilter]] = field(default_factory=list)
    malware_type: list[DslValue[StringFilter]] = field(default_factory=list)
    network_destination_domain: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    network_destination_ip_v4: list[DslValue[IpFilter]] = field(default_factory=list)
    network_destination_ip_v6: list[DslValue[IpFilter]] = field(default_factory=list)
    network_destination_port: list[DslValue[NumberFilter]] = field(default_factory=list)
    network_direction: list[DslValue[StringFilter]] = field(default_factory=list)
    network_protocol: list[DslValue[StringFilter]] = field(default_factory=list)
    network_source_domain: list[DslValue[StringFilter]] = field(default_factory=list)
    network_source_ip_v4: list[DslValue[IpFilter]] = field(default_factory=list)
    network_source_ip_v6: list[DslValue[IpFilter]] = field(default_factory=list)
    network_source_mac: list[DslValue[StringFilter]] = field(default_factory=list)
    network_source_port: list[DslValue[NumberFilter]] = field(default_factory=list)
    note_text: list[DslValue[StringFilter]] = field(default_factory=list)
    note_updated_at: list[DslValue[DateFilter]] = field(default_factory=list)
    note_updated_by: list[DslValue[StringFilter]] = field(default_factory=list)
    process_launched_at: list[DslValue[DateFilter]] = field(default_factory=list)
    process_name: list[DslValue[StringFilter]] = field(default_factory=list)
    process_parent_pid: list[DslValue[NumberFilter]] = field(default_factory=list)
    process_path: list[DslValue[StringFilter]] = field(default_factory=list)
    process_pid: list[DslValue[NumberFilter]] = field(default_factory=list)
    process_terminated_at: list[DslValue[DateFilter]] = field(default_factory=list)
    product_arn: list[DslValue[StringFilter]] = field(default_factory=list)
    product_fields: list[DslValue[MapFilter]] = field(default_factory=list)
    product_name: list[DslValue[StringFilter]] = field(default_factory=list)
    recommendation_text: list[DslValue[StringFilter]] = field(default_factory=list)
    record_state: list[DslValue[StringFilter]] = field(default_factory=list)
    region: list[DslValue[StringFilter]] = field(default_factory=list)
    related_findings_id: list[DslValue[StringFilter]] = field(default_factory=list)
    related_findings_product_arn: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_application_arn: list[DslValue[StringFilter]] = field(default_factory=list)
    resource_application_name: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_iam_instance_profile_arn: list[DslValue[StringFilter]] = (
        field(default_factory=list)
    )
    resource_aws_ec2_instance_image_id: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_ip_v4_addresses: list[DslValue[IpFilter]] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_ip_v6_addresses: list[DslValue[IpFilter]] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_key_name: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_launched_at: list[DslValue[DateFilter]] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_subnet_id: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_type: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_vpc_id: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_aws_iam_access_key_created_at: list[DslValue[DateFilter]] = field(
        default_factory=list
    )
    resource_aws_iam_access_key_principal_name: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_aws_iam_access_key_status: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_aws_iam_user_user_name: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_aws_s3_bucket_owner_id: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_aws_s3_bucket_owner_name: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_container_image_id: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_container_image_name: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    resource_container_launched_at: list[DslValue[DateFilter]] = field(
        default_factory=list
    )
    resource_container_name: list[DslValue[StringFilter]] = field(default_factory=list)
    resource_details_other: list[DslValue[MapFilter]] = field(default_factory=list)
    resource_id: list[DslValue[StringFilter]] = field(default_factory=list)
    resource_partition: list[DslValue[StringFilter]] = field(default_factory=list)
    resource_region: list[DslValue[StringFilter]] = field(default_factory=list)
    resource_tags: list[DslValue[MapFilter]] = field(default_factory=list)
    resource_type: list[DslValue[StringFilter]] = field(default_factory=list)
    sample: list[DslValue[BooleanFilter]] = field(default_factory=list)
    severity_label: list[DslValue[StringFilter]] = field(default_factory=list)
    source_url: list[DslValue[StringFilter]] = field(default_factory=list)
    threat_intel_indicator_category: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    threat_intel_indicator_last_observed_at: list[DslValue[DateFilter]] = field(
        default_factory=list
    )
    threat_intel_indicator_source: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    threat_intel_indicator_source_url: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    threat_intel_indicator_type: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    threat_intel_indicator_value: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    title: list[DslValue[StringFilter]] = field(default_factory=list)
    type_: list[DslValue[StringFilter]] = field(default_factory=list)
    updated_at: list[DslValue[DateFilter]] = field(default_factory=list)
    user_defined_fields: list[DslValue[MapFilter]] = field(default_factory=list)
    verification_state: list[DslValue[StringFilter]] = field(default_factory=list)
    vulnerabilities_exploit_available: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    vulnerabilities_fix_available: list[DslValue[StringFilter]] = field(
        default_factory=list
    )
    workflow_state: list[DslValue[StringFilter]] = field(default_factory=list)
    workflow_status: list[DslValue[StringFilter]] = field(default_factory=list)


@dataclass
class BooleanFilter(PropertyType):
    value: DslValue[bool] | None = None


@dataclass
class DateFilter(PropertyType):
    date_range: DslValue[DateRange] | None = None
    end: DslValue[str] | None = None
    start: DslValue[str] | None = None


@dataclass
class DateRange(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class IpFilter(PropertyType):
    cidr: DslValue[str] | None = None


@dataclass
class MapFilter(PropertyType):
    comparison: DslValue[str] | None = None
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class NumberFilter(PropertyType):
    eq: DslValue[float] | None = None
    gte: DslValue[float] | None = None
    lte: DslValue[float] | None = None


@dataclass
class StringFilter(PropertyType):
    comparison: DslValue[str] | None = None
    value: DslValue[str] | None = None
