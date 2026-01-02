"""PropertyTypes for AWS::CloudFront::AnycastIpList."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AnycastIpList(PropertyType):
    anycast_ips: list[String] = field(default_factory=list)
    arn: str | None = None
    id: str | None = None
    ip_count: int | None = None
    last_modified_time: str | None = None
    name: str | None = None
    status: str | None = None
    ip_address_type: str | None = None
    ipam_cidr_config_results: list[IpamCidrConfigResult] = field(default_factory=list)


@dataclass
class IpamCidrConfig(PropertyType):
    cidr: str | None = None
    ipam_pool_arn: str | None = None


@dataclass
class IpamCidrConfigResult(PropertyType):
    anycast_ip: str | None = None
    cidr: str | None = None
    ipam_pool_arn: str | None = None
    status: str | None = None


@dataclass
class Tags(PropertyType):
    items: list[Tag] = field(default_factory=list)
