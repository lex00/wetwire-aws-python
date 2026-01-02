"""PropertyTypes for AWS::VpcLattice::Service."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DnsEntry(PropertyType):
    domain_name: str | None = None
    hosted_zone_id: str | None = None
