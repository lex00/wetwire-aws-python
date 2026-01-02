"""PropertyTypes for AWS::ElasticLoadBalancing::LoadBalancer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessLoggingPolicy(PropertyType):
    enabled: bool | None = None
    s3_bucket_name: str | None = None
    emit_interval: int | None = None
    s3_bucket_prefix: str | None = None


@dataclass
class AppCookieStickinessPolicy(PropertyType):
    cookie_name: str | None = None
    policy_name: str | None = None


@dataclass
class ConnectionDrainingPolicy(PropertyType):
    enabled: bool | None = None
    timeout: int | None = None


@dataclass
class ConnectionSettings(PropertyType):
    idle_timeout: int | None = None


@dataclass
class HealthCheck(PropertyType):
    healthy_threshold: str | None = None
    interval: str | None = None
    target: str | None = None
    timeout: str | None = None
    unhealthy_threshold: str | None = None


@dataclass
class LBCookieStickinessPolicy(PropertyType):
    cookie_expiration_period: str | None = None
    policy_name: str | None = None


@dataclass
class Listeners(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ssl_certificate_id": "SSLCertificateId",
    }

    instance_port: str | None = None
    load_balancer_port: str | None = None
    protocol: str | None = None
    instance_protocol: str | None = None
    policy_names: list[String] = field(default_factory=list)
    ssl_certificate_id: str | None = None


@dataclass
class Policies(PropertyType):
    attributes: list[Json] = field(default_factory=list)
    policy_name: str | None = None
    policy_type: str | None = None
    instance_ports: list[String] = field(default_factory=list)
    load_balancer_ports: list[String] = field(default_factory=list)
