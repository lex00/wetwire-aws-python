"""PropertyTypes for AWS::EC2::NetworkInterface."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConnectionTrackingSpecification(PropertyType):
    tcp_established_timeout: DslValue[int] | None = None
    udp_stream_timeout: DslValue[int] | None = None
    udp_timeout: DslValue[int] | None = None


@dataclass
class InstanceIpv6Address(PropertyType):
    ipv6_address: DslValue[str] | None = None


@dataclass
class Ipv4PrefixSpecification(PropertyType):
    ipv4_prefix: DslValue[str] | None = None


@dataclass
class Ipv6PrefixSpecification(PropertyType):
    ipv6_prefix: DslValue[str] | None = None


@dataclass
class PrivateIpAddressSpecification(PropertyType):
    primary: DslValue[bool] | None = None
    private_ip_address: DslValue[str] | None = None


@dataclass
class PublicIpDnsNameOptions(PropertyType):
    dns_hostname_type: DslValue[str] | None = None
    public_dual_stack_dns_name: DslValue[str] | None = None
    public_ipv4_dns_name: DslValue[str] | None = None
    public_ipv6_dns_name: DslValue[str] | None = None
