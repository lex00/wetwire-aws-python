"""PropertyTypes for AWS::Route53::HealthCheck."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AlarmIdentifier(PropertyType):
    name: DslValue[str] | None = None
    region: DslValue[str] | None = None


@dataclass
class HealthCheckConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_sni": "EnableSNI",
        "ip_address": "IPAddress",
    }

    type_: DslValue[str] | None = None
    alarm_identifier: DslValue[AlarmIdentifier] | None = None
    child_health_checks: list[DslValue[str]] = field(default_factory=list)
    enable_sni: DslValue[bool] | None = None
    failure_threshold: DslValue[int] | None = None
    fully_qualified_domain_name: DslValue[str] | None = None
    health_threshold: DslValue[int] | None = None
    insufficient_data_health_status: DslValue[str] | None = None
    inverted: DslValue[bool] | None = None
    ip_address: DslValue[str] | None = None
    measure_latency: DslValue[bool] | None = None
    port: DslValue[int] | None = None
    regions: list[DslValue[str]] = field(default_factory=list)
    request_interval: DslValue[int] | None = None
    resource_path: DslValue[str] | None = None
    routing_control_arn: DslValue[str] | None = None
    search_string: DslValue[str] | None = None


@dataclass
class HealthCheckTag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
