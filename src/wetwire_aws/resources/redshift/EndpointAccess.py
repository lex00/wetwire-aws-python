"""PropertyTypes for AWS::Redshift::EndpointAccess."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class NetworkInterface(PropertyType):
    availability_zone: str | None = None
    network_interface_id: str | None = None
    private_ip_address: str | None = None
    subnet_id: str | None = None


@dataclass
class VpcEndpoint(PropertyType):
    network_interfaces: list[NetworkInterface] = field(default_factory=list)
    vpc_endpoint_id: str | None = None
    vpc_id: str | None = None


@dataclass
class VpcSecurityGroup(PropertyType):
    status: str | None = None
    vpc_security_group_id: str | None = None
