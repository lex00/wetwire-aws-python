"""PropertyTypes for AWS::Route53::HealthCheck."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AlarmIdentifier(PropertyType):
    name: str | None = None
    region: str | None = None


@dataclass
class HealthCheckConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_sni": "EnableSNI",
        "ip_address": "IPAddress",
    }

    type_: str | None = None
    alarm_identifier: AlarmIdentifier | None = None
    child_health_checks: list[String] = field(default_factory=list)
    enable_sni: bool | None = None
    failure_threshold: int | None = None
    fully_qualified_domain_name: str | None = None
    health_threshold: int | None = None
    insufficient_data_health_status: str | None = None
    inverted: bool | None = None
    ip_address: str | None = None
    measure_latency: bool | None = None
    port: int | None = None
    regions: list[String] = field(default_factory=list)
    request_interval: int | None = None
    resource_path: str | None = None
    routing_control_arn: str | None = None
    search_string: str | None = None


@dataclass
class HealthCheckTag(PropertyType):
    key: str | None = None
    value: str | None = None
