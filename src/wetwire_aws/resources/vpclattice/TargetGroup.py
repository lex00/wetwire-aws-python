"""PropertyTypes for AWS::VpcLattice::TargetGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class HealthCheckConfig(PropertyType):
    enabled: DslValue[bool] | None = None
    health_check_interval_seconds: DslValue[int] | None = None
    health_check_timeout_seconds: DslValue[int] | None = None
    healthy_threshold_count: DslValue[int] | None = None
    matcher: DslValue[Matcher] | None = None
    path: DslValue[str] | None = None
    port: DslValue[int] | None = None
    protocol: DslValue[str] | None = None
    protocol_version: DslValue[str] | None = None
    unhealthy_threshold_count: DslValue[int] | None = None


@dataclass
class Matcher(PropertyType):
    http_code: DslValue[str] | None = None


@dataclass
class Target(PropertyType):
    id: DslValue[str] | None = None
    port: DslValue[int] | None = None


@dataclass
class TargetGroupConfig(PropertyType):
    health_check: DslValue[HealthCheckConfig] | None = None
    ip_address_type: DslValue[str] | None = None
    lambda_event_structure_version: DslValue[str] | None = None
    port: DslValue[int] | None = None
    protocol: DslValue[str] | None = None
    protocol_version: DslValue[str] | None = None
    vpc_identifier: DslValue[str] | None = None
