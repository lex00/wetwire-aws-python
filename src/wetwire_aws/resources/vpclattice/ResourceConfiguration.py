"""PropertyTypes for AWS::VpcLattice::ResourceConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DnsResource(PropertyType):
    domain_name: DslValue[str] | None = None
    ip_address_type: DslValue[str] | None = None


@dataclass
class ResourceConfigurationDefinition(PropertyType):
    arn_resource: DslValue[str] | None = None
    dns_resource: DslValue[DnsResource] | None = None
    ip_resource: DslValue[str] | None = None
