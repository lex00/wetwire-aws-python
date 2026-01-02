"""PropertyTypes for AWS::CloudFront::OriginAccessControl."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class OriginAccessControlConfig(PropertyType):
    name: str | None = None
    origin_access_control_origin_type: str | None = None
    signing_behavior: str | None = None
    signing_protocol: str | None = None
    description: str | None = None
