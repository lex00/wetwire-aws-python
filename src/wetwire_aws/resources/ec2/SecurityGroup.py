"""PropertyTypes for AWS::EC2::SecurityGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Egress(PropertyType):
    ip_protocol: str | None = None
    cidr_ip: str | None = None
    cidr_ipv6: str | None = None
    description: str | None = None
    destination_prefix_list_id: str | None = None
    destination_security_group_id: str | None = None
    from_port: int | None = None
    to_port: int | None = None


@dataclass
class Ingress(PropertyType):
    ip_protocol: str | None = None
    cidr_ip: str | None = None
    cidr_ipv6: str | None = None
    description: str | None = None
    from_port: int | None = None
    source_prefix_list_id: str | None = None
    source_security_group_id: str | None = None
    source_security_group_name: str | None = None
    source_security_group_owner_id: str | None = None
    to_port: int | None = None
