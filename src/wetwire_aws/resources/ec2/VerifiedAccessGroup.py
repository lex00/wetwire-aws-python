"""PropertyTypes for AWS::EC2::VerifiedAccessGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SseSpecification(PropertyType):
    customer_managed_key_enabled: bool | None = None
    kms_key_arn: str | None = None
