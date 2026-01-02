"""PropertyTypes for AWS::EC2::IPAMPool."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ProvisionedCidr(PropertyType):
    cidr: str | None = None


@dataclass
class SourceResource(PropertyType):
    resource_id: str | None = None
    resource_owner: str | None = None
    resource_region: str | None = None
    resource_type: str | None = None
