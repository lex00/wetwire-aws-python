"""PropertyTypes for AWS::EC2::IPAMScope."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IpamScopeExternalAuthorityConfiguration(PropertyType):
    external_resource_identifier: DslValue[str] | None = None
    ipam_scope_external_authority_type: DslValue[str] | None = None
