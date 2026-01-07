"""PropertyTypes for AWS::ODB::OdbNetwork."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ManagedS3BackupAccess(PropertyType):
    ipv4_addresses: list[DslValue[str]] = field(default_factory=list)
    status: DslValue[str] | None = None


@dataclass
class ManagedServices(PropertyType):
    managed_s3_backup_access: DslValue[ManagedS3BackupAccess] | None = None
    managed_services_ipv4_cidrs: list[DslValue[str]] = field(default_factory=list)
    resource_gateway_arn: DslValue[str] | None = None
    s3_access: DslValue[S3Access] | None = None
    service_network_arn: DslValue[str] | None = None
    service_network_endpoint: DslValue[ServiceNetworkEndpoint] | None = None
    zero_etl_access: DslValue[ZeroEtlAccess] | None = None


@dataclass
class S3Access(PropertyType):
    domain_name: DslValue[str] | None = None
    ipv4_addresses: list[DslValue[str]] = field(default_factory=list)
    s3_policy_document: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class ServiceNetworkEndpoint(PropertyType):
    vpc_endpoint_id: DslValue[str] | None = None
    vpc_endpoint_type: DslValue[str] | None = None


@dataclass
class ZeroEtlAccess(PropertyType):
    cidr: DslValue[str] | None = None
    status: DslValue[str] | None = None
