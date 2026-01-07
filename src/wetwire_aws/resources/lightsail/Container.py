"""PropertyTypes for AWS::Lightsail::Container."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Container(PropertyType):
    command: list[DslValue[str]] = field(default_factory=list)
    container_name: DslValue[str] | None = None
    environment: list[DslValue[EnvironmentVariable]] = field(default_factory=list)
    image: DslValue[str] | None = None
    ports: list[DslValue[PortInfo]] = field(default_factory=list)


@dataclass
class ContainerServiceDeployment(PropertyType):
    containers: list[DslValue[Container]] = field(default_factory=list)
    public_endpoint: DslValue[PublicEndpoint] | None = None


@dataclass
class EcrImagePullerRole(PropertyType):
    is_active: DslValue[bool] | None = None
    principal_arn: DslValue[str] | None = None


@dataclass
class EnvironmentVariable(PropertyType):
    value: DslValue[str] | None = None
    variable: DslValue[str] | None = None


@dataclass
class HealthCheckConfig(PropertyType):
    healthy_threshold: DslValue[int] | None = None
    interval_seconds: DslValue[int] | None = None
    path: DslValue[str] | None = None
    success_codes: DslValue[str] | None = None
    timeout_seconds: DslValue[int] | None = None
    unhealthy_threshold: DslValue[int] | None = None


@dataclass
class PortInfo(PropertyType):
    port: DslValue[str] | None = None
    protocol: DslValue[str] | None = None


@dataclass
class PrivateRegistryAccess(PropertyType):
    ecr_image_puller_role: DslValue[EcrImagePullerRole] | None = None


@dataclass
class PublicDomainName(PropertyType):
    certificate_name: DslValue[str] | None = None
    domain_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PublicEndpoint(PropertyType):
    container_name: DslValue[str] | None = None
    container_port: DslValue[int] | None = None
    health_check_config: DslValue[HealthCheckConfig] | None = None
