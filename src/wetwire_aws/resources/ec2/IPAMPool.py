"""PropertyTypes for AWS::EC2::IPAMPool."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ProvisionedCidr(PropertyType):
    cidr: DslValue[str] | None = None


@dataclass
class SourceResource(PropertyType):
    resource_id: DslValue[str] | None = None
    resource_owner: DslValue[str] | None = None
    resource_region: DslValue[str] | None = None
    resource_type: DslValue[str] | None = None
