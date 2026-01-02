"""PropertyTypes for AWS::EC2::IPAMResourceDiscovery."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IpamOperatingRegion(PropertyType):
    region_name: str | None = None


@dataclass
class IpamResourceDiscoveryOrganizationalUnitExclusion(PropertyType):
    organizations_entity_path: str | None = None
