"""PropertyTypes for AWS::VpcLattice::ResourceConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DnsResource(PropertyType):
    domain_name: str | None = None
    ip_address_type: str | None = None


@dataclass
class ResourceConfigurationDefinition(PropertyType):
    arn_resource: str | None = None
    dns_resource: DnsResource | None = None
    ip_resource: str | None = None
