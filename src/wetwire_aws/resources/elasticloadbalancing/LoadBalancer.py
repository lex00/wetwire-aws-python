"""PropertyTypes for AWS::ElasticLoadBalancing::LoadBalancer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessLoggingPolicy(PropertyType):
    enabled: DslValue[bool] | None = None
    s3_bucket_name: DslValue[str] | None = None
    emit_interval: DslValue[int] | None = None
    s3_bucket_prefix: DslValue[str] | None = None


@dataclass
class AppCookieStickinessPolicy(PropertyType):
    cookie_name: DslValue[str] | None = None
    policy_name: DslValue[str] | None = None


@dataclass
class ConnectionDrainingPolicy(PropertyType):
    enabled: DslValue[bool] | None = None
    timeout: DslValue[int] | None = None


@dataclass
class ConnectionSettings(PropertyType):
    idle_timeout: DslValue[int] | None = None


@dataclass
class HealthCheck(PropertyType):
    healthy_threshold: DslValue[str] | None = None
    interval: DslValue[str] | None = None
    target: DslValue[str] | None = None
    timeout: DslValue[str] | None = None
    unhealthy_threshold: DslValue[str] | None = None


@dataclass
class LBCookieStickinessPolicy(PropertyType):
    cookie_expiration_period: DslValue[str] | None = None
    policy_name: DslValue[str] | None = None


@dataclass
class Listeners(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ssl_certificate_id": "SSLCertificateId",
    }

    instance_port: DslValue[str] | None = None
    load_balancer_port: DslValue[str] | None = None
    protocol: DslValue[str] | None = None
    instance_protocol: DslValue[str] | None = None
    policy_names: list[DslValue[str]] = field(default_factory=list)
    ssl_certificate_id: DslValue[str] | None = None


@dataclass
class Policies(PropertyType):
    attributes: list[DslValue[dict[str, Any]]] = field(default_factory=list)
    policy_name: DslValue[str] | None = None
    policy_type: DslValue[str] | None = None
    instance_ports: list[DslValue[str]] = field(default_factory=list)
    load_balancer_ports: list[DslValue[str]] = field(default_factory=list)
