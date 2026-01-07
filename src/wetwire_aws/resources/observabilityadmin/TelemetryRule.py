"""PropertyTypes for AWS::ObservabilityAdmin::TelemetryRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ActionCondition(PropertyType):
    action: DslValue[str] | None = None


@dataclass
class AdvancedEventSelector(PropertyType):
    field_selectors: list[DslValue[AdvancedFieldSelector]] = field(default_factory=list)
    name: DslValue[str] | None = None


@dataclass
class AdvancedFieldSelector(PropertyType):
    ends_with: list[DslValue[str]] = field(default_factory=list)
    equals: list[DslValue[str]] = field(default_factory=list)
    field_: DslValue[str] | None = None
    not_ends_with: list[DslValue[str]] = field(default_factory=list)
    not_equals: list[DslValue[str]] = field(default_factory=list)
    not_starts_with: list[DslValue[str]] = field(default_factory=list)
    starts_with: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CloudtrailParameters(PropertyType):
    advanced_event_selectors: list[DslValue[AdvancedEventSelector]] = field(
        default_factory=list
    )


@dataclass
class Condition(PropertyType):
    action_condition: DslValue[ActionCondition] | None = None
    label_name_condition: DslValue[LabelNameCondition] | None = None


@dataclass
class ELBLoadBalancerLoggingParameters(PropertyType):
    field_delimiter: DslValue[str] | None = None
    output_format: DslValue[str] | None = None


@dataclass
class FieldToMatch(PropertyType):
    method: DslValue[str] | None = None
    query_string: DslValue[str] | None = None
    single_header: DslValue[SingleHeader] | None = None
    uri_path: DslValue[str] | None = None


@dataclass
class Filter(PropertyType):
    behavior: DslValue[str] | None = None
    conditions: list[DslValue[Condition]] = field(default_factory=list)
    requirement: DslValue[str] | None = None


@dataclass
class LabelNameCondition(PropertyType):
    label_name: DslValue[str] | None = None


@dataclass
class LogDeliveryParameters(PropertyType):
    log_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class LoggingFilter(PropertyType):
    default_behavior: DslValue[str] | None = None
    filters: list[DslValue[Filter]] = field(default_factory=list)


@dataclass
class SingleHeader(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class TelemetryDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "elb_load_balancer_logging_parameters": "ELBLoadBalancerLoggingParameters",
        "vpc_flow_log_parameters": "VPCFlowLogParameters",
        "waf_logging_parameters": "WAFLoggingParameters",
    }

    cloudtrail_parameters: DslValue[CloudtrailParameters] | None = None
    destination_pattern: DslValue[str] | None = None
    destination_type: DslValue[str] | None = None
    elb_load_balancer_logging_parameters: (
        DslValue[ELBLoadBalancerLoggingParameters] | None
    ) = None
    log_delivery_parameters: DslValue[LogDeliveryParameters] | None = None
    retention_in_days: DslValue[int] | None = None
    vpc_flow_log_parameters: DslValue[VPCFlowLogParameters] | None = None
    waf_logging_parameters: DslValue[WAFLoggingParameters] | None = None


@dataclass
class TelemetryRule(PropertyType):
    resource_type: DslValue[str] | None = None
    telemetry_type: DslValue[str] | None = None
    destination_configuration: DslValue[TelemetryDestinationConfiguration] | None = None
    selection_criteria: DslValue[str] | None = None
    telemetry_source_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class VPCFlowLogParameters(PropertyType):
    log_format: DslValue[str] | None = None
    max_aggregation_interval: DslValue[int] | None = None
    traffic_type: DslValue[str] | None = None


@dataclass
class WAFLoggingParameters(PropertyType):
    log_type: DslValue[str] | None = None
    logging_filter: DslValue[LoggingFilter] | None = None
    redacted_fields: list[DslValue[FieldToMatch]] = field(default_factory=list)
