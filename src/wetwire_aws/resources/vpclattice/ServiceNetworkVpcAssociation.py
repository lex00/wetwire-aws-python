"""PropertyTypes for AWS::VpcLattice::ServiceNetworkVpcAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DnsOptions(PropertyType):
    private_dns_preference: str | None = None
    private_dns_specified_domains: list[String] = field(default_factory=list)
