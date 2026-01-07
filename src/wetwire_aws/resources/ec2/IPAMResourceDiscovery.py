"""PropertyTypes for AWS::EC2::IPAMResourceDiscovery."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IpamOperatingRegion(PropertyType):
    region_name: DslValue[str] | None = None


@dataclass
class IpamResourceDiscoveryOrganizationalUnitExclusion(PropertyType):
    organizations_entity_path: DslValue[str] | None = None
