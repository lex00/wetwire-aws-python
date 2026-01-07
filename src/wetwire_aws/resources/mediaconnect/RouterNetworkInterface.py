"""PropertyTypes for AWS::MediaConnect::RouterNetworkInterface."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PublicRouterNetworkInterfaceConfiguration(PropertyType):
    allow_rules: list[DslValue[PublicRouterNetworkInterfaceRule]] = field(
        default_factory=list
    )


@dataclass
class PublicRouterNetworkInterfaceRule(PropertyType):
    cidr: DslValue[str] | None = None


@dataclass
class RouterNetworkInterfaceConfiguration(PropertyType):
    public: DslValue[PublicRouterNetworkInterfaceConfiguration] | None = None
    vpc: DslValue[VpcRouterNetworkInterfaceConfiguration] | None = None


@dataclass
class VpcRouterNetworkInterfaceConfiguration(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_id: DslValue[str] | None = None
