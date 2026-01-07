"""PropertyTypes for AWS::Redshift::EndpointAccess."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class NetworkInterface(PropertyType):
    availability_zone: DslValue[str] | None = None
    network_interface_id: DslValue[str] | None = None
    private_ip_address: DslValue[str] | None = None
    subnet_id: DslValue[str] | None = None


@dataclass
class VpcEndpoint(PropertyType):
    network_interfaces: list[DslValue[NetworkInterface]] = field(default_factory=list)
    vpc_endpoint_id: DslValue[str] | None = None
    vpc_id: DslValue[str] | None = None


@dataclass
class VpcSecurityGroup(PropertyType):
    status: DslValue[str] | None = None
    vpc_security_group_id: DslValue[str] | None = None
