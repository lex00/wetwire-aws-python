"""PropertyTypes for AWS::VpcLattice::ServiceNetworkServiceAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DnsEntry(PropertyType):
    domain_name: DslValue[str] | None = None
    hosted_zone_id: DslValue[str] | None = None
