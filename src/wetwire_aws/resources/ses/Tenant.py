"""PropertyTypes for AWS::SES::Tenant."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ResourceAssociation(PropertyType):
    resource_arn: str | None = None
