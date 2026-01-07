"""PropertyTypes for AWS::ElasticLoadBalancingV2::LoadBalancer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LoadBalancerAttribute(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class MinimumLoadBalancerCapacity(PropertyType):
    capacity_units: DslValue[int] | None = None


@dataclass
class SubnetMapping(PropertyType):
    subnet_id: DslValue[str] | None = None
    allocation_id: DslValue[str] | None = None
    i_pv6_address: DslValue[str] | None = None
    private_i_pv4_address: DslValue[str] | None = None
    source_nat_ipv6_prefix: DslValue[str] | None = None
