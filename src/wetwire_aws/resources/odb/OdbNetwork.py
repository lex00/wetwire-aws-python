"""PropertyTypes for AWS::ODB::OdbNetwork."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ManagedS3BackupAccess(PropertyType):
    ipv4_addresses: list[String] = field(default_factory=list)
    status: str | None = None


@dataclass
class ManagedServices(PropertyType):
    managed_s3_backup_access: ManagedS3BackupAccess | None = None
    managed_services_ipv4_cidrs: list[String] = field(default_factory=list)
    resource_gateway_arn: str | None = None
    s3_access: S3Access | None = None
    service_network_arn: str | None = None
    service_network_endpoint: ServiceNetworkEndpoint | None = None
    zero_etl_access: ZeroEtlAccess | None = None


@dataclass
class S3Access(PropertyType):
    domain_name: str | None = None
    ipv4_addresses: list[String] = field(default_factory=list)
    s3_policy_document: str | None = None
    status: str | None = None


@dataclass
class ServiceNetworkEndpoint(PropertyType):
    vpc_endpoint_id: str | None = None
    vpc_endpoint_type: str | None = None


@dataclass
class ZeroEtlAccess(PropertyType):
    cidr: str | None = None
    status: str | None = None
