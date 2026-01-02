"""PropertyTypes for AWS::ElasticLoadBalancingV2::LoadBalancer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LoadBalancerAttribute(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class MinimumLoadBalancerCapacity(PropertyType):
    capacity_units: int | None = None


@dataclass
class SubnetMapping(PropertyType):
    subnet_id: str | None = None
    allocation_id: str | None = None
    i_pv6_address: str | None = None
    private_i_pv4_address: str | None = None
    source_nat_ipv6_prefix: str | None = None
