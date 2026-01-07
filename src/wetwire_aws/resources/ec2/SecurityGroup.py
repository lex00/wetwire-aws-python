"""PropertyTypes for AWS::EC2::SecurityGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Egress(PropertyType):
    ip_protocol: DslValue[str] | None = None
    cidr_ip: DslValue[str] | None = None
    cidr_ipv6: DslValue[str] | None = None
    description: DslValue[str] | None = None
    destination_prefix_list_id: DslValue[str] | None = None
    destination_security_group_id: DslValue[str] | None = None
    from_port: DslValue[int] | None = None
    to_port: DslValue[int] | None = None


@dataclass
class Ingress(PropertyType):
    ip_protocol: DslValue[str] | None = None
    cidr_ip: DslValue[str] | None = None
    cidr_ipv6: DslValue[str] | None = None
    description: DslValue[str] | None = None
    from_port: DslValue[int] | None = None
    source_prefix_list_id: DslValue[str] | None = None
    source_security_group_id: DslValue[str] | None = None
    source_security_group_name: DslValue[str] | None = None
    source_security_group_owner_id: DslValue[str] | None = None
    to_port: DslValue[int] | None = None
