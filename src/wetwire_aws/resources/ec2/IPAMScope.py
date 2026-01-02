"""PropertyTypes for AWS::EC2::IPAMScope."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IpamScopeExternalAuthorityConfiguration(PropertyType):
    external_resource_identifier: str | None = None
    ipam_scope_external_authority_type: str | None = None
