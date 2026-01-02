"""PropertyTypes for AWS::MediaConnect::RouterNetworkInterface."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PublicRouterNetworkInterfaceConfiguration(PropertyType):
    allow_rules: list[PublicRouterNetworkInterfaceRule] = field(default_factory=list)


@dataclass
class PublicRouterNetworkInterfaceRule(PropertyType):
    cidr: str | None = None


@dataclass
class RouterNetworkInterfaceConfiguration(PropertyType):
    public: PublicRouterNetworkInterfaceConfiguration | None = None
    vpc: VpcRouterNetworkInterfaceConfiguration | None = None


@dataclass
class VpcRouterNetworkInterfaceConfiguration(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_id: str | None = None
