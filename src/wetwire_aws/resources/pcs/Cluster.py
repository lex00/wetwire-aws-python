"""PropertyTypes for AWS::PCS::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Accounting(PropertyType):
    mode: DslValue[str] | None = None
    default_purge_time_in_days: DslValue[int] | None = None


@dataclass
class AuthKey(PropertyType):
    secret_arn: DslValue[str] | None = None
    secret_version: DslValue[str] | None = None


@dataclass
class Endpoint(PropertyType):
    port: DslValue[str] | None = None
    private_ip_address: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    ipv6_address: DslValue[str] | None = None
    public_ip_address: DslValue[str] | None = None


@dataclass
class ErrorInfo(PropertyType):
    code: DslValue[str] | None = None
    message: DslValue[str] | None = None


@dataclass
class JwtAuth(PropertyType):
    jwt_key: DslValue[JwtKey] | None = None


@dataclass
class JwtKey(PropertyType):
    secret_arn: DslValue[str] | None = None
    secret_version: DslValue[str] | None = None


@dataclass
class Networking(PropertyType):
    network_type: DslValue[str] | None = None
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Scheduler(PropertyType):
    type_: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class SlurmConfiguration(PropertyType):
    accounting: DslValue[Accounting] | None = None
    auth_key: DslValue[AuthKey] | None = None
    jwt_auth: DslValue[JwtAuth] | None = None
    scale_down_idle_time_in_seconds: DslValue[int] | None = None
    slurm_custom_settings: list[DslValue[SlurmCustomSetting]] = field(
        default_factory=list
    )
    slurm_rest: DslValue[SlurmRest] | None = None


@dataclass
class SlurmCustomSetting(PropertyType):
    parameter_name: DslValue[str] | None = None
    parameter_value: DslValue[str] | None = None


@dataclass
class SlurmRest(PropertyType):
    mode: DslValue[str] | None = None
