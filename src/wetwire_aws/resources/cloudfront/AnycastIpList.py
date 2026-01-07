"""PropertyTypes for AWS::CloudFront::AnycastIpList."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AnycastIpList(PropertyType):
    anycast_ips: list[DslValue[str]] = field(default_factory=list)
    arn: DslValue[str] | None = None
    id: DslValue[str] | None = None
    ip_count: DslValue[int] | None = None
    last_modified_time: DslValue[str] | None = None
    name: DslValue[str] | None = None
    status: DslValue[str] | None = None
    ip_address_type: DslValue[str] | None = None
    ipam_cidr_config_results: list[DslValue[IpamCidrConfigResult]] = field(
        default_factory=list
    )


@dataclass
class IpamCidrConfig(PropertyType):
    cidr: DslValue[str] | None = None
    ipam_pool_arn: DslValue[str] | None = None


@dataclass
class IpamCidrConfigResult(PropertyType):
    anycast_ip: DslValue[str] | None = None
    cidr: DslValue[str] | None = None
    ipam_pool_arn: DslValue[str] | None = None
    status: DslValue[str] | None = None


@dataclass
class Tags(PropertyType):
    items: list[DslValue[Tag]] = field(default_factory=list)
