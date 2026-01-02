"""PropertyTypes for AWS::PCS::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Accounting(PropertyType):
    mode: str | None = None
    default_purge_time_in_days: int | None = None


@dataclass
class AuthKey(PropertyType):
    secret_arn: str | None = None
    secret_version: str | None = None


@dataclass
class Endpoint(PropertyType):
    port: str | None = None
    private_ip_address: str | None = None
    type_: str | None = None
    ipv6_address: str | None = None
    public_ip_address: str | None = None


@dataclass
class ErrorInfo(PropertyType):
    code: str | None = None
    message: str | None = None


@dataclass
class JwtAuth(PropertyType):
    jwt_key: JwtKey | None = None


@dataclass
class JwtKey(PropertyType):
    secret_arn: str | None = None
    secret_version: str | None = None


@dataclass
class Networking(PropertyType):
    network_type: str | None = None
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class Scheduler(PropertyType):
    type_: str | None = None
    version: str | None = None


@dataclass
class SlurmConfiguration(PropertyType):
    accounting: Accounting | None = None
    auth_key: AuthKey | None = None
    jwt_auth: JwtAuth | None = None
    scale_down_idle_time_in_seconds: int | None = None
    slurm_custom_settings: list[SlurmCustomSetting] = field(default_factory=list)
    slurm_rest: SlurmRest | None = None


@dataclass
class SlurmCustomSetting(PropertyType):
    parameter_name: str | None = None
    parameter_value: str | None = None


@dataclass
class SlurmRest(PropertyType):
    mode: str | None = None
