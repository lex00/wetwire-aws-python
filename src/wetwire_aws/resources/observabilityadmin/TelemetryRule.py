"""PropertyTypes for AWS::ObservabilityAdmin::TelemetryRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ActionCondition(PropertyType):
    action: str | None = None


@dataclass
class AdvancedEventSelector(PropertyType):
    field_selectors: list[AdvancedFieldSelector] = field(default_factory=list)
    name: str | None = None


@dataclass
class AdvancedFieldSelector(PropertyType):
    ends_with: list[String] = field(default_factory=list)
    equals: list[String] = field(default_factory=list)
    field_: str | None = None
    not_ends_with: list[String] = field(default_factory=list)
    not_equals: list[String] = field(default_factory=list)
    not_starts_with: list[String] = field(default_factory=list)
    starts_with: list[String] = field(default_factory=list)


@dataclass
class CloudtrailParameters(PropertyType):
    advanced_event_selectors: list[AdvancedEventSelector] = field(default_factory=list)


@dataclass
class Condition(PropertyType):
    action_condition: ActionCondition | None = None
    label_name_condition: LabelNameCondition | None = None


@dataclass
class ELBLoadBalancerLoggingParameters(PropertyType):
    field_delimiter: str | None = None
    output_format: str | None = None


@dataclass
class FieldToMatch(PropertyType):
    method: str | None = None
    query_string: str | None = None
    single_header: SingleHeader | None = None
    uri_path: str | None = None


@dataclass
class Filter(PropertyType):
    behavior: str | None = None
    conditions: list[Condition] = field(default_factory=list)
    requirement: str | None = None


@dataclass
class LabelNameCondition(PropertyType):
    label_name: str | None = None


@dataclass
class LogDeliveryParameters(PropertyType):
    log_types: list[String] = field(default_factory=list)


@dataclass
class LoggingFilter(PropertyType):
    default_behavior: str | None = None
    filters: list[Filter] = field(default_factory=list)


@dataclass
class SingleHeader(PropertyType):
    name: str | None = None


@dataclass
class TelemetryDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "elb_load_balancer_logging_parameters": "ELBLoadBalancerLoggingParameters",
        "vpc_flow_log_parameters": "VPCFlowLogParameters",
        "waf_logging_parameters": "WAFLoggingParameters",
    }

    cloudtrail_parameters: CloudtrailParameters | None = None
    destination_pattern: str | None = None
    destination_type: str | None = None
    elb_load_balancer_logging_parameters: ELBLoadBalancerLoggingParameters | None = None
    log_delivery_parameters: LogDeliveryParameters | None = None
    retention_in_days: int | None = None
    vpc_flow_log_parameters: VPCFlowLogParameters | None = None
    waf_logging_parameters: WAFLoggingParameters | None = None


@dataclass
class TelemetryRule(PropertyType):
    resource_type: str | None = None
    telemetry_type: str | None = None
    destination_configuration: TelemetryDestinationConfiguration | None = None
    selection_criteria: str | None = None
    telemetry_source_types: list[String] = field(default_factory=list)


@dataclass
class VPCFlowLogParameters(PropertyType):
    log_format: str | None = None
    max_aggregation_interval: int | None = None
    traffic_type: str | None = None


@dataclass
class WAFLoggingParameters(PropertyType):
    log_type: str | None = None
    logging_filter: LoggingFilter | None = None
    redacted_fields: list[FieldToMatch] = field(default_factory=list)
