"""PropertyTypes for AWS::Lightsail::Container."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Container(PropertyType):
    command: list[String] = field(default_factory=list)
    container_name: str | None = None
    environment: list[EnvironmentVariable] = field(default_factory=list)
    image: str | None = None
    ports: list[PortInfo] = field(default_factory=list)


@dataclass
class ContainerServiceDeployment(PropertyType):
    containers: list[Container] = field(default_factory=list)
    public_endpoint: PublicEndpoint | None = None


@dataclass
class EcrImagePullerRole(PropertyType):
    is_active: bool | None = None
    principal_arn: str | None = None


@dataclass
class EnvironmentVariable(PropertyType):
    value: str | None = None
    variable: str | None = None


@dataclass
class HealthCheckConfig(PropertyType):
    healthy_threshold: int | None = None
    interval_seconds: int | None = None
    path: str | None = None
    success_codes: str | None = None
    timeout_seconds: int | None = None
    unhealthy_threshold: int | None = None


@dataclass
class PortInfo(PropertyType):
    port: str | None = None
    protocol: str | None = None


@dataclass
class PrivateRegistryAccess(PropertyType):
    ecr_image_puller_role: EcrImagePullerRole | None = None


@dataclass
class PublicDomainName(PropertyType):
    certificate_name: str | None = None
    domain_names: list[String] = field(default_factory=list)


@dataclass
class PublicEndpoint(PropertyType):
    container_name: str | None = None
    container_port: int | None = None
    health_check_config: HealthCheckConfig | None = None
