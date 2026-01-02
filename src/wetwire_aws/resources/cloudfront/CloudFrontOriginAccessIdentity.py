"""PropertyTypes for AWS::CloudFront::CloudFrontOriginAccessIdentity."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudFrontOriginAccessIdentityConfig(PropertyType):
    comment: str | None = None
