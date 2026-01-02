"""PropertyTypes for AWS::SecurityHub::Insight."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AwsSecurityFindingFilters(PropertyType):
    aws_account_id: list[StringFilter] = field(default_factory=list)
    aws_account_name: list[StringFilter] = field(default_factory=list)
    company_name: list[StringFilter] = field(default_factory=list)
    compliance_associated_standards_id: list[StringFilter] = field(default_factory=list)
    compliance_security_control_id: list[StringFilter] = field(default_factory=list)
    compliance_security_control_parameters_name: list[StringFilter] = field(
        default_factory=list
    )
    compliance_security_control_parameters_value: list[StringFilter] = field(
        default_factory=list
    )
    compliance_status: list[StringFilter] = field(default_factory=list)
    confidence: list[NumberFilter] = field(default_factory=list)
    created_at: list[DateFilter] = field(default_factory=list)
    criticality: list[NumberFilter] = field(default_factory=list)
    description: list[StringFilter] = field(default_factory=list)
    finding_provider_fields_confidence: list[NumberFilter] = field(default_factory=list)
    finding_provider_fields_criticality: list[NumberFilter] = field(
        default_factory=list
    )
    finding_provider_fields_related_findings_id: list[StringFilter] = field(
        default_factory=list
    )
    finding_provider_fields_related_findings_product_arn: list[StringFilter] = field(
        default_factory=list
    )
    finding_provider_fields_severity_label: list[StringFilter] = field(
        default_factory=list
    )
    finding_provider_fields_severity_original: list[StringFilter] = field(
        default_factory=list
    )
    finding_provider_fields_types: list[StringFilter] = field(default_factory=list)
    first_observed_at: list[DateFilter] = field(default_factory=list)
    generator_id: list[StringFilter] = field(default_factory=list)
    id: list[StringFilter] = field(default_factory=list)
    last_observed_at: list[DateFilter] = field(default_factory=list)
    malware_name: list[StringFilter] = field(default_factory=list)
    malware_path: list[StringFilter] = field(default_factory=list)
    malware_state: list[StringFilter] = field(default_factory=list)
    malware_type: list[StringFilter] = field(default_factory=list)
    network_destination_domain: list[StringFilter] = field(default_factory=list)
    network_destination_ip_v4: list[IpFilter] = field(default_factory=list)
    network_destination_ip_v6: list[IpFilter] = field(default_factory=list)
    network_destination_port: list[NumberFilter] = field(default_factory=list)
    network_direction: list[StringFilter] = field(default_factory=list)
    network_protocol: list[StringFilter] = field(default_factory=list)
    network_source_domain: list[StringFilter] = field(default_factory=list)
    network_source_ip_v4: list[IpFilter] = field(default_factory=list)
    network_source_ip_v6: list[IpFilter] = field(default_factory=list)
    network_source_mac: list[StringFilter] = field(default_factory=list)
    network_source_port: list[NumberFilter] = field(default_factory=list)
    note_text: list[StringFilter] = field(default_factory=list)
    note_updated_at: list[DateFilter] = field(default_factory=list)
    note_updated_by: list[StringFilter] = field(default_factory=list)
    process_launched_at: list[DateFilter] = field(default_factory=list)
    process_name: list[StringFilter] = field(default_factory=list)
    process_parent_pid: list[NumberFilter] = field(default_factory=list)
    process_path: list[StringFilter] = field(default_factory=list)
    process_pid: list[NumberFilter] = field(default_factory=list)
    process_terminated_at: list[DateFilter] = field(default_factory=list)
    product_arn: list[StringFilter] = field(default_factory=list)
    product_fields: list[MapFilter] = field(default_factory=list)
    product_name: list[StringFilter] = field(default_factory=list)
    recommendation_text: list[StringFilter] = field(default_factory=list)
    record_state: list[StringFilter] = field(default_factory=list)
    region: list[StringFilter] = field(default_factory=list)
    related_findings_id: list[StringFilter] = field(default_factory=list)
    related_findings_product_arn: list[StringFilter] = field(default_factory=list)
    resource_application_arn: list[StringFilter] = field(default_factory=list)
    resource_application_name: list[StringFilter] = field(default_factory=list)
    resource_aws_ec2_instance_iam_instance_profile_arn: list[StringFilter] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_image_id: list[StringFilter] = field(default_factory=list)
    resource_aws_ec2_instance_ip_v4_addresses: list[IpFilter] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_ip_v6_addresses: list[IpFilter] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_key_name: list[StringFilter] = field(default_factory=list)
    resource_aws_ec2_instance_launched_at: list[DateFilter] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_subnet_id: list[StringFilter] = field(
        default_factory=list
    )
    resource_aws_ec2_instance_type: list[StringFilter] = field(default_factory=list)
    resource_aws_ec2_instance_vpc_id: list[StringFilter] = field(default_factory=list)
    resource_aws_iam_access_key_created_at: list[DateFilter] = field(
        default_factory=list
    )
    resource_aws_iam_access_key_principal_name: list[StringFilter] = field(
        default_factory=list
    )
    resource_aws_iam_access_key_status: list[StringFilter] = field(default_factory=list)
    resource_aws_iam_user_user_name: list[StringFilter] = field(default_factory=list)
    resource_aws_s3_bucket_owner_id: list[StringFilter] = field(default_factory=list)
    resource_aws_s3_bucket_owner_name: list[StringFilter] = field(default_factory=list)
    resource_container_image_id: list[StringFilter] = field(default_factory=list)
    resource_container_image_name: list[StringFilter] = field(default_factory=list)
    resource_container_launched_at: list[DateFilter] = field(default_factory=list)
    resource_container_name: list[StringFilter] = field(default_factory=list)
    resource_details_other: list[MapFilter] = field(default_factory=list)
    resource_id: list[StringFilter] = field(default_factory=list)
    resource_partition: list[StringFilter] = field(default_factory=list)
    resource_region: list[StringFilter] = field(default_factory=list)
    resource_tags: list[MapFilter] = field(default_factory=list)
    resource_type: list[StringFilter] = field(default_factory=list)
    sample: list[BooleanFilter] = field(default_factory=list)
    severity_label: list[StringFilter] = field(default_factory=list)
    source_url: list[StringFilter] = field(default_factory=list)
    threat_intel_indicator_category: list[StringFilter] = field(default_factory=list)
    threat_intel_indicator_last_observed_at: list[DateFilter] = field(
        default_factory=list
    )
    threat_intel_indicator_source: list[StringFilter] = field(default_factory=list)
    threat_intel_indicator_source_url: list[StringFilter] = field(default_factory=list)
    threat_intel_indicator_type: list[StringFilter] = field(default_factory=list)
    threat_intel_indicator_value: list[StringFilter] = field(default_factory=list)
    title: list[StringFilter] = field(default_factory=list)
    type_: list[StringFilter] = field(default_factory=list)
    updated_at: list[DateFilter] = field(default_factory=list)
    user_defined_fields: list[MapFilter] = field(default_factory=list)
    verification_state: list[StringFilter] = field(default_factory=list)
    vulnerabilities_exploit_available: list[StringFilter] = field(default_factory=list)
    vulnerabilities_fix_available: list[StringFilter] = field(default_factory=list)
    workflow_state: list[StringFilter] = field(default_factory=list)
    workflow_status: list[StringFilter] = field(default_factory=list)


@dataclass
class BooleanFilter(PropertyType):
    value: bool | None = None


@dataclass
class DateFilter(PropertyType):
    date_range: DateRange | None = None
    end: str | None = None
    start: str | None = None


@dataclass
class DateRange(PropertyType):
    unit: str | None = None
    value: float | None = None


@dataclass
class IpFilter(PropertyType):
    cidr: str | None = None


@dataclass
class MapFilter(PropertyType):
    comparison: str | None = None
    key: str | None = None
    value: str | None = None


@dataclass
class NumberFilter(PropertyType):
    eq: float | None = None
    gte: float | None = None
    lte: float | None = None


@dataclass
class StringFilter(PropertyType):
    comparison: str | None = None
    value: str | None = None
