"""PropertyTypes for AWS::VpcLattice::TargetGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class HealthCheckConfig(PropertyType):
    enabled: bool | None = None
    health_check_interval_seconds: int | None = None
    health_check_timeout_seconds: int | None = None
    healthy_threshold_count: int | None = None
    matcher: Matcher | None = None
    path: str | None = None
    port: int | None = None
    protocol: str | None = None
    protocol_version: str | None = None
    unhealthy_threshold_count: int | None = None


@dataclass
class Matcher(PropertyType):
    http_code: str | None = None


@dataclass
class Target(PropertyType):
    id: str | None = None
    port: int | None = None


@dataclass
class TargetGroupConfig(PropertyType):
    health_check: HealthCheckConfig | None = None
    ip_address_type: str | None = None
    lambda_event_structure_version: str | None = None
    port: int | None = None
    protocol: str | None = None
    protocol_version: str | None = None
    vpc_identifier: str | None = None
